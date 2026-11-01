---
language:
- vi
- en
- ru
- fr
- zh
- yue
- de
- ja
- ko
- hi
- uk
license: gemma
tags:
- vietnamese
- translation
- multilingual
- gemma
- low-resource
- ancient-chinese
- buddhist-texts
- llama.cpp
- vllm
- gguf
base_model:
- google/gemma-3-4b-it
- erax-ai/EraX-Translator-V1.0
model-index:
- name: EraX-Translator-V1.0
  results: []
---

<p align="left">
  <img src="https://cdn-uploads.huggingface.co/production/uploads/63d8d8879dfcfa941d4d7cd9/GsQKdaTyn2FFx_cZvVHk3.png" alt="Logo">
</p>

# EraX-Translator-V1.0: A Compact and Capable Multilingual Translation Model

This repository provides GGUF-formatted versions of the EraX-Translator-V1.0 model, optimized for use with platforms such as Ollama, LM-Studio, vLLM, and llama.cpp. Performance testing was conducted on a MacBook M3.

Available Quantizations and Performance:

*   **BF16:** *EraX-Translator-V1.0-BF16.gguf* - Offers excellent quality, achieving 24 tokens per second (toks/s) and requiring 16GB of VRAM.
*   **Q8_0:** *EraX-Translator-V1.0-Q8_0.gguf* - Delivers good quality at a speed of 61 toks/s, utilizing 6GB of VRAM.
*   **Q6_K:** *EraX-Translator-V1.0-Q6_K.gguf* - Presents a balanced approach, providing a fast 70 toks/s with a VRAM footprint of 4GB.
*   **Q5_K_M:** *EraX-Translator-V1.0-Q5_K_M.gguf* - Offers a good balance between speed and resource usage, achieving 75 toks/s and requiring 3.2GB of VRAM.
*   **Q4_K_M:** *EraX-Translator-V1.0-Q4_K_M.gguf* - Prioritizes speed, reaching 80 toks/s with a minimal VRAM requirement of 2.6GB. Note that this quantization level may impact output quality.

<p align="center">
  <video controls>
  <source src="https://huggingface.co/erax-ai/EraX-Translator-V1.0-GGUF/resolve/main/My%20Video-1.mp4?download=true" type="video/mp4">
  <p align="center"><em>EraX Translator V1.0 run with LM Studio, quantization Q6_K</em></p>
</video>
</p>

For enhanced performance and load balancing, consider leveraging **vLLM** as an alternative to a standalone llama.cpp server.
You shoud also **install or upgrade to all the latest packages**:

```
# Build llama.cpp from latest source https://github.com/ggml-org/llama.cpp.git
# Update packages:
sudo apt install ollama
pip install llama-cpp-python -U
pip install llama-cpp-python[server]
pip install git+https://github.com/huggingface/transformers@v4.49.0-Gemma-3 or
pip install git+https://github.com/huggingface/transformers
pip install vllm==0.7.3
```

EraX-Translator-V1.0 is a compact, Gemma3-4B-based multilingual translation model designed for efficient deployment and high throughput, even on resource-constrained hardware.  We aim to provide a practical tool for a wide range of translation tasks, with a particular focus on languages where high-quality data and models are less readily available.

## Model Description

This model leverages the architectural strengths of the Gemma3-4B foundation model (4 trillion tokens, 140 languages pretrained) and has been fine-tuned for translation across a diverse set of languages.  A key feature is its ability to translate Classical Chinese, demonstrating potential utility in translating Buddhist texts and other historical documents.

**Key features:**
*   **Compact Size:** Based on the Gemma3-4B architecture, the model can be efficiently deployed on devices with limited resources.
*   **High Throughput:** Achieves approximately 80 tokens/s (bfloat16) using vLLM with ~20GB VRAM.  Potential for **>100 tokens/s with GGUF 6bit quantization on better GPU** (though optimal llama.cpp support for Gemma3 is still under development).

*   **Multilingual:** Trained on a diverse dataset to support translation **between - bidirectional** multiple languages.
      - Việt Nam 🇻🇳
      - English 🇬🇧 / 🇺🇸 
      - Chinese 🇨🇳
      - Cantonese 🇨🇳 / 🇭🇰
      - Ancient Chinese (Cổ Văn Trung Hoa 古典文學, Kinh Phật cổ 古佛經) 🇨🇳 📜
      - Russian 🇷🇺
      - Ukrainian 🇺🇦
      - French 🇫🇷
      - German 🇩🇪
      - Dutch 🇳🇱
      - Korean 🇰🇷
      - Japanese 🇯🇵
      - Hindi 🇮🇳

