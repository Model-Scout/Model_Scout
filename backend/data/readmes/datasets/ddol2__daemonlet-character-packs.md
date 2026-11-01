---
language:
- ko
- en
tags:
- daemonlet
- character-packs
- petchar
---
# DAEMONLET Character Packs

DAEMONLET용 외부 캐릭터팩 저장소입니다. 아스마 토키 v3·v4·v5, 이치노세 아스나(교복), 벨, 쿠로미 세리카, 시로미 이오리를 제공합니다.

**v3 / v4 / v5는 외형 이름이며 순차 업데이트 버전이 아닙니다.** 업데이트 대응 팩은 독립 ID·독립 피드를 사용합니다. 토키 v3가 v4·v5나 아스나로 자동 교체되지 않습니다.

| 외형 / Appearance | Pack ID | Pack version | Download |
|---|---|---|---|
| 아스마 토키v3 · 립싱크 · 31포즈 | asuma-toki-v3 | 1.3.5 | [1.3.5.petchar](packs/asuma-toki-v3/1.3.5.petchar) |
| 아스마 토키v4 | asuma-toki-v4 | 1.0.5 | [1.0.5.petchar](packs/asuma-toki-v4/1.0.5.petchar) |
| 아스마 토키v5 | asuma-toki-v5 | 1.0.5 | [1.0.5.petchar](packs/asuma-toki-v5/1.0.5.petchar) |
| 이치노세 아스나(교복) | ichinose-asuna-school | 0.1.3 | [0.1.3.petchar](packs/ichinose-asuna-school/0.1.3.petchar) |
| 벨 · 37포즈 | belle | 1.2.3 | [1.2.3.petchar](packs/belle/1.2.3.petchar) |
| 벨(실내복) · 35포즈 | belle-indoor | 1.0.1 | [1.0.1.petchar](packs/belle-indoor/1.0.1.petchar) |
| 쿠로미 세리카 · 36포즈 | kuromi-serika | 1.0.2 | [1.0.2.petchar](packs/kuromi-serika/1.0.2.petchar) |
| 시로미 이오리 · 28포즈 | shiromi-iori | 1.0.9 | [1.0.9.petchar](packs/shiromi-iori/1.0.9.petchar) |

## 벨(실내복) 1.0.1 — 35포즈 · 앱 내 업데이트 지원

별도 외형 ID `belle-indoor`와 전용 피드 `updates/belle-indoor/stable.json`을 사용합니다. 기존 벨 또는 외출복을 다른 외형으로 바꾸지 않습니다. **Daemonlet 0.8.4 이상**이 필요합니다.

35개 독립 모델과 32개 대화 포즈 규칙을 포함합니다. 로컬 1.0.0에서 업데이트 출처·팩 버전만 변경했으며, 그림·PSD·리깅·모션·표정·고정 대사·페르소나·출처·LICENSE 등 147개 payload 파일은 바이트 단위로 동일합니다. 원본 제작에서는 설치된 0.8.4 렌더러로 35개 모델의 정적 1,400건·모션 5,055프레임 비교, 전환·상호작용·앱 재시작을 확인했습니다. 대화 연결은 의미값 주입 검수이며 실제 LLM 답변·새 음성 생성의 전수 검수는 아닙니다. 앱의 PET는 기본 한 포즈를 사용하며 두 번째 쓰다듬기 그림은 대화 청취 포즈에 연결됩니다.

출처가 없는 1.0.0 사용자는 위 팩을 한 번 내려받아 **설정 → 캐릭터·표시 → 벨(실내복) → 수정본 가져오기**로 설치하세요. 이후 **업데이트 확인 → 다운로드 → 검증 → 적용**으로 같은 실내복 팩의 새 버전을 받을 수 있습니다. 자동 다운로드·자동 적용은 하지 않습니다.

원작 캐릭터·참고 이미지 및 모델 권리 조건은 별개이며, 이 게시가 새로운 재배포 권한을 부여하지 않습니다. 팩 내부 권리 고지와 미확인 조건을 보존했습니다.

