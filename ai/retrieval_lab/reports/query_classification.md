# 쿼리 유형 분류 실험

- 골든셋 질의 178개 (semantic_golden + semantic_judged, plan_query_type 라벨)
- LLM `gpt-4o-mini`, 프롬프트 v3, few-shot 예시는 골든셋과 별도로 작성

## 방식별 결과

| 방식 | Accuracy | Macro F1 | LLM 호출 |
|---|---:|---:|---:|
| 규칙만 (나머지 semantic_capability) | 0.444 | 0.394 | 0 |
| LLM만 | 0.781 | 0.813 | 178 |
| 규칙 + LLM | 0.815 | 0.849 | 137 |

## 유형별 (규칙 + LLM)

| 유형 | Precision | Recall | F1 | 질의 수 |
|---|---:|---:|---:|---:|
| model_comparison | 1.000 | 1.000 | 1.000 | 21 |
| semantic_capability | 1.000 | 0.763 | 0.866 | 38 |
| lexical_exact | 0.958 | 1.000 | 0.979 | 23 |
| structured_constraint | 0.475 | 0.792 | 0.594 | 24 |
| benchmark_lookup | 1.000 | 0.905 | 0.950 | 21 |
| semantic_constraint | 0.756 | 0.667 | 0.708 | 51 |

## Confusion Matrix (행: 정답, 열: 예측)

| 정답 \ 예측 | model comparison | semantic capability | lexical exact | structured constraint | benchmark lookup | semantic constraint |
|---|---|---|---|---|---|---|
| model comparison | 21 | 0 | 0 | 0 | 0 | 0 |
| semantic capability | 0 | 29 | 0 | 4 | 0 | 5 |
| lexical exact | 0 | 0 | 23 | 0 | 0 | 0 |
| structured constraint | 0 | 0 | 0 | 19 | 0 | 5 |
| benchmark lookup | 0 | 0 | 0 | 1 | 19 | 1 |
| semantic constraint | 0 | 0 | 1 | 16 | 0 | 34 |

## 틀린 질의 (33개)

