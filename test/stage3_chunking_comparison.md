# Stage 3 청킹 방식 비교

이 문서는 Stage 3 의미 메타데이터 생성에 사용한 README 청킹 방식과 20개 표본 비교 결과를 기록한다. 각 방식은 모델 설명을 구조화된 요약으로 만들기 전에 README를 LLM 입력 단위로 나누는 방법이다.

## 골든셋 20개 모델

청킹 비교에는 아래 20개 모델을 고정 표본으로 사용했다. 1~10번은 초기 비교 표본이고, 11~20번은 작업 유형과 모델 형식을 넓힌 확장 표본이다. 이 목록은 매 방식에 동일하게 적용해 입력 표본 차이로 인한 비교 편향을 줄였다.

| 번호 | 모델 ID | Source pool | 선정 이유 |
|---:|---|---|---|
| 1 | `sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2` | Core | 한국어가 포함된 다국어 임베딩 모델과 sentence-similarity README를 대표 |
| 2 | `Xenova/opus-mt-ko-en` | Core | `ko-en` 번역 pair와 짧은 README를 검증 |
| 3 | `skt/kobert-base-v1` | Core | 강한 한국어 모델명 근거를 가진 BERT 계열 |
| 4 | `openai/whisper-large-v3` | Core | 대형 ASR 모델과 긴 사용 문서 |
| 5 | `CohereLabs/aya-vision-8b` | Core | 다국어·멀티모달 image-text-to-text 모델 |
| 6 | `circulus/koelectra-polite-v1` | Core | 한국어 이름 근거는 있으나 README가 없는 `no_source` 경계 사례 |
| 7 | `featherless-ai-quants/fiveflow-KoLlama-3-8B-Instruct-GGUF` | Low | 한국어 이름 근거, GGUF 변형, 양이 많은 README |
| 8 | `ooeoeo/opus-mt-tc-big-en-ko-ct2-float16` | Low | `en-ko` 번역 pair와 변환·양자화 artifact |
| 9 | `semin-pk/klue-roberta-base-klue-sts-mrc` | Low | KLUE 기반 한국어 sentence-similarity 변형 모델 |
| 10 | `BM-K/KoSimCSE-Unsup-RoBERTa` | Low | 한국어 문장 임베딩과 긴 코드·표·설명 블록 |
| 11 | `timpal0l/mdeberta-v3-base-squad2` | Core | question-answering과 다국어 encoder 문서 |
| 12 | `csebuetnlp/mT5_multilingual_XLSum` | Core | multilingual summarization 모델과 요약 관련 문서 |
| 13 | `skt/kogpt2-base-v2` | Core | 한국어 생성 모델명과 decoder 계열 |
| 14 | `jinaai/jina-embeddings-v3` | Core | 다국어 임베딩 모델의 모델 카드·사용 예시 |
| 15 | `ghost613/whisper-large-v3-turbo-korean` | Core | 한국어 ASR 변형과 base model lineage |
| 16 | `mradermacher/Prototype-Virus-1B-GGUF` | Low | 저인기 GGUF·질문응답 후보와 artifact 정보 |
| 17 | `ainize/kobart-news` | Low | 한국어 이름 근거와 summarization 계열 |
| 18 | `Neurora/opus-hplt-en-ko-v2.0` | Low | `en-ko` 번역 pair와 번역 문서 |
| 19 | `vitaldb/whisper-v3-turbo-kor-or-lora` | Low | 한국어 ASR LoRA 변형과 파생 모델 문서 |
| 20 | `nopesadly/GLM-OCR-Q4_K_M.gguf` | Low | image-text-to-text OCR과 GGUF 형식의 멀티모달 사례 |

표본 구성은 다음 기준을 함께 만족하도록 정했다.

- **작업 범위:** sentence similarity, translation, feature extraction, automatic speech recognition, image-text-to-text, text classification, text generation, question answering, summarization을 포함한다.
- **근거 유형:** `korean_explicit`, `korean_translation_pair`, `korean_name_strong` 사례를 포함한다.
- **모델 형식:** encoder·decoder, 임베딩, ASR, 번역, 멀티모달, GGUF·LoRA·양자화 변형을 포함한다.
- **문서 상태:** 긴 README, 짧은 README, 코드·표가 많은 README, README가 없는 모델을 포함한다.
- **Source pool:** Core 11개와 Low Popularity 9개로 구성해 인기도가 다른 모델에서 청킹 결과를 확인한다.

이 표본은 사람 손으로 정답 요약을 붙인 학습 데이터가 아니다. 청킹 방식을 동일한 입력에서 비교하기 위한 고정 holdout이며, 측정값은 전체 모델군의 절대 정확도가 아니라 방식 간 근거 연결성·비용·문서 처리 안정성을 비교하는 지표로 해석한다.


## 청킹 방식 설명