## 세리카 1.0.2 · 이오리 1.0.9 — 앱 내 업데이트 지원

두 캐릭터에 독립적인 Hugging Face 업데이트 출처와 피드를 추가했습니다. **Daemonlet 0.8.4 이상**에서 사용할 수 있습니다. 세리카 36포즈와 이오리 28포즈의 그림·리깅·모션·표정·립싱크·페르소나 파일은 이전 버전과 바이트 단위로 동일합니다.

기존 세리카 1.0.1 / 이오리 1.0.8에는 업데이트 주소가 없으므로, 위 표의 새 팩을 **한 번 다운로드하여 설정 → 캐릭터·표시 → 해당 카드의 수정본 가져오기**로 설치하세요. 이후 카드의 출처를 확인하고 **업데이트 확인 → 다운로드 → 검증 → 적용**을 사용할 수 있습니다. 자동 다운로드나 자동 적용은 하지 않습니다.

각 피드는 자기 캐릭터의 동일 ID만 따라갑니다. 기존 세리카 이름에 표시된 ‘1.0.1’은 그림·프로필 보존을 위해 유지된 표시 이름이며, 실제 팩 버전은 카드의 버전 항목을 확인하세요.

아래 이전 버전 설명의 ‘수동 설치용’은 당시 팩에만 해당합니다.

## 시로미 이오리 1.0.8 — 28포즈 · Daemonlet 0.8.4 호환

작업·상호작용 12개와 대화 16개의 독립 포즈, 포즈별 모션·표정, 한국어 대사와 페르소나, 입 전용 립싱크를 포함합니다. 이전 로컬 팩에서 배포판에 없던 메시 기능을 사용한 문제를 수정했습니다. 선택 원화와 모션 시간·강도는 보존했습니다.

**수동 설치용입니다.** 검증한 1.0.8 파일을 재패키징 없이 게시했으며 HF 업데이트 출처·피드는 포함하지 않습니다. 다운로드 후 설정 → 캐릭터·표시 → 캐릭터 추가로 가져오세요. 실제 배포판 **Daemonlet 0.8.4**에서 가져오기와 선택을 확인했습니다.

28개 모델의 정적 1,120건·모션 3,618프레임, 접촉부·손·다리·표정과 320/460px 재생을 확인했습니다. 재시작·네이티브 Motion Lab·실시간 LLM/음성은 이번 호환 수정에서 재검증하지 않았습니다. [검증 범위와 출처 안내](packs/shiromi-iori/1.0.8.README.md)를 확인하세요.

## 쿠로미 세리카 1.0.1 — 36개 독립 포즈

작업·상호작용 14개와 대화 11상황 × 2종의 22개 포즈, 포즈별 모션, 한국어 고정 대사, 출처 기반 페르소나, 입 전용 PCM 립싱크를 포함합니다. 대화 포즈에는 검수된 자체 모션을 재생하도록 연결했습니다.

**수동 설치용입니다.** 검수한 1.0.1 파일을 재패키징 없이 게시했으며 HF 업데이트 출처·피드는 포함하지 않습니다. 다운로드 후 설정 → 캐릭터·표시 → 캐릭터 추가로 가져오세요. DAEMONLET 0.8.3 이상과 팩에 선언된 런타임 기능 지원이 필요합니다.

36포즈 렌더·PCM 검사, 클릭·쓰다듬기·작업 선점, 대화 컨트롤러의 11쌍 선택, 격리 Mac 앱의 가져오기·재시작을 확인했습니다. 실제 모델 대화·음성 바인딩은 미검수입니다. [검증 범위와 알려진 제한](packs/kuromi-serika/1.0.1.README.md)을 확인하세요.

![쿠로미 세리카 36포즈](packs/kuromi-serika/1.0.1-preview.jpg)

## 벨 1.2.3 — 37포즈 입 전용 립싱크 및 앱 업데이트 지원

