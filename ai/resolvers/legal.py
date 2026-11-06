"""라이선스 → 상업 이용 판정. 계약 `README.md` 3절의 정책을 코드로 옮긴 것이다.

분류 어휘를 새로 만들지 않는다
------------------------------
``taxonomy.yaml``의 ``commercial_use`` 패싯이 이미 분류한다. 매핑 테이블을
또 만들면 두 벌이 생기고 어느 쪽이 맞는지 아무도 모른다.

    taxonomy.normalize("commercial_use", raw)  →  commercial_status
      commercial      → permitted
      non_commercial  → prohibited
      conditional     → review_required
      unknown / None  → unknown

``permitted``가 "법적으로 안전"을 뜻하지 않는다
---------------------------------------------
이 값은 **저장소가 선언한 라이선스가 어느 계열인가**만 말한다. base model /
adapter의 원래 약관, 학습 데이터의 라이선스, 서비스 운영 방식은 말하지 않는다.
그래서 ``base_model_constraint``를 따로 둔다 — apache-2.0으로 선언된 Llama
파인튜닝이면 Llama 약관이 따라온다.

LICENSE 원문을 LLM에 읽혀 자동 판정하지 않는다
---------------------------------------------
법적 성격이 있는 판단이고, 틀렸을 때 사용자가 입는 피해가 "모른다"고 말하는
것보다 크다. 원문과 해시를 모아 검토 큐에 올리는 데까지가 파이프라인의 일이다.
"""

from __future__ import annotations

import sys
from pathlib import Path
from typing import Any, Callable, Dict, List, Optional, Sequence

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import taxonomy  # noqa: E402

from . import facts  # noqa: E402

STATUS_FROM_FACET = {
    "commercial": "permitted",
    "non_commercial": "prohibited",
    "conditional": "review_required",
    "unknown": "unknown",
    None: "unknown",
}

# 제한이 센 순서. 라이선스가 여러 개면 가장 제한적인 것을 따른다.
RESTRICTIVENESS = ("prohibited", "review_required", "unknown", "permitted")

LICENSE_FILENAMES = {
    "license", "license.md", "license.txt", "license.rst",
    "licence", "licence.md", "licence.txt",
    "copying", "copying.md", "copying.txt",
    "notice", "notice.md", "notice.txt",
    "license.apache", "license.mit", "license_llama3", "use_policy.md",
}

MESSAGES = {
    "permitted": "저장소가 선언한 라이선스({raw})는 상업 이용을 허용하는 계열입니다. "
                 "고지·표기 의무는 원문을 확인하세요.",
    "prohibited": "선언된 라이선스({raw})는 비상업 용도로만 허용합니다. "
                  "상업 서비스에는 사용할 수 없습니다.",
    "review_required": "선언된 라이선스({raw})는 자체 약관이나 추가 조건이 있어 "
                       "직접 확인이 필요합니다.",
    "unknown": "저장소에 라이선스 정보가 없어 상업 이용 여부를 확인할 수 없습니다. "
               "작성자에게 직접 확인하세요.",
}


def classify(raw: Any) -> str:
    """원시 라이선스 값 → commercial_status. 여러 개면 가장 제한적인 것."""
    if isinstance(raw, (list, tuple)):
        values = [item for item in raw if item]
        if not values:
            return "unknown"
        statuses = {classify(item) for item in values}
        for name in RESTRICTIVENESS:
            if name in statuses:
                return name
        return "unknown"
    return STATUS_FROM_FACET.get(taxonomy.normalize("commercial_use", raw), "unknown")


def extract_raw(card_data: Optional[Dict[str, Any]], tags: Sequence[str]) -> tuple:
    """(값, 출처). cardData가 1차, tags의 ``license:*``가 2차다."""
    value = (card_data or {}).get("license")
    if value:
        return value, "model_card:cardData.license"
    tagged = [tag.split(":", 1)[1] for tag in tags or () if tag.startswith("license:")]
    tagged = [item for item in tagged if item and item != "other"] or tagged
    if tagged:
        return (tagged[0] if len(tagged) == 1 else tagged), "hf_api:tags[license:*]"
    return None, ""


def find_license_file(siblings: Sequence[Dict[str, Any]]) -> Optional[Dict[str, Any]]:
    """LICENSE 류 파일을 찾는다. 내용은 아직 읽지 않는다.

    ``sha256``과 ``chars``는 파일을 실제로 내려받아야 안다. siblings가 주는
    ``blobId``는 git object id이고 내용의 sha256이 아니다. 계산하지 않은 해시를
    sha256 자리에 넣으면 나중에 원문이 바뀌었는지 비교할 때 조용히 틀린다.
    """
    for sibling in siblings or ():
        name = sibling.get("rfilename") or ""
        if name.rsplit("/", 1)[-1].lower() in LICENSE_FILENAMES:
            return {
                "path": name,
                "bytes": sibling.get("size"),
                "blob_id": sibling.get("blobId") or sibling.get("blob_id"),
                "sha256": None,
                "chars": None,
            }
    return None


