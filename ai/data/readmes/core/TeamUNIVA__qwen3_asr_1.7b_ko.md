---
language:
- ko
license: apache-2.0
base_model: Qwen/Qwen3-ASR-1.7B
pipeline_tag: automatic-speech-recognition
tags:
- automatic-speech-recognition
- speech
- korean
- qwen3-asr
---

# TeamUNIVA/qwen3_asr_1.7b_ko

<a id="en"></a>
**English** | [한국어](#ko)

This model is a fine-tune of `Qwen/Qwen3-ASR-1.7B` on Korean speech data for automatic speech recognition (ASR), and the successor to [`TeamUNIVA/qwen3_asr_1.7b_ko_beta`](https://huggingface.co/TeamUNIVA/qwen3_asr_1.7b_ko_beta). It was initialized from the beta model and further trained with two rounds of SFT followed by reinforcement learning (GSPO) on an expanded dataset. It achieves lower error rates than both the base model and the beta model across Korean benchmarks, with a small degradation on English (LibriSpeech, +0.27 %p WER vs. the base model).

## Evaluation Results

Korean scores are measured in CER (Character Error Rate); the English score is measured in WER (Word Error Rate). Lower is better for both metrics. Scores are computed after text normalization (punctuation removed and case-folded; the Whisper English normalizer is used for LibriSpeech). The "Change" column is relative to the base model.

<table>
  <thead>
    <tr>
      <th align="left">Dataset</th>
      <th>Metric</th>
      <th>Qwen3-ASR-1.7B (base)</th>
      <th>qwen3_asr_1.7b_ko_beta</th>
      <th>This model</th>
      <th>Change (%p)</th>
    </tr>
  </thead>
  <tbody>
    <tr><td>clova_call</td><td>CER</td><td>0.0448</td><td>0.0293</td><td><b>0.0283</b></td><td>-1.65</td></tr>
    <tr><td>common_voice_ko</td><td>CER</td><td>0.0719</td><td>0.0628</td><td><b>0.0603</b></td><td>-1.16</td></tr>
    <tr><td>fleurs_ko</td><td>CER</td><td>0.0142</td><td>0.0138</td><td><b>0.0126</b></td><td>-0.16</td></tr>
    <tr><td>ksponspeech</td><td>CER</td><td>0.0865</td><td>0.0670</td><td><b>0.0594</b></td><td>-2.71</td></tr>
    <tr><td>zeroth</td><td>CER</td><td>0.0264</td><td>0.0230</td><td><b>0.0220</b></td><td>-0.44</td></tr>
    <tr>
      <td style="background-color:#e3edf5; color:#000000;"><b>Korean total</b></td>
      <td style="background-color:#e3edf5; color:#000000;">CER</td>
      <td style="background-color:#e3edf5; color:#000000;"><b>0.0686</b></td>
      <td style="background-color:#e3edf5; color:#000000;"><b>0.0537</b></td>
      <td style="background-color:#e3edf5; color:#000000;"><b>0.0483</b></td>
      <td style="background-color:#e3edf5; color:#000000;"><b>-2.03</b></td>
    </tr>
    <tr><td>librispeech (English, reference)</td><td>WER</td><td>0.0250</td><td>0.0246</td><td>0.0277</td><td>+0.27</td></tr>
  </tbody>
</table>

### Additional evaluation with kocer

[kocer](https://github.com/Choi-kwan-u/kocer) (v0.1.5) is a CER for Korean ASR that does not count differences in spacing, punctuation, number notation (e.g., 3개 = 세 개) or Latin-acronym spelling (e.g., AI = 에이아이) as errors. We re-scored the same model outputs on the same reviewed evaluation set with kocer; as above, each utterance is scored against both the TN and ITN transcripts and the better-scoring one is used. Lower is better; the "Change" column is relative to the base model.

<table>
  <thead>
    <tr>
      <th align="left">Dataset</th>
      <th>Metric</th>
      <th>Qwen3-ASR-1.7B (base)</th>
      <th>qwen3_asr_1.7b_ko_beta</th>
      <th>This model</th>
      <th>Change (%p)</th>
    </tr>
  </thead>
  <tbody>
    <tr><td>clova_call</td><td>CER (kocer)</td><td>0.0429</td><td>0.0280</td><td><b>0.0264</b></td><td>-1.65</td></tr>
    <tr><td>common_voice_ko</td><td>CER (kocer)</td><td>0.0718</td><td>0.0628</td><td><b>0.0602</b></td><td>-1.16</td></tr>
    <tr><td>fleurs_ko</td><td>CER (kocer)</td><td>0.0127</td><td>0.0125</td><td><b>0.0112</b></td><td>-0.15</td></tr>
    <tr><td>ksponspeech</td><td>CER (kocer)</td><td>0.0860</td><td>0.0664</td><td><b>0.0585</b></td><td>-2.75</td></tr>
    <tr><td>zeroth</td><td>CER (kocer)</td><td>0.0253</td><td>0.0202</td><td><b>0.0194</b></td><td>-0.59</td></tr>
    <tr>
      <td style="background-color:#e3edf5; color:#000000;"><b>Korean total</b></td>
      <td style="background-color:#e3edf5; color:#000000;">CER (kocer)</td>
      <td style="background-color:#e3edf5; color:#000000;"><b>0.0679</b></td>
      <td style="background-color:#e3edf5; color:#000000;"><b>0.0528</b></td>
      <td style="background-color:#e3edf5; color:#000000;"><b>0.0472</b></td>
      <td style="background-color:#e3edf5; color:#000000;"><b>-2.07</b></td>
    </tr>
  </tbody>
</table>

The ranking is the same as with the metric above. kocer scores hardly depend on which transcript is used as the reference: for this model, the Korean total is 0.0481 against the TN transcripts only, 0.0491 against the ITN transcripts only, and 0.0472 with the better of the two.

### Evaluation Set

All open Korean benchmark evaluation sets used above were fully reviewed by hand: each utterance was checked for dual TN/ITN (text normalization / inverse text normalization) transcripts, low-quality samples were filtered out, and mis-transcriptions were corrected. Every utterance was then evaluated against both the TN and ITN transcripts, and the better-scoring transcript of the pair was used for the final aggregated result. After this review, 8,383 of the original 8,489 records were retained (106 excluded):

| Dataset | Retained records |
| --- | --- |
| clova_call | 1,083 |
| common_voice_ko | 564 |
| fleurs_ko | 382 |
| zeroth | 449 |
| kspon_eval_clean | 2,946 |
| kspon_eval_other | 2,959 |
| **Total** | **8,383** |

**Public release.** The reviewed evaluation sets for `zeroth`, `common_voice_ko` and `fleurs_ko` are published at [TeamUNIVA/ko_asr_benchmarks](https://huggingface.co/datasets/TeamUNIVA/ko_asr_benchmarks). The other sets (`clova_call`, `kspon_eval_clean`, `kspon_eval_other`) are not released because of the license terms of their original datasets.

## Examples

Examples of how actual recognition results change across models (base → beta → this model). Each example comes with its audio clip (stored in this repository under `audio/`), so you can listen to it with the player above the table.

**Example 1**

<audio controls src="https://huggingface.co/TeamUNIVA/qwen3_asr_1.7b_ko/resolve/main/audio/example_1.wav"></audio>

| Model | Transcription |
| --- | --- |
| Reference | 범어네거리에서 걸어가면 가까운가요? |
| Qwen3-ASR-1.7B (base) | 버머네거리에서 걸어가면 가까운가요? |
| qwen3_asr_1.7b_ko_beta | 범어내거리에서 걸어가면 가까운가요? |
| **This model** | 범어네거리에서 걸어가면 가까운가요? |

**Example 2**

<audio controls src="https://huggingface.co/TeamUNIVA/qwen3_asr_1.7b_ko/resolve/main/audio/example_2.wav"></audio>

| Model | Transcription |
| --- | --- |
| Reference | 찬드라 셰카르 솔랑키 경찰서장은 피고인이 얼굴을 가린 채 법정에 나왔다고 말했다. |
| Qwen3-ASR-1.7B (base) | 찬드라 시에카르 솔랑키 경찰서장은 피고인이 얼굴을 가린 채 법정에 나왔다고 말했다. |
| qwen3_asr_1.7b_ko_beta | 찬드라 샤카르 솔랑키 경찰서장은 피고인이 얼굴을 가린 채 법정에 나왔다고 말했다. |
| **This model** | 찬드라 셰카르 솔랑키 경찰서장은 피고인이 얼굴을 가린 채 법정에 나왔다고 말했다. |

**Example 3**

<audio controls src="https://huggingface.co/TeamUNIVA/qwen3_asr_1.7b_ko/resolve/main/audio/example_3.wav"></audio>

| Model | Transcription |
| --- | --- |
| Reference | 그리고 이 나무는 태즈메이니아 남부 지역에 부는 남극의 바람을 맞으면서도 또한 해안에 위치한 산간 지방의 안개가 많은 환경에서도 무성하게 자랍니다 |
| Qwen3-ASR-1.7B (base) | 그리고 이 나무는 텍사스 메인 이아 남부 지역에 부는 남극의 바람을 맞으면서도 또한 해안에 위치한 상간 지방의 안개가 많은 환경에서도 무성하게 자랍니다. |
| qwen3_asr_1.7b_ko_beta | 그리고 이 나무는 테즈메인 이하 남부 지역에 부는 남극의 바람을 맞으면서도 또한 해안에 위치한 상간 지방의 안개가 많은 환경에서도 무성하게 자랍니다. |
| **This model** | 그리고 이 나무는 테즈메이니아 남부 지역에 부는 남극의 바람을 맞으면서도 또한 해안에 위치한 상간 지방의 안개가 많은 환경에서도 무성하게 자랍니다. |

**Example 4**

<audio controls src="https://huggingface.co/TeamUNIVA/qwen3_asr_1.7b_ko/resolve/main/audio/example_4.wav"></audio>

| Model | Transcription |
| --- | --- |
| Reference | 근데 경쟁률이 올라가잖아. |
| Qwen3-ASR-1.7B (base) | 그때 경준이 올라가잖아. |
| qwen3_asr_1.7b_ko_beta | 근데 경신이 올라가잖아. |
| **This model** | 근데 경쟁률이 올라가잖아. |

**Example 5**

<audio controls src="https://huggingface.co/TeamUNIVA/qwen3_asr_1.7b_ko/resolve/main/audio/example_5.wav"></audio>

| Model | Transcription |
| --- | --- |
| Reference | 그 이미지 처리로 우리 아버지가 취미가 물고기 기르는 기르는 거잖아. |
| Qwen3-ASR-1.7B (base) | 그 이미지 처리로 우리 아버지가 취미가 무국이 기르는 거잖아. |
| qwen3_asr_1.7b_ko_beta | 그 이미지 처리로 우리 아버지가 취미가 무국이 기르는 기르는 거잖아. |
| **This model** | 그 이미지 처리로 우리 아버지가 취미가 물고기 기르 기르는 거잖아. |

**Example 6**

<audio controls src="https://huggingface.co/TeamUNIVA/qwen3_asr_1.7b_ko/resolve/main/audio/example_6.wav"></audio>

| Model | Transcription |
| --- | --- |
| Reference | 토트 토트넘은 언제 경기하냐? |
| Qwen3-ASR-1.7B (base) | 도토 도토나면 언제 경기하냐? |
| qwen3_asr_1.7b_ko_beta | 토트 토트넘 언제 경기하냐? |
| **This model** | 토트 토트넘은 언제 경기하냐? |

**Example 7**

<audio controls src="https://huggingface.co/TeamUNIVA/qwen3_asr_1.7b_ko/resolve/main/audio/example_7.wav"></audio>

| Model | Transcription |
| --- | --- |
| Reference | 제가 주차를 잘 못해서 서초점은 발레파킹이 안된다고 하는데, 거기 지점은 되나요? |
| Qwen3-ASR-1.7B (base) | 제가 주차를 잘 못해서 섭초잡은 발렛 파킹이 안 된다고 하는데 거기 지점은 되나요? |
| qwen3_asr_1.7b_ko_beta | 제가 주차를 잘 못해서 서초잡은 발레파킹이 안된다고 하는데 거기 지점은 되나요? |
| **This model** | 제가 주차를 잘 못해서 서초점은 발레파킹이 안 된다고 하는데 거기 지점은 되나요? |

## Training

Starting from `TeamUNIVA/qwen3_asr_1.7b_ko_beta` (itself an SFT-only fine-tune of `Qwen/Qwen3-ASR-1.7B`), the model was trained with full-parameter updates in four sequential stages, using [ms-swift](https://github.com/modelscope/ms-swift):

| Stage | Method |
| --- | --- |
| 1 | SFT |
| 2 | RL (GSPO) |
| 3 | SFT |
| 4 | RL (GSPO) |

The RL stages use GSPO (Group Sequence Policy Optimization) with a reward based on the character error rate of the sampled transcription against the reference.

## Usage

Uses the same `qwen-asr` package as the base model.

```bash
pip install -U qwen-asr
```

```python
import torch
from qwen_asr import Qwen3ASRModel

model = Qwen3ASRModel.from_pretrained(
    "TeamUNIVA/qwen3_asr_1.7b_ko",
    dtype=torch.bfloat16,
    device_map="cuda:0",
    max_inference_batch_size=32,
    max_new_tokens=256,
)

results = model.transcribe(
    audio="path/to/audio.wav",
)

print(results[0].text)
```

## Limitations

- This model was fine-tuned specifically for Korean speech recognition; performance on other languages may be similar to the base model or require separate validation. In particular, English (LibriSpeech) WER is slightly higher than that of the base model (0.0277 vs. 0.0250).
- Evaluation is based on the benchmark datasets listed above; results may differ in real-world production conditions (noise, speaker variability, etc.).

---

<a id="ko"></a>
## 한국어 (Korean)

[English](#en) | **한국어**

이 모델은 `Qwen/Qwen3-ASR-1.7B`를 한국어 음성 데이터로 파인튜닝한 자동 음성 인식(ASR) 모델이며, [`TeamUNIVA/qwen3_asr_1.7b_ko_beta`](https://huggingface.co/TeamUNIVA/qwen3_asr_1.7b_ko_beta)의 후속 모델입니다. beta 모델에서 시작해, 확장된 데이터셋으로 두 차례의 SFT와 강화학습(GSPO)을 추가로 수행했습니다. 한국어 벤치마크 전반에서 기본(base) 모델과 beta 모델보다 낮은 오류율을 보이며, 영어(LibriSpeech)에서는 소폭 하락했습니다(base 모델 대비 WER +0.27 %p).

## 평가 결과

한국어는 CER(문자 오류율), 영어는 WER(단어 오류율)로 측정했으며, 두 지표 모두 낮을수록 좋습니다. 점수는 텍스트 정규화(구두점 제거, 소문자화; LibriSpeech는 Whisper 영어 normalizer 사용) 후 계산했습니다. "변화" 열은 base 모델 대비입니다.

<table>
  <thead>
    <tr>
      <th align="left">데이터셋</th>
      <th>지표</th>
      <th>Qwen3-ASR-1.7B (base)</th>
      <th>qwen3_asr_1.7b_ko_beta</th>
      <th>본 모델</th>
      <th>변화 (%p)</th>
    </tr>
  </thead>
  <tbody>
    <tr><td>clova_call</td><td>CER</td><td>0.0448</td><td>0.0293</td><td><b>0.0283</b></td><td>-1.65</td></tr>
    <tr><td>common_voice_ko</td><td>CER</td><td>0.0719</td><td>0.0628</td><td><b>0.0603</b></td><td>-1.16</td></tr>
    <tr><td>fleurs_ko</td><td>CER</td><td>0.0142</td><td>0.0138</td><td><b>0.0126</b></td><td>-0.16</td></tr>
    <tr><td>ksponspeech</td><td>CER</td><td>0.0865</td><td>0.0670</td><td><b>0.0594</b></td><td>-2.71</td></tr>
    <tr><td>zeroth</td><td>CER</td><td>0.0264</td><td>0.0230</td><td><b>0.0220</b></td><td>-0.44</td></tr>
    <tr>
      <td style="background-color:#e3edf5; color:#000000;"><b>한국어 전체</b></td>
      <td style="background-color:#e3edf5; color:#000000;">CER</td>
      <td style="background-color:#e3edf5; color:#000000;"><b>0.0686</b></td>
      <td style="background-color:#e3edf5; color:#000000;"><b>0.0537</b></td>
      <td style="background-color:#e3edf5; color:#000000;"><b>0.0483</b></td>
      <td style="background-color:#e3edf5; color:#000000;"><b>-2.03</b></td>
    </tr>
    <tr><td>librispeech (영어, 참고용)</td><td>WER</td><td>0.0250</td><td>0.0246</td><td>0.0277</td><td>+0.27</td></tr>
  </tbody>
</table>

### kocer를 이용한 추가 평가

[kocer](https://github.com/Choi-kwan-u/kocer)(v0.1.5)는 띄어쓰기, 문장부호, 숫자 표기(예: 3개 = 세 개), 라틴 약어 표기(예: AI = 에이아이)의 차이를 오류로 세지 않는 한국어 음성 인식용 CER입니다. 위와 동일한 검수 평가셋에서 같은 모델 출력을 kocer로 다시 채점했습니다. 위와 마찬가지로 각 발화를 TN 전사와 ITN 전사 각각에 대해 채점하고 더 좋은 쪽을 사용했습니다. 낮을수록 좋으며, "변화" 열은 base 모델 대비입니다.

<table>
  <thead>
    <tr>
      <th align="left">데이터셋</th>
      <th>지표</th>
      <th>Qwen3-ASR-1.7B (base)</th>
      <th>qwen3_asr_1.7b_ko_beta</th>
      <th>본 모델</th>
      <th>변화 (%p)</th>
    </tr>
  </thead>
  <tbody>
    <tr><td>clova_call</td><td>CER (kocer)</td><td>0.0429</td><td>0.0280</td><td><b>0.0264</b></td><td>-1.65</td></tr>
    <tr><td>common_voice_ko</td><td>CER (kocer)</td><td>0.0718</td><td>0.0628</td><td><b>0.0602</b></td><td>-1.16</td></tr>
    <tr><td>fleurs_ko</td><td>CER (kocer)</td><td>0.0127</td><td>0.0125</td><td><b>0.0112</b></td><td>-0.15</td></tr>
    <tr><td>ksponspeech</td><td>CER (kocer)</td><td>0.0860</td><td>0.0664</td><td><b>0.0585</b></td><td>-2.75</td></tr>
    <tr><td>zeroth</td><td>CER (kocer)</td><td>0.0253</td><td>0.0202</td><td><b>0.0194</b></td><td>-0.59</td></tr>
    <tr>
      <td style="background-color:#e3edf5; color:#000000;"><b>한국어 전체</b></td>
      <td style="background-color:#e3edf5; color:#000000;">CER (kocer)</td>
      <td style="background-color:#e3edf5; color:#000000;"><b>0.0679</b></td>
      <td style="background-color:#e3edf5; color:#000000;"><b>0.0528</b></td>
      <td style="background-color:#e3edf5; color:#000000;"><b>0.0472</b></td>
      <td style="background-color:#e3edf5; color:#000000;"><b>-2.07</b></td>
    </tr>
  </tbody>
</table>

위 지표와 순위는 동일합니다. kocer 점수는 어느 전사를 정답으로 쓰는지에 거의 좌우되지 않습니다. 본 모델의 한국어 전체는 TN 전사만 사용하면 0.0481, ITN 전사만 사용하면 0.0491, 둘 중 더 좋은 쪽을 쓰면 0.0472입니다.

### 평가셋

위에서 사용한 공개 한국어 벤치마크 평가셋은 모두 사람이 전수 검수했습니다. 각 발화마다 TN/ITN(텍스트 정규화 / 역정규화) 이중 전사 여부를 확인하고, 품질이 낮은 샘플은 제외하고, 오전사는 수정했습니다. 이후 모든 발화를 TN 전사와 ITN 전사 각각에 대해 평가하고, 둘 중 점수가 더 좋은 쪽을 최종 집계에 사용했습니다. 검수 후 원본 8,489건 중 8,383건이 남았습니다(106건 제외).

| 데이터셋 | 유지된 레코드 수 |
| --- | --- |
| clova_call | 1,083 |
| common_voice_ko | 564 |
| fleurs_ko | 382 |
| zeroth | 449 |
| kspon_eval_clean | 2,946 |
| kspon_eval_other | 2,959 |
| **합계** | **8,383** |

**공개 안내.** 검수를 마친 평가셋 중 `zeroth`, `common_voice_ko`, `fleurs_ko`는 [TeamUNIVA/ko_asr_benchmarks](https://huggingface.co/datasets/TeamUNIVA/ko_asr_benchmarks)에 공개했습니다. 나머지(`clova_call`, `kspon_eval_clean`, `kspon_eval_other`)는 원본 데이터셋의 라이선스 조건상 공개하지 않습니다.

## 예시

모델별(base → beta → 본 모델) 실제 인식 결과가 어떻게 달라지는지 보여주는 예시입니다. 각 예시에는 오디오가 함께 제공되며(이 저장소의 `audio/` 폴더), 표 위의 플레이어로 들어볼 수 있습니다.

**예시 1**

<audio controls src="https://huggingface.co/TeamUNIVA/qwen3_asr_1.7b_ko/resolve/main/audio/example_1.wav"></audio>

| 모델 | 전사 결과 |
| --- | --- |
| 정답 | 범어네거리에서 걸어가면 가까운가요? |
| Qwen3-ASR-1.7B (base) | 버머네거리에서 걸어가면 가까운가요? |
| qwen3_asr_1.7b_ko_beta | 범어내거리에서 걸어가면 가까운가요? |
| **본 모델** | 범어네거리에서 걸어가면 가까운가요? |

**예시 2**

<audio controls src="https://huggingface.co/TeamUNIVA/qwen3_asr_1.7b_ko/resolve/main/audio/example_2.wav"></audio>

| 모델 | 전사 결과 |
| --- | --- |
| 정답 | 찬드라 셰카르 솔랑키 경찰서장은 피고인이 얼굴을 가린 채 법정에 나왔다고 말했다. |
| Qwen3-ASR-1.7B (base) | 찬드라 시에카르 솔랑키 경찰서장은 피고인이 얼굴을 가린 채 법정에 나왔다고 말했다. |
| qwen3_asr_1.7b_ko_beta | 찬드라 샤카르 솔랑키 경찰서장은 피고인이 얼굴을 가린 채 법정에 나왔다고 말했다. |
| **본 모델** | 찬드라 셰카르 솔랑키 경찰서장은 피고인이 얼굴을 가린 채 법정에 나왔다고 말했다. |

**예시 3**

<audio controls src="https://huggingface.co/TeamUNIVA/qwen3_asr_1.7b_ko/resolve/main/audio/example_3.wav"></audio>

| 모델 | 전사 결과 |
| --- | --- |
| 정답 | 그리고 이 나무는 태즈메이니아 남부 지역에 부는 남극의 바람을 맞으면서도 또한 해안에 위치한 산간 지방의 안개가 많은 환경에서도 무성하게 자랍니다 |
| Qwen3-ASR-1.7B (base) | 그리고 이 나무는 텍사스 메인 이아 남부 지역에 부는 남극의 바람을 맞으면서도 또한 해안에 위치한 상간 지방의 안개가 많은 환경에서도 무성하게 자랍니다. |
| qwen3_asr_1.7b_ko_beta | 그리고 이 나무는 테즈메인 이하 남부 지역에 부는 남극의 바람을 맞으면서도 또한 해안에 위치한 상간 지방의 안개가 많은 환경에서도 무성하게 자랍니다. |
| **본 모델** | 그리고 이 나무는 테즈메이니아 남부 지역에 부는 남극의 바람을 맞으면서도 또한 해안에 위치한 상간 지방의 안개가 많은 환경에서도 무성하게 자랍니다. |

**예시 4**

<audio controls src="https://huggingface.co/TeamUNIVA/qwen3_asr_1.7b_ko/resolve/main/audio/example_4.wav"></audio>

| 모델 | 전사 결과 |
| --- | --- |
| 정답 | 근데 경쟁률이 올라가잖아. |
| Qwen3-ASR-1.7B (base) | 그때 경준이 올라가잖아. |
| qwen3_asr_1.7b_ko_beta | 근데 경신이 올라가잖아. |
| **본 모델** | 근데 경쟁률이 올라가잖아. |

**예시 5**

<audio controls src="https://huggingface.co/TeamUNIVA/qwen3_asr_1.7b_ko/resolve/main/audio/example_5.wav"></audio>

| 모델 | 전사 결과 |
| --- | --- |
| 정답 | 그 이미지 처리로 우리 아버지가 취미가 물고기 기르는 기르는 거잖아. |
| Qwen3-ASR-1.7B (base) | 그 이미지 처리로 우리 아버지가 취미가 무국이 기르는 거잖아. |
| qwen3_asr_1.7b_ko_beta | 그 이미지 처리로 우리 아버지가 취미가 무국이 기르는 기르는 거잖아. |
| **본 모델** | 그 이미지 처리로 우리 아버지가 취미가 물고기 기르 기르는 거잖아. |

**예시 6**

<audio controls src="https://huggingface.co/TeamUNIVA/qwen3_asr_1.7b_ko/resolve/main/audio/example_6.wav"></audio>

| 모델 | 전사 결과 |
| --- | --- |
| 정답 | 토트 토트넘은 언제 경기하냐? |
| Qwen3-ASR-1.7B (base) | 도토 도토나면 언제 경기하냐? |
| qwen3_asr_1.7b_ko_beta | 토트 토트넘 언제 경기하냐? |
| **본 모델** | 토트 토트넘은 언제 경기하냐? |

**예시 7**

<audio controls src="https://huggingface.co/TeamUNIVA/qwen3_asr_1.7b_ko/resolve/main/audio/example_7.wav"></audio>

| 모델 | 전사 결과 |
| --- | --- |
| 정답 | 제가 주차를 잘 못해서 서초점은 발레파킹이 안된다고 하는데, 거기 지점은 되나요? |
| Qwen3-ASR-1.7B (base) | 제가 주차를 잘 못해서 섭초잡은 발렛 파킹이 안 된다고 하는데 거기 지점은 되나요? |
| qwen3_asr_1.7b_ko_beta | 제가 주차를 잘 못해서 서초잡은 발레파킹이 안된다고 하는데 거기 지점은 되나요? |
| **본 모델** | 제가 주차를 잘 못해서 서초점은 발레파킹이 안 된다고 하는데 거기 지점은 되나요? |

## 학습

`TeamUNIVA/qwen3_asr_1.7b_ko_beta`(그 자체로 `Qwen/Qwen3-ASR-1.7B`를 SFT만으로 파인튜닝한 모델)에서 시작해, [ms-swift](https://github.com/modelscope/ms-swift)를 사용하여 전체 파라미터를 업데이트하는 4단계를 순차적으로 학습했습니다.

| 단계 | 방법 |
| --- | --- |
| 1 | SFT |
| 2 | RL (GSPO) |
| 3 | SFT |
| 4 | RL (GSPO) |

RL 단계는 GSPO(Group Sequence Policy Optimization)를 사용하며, 샘플링한 전사 결과의 정답 대비 문자 오류율을 보상으로 삼습니다.

## 사용법

base 모델과 동일한 `qwen-asr` 패키지를 사용합니다.

```bash
pip install -U qwen-asr
```

```python
import torch
from qwen_asr import Qwen3ASRModel

model = Qwen3ASRModel.from_pretrained(
    "TeamUNIVA/qwen3_asr_1.7b_ko",
    dtype=torch.bfloat16,
    device_map="cuda:0",
    max_inference_batch_size=32,
    max_new_tokens=256,
)

results = model.transcribe(
    audio="path/to/audio.wav",
)

print(results[0].text)
```

## 한계

- 이 모델은 한국어 음성 인식에 특화되어 파인튜닝되었습니다. 다른 언어에서의 성능은 base 모델과 비슷하거나 별도 검증이 필요할 수 있습니다. 특히 영어(LibriSpeech) WER은 base 모델보다 약간 높습니다(0.0277 vs. 0.0250).
- 평가는 위에 나열한 벤치마크 데이터셋을 기준으로 하며, 실제 운영 환경(소음, 화자 편차 등)에서는 결과가 다를 수 있습니다.
