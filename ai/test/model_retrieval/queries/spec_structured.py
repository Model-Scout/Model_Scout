"""structured_constraint 질문 40개.

이 유형은 채점 규칙이 없다. 하드 필터를 통과하면 그것이 정답이다
(scan.classify_semantic 이 must/must_id 가 없으면 "하드 필터 조건만으로 판정").
그래서 사람이 볼 것은 **질문 문장과 조건이 맞아떨어지는가** 하나뿐이다.

구 골든셋 24문항은 질문 문장이 "상업 서비스라 라이선스 제약이 없어야 해"라고
말하면서 조건에는 commercial_status 가 없었다. 계약 필터가 그때 없었기
때문이다. 질문 문장에 적힌 것을 조건으로 되살렸다(v3 의 conditions_fidelity
원칙 — 조건마다 질문 속 근거가 있어야 한다).

후보가 0인 조합은 쓰지 않는다. '요약 + 1B 이하 + 상업 허용'이 0이라 뺐다.
"""

EMB = ["sentence-similarity", "feature-extraction"]
GEN = ["text-generation"]
ASR = ["automatic-speech-recognition"]
VLM = ["image-text-to-text"]
CLS = ["text-classification"]
QA = ["question-answering"]
TR = ["translation"]
SUM = ["summarization"]
PERMITTED = ["permitted"]


def q(qid, text, conditions, fidelity, origin="label_reused", persona="backend_dev", style="mixed"):
    return {
        "qid": qid, "text": text, "query_type": "structured_constraint", "origin": origin,
        "persona": persona, "expression_style": style,
        "conditions": {"korean_required": True, **conditions},
        "conditions_fidelity": fidelity,
        "relevance_rule": {
            "grade_2": "조건을 모두 만족하는 원본 모델",
            "grade_1": "조건은 만족하지만 원본의 변환·양자화·재업로드본",
        },
    }