| 방식 | 기법 요약 |
|---|---|
| `fixed_window` | README 전체를 일정한 토큰 창과 겹침으로 자른다. 구현은 단순하지만 제목과 표의 의미가 청크 경계에서 끊길 수 있다. |
| `section_aware` | Markdown 제목을 기준으로 섹션을 분리한다. 문서 구조는 보존되지만 작은 섹션이 많으면 청크 수와 입력량이 늘어난다. |
| `section_packed` | Markdown heading을 기준으로 README를 섹션으로 나눈 뒤, 인접한 문단·목록·표·코드 블록을 토큰 한도 안에서 하나의 청크로 묶는다. 각 청크에는 섹션 문맥을 함께 넣어 관련 내용이 같은 입력에 남도록 하고, 이렇게 만든 비교적 큰 청크 전체를 LLM에 전달해 요약·장점·제한·사용 사례를 생성한다. 출력의 evidence ID와 인용문은 청크 원문을 기준으로 사후 검증하지만, LLM이 청크 안의 문장을 재구성할 수 있어 원자 span 방식보다 인용문 불일치가 생길 가능성이 있다. |
| `adaptive_section_packed` | 섹션 묶기를 기본으로 사용하고 긴 문단은 문장 단위로 추가 분할한다. 문서 구조와 길이 제한을 함께 맞춘다. |
| `markdown_packed` | 문단·표·코드 블록 같은 Markdown 블록을 단위로 묶는다. 구조는 유지하지만 항목별 근거 선택은 별도로 하지 않는다. |
| `hierarchical` | 상위 섹션 요약과 하위 근거 청크를 함께 구성한다. 전후 맥락은 풍부하지만 호출·청크 수가 증가한다. |
| `evidence_routed_section_packed` | 출력 필드별 관련어로 섹션을 라우팅한 뒤 필요한 섹션만 묶는다. 무관한 입력을 줄이지만 관련어 설계의 영향을 받는다. |
| `atomic_evidence` | README를 문장·목록·표 행·코드 블록 단위의 원자적 span으로 나눈다. 각 span에 ID·heading 경로·콘텐츠 유형·해시를 붙이고, 요약·장점·제한·사용 사례 같은 출력 필드별로 관련 span만 라우팅한다. LLM은 사실을 새로 만들지 않고 전달된 span ID만 선택하며, 코드는 선택된 ID의 원문을 `supporting_quote`로 직접 복사하고 참조 ID·인용문 일치 여부를 검증한다. |

## 전체 집계

| 방식 | 행 수 | 완료 | 원문 없음 | 오류 | 평균 청크 수 | 총 입력 토큰 | 총 주장 수 | 인용 불일치 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `adaptive_section_packed` | 10 | 9 | 1 | 0 | 5.7 | 31,605 | 38 | 12 |
| `atomic_evidence` (10개) | 10 | 9 | 1 | 0 | 7.2 | 3,776 | 52 | 0 |
| `evidence_routed_section_packed` | 10 | 9 | 1 | 0 | 4.9 | 24,100 | 35 | 4 |
| `fixed_window` | 10 | 9 | 1 | 0 | 4.8 | 33,610 | 37 | 5 |
| `hierarchical` | 10 | 9 | 1 | 0 | 15.1 | 31,501 | 35 | 6 |
| `markdown_packed` | 10 | 9 | 1 | 0 | 5.7 | 31,605 | 38 | 12 |
| `section_aware` | 10 | 9 | 1 | 0 | 14.1 | 32,110 | 38 | 4 |
| `section_packed` (10개) | 10 | 9 | 1 | 0 | 5.4 | 32,110 | 35 | 5 |
| `atomic_evidence` (20개) | 20 | 19 | 1 | 0 | 6.6 | 5,627 | 114 | 0 |
| `section_packed` (20개) | 20 | 19 | 1 | 0 | 4.8 | 62,499 | 80 | 13 |

## 동일 20개 표본 비교

| 지표 | `atomic_evidence` | `section_packed` |
|---|---:|---:|
| 전체 행 | 20 | 20 |
| 완료 행 | 19 | 19 |
| README 원문 없음 | 1 | 1 |
| 오류 | 0 | 0 |
| 잘못된 근거 ID | 0 | 0 |
| 근거 없는 주장 | 0 | 0 |
| 인용문 불일치 | 0 | 13 |
| 엄격한 인용문 불일치 | 0 | 11 |
| 엄격한 근거 연결 성공 | 19/19 | 13/19 |
| 총 입력 토큰 | 5,627 | 62,499 |
| 평균 청크 수 | 6.6 | 4.8 |

## 해석

20개 표본에서 `atomic_evidence`는 `section_packed`보다 입력 토큰이 적고, 인용문 불일치가 없으며, 완료된 모든 행이 원문 근거와 연결되었다. `section_packed`는 평균 청크 수가 더 적지만 넓은 문맥을 전달하므로 입력 비용이 커지고 인용문 재구성 오류가 더 많았다.

`atomic_evidence`의 결과도 README에 실제 근거가 있는 주장만 생성한다는 의미이지, 모델의 품질을 자동으로 판정한다는 의미는 아니다. README가 없거나 정보가 부족한 항목은 보수적으로 `no_source` 또는 빈 근거로 남긴다. 따라서 이 방식은 최종 전체 실행의 기본 청킹 방식으로 채택하고, 생성 후에는 근거 ID·인용문·필수 필드 검증을 계속 적용한다.