def resolve(
    raw: Dict[str, Any],
    *,
    base_status_of: Optional[Callable[[str], Optional[str]]] = None,
    retrieved_at: Optional[str] = None,
) -> Dict[str, Any]:
    """계약의 ``legal`` 그룹과 provenance 항목을 만든다.

    ``base_status_of``는 base model의 commercial_status를 돌려주는 콜백이다.
    코퍼스 전체를 들고 있어야 알 수 있으므로 호출자가 넘긴다. 없으면
    base_model_constraint를 판정하지 않는다.
    """
    card_data = raw.get("cardData") or raw.get("card_data") or {}
    tags = raw.get("tags") or []
    siblings = raw.get("siblings") or []

    license_raw, license_source = extract_raw(card_data, tags)
    status = classify(license_raw)
    license_file = find_license_file(siblings)

    # base model 제약
    constraint = None
    declared = card_data.get("base_model") or raw.get("base_models") or []
    if isinstance(declared, str):
        declared = [declared]
    if base_status_of:
        for base_id in declared:
            base_id = base_id.get("name") if isinstance(base_id, dict) else base_id
            if not isinstance(base_id, str):
                continue
            base_status = base_status_of(base_id)
            if base_status is None:
                continue
            if RESTRICTIVENESS.index(base_status) < RESTRICTIVENESS.index(status):
                constraint = {
                    "base_model_id": base_id,
                    "commercial_status": base_status,
                    "more_restrictive": True,
                }
                break
            if constraint is None:
                constraint = {
                    "base_model_id": base_id,
                    "commercial_status": base_status,
                    "more_restrictive": False,
                }

    review_required = status in {"review_required", "unknown"} or bool(
        (constraint or {}).get("more_restrictive")
    )
    reasons: List[str] = []
    if status == "unknown":
        reasons.append("라이선스 태그가 없다")
        if not license_file:
            reasons.append("LICENSE 류 파일도 없다")
    elif status == "review_required":
        reasons.append(f"선언된 라이선스가 조건부 계열이다({license_raw})")
    if (constraint or {}).get("more_restrictive"):
        reasons.append(
            f"base model {constraint['base_model_id']}이 더 제한적이다"
            f"({constraint['commercial_status']})"
        )

    message = MESSAGES[status].format(
        raw=license_raw if not isinstance(license_raw, list) else ", ".join(license_raw)
    )
    if license_file and status in {"review_required", "unknown"}:
        message += f" 저장소에 `{license_file['path']}` 원문이 있습니다."
    if (constraint or {}).get("more_restrictive"):
        message += (
            f" 이 모델은 {constraint['base_model_id']}에서 파생되었고, 원본의 조건"
            f"({constraint['commercial_status']})이 더 제한적입니다."
        )

    provenance = {
        "legal.license_raw": (
            facts.fact("documented", [license_source], None, retrieved_at)
            if license_raw
            else facts.unknown("cardData와 tags에 license가 없다")
        ),
        "legal.license_file": (
            facts.fact("documented", [f"hf_file:{license_file['path']}"], None, retrieved_at)
            if license_file
            else facts.unknown("LICENSE / COPYING / NOTICE 류 파일이 없다")
        ),
        "legal.commercial_status": (
            facts.fact("documented", [license_source], None, retrieved_at)
            if license_raw
            else facts.unknown("license_raw가 unknown이므로 분류할 수 없다")
        ),
        "legal.base_model_constraint": (
            facts.fact("documented", [f"derived_from:{constraint['base_model_id']}"], None, retrieved_at)
            if constraint
            else facts.not_applicable(
                "선언된 base_model이 없다" if not declared else "base model의 라이선스를 모른다"
            )
        ),
    }

    review_queue = []
    if status == "unknown":
        review_queue.append({
            "field": "legal.commercial_status",
            "reason": "라이선스 태그가 없다. 상업 이용 여부를 판단할 수 없다.",
            "hint": f"https://huggingface.co/{raw.get('id') or raw.get('modelId')}/discussions",
        })
    elif status == "review_required" and license_file:
        review_queue.append({
            "field": "legal.commercial_status",
            "reason": f"조건부 라이선스({license_raw})이고 원문 파일이 있다. 사람이 읽어 판정한다.",
            "hint": f"hf_file:{license_file['path']}",
        })

    return {
        "legal": {
            "license_raw": license_raw,
            "license_file": license_file,
            "commercial_status": status,
            "base_model_constraint": constraint,
            "redistribution": "permitted" if status == "permitted" else "unknown",
            "review_required": review_required,
            "review_reason": " / ".join(reasons) or None,
            "user_message": message,
        },
        "provenance": provenance,
        "review_queue": review_queue,
    }