QUERIES = [
    # ── 질의응답 ───────────────────────────────────────────────
    q("st01", "한국어 FAQ 문서에서 질문에 해당하는 답 구간을 뽑아주는 추출형 QA 모델이 필요해. CPU 서버에서 돌릴 거라 500M 파라미터 이하로.",
      {"tasks": QA, "max_parameters_billion": 0.5},
      {"tasks": "추출형 QA 모델", "max_parameters_billion": "500M 파라미터 이하"}),
    q("st02", "모바일 앱에 넣을 작은 한국어 기계독해 모델이 필요해. 파라미터 1B 이하면 좋겠어.",
      {"tasks": QA, "max_parameters_billion": 1.0},
      {"tasks": "기계독해 모델", "max_parameters_billion": "파라미터 1B 이하"}),
    q("st03", "사내 규정 문서에 대한 한국어 질의응답 기능을 넣으려고 해. 상업 서비스라 라이선스 제약이 없어야 해.",
      {"tasks": QA, "commercial_status": PERMITTED},
      {"tasks": "질의응답 기능", "commercial_status": "상업 서비스라 라이선스 제약이 없어야"}),
    q("st04", "Apache-2.0 라이선스로 배포된 한국어 질의응답 모델이 있나요?",
      {"tasks": QA, "commercial_status": PERMITTED},
      {"tasks": "질의응답 모델", "commercial_status": "Apache-2.0 라이선스로 배포된"}),

    # ── 비전 언어 ──────────────────────────────────────────────
    q("st05", "한국어 질문으로 이미지 내용을 설명해 주는 가벼운 VLM이 필요해. 노트북에서 돌릴 거라 1.5B 이하이고 상업 이용도 가능해야 해.",
      {"tasks": VLM, "max_parameters_billion": 1.5, "commercial_status": PERMITTED},
      {"tasks": "이미지 내용을 설명해 주는 VLM", "max_parameters_billion": "1.5B 이하",
       "commercial_status": "상업 이용도 가능해야"}),
    q("st06", "1B 이하의 아주 작은 비전 언어 모델로 한국어 이미지 설명을 엣지 기기에서 돌리고 싶어.",
      {"tasks": VLM, "max_parameters_billion": 1.0},
      {"tasks": "비전 언어 모델", "max_parameters_billion": "1B 이하"}),
    q("st07", "8GB 그래픽카드 노트북에서 llama.cpp 로 이미지 설명 모델을 돌리려고요. 파라미터 2B 이하 GGUF 중 상업 이용 허용 계열만 알려 주세요.",
      {"tasks": VLM, "max_parameters_billion": 2, "require_artifact": ["gguf"], "commercial_status": PERMITTED},
      {"tasks": "이미지 설명 모델", "max_parameters_billion": "파라미터 2B 이하",
       "require_artifact": "llama.cpp 로 … GGUF", "commercial_status": "상업 이용 허용 라이선스 계열"}),
    q("st08", "GGUF 로 받을 수 있는 한국어 비전 언어 모델이 있나요? 파일 크기는 2GB 이하였으면 합니다.",
      {"tasks": VLM, "require_artifact": ["gguf"], "max_artifact_gib": 2},
      {"tasks": "비전 언어 모델", "require_artifact": "GGUF 로 받을 수 있는", "max_artifact_gib": "파일 크기는 2GB 이하"}),

    # ── 생성 ───────────────────────────────────────────────────
    q("st09", "노트북 CPU에서 돌아가는 아주 작은 한국어 대화 모델이 필요해. 0.6B 이하이고 승인 없이 바로 받을 수 있으며 상업 이용도 돼야 해.",
      {"tasks": GEN, "max_parameters_billion": 0.6, "commercial_status": PERMITTED, "exclude_gated": True},
      {"tasks": "대화 모델", "max_parameters_billion": "0.6B 이하",
       "exclude_gated": "승인 없이 바로 받을 수 있으며", "commercial_status": "상업 이용도 돼야"}),
    q("st10", "GPU 없는 사내 서버에서 돌릴 한국어 챗봇이 필요해. 상업 이용이 가능하고 1.5B 이하, 컨텍스트는 32K 이상이면 좋겠어.",
      {"tasks": GEN, "max_parameters_billion": 1.5, "commercial_status": PERMITTED, "min_context_length": 32768},
      {"tasks": "챗봇(생성 모델)", "max_parameters_billion": "1.5B 이하",
       "commercial_status": "상업 이용이 가능하고", "min_context_length": "컨텍스트는 32K 이상"}),
    q("st11", "128K 토큰 이상 긴 문맥을 다루는 한국어 LLM이 필요해. 긴 보고서를 통째로 넣고 질문할 건데 2B 이하이고 상업 이용이 가능해야 해.",
      {"tasks": GEN, "min_context_length": 131072, "max_parameters_billion": 2, "commercial_status": PERMITTED},
      {"tasks": "한국어 LLM", "min_context_length": "128K 토큰 이상 긴 문맥",
       "max_parameters_billion": "2B 이하", "commercial_status": "상업 이용이 가능해야"}),
    q("st12", "상업 이용 가능, 파라미터 3B 이하, 컨텍스트 32K 토큰 이상, GGUF 로 받을 수 있는 한국어 LLM 목록이 필요해.",
      {"tasks": GEN, "max_parameters_billion": 3.0, "min_context_length": 32768,
       "commercial_status": PERMITTED, "require_artifact": ["gguf"]},
      {"tasks": "한국어 LLM", "max_parameters_billion": "파라미터 3B 이하",
       "min_context_length": "컨텍스트 32K 토큰 이상", "commercial_status": "상업 이용 가능",
       "require_artifact": "GGUF 로 받을 수 있는"}),
    q("st13", "브라우저 확장에 넣을 아주 가벼운 한국어 생성 모델이 필요해요. ONNX 로 배포돼 있고 1B 이하, 상업 이용이 가능해야 합니다.",
      {"tasks": GEN, "require_artifact": ["onnx"], "max_parameters_billion": 1, "commercial_status": PERMITTED},
      {"tasks": "생성 모델", "require_artifact": "ONNX 로 배포돼 있고",
       "max_parameters_billion": "1B 이하", "commercial_status": "상업 이용이 가능해야"}),
    q("st14", "Ollama 로 돌릴 한국어 LLM 중 GGUF 파일이 1GB 이하이고 파라미터 1B 이하인 걸 찾습니다.",
      {"tasks": GEN, "require_artifact": ["gguf"], "max_artifact_gib": 1, "max_parameters_billion": 1},
      {"tasks": "한국어 LLM", "require_artifact": "Ollama 로 돌릴 … GGUF",
       "max_artifact_gib": "GGUF 파일이 1GB 이하", "max_parameters_billion": "파라미터 1B 이하"}),
    q("st15", "관리자 승인 없이 바로 받을 수 있고 상업 이용도 가능한 한국어 생성 모델 중 2B 이하인 걸 보고 싶어요.",
      {"tasks": GEN, "exclude_gated": True, "max_parameters_billion": 1,
       "commercial_status": PERMITTED, "min_context_length": 8192},
      {"tasks": "생성 모델", "exclude_gated": "관리자 승인 없이 바로 받을 수 있고",
       "max_parameters_billion": "1B 이하", "commercial_status": "상업 이용도 가능한",
       "min_context_length": "컨텍스트 8K 이상"}),
    q("st16", "가벼운 한국어 LLM을 찾습니다. 상업 이용이 가능하고 실행 파일이 1GB 이하, 파라미터는 0.5B 이하면 좋겠어요.",  # noqa: E501
      {"tasks": GEN, "commercial_status": PERMITTED, "max_artifact_gib": 1, "max_parameters_billion": 0.5},
      {"tasks": "한국어 LLM", "commercial_status": "상업 이용이 가능하고",
       "max_artifact_gib": "실행 파일이 1GB 이하", "max_parameters_billion": "파라미터는 0.5B 이하"}),

    # ── 임베딩 ─────────────────────────────────────────────────
    q("st17", "벡터 DB 비용 때문에 작고 빠른 한국어 임베딩 모델이 필요해. 100M 파라미터 이하.",
      {"tasks": EMB, "max_parameters_billion": 0.1},
      {"tasks": "임베딩 모델", "max_parameters_billion": "100M 파라미터 이하"}),
    q("st18", "한국어 문서 검색용 임베딩을 쓰려는데 입력이 32K 토큰 이상이고 상업 이용이 가능해야 해.",
      {"tasks": EMB, "min_context_length": 32768, "commercial_status": PERMITTED},
      {"tasks": "검색용 임베딩", "min_context_length": "입력이 32K 토큰 이상",
       "commercial_status": "상업 이용이 가능해야"}),
    q("st19", "상업 이용 가능, 0.6B 이하, 입력 8192 토큰 이상인 한국어 임베딩 모델이 필요해. CPU에서 돌릴 거야.",
      {"tasks": EMB, "max_parameters_billion": 0.6, "min_context_length": 8192, "commercial_status": PERMITTED},
      {"tasks": "임베딩 모델", "max_parameters_billion": "0.6B 이하",
       "min_context_length": "입력 8192 토큰 이상", "commercial_status": "상업 이용 가능"}),
    q("st20", "파라미터가 0.2B 이하이고 ONNX 가중치가 함께 올라온 한국어 문장 임베딩 모델 목록을 보고 싶어요.",
      {"tasks": EMB, "max_parameters_billion": 0.2, "require_artifact": ["onnx"]},
      {"tasks": "문장 임베딩 모델", "max_parameters_billion": "파라미터가 0.2B 이하",
       "require_artifact": "ONNX 가중치가 함께 올라온"}),
    q("st21", "한국어 특화 임베딩 모델을 상업 서비스에 넣으려고 해. 라이선스가 명확해야 하고 0.2B 이하면 좋겠어.",
      {"tasks": EMB, "commercial_status": PERMITTED, "max_parameters_billion": 0.2},
      {"tasks": "임베딩 모델", "commercial_status": "상업 서비스에 넣으려고 … 라이선스가 명확해야",
       "max_parameters_billion": "0.2B 이하"}),
    q("st22", "메모리 2GB 클라우드 서버에서 CPU로 돌릴 한국어 임베딩 모델이 필요해. 실행 파일이 150MB 이하였으면 해.",
      {"tasks": EMB, "max_artifact_gib": 0.15},
      {"tasks": "임베딩 모델", "max_artifact_gib": "실행 파일이 150MB 이하"}),
    q("st23", "GGUF 로 받을 수 있는 한국어 임베딩 모델이 있을까요? llama.cpp 로 돌리려고 합니다.",
      {"tasks": EMB, "require_artifact": ["gguf"]},
      {"tasks": "임베딩 모델", "require_artifact": "llama.cpp … GGUF 로 받을 수 있는"}),

    # ── 음성 인식 ──────────────────────────────────────────────
    q("st24", "모바일 기기에서 돌릴 한국어 음성인식 모델이 필요해. 상업 서비스이고 100M 파라미터 이하여야 해.",
      {"tasks": ASR, "max_parameters_billion": 0.1, "commercial_status": PERMITTED},
      {"tasks": "음성인식 모델", "max_parameters_billion": "100M 파라미터 이하",
       "commercial_status": "상업 서비스이고"}),
    q("st25", "상업 이용 가능하고 1B 이하인 한국어 음성인식 모델을 보고 싶어.",
      {"tasks": ASR, "max_parameters_billion": 1.0, "commercial_status": PERMITTED},
      {"tasks": "음성인식 모델", "max_parameters_billion": "1B 이하", "commercial_status": "상업 이용 가능"}),
    q("st26", "상업 서비스에 넣을 한국어 음성 인식을 ONNX Runtime 으로 서버에 올리려고 해요. 라이선스가 상업 이용을 허용하는 계열인 모델만 알려 주세요.",
      {"tasks": ASR, "require_artifact": ["onnx"], "commercial_status": PERMITTED},
      {"tasks": "음성 인식", "require_artifact": "ONNX Runtime 으로",
       "commercial_status": "라이선스가 상업 이용을 허용하는 계열"}),
    q("st27", "RAM 4GB PC에서 돌릴 한국어 음성인식 모델이 필요해. 실행 파일이 200MB 이하면 좋겠어.",
      {"tasks": ASR, "max_artifact_gib": 0.2},
      {"tasks": "음성인식 모델", "max_artifact_gib": "실행 파일이 200MB 이하"}),
    q("st28", "GGUF 로 받을 수 있는 한국어 음성 인식 모델을 찾습니다. whisper.cpp 로 돌릴 거라 1GB 이하였으면 해요.",
      {"tasks": ASR, "require_artifact": ["gguf"], "max_artifact_gib": 1},
      {"tasks": "음성 인식 모델", "require_artifact": "whisper.cpp … GGUF 로 받을 수 있는",
       "max_artifact_gib": "1GB 이하"}),

    # ── 분류 ───────────────────────────────────────────────────
    q("st29", "상업 이용 가능, 150M 파라미터 이하, CPU에서 돌아가는 한국어 텍스트 분류 모델이 필요해.",
      {"tasks": CLS, "max_parameters_billion": 0.15, "commercial_status": PERMITTED},
      {"tasks": "텍스트 분류 모델", "max_parameters_billion": "150M 파라미터 이하",
       "commercial_status": "상업 이용 가능"}),
    q("st30", "사내 티켓 자동 분류 API 에 붙일 한국어 텍스트 분류 모델을 찾고 있어요. ONNX 파일이 있고 실행 파일 크기가 0.5GB 이하, 라이선스는 상업 이용 허용 계열이어야 합니다.",
      {"tasks": CLS, "require_artifact": ["onnx"], "max_artifact_gib": 0.5, "commercial_status": PERMITTED},
      {"tasks": "텍스트 분류 모델", "require_artifact": "ONNX 파일이 있고",
       "max_artifact_gib": "실행 파일 크기가 0.5GB 이하", "commercial_status": "상업 이용 허용 계열"}),
    q("st31", "관리자 승인 없이 바로 받을 수 있는 0.1B 이하 한국어 텍스트 분류 모델이 있나요?",
      {"tasks": CLS, "exclude_gated": True, "max_parameters_billion": 0.1},
      {"tasks": "텍스트 분류 모델", "exclude_gated": "관리자 승인 없이 바로 받을 수 있는",
       "max_parameters_billion": "0.1B 이하"}),
    q("st32", "safetensors 가중치가 올라온 한국어 텍스트 분류 모델 중 0.2B 이하이고 상업 이용 가능한 걸 추려 주세요.",
      {"tasks": CLS, "require_artifact": ["safetensors"], "max_parameters_billion": 0.2,
       "commercial_status": PERMITTED},
      {"tasks": "텍스트 분류 모델", "require_artifact": "safetensors 가중치가 올라온",
       "max_parameters_billion": "0.2B 이하", "commercial_status": "상업 이용 가능한"}),

    # ── 요약 ───────────────────────────────────────────────────
    q("st33", "task 가 summarization 으로 분류된 한국어 모델 중에서 safetensors 가중치가 있는 것만 추려 줄 수 있나요?",
      {"tasks": SUM, "require_artifact": ["safetensors"]},
      {"tasks": "task 가 summarization 으로 분류된", "require_artifact": "safetensors 가중치가 있는"}),
    q("st34", "한국어 문서 요약 모델 중 1B 이하인 가벼운 걸 찾습니다.",
      {"tasks": SUM, "max_parameters_billion": 1.0},
      {"tasks": "문서 요약 모델", "max_parameters_billion": "1B 이하"}),

    # ── 번역 ───────────────────────────────────────────────────
    q("st35", "Ollama 로 노트북에서 한국어 번역기를 돌려 보려는데, GGUF 파일 크기가 2GB 이하이고 상업적으로도 쓸 수 있는 라이선스 계열이면 좋겠어요.",
      {"tasks": TR, "require_artifact": ["gguf"], "max_artifact_gib": 2, "commercial_status": PERMITTED},
      {"tasks": "번역기", "require_artifact": "Ollama 로 … GGUF",
       "max_artifact_gib": "GGUF 파일 크기가 2GB 이하", "commercial_status": "상업적으로도 쓸 수 있는 라이선스 계열"}),
    q("st36", "번역 모델 중에 컨텍스트가 32K 토큰 이상이고 파라미터 4B 이하이면서 상업 이용 허용 계열 라이선스인 걸 찾아 줘.",
      {"tasks": TR, "min_context_length": 32768, "max_parameters_billion": 4, "commercial_status": PERMITTED},
      {"tasks": "번역 모델", "min_context_length": "컨텍스트가 32K 토큰 이상",
       "max_parameters_billion": "파라미터 4B 이하", "commercial_status": "상업 이용 허용 계열 라이선스"}),
    q("st37", "ONNX 로 제공되는 한국어 번역 모델이 있나요? 브라우저에서 돌리려고 합니다.",
      {"tasks": TR, "require_artifact": ["onnx"]},
      {"tasks": "번역 모델", "require_artifact": "ONNX 로 제공되는"}),
    q("st38", "1B 이하 한국어 번역 모델 중 상업 이용이 가능한 걸 추려 주세요.",
      {"tasks": TR, "max_parameters_billion": 1.0, "commercial_status": PERMITTED},
      {"tasks": "번역 모델", "max_parameters_billion": "1B 이하", "commercial_status": "상업 이용이 가능한"}),

    # ── 인기도·게이팅 ──────────────────────────────────────────
    q("st39", "많이 쓰이는 한국어 생성 모델만 보고 싶어요. 다운로드가 많은 쪽으로, 2B 이하이고 상업 이용이 가능한 걸로요.",
      {"tasks": GEN, "popularity_tier": "main", "max_parameters_billion": 2, "commercial_status": PERMITTED},
      {"tasks": "생성 모델", "popularity_tier": "많이 쓰이는 … 다운로드가 많은 쪽",
       "max_parameters_billion": "2B 이하", "commercial_status": "상업 이용 가능"},
      persona="local_user", style="goal_oriented"),
    q("st40", "관리자 승인 없이 바로 받을 수 있고 상업 이용도 가능한 0.5B 이하 한국어 음성 인식 모델을 찾습니다.",
      {"tasks": ASR, "exclude_gated": True, "commercial_status": PERMITTED, "max_parameters_billion": 0.5},
      {"tasks": "음성 인식 모델", "exclude_gated": "관리자 승인 없이 바로 받을 수 있고",
       "commercial_status": "상업 이용도 가능한", "max_parameters_billion": "0.5B 이하"}),
]