| 질의 | 정답 | 예측 | 문장 |
|---|---|---|---|
| sg_g004 | semantic_capability | semantic_constraint | 한국어 법령·판례 검색용 RAG를 만들려고 해. GPU 없이 CPU에서 돌아가는 가벼운 임베딩 모델이 필요해. |
| sg_g008 | semantic_constraint | structured_constraint | 한국어 회의 녹음 전사를 로컬 GPU(12GB)로 돌리려고 해. 정확도를 우선하고 싶어. |
| sg_g009 | semantic_constraint | structured_constraint | 회의 전사록을 요약해 회의록 초안을 만드는 기능을 로컬에서 돌리려고 해. GPU는 8GB야. |
| sg_g010 | semantic_constraint | structured_constraint | 한국어로 된 문서 사진, 표, 차트를 이해하고 질문에 답하는 비전-언어 모델이 필요해. 14B급까지만 로컬 서버에서 돌릴 거야 |
| sg_g014 | semantic_capability | structured_constraint | 한국어 경제 뉴스 기사 수백 건에 긍정·부정·중립 감성 점수를 매기려고 해. 추가 학습 없이 바로 쓸 수 있는 분류 모델이 필 |
| sg_g015 | semantic_constraint | structured_constraint | 한국어 문서를 근거로 답하는 RAG를 개인 PC의 Docker에서만 돌리려고 해. 7.8B 모델은 답변에 2분 넘게 걸려서 더 |
| sg_g017 | semantic_constraint | structured_constraint | RTX 3060(12GB) 한 장에서 Ollama로 돌릴 한국어 멀티턴 대화용 LLM이 필요해. FP16은 너무 느려서 int |
| sg_g018 | benchmark_lookup | structured_constraint | GPU 없는 t3.medium급 서버에서 한국어 음성인식을 로컬로 돌리려고 해. 외부 API가 실패할 때 쓰는 폴백이고, 정확 |
| sg_g021 | semantic_constraint | structured_constraint | 유저 계정과 미출시 콘텐츠가 담긴 한국어 게임 버그 리포트를 QA 담당자 노트북에서 분류·정리할 로컬 LLM이 필요해. 외부  |
| sg_g022 | semantic_capability | structured_constraint | 사내 취업규칙 문서를 근거 조항으로만 답하는 한국어 RAG 챗봇을 만들 거야. 사내 규정을 외부로 보낼 수 없어서 완전히 로컬 |
| sg_g023 | semantic_capability | semantic_constraint | 휴대폰·태블릿 안에서만 녹취문을 요약하고 분류하는 온디바이스 앱을 만들고 있어. 녹취를 외부 서버로 보낼 수 없고, 0.6B급 |
| sg_g024 | semantic_capability | structured_constraint | Jetson 보드에서 3B급 소형 LLM과 함께 올릴 한국어 임베딩 모델이 필요해. 메모리가 빠듯해서 작게 양자화된 버전이면  |
| sg_g025 | semantic_capability | structured_constraint | API 키 없이 로컬 GPU에서 sentence-transformers로 돌릴 한국어 서비스용 임베딩 모델을 고르려고 해. 한 |
| sg_g027 | structured_constraint | semantic_constraint | M1 이상 맥(RAM 16GB)에서 100% 오프라인으로 도는 한국어 회의 전사 시스템을 만들려고 해. 외부 전송 없이 안정적 |
| sg_g028 | semantic_constraint | structured_constraint | 휴대폰·태블릿에서 온디바이스로 한국어 녹취를 받아적어야 해. 저장공간과 메모리 부담이 적어야 해서 medium보다 작은 모델을 |
| sg_g029 | semantic_constraint | structured_constraint | M1 이상 맥(RAM 16GB)에서 오프라인으로 한국어 회의록을 요약하고 교정할 LLM이 필요해. Ollama 없이 통합 메모 |
| sg_g030 | semantic_constraint | structured_constraint | 회의 녹음에서 할 일과 기여도를 뽑아내는 웹 플랫폼에 쓸 한국어 LLM을 자체 GPU 서버(10~16GB)에서 서빙하려고 해. |
| sg_g016 | semantic_constraint | structured_constraint | 한국어 문서를 근거로 답하는 RAG를 사내 서버에서만 돌리려고 해. 7.8B 모델은 너무 느려서 더 작고 빠른 한국어 모델이  |
| sg_h002 | structured_constraint | semantic_constraint | 사내 규정 문서에 대한 한국어 질의응답 기능을 넣으려고 해. 답은 문서 안에서 찾으면 되고, 상업 서비스라 라이선스 제약이 없 |
| sg_h009 | semantic_constraint | structured_constraint | 한국어 영수증이나 문서 사진에서 글자를 읽고 내용을 정리하는 비전 언어 모델이 필요해. GPU 24GB 한 장에서 돌릴 거야. |
| sg_h015 | semantic_constraint | structured_constraint | 회의록 같은 긴 한국어 문서를 요약하는 기능을 로컬 GPU 16GB에서 돌리려고 해. 상업적으로 쓸 수 있어야 해. |
| sg_h021 | semantic_constraint | structured_constraint | 한국어 손글씨 메모 사진을 텍스트로 옮기는 모델이 필요해. 앱 서버에서 돌릴 거라 3B 이하였으면 해. |
| sg_h026 | semantic_capability | semantic_constraint | 한국어 수학 문제 사진을 보고 풀이를 설명하는 모델이 필요해. 정확도가 중요하고 큰 GPU 서버가 있어. |
| sg_h028 | semantic_capability | semantic_constraint | 메신저 대화 캡처 화면을 읽고 내용을 한국어로 정리하는 모델이 필요해. 로컬에서만 돌려야 해. |
| sg_h030 | semantic_constraint | structured_constraint | 한국어 코딩 질문에 답하는 로컬 LLM이 필요해. GPU 24GB 한 장이야. |
| sg_h031 | semantic_capability | semantic_constraint | 한국어 법률 상담 챗봇을 만들려고 해. 법률 도메인 지식이 있는 모델이면 좋겠어. |
| sg_h036 | structured_constraint | semantic_constraint | 한국어 LLM을 GPU 서버 여러 대에 올려 서빙하려고 해. 상업 이용이 가능해야 하고 성능이 최우선이야. |
| sg_h043 | semantic_constraint | structured_constraint | 한국어 RAG 리랭커를 CPU에서 돌리려고 해. 300M 이하의 가벼운 모델이면 좋겠어. |
| sg_h045 | structured_constraint | semantic_constraint | 한국어 특화 임베딩 모델을 상업 서비스에 넣으려고 해. 라이선스가 명확해야 해. |
| sg_h052 | semantic_constraint | lexical_exact | 한국어·영어·중국어·일본어를 서로 번역하는 다국어 번역 모델 하나로 해결하고 싶어. GPU 24GB 서버 한 장이야. |
| sg_h062 | benchmark_lookup | semantic_constraint | 한국어 위키 문서에서 질문의 답을 찾는 KorQuAD 수준의 기계독해 모델이 필요해. 정확도가 중요해. |
| sg_h064 | structured_constraint | semantic_constraint | 한국어 질의응답 모델을 상업 서비스에 넣으려고 해. 라이선스가 확실한 모델만 원해. |
| sg_h066 | semantic_constraint | structured_constraint | 1B 이하 소형 생성형 모델로 한국어 문서 질의응답을 하려고 해. |