*   **Classical Chinese Translation:**  Demonstrates proficiency in translating Classical Chinese, particularly Buddhist texts.

## Intended Uses

This model is intended for:

*   General-purpose multilingual translation.
*   Translation of Classical Chinese texts, particularly those related to Buddhism.
*   Research and experimentation in low-resource machine translation.
*   Deployment in applications where computational resources are limited.
*   Overcome Google Translate suboptimal quality

## Training Data & Training Strategy: 

The model was trained on approximately **8 million multilingual samples**.  This data includes:

*   Publicly available translation datasets.
*   Datasets from public Hugging Face repositories.
*   A substantial portion of the training data was synthetically generated using Gemmini.
*   **A significant contribution of 15,000 samples of translated Buddhist texts from Classical Chinese to Vietnamese, generously provided by experts in Han-Nom from the [Trần Nhân Tông Institute](https://tnti.vnu.edu.vn/), Vietnam National University, Hanoi.**  We are deeply grateful for their invaluable contribution.
*   To optimize the efficiency and performance of EraX-Translator-V1.0, we explored selective parameter freezing rather than employing Low-Rank Adaptation (`LoRA`), which yielded suboptimal results in preliminary experiments. Guided by the **Signal-to-Noise Ratio (SNR) metric** proposed in [SNR paper: https://arxiv.org/pdf/2406.06623], we identified the most salient layers within the Gemma3-4B architecture for retention. Specifically, we computed the SNR for each layer, excluding the `vision_tower` module and the feedforward network layers `fc1` and `fc2`. We then selectively **retained the 50% of layers exhibiting the highest SNR values**, including `embed_tokens` layer, and freezing the remaining parameters. This methodology resulted in a significant improvement in translation quality compared to LoRA-based fine-tuning, suggesting that targeted parameter retention based on SNR is an effective strategy for resource-efficient adaptation of large language models for translation tasks.
*   The model underwent training for 2 epochs with a global batch size of 384. Training was performed on a distributed system comprised of 4 NVIDIA H100 NVL GPUs, each equipped with 94 GB of memory.

## Evaluation

While comprehensive evaluation is ongoing, preliminary results indicate strong performance in a variety of translation tasks. We are actively working to benchmark the model against established translation models and will release detailed evaluation metrics as soon as they are available.  We encourage the community to contribute to the evaluation process.

**Known Limitations:**

*   As with any machine translation model, EraX-Translator-V1.0 may produce errors or generate translations that are not entirely accurate or fluent.
*   Performance may vary depending on the specific language pair and the complexity of the text being translated.
*   While the model shows promise in translating Classical Chinese, further refinement may be necessary to achieve optimal results.
*   This model can only be used for translation
*   This model was not trained for translating math LaTeX & coding
*   The model works best for context length (text to be translated mostly) not exceeding 1024 tokens or **++800 Vietnamese words (1 A4 page)** in one go !

## Usage

Here's a few examples:

  ```
  temperature 0.2
  top_p 0.95
  frequency penalty: 1.05
  top_k: 64
  min_p: 0.1
  With max tokens < 1024 works best!
  ```

  * **English → Việt & French:**
  ```
  “China and the US are now direct rivals in reshaping the international trade order,” said another, Ju Jiandong, a professor at the People’s Bank of China School of Finance of Tsinghua University. “We’re willing to take on the challenge – we’re ready to compete with the US in redefining the new global trade system.”. China’s trade partners are likely to take such messaging with a grain of salt.
  Beijing is well known to have wielded access to its massive market as a weapon to coerce countries, often over political stances that sparked Beijing’s ire. Many will also be looking warily at whether Chinese exports will flood their own markets, hurting their own domestic production or driving down consumer prices.
  But countries may have little choice but to look to strengthen ties with China if US tariffs, which hit American allies as well as rivals, become the new normal.
  Beijing over the past month held economic talks with Japan and South Korea, hit last week with 24% and 25% tariffs respectively, as well as with the European Union, which was slapped with 20% duties.
  Many Southeast Asian economies – key manufacturing hubs for companies looking to diversify away from China – have been hit particularly hard by Trump’s tariff war. While few want to pick a fight with Washington publicly, the region is rattled.

  → Việt Nam: "Trung Quốc và Mỹ hiện là các đối thủ trực tiếp trong việc định hình lại trật tự thương mại quốc tế", một người khác, Ju Jiandong, giáo sư tại Trường Tài chính Ngân hàng Nhân dân của Đại học Thanh Hoa, nói. "Chúng tôi sẵn sàng chấp nhận thử thách - chúng tôi đã sẵn sàng cạnh tranh với Mỹ trong việc xác định lại hệ thống thương mại toàn cầu mới.". 
  Các đối tác thương mại của Trung Quốc có thể sẽ xem nhẹ thông điệp như vậy. Bắc Kinh nổi tiếng là đã sử dụng quyền tiếp cận thị trường khổng lồ của mình như một vũ khí để ép buộc các nước, thường là vì lập trường chính trị gây phẫn nộ ở Bắc Kinh. Nhiều người cũng sẽ cảnh giác về việc liệu hàng xuất khẩu của Trung Quốc có làm tràn ngập thị trường của họ, ảnh hưởng đến sản xuất trong nước của họ hay đẩy giá tiêu dùng xuống hay không.
  Nhưng các quốc gia có thể ít có lựa chọn nào khác ngoài việc tìm cách tăng cường quan hệ với Trung Quốc nếu thuế quan của Mỹ, áp dụng cho các đồng minh cũng như đối thủ của Mỹ, trở thành xu hướng mới. Bắc Kinh trong tháng qua đã tổ chức các cuộc đàm phán kinh tế với Nhật Bản và Hàn Quốc, đạt mức 24% và 25% mức thuế tương ứng vào tuần trước, cũng như với Liên minh châu Âu, vốn đã áp thuế 20%. Nhiều nền kinh tế Đông Nam Á - trung tâm sản xuất quan trọng của các công ty đang tìm cách đa dạng hóa khỏi Trung Quốc - đã bị ảnh hưởng đặc biệt nặng nề bởi cuộc chiến thuế quan của Trump.
  Trong khi một số ít muốn công khai gây chiến với Washington, khu vực này đang bối rối.

  → French: "La Chine et les États-Unis sont maintenant des rivaux directs dans le remodelage de l'ordre commercial international," a déclaré un autre, Ju Jiandong, professeur à la Banque populaire de Chine, École des finances de l'Université Tsinghua. "Nous sommes prêts à relever le défi - nous sommes prêts à concourir avec les États-Unis pour redéfinir le nouveau système commercial mondial."
  Les partenaires commerciaux de la Chine ont probablement pris un message de cette manière avec un grain de sel.
  Pékin est bien connu pour avoir utilisé son accès à son marché vaste comme un moyen de coercition pour les pays, souvent sur des positions politiques qui ont provoqué l'indignation de Pékin. Beaucoup d'entre eux s'examineront également attentivement pour voir si les exportations chinoises inonderont leurs propres marchés, en nuisiraient à leur production domestique ou en feraient baisser les prix à la consommation.
  Mais les pays pourraient avoir peu de choix que de chercher à renforcer les liens avec la Chine si les tarifs américains, qui touchent aussi bien les alliés qu'les rivaux américains, deviennent la nouvelle norme.
  Pékin a tenu le mois dernier des négociations économiques avec le Japon et la Corée du Sud, respectivement frappés en semaine dernière par des tarifs de 24 % et 25 %, ainsi que avec l'Union européenne, qui a été frappée par des droits de douane de 20 %.
  Nombre d'économies d'Asie du Sud-Est – principaux centres de fabrication pour les entreprises cherchant à diversifier en dehors de la Chine – ont été particulièrement durement touchées par la guerre tarifaire de Trump. Bien que peu aient voulu engager un combat public avec Washington, la région est en proie au tumulte. 
  ```

  * **English to 9 others**:
  ```
  "She's your queen to be!"

  "Cô ấy sẽ là nữ hoàng của bạn!"
  "她是你的皇后！"
  "Она твоя королева!""
  "Elle sera ta reine !"
  "Sie ist Ihre Königin zu werden!"
  그녀는 당신의 여왕이 될 거예요!
  彼女はあなた様の未来の女王になるでしょう！
  वह तुम्हारी रानी बनने वाली है!
  "Zij is jouw koningin te worden!"
  ```

  * **Việt → Russian**
  ```
  Đối với Mỹ, Việt Nam là nước xuất siêu lớn thứ ba. Hơn nữa, dưới mắt của Mỹ, Việt Nam là nước trung chuyển hàng công nghiệp xuất từ Trung Quốc vì hàng công nghiệp xuất khẩu của Việt Nam có hàm lượng nhập khẩu hàng sơ chế, linh kiện và nhiều sản phẩm trung gian khác từ Trung Quốc rất cao. Ngoài ra, từ khi Mỹ có chính sách áp thuế và kiềm chế Trung Quốc (từ 2018), đầu tư trực tiếp (FDI) của Trung Quốc sang Việt Nam ngày càng nhiều.

  → США являются третьим по величине экспортером в Вьетнам. Кроме того, в США Вьетнам рассматривается как страна конвертации экспортных товаров из Китая, поскольку доля импорта сырья, полуфабрикатов и промежуточных продукции из Китая очень высока. К тому же, с момента начала политики США, направленной против Китая (с 2018 года), инвестиции Китая в Вьетнам растут.
  ```

  * **Việt → French**
  ```
  Chính quyền ông Trump đã cảnh báo các nước khác không trả đũa sau khi công bố chính sách thuế quan mới vào tuần trước.
  Nhiều quốc gia, bao gồm Nhật Bản, bày tỏ sẵn sàng đàm phán về thuế quan, nhưng Trung Quốc đang có lập trường cứng rắn hơn.
  Các động thái trả đũa thuế quan liên tục có nguy cơ khiến hoạt động thương mại giữa 2 nền kinh tế quan trọng nhất thế giới bị đình trệ, tờ CNBC nhận định.
  Trước động thái mới nhất của Trung Quốc, chứng khoán tương lai Mỹ giảm mạnh.
  Chỉ số công nghiệp trung bình Dow Jones giảm gần 560 điểm, tương đương 1,5%. S&P giảm 1,3% còn Nasdaq 100 giảm 0,9%.

  → L'administration Trump a averti d'autres pays de ne pas riposter après avoir annoncé sa nouvelle politique tarifaire la semaine dernière.
  De nombreux pays, dont le Japon, ont exprimé leur volonté de négocier sur les droits de douane, mais la Chine adopte une position plus ferme.
  Les mesures retaliatoires tarifaires répétées risquent de freiner le commerce entre les deux economies les plus importantes du monde, selon CNBC.
  Suite à la nouvelle action de la Chine, les contrats boursiers américains ont chuté de manière significative.
  L'indice industrial moyen Dow Jones a baissé de près de 560 points, soit 1,5 %. Le S&P a chuté de 1,3 % et le Nasdaq 100 de 0,9 %.
  ```

  * **German → Việt:**

  ```
  Trumps so überraschende wie knappe Ankündigung in den sozialen Medien ließ viele Fragen offen.
  Seinen Schwenk begründete der US-Präsident später etwas wortreicher.
  Er verwies dabei auf die wachsende Nervosität der anderen. So kann man die wachsende Angst vor einer Rezession und globaler Wirtschaftskrise natürlich auch umschreiben.
  Die »Leute« seien etwas unruhig und »ein bisschen ängstlich« geworden, sagte Trump lapidar bei einer Veranstaltung vor dem Weißen Haus auf die Frage nach seinen Beweggründen für den jüngsten Kurswechsel in der Handelspolitik.
  »Man muss flexibel sein.«

  → Thông báo gây sốc đột ngột này trên mạng xã hội đã để lại nhiều câu hỏi chưa có lời giải đáp. Tổng thống Mỹ sau đó đã giải thích động cơ của mình một cách dài dòng hơn.
  Ông ta chỉ ra sự lo lắng ngày càng tăng của những người khác. Điều này tất nhiên có thể diễn đạt lại nỗi sợ hãi ngày càng tăng về suy thoái kinh tế và khủng hoảng kinh tế toàn cầu.
  "Mọi người" đã trở nên hơi bồn chồn và "hơi lo lắng", Trump nói ngắn gọn tại một sự kiện trước Nhà Trắng khi trả lời câu hỏi về động cơ đổi hướng gần đây trong chính sách thương mại: "Phải linh hoạt".
  ```
  
  * **Ancient Chinese (Cổ văn) → Việt:**
  ```
  《長部經典》：「於久遠之前，於十五日布薩之滿月夜，三十三天之諸天，皆集會於善法堂，天人之大會眾，徧坐於週遭，四天王就坐於四方：東方持國天王於諸天之前，向西而坐；南方增長天王於諸天之前，向北而坐；西方廣目天王於諸天之前，向東而坐；北方多聞天王於諸天之前，向南而坐。世尊！三十三天之諸天，皆集會於善法堂，天人之大會眾，徧坐於週遭，四大天王坐於四方，此是彼等〔四天王〕之坐法；然後乃我等之座。世尊！曾於世尊之處修梵行而新生於三十三天之天眾，容貌與光輝，比其他天眾殊勝光耀，世尊！是故三十三天之諸天，歡喜、悅樂、喜悅、滿足言：『實然！諸天眾在增盛，阿修羅眾在衰減。

  →  Trong kinh Trường Bộ, chúng tôi nghe như vầy:
    - Thuở xưa rất xa, vào ngày rằm trăng tròn, có đại hội chư Thiên cõi trời Ba Mươi Ba họp tại Thiện pháp đường, đại chúng của chư Thiên ở xung quanh, Tứ Đại Thiên Vương ngồi ở bốn phương: Đấng Trì Quốc Thiên Vương ở phía trước chư Thiên hướng về Tây; Đấng Tăng Trưởng Thiên Vương ở trước chư Thiên hướng về Bắc; Đấng Quảng Mục Thiên Vương ở trước chư Thiên hướng về Đông; Đấng Đa Văn Thiên Vương ở trước chư Thiên hướng về Nam.
      Này Thế Tôn! Chư Thiên ở Ba Mươi Ba tập hợp tại Thiện pháp đường, đại chúng của chư Thiên ở xung quanh, Tứ Đại Thiên Vương ngồi ở bốn phương, đây là cách an tọa của các Ngài, sau đó mới đến lượt chúng con.
      Này Thế Tôn! Chúng con từng tu hành khổ hạnh ở chỗ Thế Tôn, sau khi tái sinh vào hàng chư Thiên ở cõi trời Ba Mươi Ba, nhan sắc và ánh sáng hơn hẳn chư Thiên khác.
      Này Thế Tôn! Vì thế, chư Thiên ở Ba Mươi Ba vui mừng, hoan hỷ, thỏa mãn và nói: "Thật vậy, số lượng chư Thiên tăng lên, số lượng chúng A Tu La giảm bớt.
  ```

```python

# Install Transformers from main branch to support Gemma3
# pip install git+https://github.com/huggingface/transformers@v4.49.0-Gemma-3
# MAX_JOBS=4 pip install flash-attn --no-build-isolation
# pip install vllm==0.7.3 

import os, torch
os.environ["CUDA_VISIBLE_DEVICES"] = "0"

from transformers import AutoTokenizer, AutoProcessor, Gemma3ForConditionalGeneration, AutoModel
import torch

model_path = "erax-ai/EraX-Translator-V1.0"

model =  Gemma3ForConditionalGeneration.from_pretrained(model_path,
                                        torch_dtype=torch.bfloat16,
                                        attn_implementation="flash_attention_2").to("cuda")
tokenizer =  AutoTokenizer.from_pretrained(model_path)
processor =  AutoProcessor.from_pretrained(model_path)

system_prompt = """Bạn là Trợ lý AI xuất sắc về dịch thuật nhiều ngôn ngữ, đặc biệt tiếng Anh, tiếng Trung Hoa, tiếng Việt. 
Bạn cũng là 1 Hoà thượng Phật giáo uyên thâm về dịch thuật Cổ văn Trung Quốc. Người dùng sẽ giao nhiệm vụ dịch thuật cho bạn từ ngôn ngữ bất kỳ sang một ngôn ngữ được chỉ định.
Nhiệm vụ của bạn là dịch thật sát nghĩa, thể hiện đúng ý của bài gốc và không chế tác hay bịa đặt gì thêm. Đặc biệt lưu ý danh xưng phải giữ nguyên vẹn, dịch đúng tên người, tên địa danh phải tuyệt đối chính xác. Không được bình luận, không được cung cấp lời giới thiệu hay mở bài hay kết luận gì, chỉ dịch thật sát nghĩa và không bỏ qua bất kỳ ý hay từ nào.
"""

system_tag = {
    "role": "system",
    "content": system_prompt
}

to_lang = "Việt"
instruct = f"\nDịch sang tiếng {to_lang}."

to_translate = "三寶者，吾輩塵世之至尊也。夫欲出家者，始亦皈依三寶，繼受五戒，乃至八關齋戒，其後方成沙彌。此誠佛道常軌，凡奉佛國，咸所遵行。吾法華道場亦然。故發宏願：願世世生生，值遇三寶，恭敬供養，依佛聖教，奉行眾善。此即吾等所嚮之鵠的也。"

prompt_in = [
    system_tag,
    {
        "role": "user",
        "content": to_translate + instruct
    }
]


input_ids = tokenizer.apply_chat_template(prompt_in, tokenize=False, add_generation_prompt=True)
input_ids = tokenizer(input_ids, return_tensors="pt").to("cuda")

import time
from transformers import TextIteratorStreamer
from threading import Thread

streamer = TextIteratorStreamer(
        tokenizer,
        skip_prompt=True,
        timeout=5.0,
)

generation_args = {
        "max_length": 8192,
        "streamer": streamer,
        "temperature": 0.2, 
        "top_k": 64, 
        "top_p": 0.95,
        "min_p": 0.0,
        "repetition_penalty": 1.05,
        "do_sample": True,
    }
generation_args.update(input_ids)

thread = Thread(
        target=model.generate,
        kwargs=generation_args,
    )
thread.start()

acc_text = ""
for text_token in streamer:
    #time.sleep(0.04)
    if text_token != tokenizer.eos_token:
        print (text_token, end="", flush=True)
        acc_text += text_token
thread.join()

>>> Tam Bảo là ngôi báu cao quý nhất ở nơi chúng ta sinh sống. Đối với những người xuất gia thì đầu tiên họ xin quy y Tam Bảo, tiếp đó là thọ ngũ giới rồi Bát Quan Trai giới, sau đó họ mới trở thành Sa Di. Đây mới chính là cách thức mà đạo Phật vẫn thường làm, bất kỳ quốc gia nào theo đạo Phật đều làm như vậy. Đạo tràng Pháp Hoa của tác giả cũng là một ví dụ điển hình. Vì thế tác giả đã có lời nguyện rằng: Nguyện đời đời kiếp kiếp gặp được Tam Bảo, tôn kính cúng dường và làm theo lời dạy của đức Phật cùng các thánh tăng, phụng hành mọi điều thiện. Đây chính là mục tiêu hướng đến của chúng ta.

```

## NOTA BENE on instruction for Chinese language:
  Providing this precise instruction, such as "Dịch sang tiếng [specified dialect]", will significantly improve the quality and appropriateness of the translation output. For example, in Vietnamese, "Dịch sang tiếng [Chinese dialect]" will provide better context for accurate translations. 
  Try them out, such as:
  - "Dịch sang tiếng Hoa"
  - "Dịch sang tiếng Chinese"
  - "Dịch sang tiếng Quảng Đông"
  - "Dịch sang tiếng Cantonese"
  - "Dịch sang tiếng Cổ Văn Trung Hoa"

You can also use **vLLM docker** to run to get fatest speed (80 tokens/second) and use Ollama to connect to http://localhost:8005/v1
```
docker pull thusinh1969/vllm_gemma3:latest
docker run --rm -it --entrypoint "/usr/bin/bash" --gpus '"device=1"' -v ./:/models --shm-size=32gb  -p 8005:8000 thusinh1969/vllm_gemma3:latest \
  -c "python3 -m vllm.entrypoints.openai.api_server --dtype auto --max_model_len 4096 --tensor-parallel-size 1 --model /models/gemma3/erax-translator-v1.0" <== check model path
```

## Ethical Considerations

We recognize the potential for misuse of machine translation technology and encourage users to use this model responsibly and ethically.  We are committed to addressing potential biases in the model and improving its fairness and accuracy.

## Acknowledgements

We would like to express our sincere gratitude to:

*   The developers of the Gemma3 family of models.
*   The open-source community for their contributions to the development of machine translation technology.
*   The Trần Nhân Tông Institute, Vietnam National University, Hanoi, for their invaluable contribution of translated Buddhist texts.

## Future Directions

We are actively working to improve the model in the following areas:

*   Expanding the language coverage.
*   Improving the accuracy and fluency of translations.
*   Developing more robust evaluation metrics.
*   Optimizing the model for even greater efficiency.
*   Exploring techniques for mitigating bias.
*   Better supporting llama.cpp.

We welcome feedback from the community and look forward to working together to advance the field of multilingual translation.

## License: 

We are bound with [Google Gemma license](https://ai.google.dev/gemma/terms). You are mostly free to use.

## Citation 📝
If you find our project useful, we would appreciate it if you could star our repository and cite our work as follows:
```
@article{title={EraX-Translatoe-V1.0: A Compact and Capable Multilingual Translation Model},
  author={Nguyễn Anh Nguyên, Hatto & EraX Team},
  organization={Hatto & EraX},
  year={2025},
  url={https://huggingface.co/erax-ai/EraX-Translator-V1.0}
}
```