기존 37포즈를 유지하며 실제 재생 오디오 크기에 따라 입만 움직이는 립싱크를 제공합니다. 오디오가 턱·머리·얼굴 전체를 변형하지 않습니다. 기존 그림·PSD·페르소나·음성 바인딩과 팩 내부 출처·라이선스는 보존합니다. 모델·음성 런타임·앱 실행파일은 팩에 포함하지 않습니다.

**[DAEMONLET 0.8.3 이상](https://github.com/ddol2ya/DAEMONLET/releases/tag/v0.8.3)**과 **`audio-lipsync-closed-target-v1`** 지원이 필요합니다. 앱을 먼저 업데이트하세요. `updates/belle/stable.json`은 이제 1.2.3을 제공하며, 1.2.1 사용자는 호환 앱에서 업데이트 확인 → 다운로드 → 검증 → 적용을 선택할 수 있습니다. 자동 다운로드·적용은 하지 않습니다. 0.8.2 이하 앱은 앱 업데이트가 필요한 상태로 차단됩니다. 기능을 제거해 구형 앱에 강제로 제공하지 않습니다.

이전 [1.2.1 팩](packs/belle/1.2.1.petchar)은 보존합니다. 업데이트 출처가 없는 로컬 벨 팩은 호환 앱에서 1.2.3을 한 번 가져와야 이후 업데이트를 확인할 수 있습니다. 다른 캐릭터의 팩·피드는 변경하지 않습니다. 이전 앱으로 돌아갈 때는 지원되는 이전 팩을 먼저 복원하세요.

검증 범위: 37포즈 closed/small/wide mesh와 입 외 vertex/alpha·턱 고정·전환·원래 표정 복구를 격리 renderer에서 확인했고, 대표 8포즈에 기존 Belle PCM을 이용한 무음 캡처를 수행했습니다. 팩 bytes/SHA256·CRC·내부 metadata와 0.8.3의 updater 호환성도 확인했습니다. 모든 포즈의 새 TTS 생성·주관적 청취, Windows 37포즈 전수 GUI 검증을 새로 수행한 것으로 표시하지 않습니다. [1.2.3 상세 안내](packs/belle/1.2.3.README.md)를 확인하세요.

## 토키 v3 1.3.5 — 31포즈 입 전용 립싱크

기존 1.3.4의 31개 포즈 전부에 실제 재생 PCM 음량에 따른 3단계 립싱크(닫힘 / 작게 / 크게)를 추가했습니다. 각 포즈의 원래 입 그림과 좌표를 사용하며, 머리·얼굴·턱·몸은 음성 때문에 움직이지 않습니다. 원본 PSD·이미지, 기존 비음성 표정·모션, 페르소나·대사·캐릭터챗 설정을 보존했습니다.

**Daemonlet 0.8.3 이상과 `audio-lipsync-closed-target-v1` 지원이 필요합니다.** 음성 모델은 팩에 포함되지 않습니다. 앱에서 선택한 목소리의 실제 재생에 입이 반응하며, 음소 인식 방식은 아닙니다. 기존 v3 팩 카드에서 업데이트를 확인하거나 위 파일을 ‘수정본 가져오기’로 설치하세요.

검증: 전 31포즈의 닫힘·작게·크게 렌더 93장, 포즈별 실제 PCM 재생 및 음소거·재개·일시정지·중지, 포즈 전환과 원래 표정 복귀를 확인했습니다. 숨겨진 입 메시까지 현재 상태로 계산해 유한 좌표와 뒤집힘 0을 검사했습니다. macOS 0.8.3의 별도 프로필에서 1.3.4 → 1.3.5 업데이트 설치, 재시작, 터치 반응도 확인했습니다. 새 TTS 생성·음성 품질 청취·Windows GUI 검수는 이번 업데이트의 검증 범위에 포함되지 않습니다.

이전 [1.3.4 팩](packs/asuma-toki-v3/1.3.4.petchar)과 다른 캐릭터 팩·피드는 유지합니다.

## 이전 토키 팩 업데이트

- **v3 1.3.4 — 모션 수정:** 대화에 연결되는 21개 자세의 동작·타이밍을 강화하고 34개 규칙에서 포즈 모션을 재생합니다. 장난용 경례는 머리 위 토끼 귀로, 일반 기쁨용 양손 브이는 안아 달라는 두 팔로 교체했습니다. 별도 수긍·축하 연결은 유지합니다. 전체 포즈는 31개입니다.
- **v4·v5 1.0.5 — 캐릭터챗 대응:** 각 16개 캐릭터챗 포즈 연결을 추가하고, v3 1.3.4의 페르소나·원작 설정·인물 관계·기본 대화 장면·예문을 동일하게 적용했습니다. 각 팩의 28개 원화·PSD·리깅·기존 모션·고정 클릭 대사는 보존했습니다.
- 세 팩 모두 대화 표시 이름은 **아스마 토키**이며 팩 ID와 외형은 각각 유지됩니다. 이전 공개 버전과 아스나 팩·피드는 보존합니다.

**세 최신 토키 팩 모두 `character-chat-v1` 지원 앱이 필요합니다.** 앱 버전 숫자만으로 호환성을 판단하지 마세요. 기존 공개 v0.7.2와는 지원 기능이 다를 수 있습니다. 피드의 runtime capability로 설치 호환성을 확인합니다.

검증 범위: 팩 전체 검증 및 파일 보존 비교, v3 개선 모션의 렌더·주요 접점 검사, v3 1.3.4 / v4·v5 1.0.4의 분리된 Mac 앱 표시·전환 확인. v4·v5 1.0.5는 동일한 시각 파일을 유지한 페르소나·대화 프로필 수정이며 파일 비교 검증을 완료했습니다. 최종 팩의 새 LLM 대화 품질시험이나 Windows 재실행은 하지 않았습니다. 사람의 모션 선호도 검수 완료를 주장하지 않습니다.

Existing in-pack provenance and rights notices remain intact. Earlier metadata-only descriptions in PROVENANCE.md concern those earlier releases, not the motion/persona changes described above. No new rights clearance is claimed.

## 이전 업데이트: 토키 v3 1.3.3 — 캐릭터챗 대응

업데이트 내용: **캐릭터챗 대응 모션 추가**

31개 포즈, 대화용 의미 연결과 보완된 페르소나를 포함합니다. 팩 관리 이름은 **아스마 토키v3**, 대화 표시 이름은 **아스마 토키**입니다. Mac·Windows 캐릭터챗 검증에서 사용한 동일한 팩 파일을 재패키징 없이 게시했습니다. 모든 포즈 조합을 시각 검수했다는 뜻은 아닙니다.

**`character-chat-v1`을 지원하는 앱 빌드가 필요합니다.** 해당 기능은 [DAEMONLET PR #22](https://github.com/ddol2ya/DAEMONLET/pull/22)에서 main에 병합됐습니다. 기존 공개 v0.7.2와 버전 숫자가 같더라도 지원 기능이 다를 수 있으므로, 기존 공개 앱만으로 1.3.3을 설치할 수 있다고 보장하지 않습니다. 기존 앱용 [v3 1.2.2](packs/asuma-toki-v3/1.2.2.petchar)도 유지합니다. 업데이트 피드에는 필요한 runtime capability가 포함되어 있습니다. v4·v5·아스나 팩과 피드는 변경하지 않습니다.

This upload publishes the already-tested v3 1.3.3 archive unchanged: 31 poses, character-chat semantic mappings, revised persona and a version-free conversation display name. It requires an app build supporting `character-chat-v1`; the older public v0.7.2 release must not be assumed compatible based on its version number alone. The earlier 1.2.2 archive remains available. The metadata-only preservation descriptions in PROVENANCE.md describe earlier releases, not the changes from v3 1.2.2 to 1.3.3. Existing in-pack provenance and asset-rights notices are preserved; no new rights clearance is claimed.

## 설치·업데이트

DAEMONLET **0.7.2 이상**의 HF 캐릭터팩 업데이트 지원 앱이 필요합니다. [최신 공개 앱 0.8.3](https://github.com/ddol2ya/DAEMONLET/releases/tag/v0.8.3)는 GitHub에서 받을 수 있으며 이 저장소에는 앱 실행파일을 배포하지 않습니다.

1. 업데이트 대응 앱을 설치합니다.
2. 원하는 외형의 `.petchar`를 다운로드한 뒤 설정 → 캐릭터·표시 → 캐릭터 추가에서 최초 한 번 가져옵니다. 기존 동일 ID 팩보다 높은 버전으로 설치됩니다. 서로 다른 ID의 팩을 함께 설치할 수 있습니다.
3. 이후 해당 카드의 HF 출처를 확인하고 **업데이트 확인 → 다운로드 → 검증 → 업데이트 적용**을 선택합니다. 자동 확인은 팩별 기본 OFF이며, 자동 다운로드·적용은 없습니다.
4. 필요하면 카드의 **이전 버전 복원**으로 돌아갑니다. 기존 출처 없는 팩은 자동으로 대응되지 않으며 이름으로 연결하지 않습니다.

아스나 **0.1.2 → 0.1.3**은 업데이트 출처 추가만 포함합니다. ID와 14개 포즈, 원화·PSD·리깅·동작·고정 대사·페르소나는 그대로입니다. 출처 없는 0.1.2를 사용 중이라면 0.1.3 파일을 한 번 가져와야 이후 업데이트를 확인할 수 있습니다. 기존 토키 팩과 피드는 변경하지 않았습니다.

## Installation and updates

Requires an app with HF character pack update support and each feed's stated minimum version/runtime capabilities. Belle 1.2.3 requires DAEMONLET 0.8.3 or newer with `audio-lipsync-closed-target-v1`; older apps are blocked. [The public 0.8.3 app release](https://github.com/ddol2ya/DAEMONLET/releases/tag/v0.8.3) is available on GitHub. This repository contains no app executables.

Kuromi Serika 1.0.2 and Shiromi Iori 1.0.9 support independent HF update feeds. Older source-less versions need one manual import of these new packs to enable update checks. For the other update-enabled packs, import the chosen appearance's `.petchar` once via Settings → Character & Display → Add character. Later, confirm its displayed source, check, download, validate and apply from that card. Automatic checks are optional and off by default; download and apply are always manual. Use Restore previous version to roll back. Appearance labels, pack SemVer and app version are independent.

Ichinose Asuna (school) 0.1.3 adds update-source metadata to 0.1.2 while preserving its ID and every payload file, including all 14 poses, artwork, PSDs, rigging, motion, fixed dialogue and persona. Import 0.1.3 once to enable future update checks for source-less 0.1.2 installations. Existing Toki archives and feeds are unchanged.

## Feeds and integrity

Each `updates/<pack-id>/stable.json` follows only the same pack ID. Feeds on main pin artifact paths to complete immutable HF commits. SHA256SUMS.txt contains archive hashes. Hashes check file consistency; they do not authenticate the original creator or protect against repository account compromise.

## Rights and provenance

These are fan character assets depicting Asuma Toki and Ichinose Asuna from Blue Archive. Original character/IP rights remain with their respective rights holders. Existing in-pack provenance and persona records are preserved. The update-source changes add distribution metadata only; they do not grant new rights to the artwork or certify unrestricted redistribution. The DAEMONLET application's MIT license does **not** license these character assets. See [PROVENANCE.md](PROVENANCE.md).

Belle retains its own in-pack LICENSE.txt and provenance.json. Original character/artwork rights remain with their respective holders; this publication and the application MIT license do not grant new rights to those assets.
