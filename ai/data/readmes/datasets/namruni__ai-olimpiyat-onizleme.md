---
pretty_name: AI Olimpiyat Soruları — Önizleme
license: other
language: [en, pt, ko, vi, hu, zh, ru]
tags: [artificial-intelligence, olympiad, machine-learning, education, k12, preview]
---

# 🧠 AI Olimpiyat Soruları — Önizleme

**Ortaokul ve lise düzeyi yapay zeka olimpiyatı** sorularından derlenen çok dilli bir veri setinin **halka açık önizlemesi.** Aşağıdaki **56 örnek** sorunun her birinde **orijinal dili** ve hemen **altında Türkçesi** verilmiştir; görsele dayanan sorularda **görsel**, pratik/kod görevlerinde ise **çözüm veya resmî baseline** de dâhildir.

**Kapsanan ülkelerden bir kesit:** 🇮🇳 🇸🇬 🇧🇷 🇰🇷 🇻🇳 🇭🇺 🇨🇳 🇿🇦 🇨🇦 🇷🇺

---

## ℹ️ Bu önizleme neden var?

Dünyanın dört bir yanından (~28 ülke) toplanan **1151 AI olimpiyat sorusunu** künyeli, doğrulanabilir ve model geliştirmeye açık bir kaynağa dönüştürüyoruz. Bu kart, projenin **kapsamını ve soru tarzlarını** şeffaf biçimde göstermek içindir.

## ⏳ Tam veri seti ne zaman açılacak?

Tam veri seti şu an **özeldir (private).** İki süreç sürüyor: **(1) kontrol / doğrulama** ve **(2) Türkçe çeviri.** İkisi tamamlanınca tam veri seti **kamuya açılacaktır.**

## 📊 Kapsam (tam veri setinde)

| | |
|---|---|
| **Toplam soru** | 1138 (kalite denetiminden geçmiş) |
| **Cevap veya çözüm** | **%100** (her soruda cevap ya da çözüm/yaklaşım) |
| **Soru tipi** | çoktan seçmeli · açık uçlu · pratik/kod · kısa cevap |
| **Pratik görevler** | 98/98'i çözüm, **resmî baseline** ya da göreve özel yaklaşımla |
| **Diller** | en, vi, pt, ko, id, hu, ru, pl, zh, el, ro, cs, ja, sr |

---

## 📝 Bölüm 1 — Çoktan Seçmeli Sorular


> ### 1 · 🇮🇳 Hindistan · UAIO 2026
>
> **❓ Soru** · `en`
>
> Which of the following statements is TRUE?
>
> - **A)** A decision tree can only have one branch at each node.
> - **B)** Decision trees cannot be used for classification tasks.
> - **C)** Every path in a decision tree must end at the same leaf node.
> - **D)** Each internal node of a decision tree tests a condition that splits the data further.
>
> **🇹🇷 Türkçe**
>
> Aşağıdaki ifadelerden hangisi DOĞRUDUR?
>
> - **A)** Bir karar ağacı her düğümde yalnızca bir dala sahip olabilir.
> - **B)** Karar ağaçları sınıflandırma görevlerinde kullanılamaz.
> - **C)** Bir karar ağacındaki her yol aynı yaprak düğümde bitmelidir.
> - **D)** Bir karar ağacının her iç düğümü, veriyi daha da bölen bir koşulu test eder.
>
> **✅ Cevap:** **D** — Bir karar ağacının her iç düğümü, veriyi daha da bölen bir koşulu test eder.

---

> ### 2 · 🇮🇳 Hindistan · UAIO 2026
>
> **❓ Soru** · `en`
>
> Which of the following statements is TRUE?
>
> - **A)** Users should always verify AI-generated content before sharing it as fact.
> - **B)** AI systems never make mistakes, so verification is unnecessary.
> - **C)** It is acceptable to present AI-generated work as entirely your own without disclosure.
> - **D)** AI tools are only used by adults and are not relevant to students.
>
> **🇹🇷 Türkçe**
>
> Aşağıdaki ifadelerden hangisi DOĞRUDUR?
>
> - **A)** Kullanıcılar, AI tarafından üretilen içeriği gerçek olarak paylaşmadan önce her zaman doğrulamalıdır.
> - **B)** AI sistemleri asla hata yapmaz, bu yüzden doğrulama gereksizdir.
> - **C)** AI tarafından üretilen çalışmayı, belirtmeden tamamen kendi çalışmanız gibi sunmak kabul edilebilir.
> - **D)** AI araçları yalnızca yetişkinler tarafından kullanılır ve öğrenciler için önemsizdir.
>
> **✅ Cevap:** **A** — Kullanıcılar, AI tarafından üretilen içeriği gerçek olarak paylaşmadan önce her zaman doğrulamalıdır.

---

> ### 3 · 🇸🇬 Singapur · NOAI 2025
>
> **❓ Soru** · `en`
>
> What is the purpose of the "CLS" token in BERT?
>
> - **A)** To serve as a separator between input sentences
> - **B)** To represent the pooled representation of the input for classification tasks
> - **C)** To signal the beginning of each sentence in a sequence
> - **D)** To improve attention mechanism during training
>
> **🇹🇷 Türkçe**
>
> BERT'te "CLS" token'ının amacı nedir?
>
> - **A)** Girdi cümleleri arasında ayırıcı görevi görmek
> - **B)** Sınıflandırma görevleri için girdinin havuzlanmış (pooled) temsilini temsil etmek
> - **C)** Bir dizideki her cümlenin başlangıcını işaret etmek
> - **D)** Eğitim sırasında dikkat (attention) mekanizmasını geliştirmek
>
> **✅ Cevap:** **B** — Sınıflandırma görevleri için girdinin havuzlanmış (pooled) temsilini temsil etmek

---

> ### 4 · 🇸🇬 Singapur · NOAI 2025
>
> **❓ Soru** · `en`
>
> What is the primary function of pooling layers in a CNN?
>
> - **A)** To add non-linearity to the model
> - **B)** To reduce the spatial dimensions of the feature maps
> - **C)** To learn features from the data
> - **D)** To normalize the feature maps
>
> **🇹🇷 Türkçe**
>
> Bir CNN'de havuzlama (pooling) katmanlarının başlıca işlevi nedir?
>
> - **A)** Modele doğrusal olmayanlık (non-linearity) katmak
> - **B)** Öznitelik haritalarının (feature map) uzamsal boyutlarını küçültmek
> - **C)** Veriden öznitelik öğrenmek
> - **D)** Öznitelik haritalarını normalize etmek
>
> **✅ Cevap:** **B** — Öznitelik haritalarının uzamsal boyutlarını küçültmek

---

> ### 5 · 🇸🇬 Singapur · NOAI 2025
>
> **❓ Soru** · `en`
>
> In ensemble methods, what is 'bagging' typically used for?
>
> - **A)** To decrease variance
> - **B)** To decrease bias
> - **C)** To optimize the loss function
> - **D)** To increase interpretability
>
> **🇹🇷 Türkçe**
>
> Topluluk (ensemble) yöntemlerinde 'bagging' genellikle ne için kullanılır?
>
> - **A)** Varyansı azaltmak
> - **B)** Yanlılığı (bias) azaltmak
> - **C)** Kayıp fonksiyonunu optimize etmek
> - **D)** Yorumlanabilirliği artırmak
>
> **✅ Cevap:** **A** — Varyansı azaltmak

---

> ### 6 · 🇸🇬 Singapur · NOAI 2025
>
> **❓ Soru** · `en`
>
> What does a 'vanishing gradient' problem typically affect?
>
> - **A)** The performance of shallow neural networks
> - **B)** The training of deep neural networks
> - **C)** The dimensionality of the input data
> - **D)** The size of the training dataset
>
> **🇹🇷 Türkçe**
>
> 'Kaybolan gradyan' (vanishing gradient) problemi tipik olarak neyi etkiler?
>
> - **A)** Sığ sinir ağlarının performansını
> - **B)** Derin sinir ağlarının eğitimini
> - **C)** Girdi verisinin boyutunu
> - **D)** Eğitim veri kümesinin büyüklüğünü
>
> **✅ Cevap:** **B** — Derin sinir ağlarının eğitimini

---

> ### 7 · 🇧🇷 Brezilya · ONIA
>
> **❓ Soru** · `pt`
>
> Questão 3
> Qual é o principal risco ao usar recursão sem uma
> condição de parada adequada?
>
> - **A)** O algoritmo se torna muito lento.
> - **B)** O computador desliga.
> - **C)** Ocorrerá um estouro de pilha (stack overflow).
> - **D)** O código não imprime nada.
> - **E)** O algoritmo não faz nenhuma repetição.
>
> **🇹🇷 Türkçe**
>
> Soru 3
> Uygun bir durdurma koşulu olmadan özyineleme (recursion) kullanmanın başlıca riski nedir?
>
> - **A)** Algoritma çok yavaşlar.
> - **B)** Bilgisayar kapanır.
> - **C)** Yığın taşması (stack overflow) oluşur.
> - **D)** Kod hiçbir şey yazdırmaz.
> - **E)** Algoritma hiç tekrar yapmaz.
>
> **✅ Cevap:** **C** — Yığın taşması (stack overflow) oluşur.

---

> ### 8 · 🇧🇷 Brezilya · ONIA
>
> **❓ Soru** · `pt`
>
> Questão 2
> Qual estrutura é melhor para representar caminhos
> entre cidades com distâncias?
> A) Lista. B) Fila. C) String.
> D) Pilha. E) Grafo.
>
> - **A)** Lista.
> - **B)** Fila.
> - **C)** String.
> - **D)** Pilha.
> - **E)** Grafo.
>
> **🇹🇷 Türkçe**
>
> Soru 2
> Şehirler arasındaki mesafeli yolları temsil etmek için en iyi yapı hangisidir?
>
> - **A)** Liste.
> - **B)** Kuyruk.
> - **C)** Dizgi (String).
> - **D)** Yığın.
> - **E)** Çizge (Graph).
>
> **✅ Cevap:** **E** — Çizge (Graph).

---

> ### 9 · 🇧🇷 Brezilya · ONIA
>
> **❓ Soru** · `pt`
>
> Questão 6
> Em um classificador k-NN, qual efeito esperado ao escolher um valor de k muito grande?
> Justificativa da escolha: _________________________________
>
> - **A)** Aumento da variância e diminuição do viés
> - **B)** Diminuição da variância e aumento do viés
> - **C)** Redução do custo computacional
> - **D)** Maior sensibilidade a ruídos nos dados
> - **E)** Classe minoritária tende a ser privilegiada
>
> **🇹🇷 Türkçe**
>
> Soru 6
> Bir k-NN sınıflandırıcısında, çok büyük bir k değeri seçmenin beklenen etkisi nedir?
>
> - **A)** Varyansın artması ve yanlılığın (bias) azalması
> - **B)** Varyansın azalması ve yanlılığın (bias) artması
> - **C)** Hesaplama maliyetinin azalması
> - **D)** Verideki gürültüye karşı daha yüksek duyarlılık
> - **E)** Azınlık sınıfının kayrılma eğilimi
>
> **✅ Cevap:** **B** — Varyansın azalması ve yanlılığın (bias) artması

---

> ### 10 · 🇧🇷 Brezilya · ONIA
>
> **❓ Soru** · `pt`
>
> Questão 4
> Em um algoritmo de recomendação, o sistema analisa
> os itens que o usuário já viu e tenta prever o que ele
> gostaria. Esse tipo de IA é mais próximo de:
>
> - **A)** Aprendizado supervisionado.
> - **B)** Busca cega.
> - **C)** Inteligência artificial simbólica.
> - **D)** Aprendizado não-supervisionado.
> - **E)** Repetição de escolha prévia.
>
> **🇹🇷 Türkçe**
>
> Soru 4
> Bir öneri algoritmasında sistem, kullanıcının daha önce gördüğü öğeleri analiz eder ve neyi beğeneceğini tahmin etmeye çalışır. Bu tür bir yapay zeka en çok neye yakındır:
>
> - **A)** Gözetimli öğrenme.
> - **B)** Kör arama.
> - **C)** Sembolik yapay zeka.
> - **D)** Gözetimsiz öğrenme.
> - **E)** Önceki seçimin tekrarı.
>
> **✅ Cevap:** **A** — Gözetimli öğrenme.

---

> ### 11 · 🇰🇷 Güney Kore · KOAI 2026
>
> **❓ Soru** · `ko`
>
> Adam과 AdamW의 차이로 가장 옳은 것은?
>
> - **A)** Adam은 모멘텀을 사용하지 않는다.
> - **B)** AdamW는 가중치 감쇠(weight decay)를 그래디언트에 더하지 않고 파라미터 업데이트 시 분리해서 적용한다.
> - **C)** AdamW는 일차 모멘트만 추정한다.
> - **D)** Adam과 AdamW는 완전히 동일한 알고리즘이다.
>
> **🇹🇷 Türkçe**
>
> Adam ve AdamW arasındaki fark için en doğru olan hangisidir?
>
> - **A)** Adam momentum kullanmaz.
> - **B)** AdamW, ağırlık sönümünü (weight decay) gradyana eklemez; parametre güncellemesi sırasında ayrıştırarak uygular.
> - **C)** AdamW yalnızca birinci moment kestirimini yapar.
> - **D)** Adam ve AdamW tamamen aynı algoritmadır.
>
> **✅ Cevap:** **B** — AdamW, ağırlık sönümünü gradyana eklemez; parametre güncellemesinde ayrıştırarak uygular.

---

> ### 12 · 🇰🇷 Güney Kore · KOAI 2026
>
> **❓ Soru** · `ko`
>
> ResNet의 핵심 아이디어로 가장 옳은 것은?
>
> - **A)** 잔차 연결(residual connection)을 통해 매우 깊은 네트워크의 학습을 용이하게 한다.
> - **B)** 합성곱 없이 완전연결층만 쌓는다.
> - **C)** 풀링을 일절 사용하지 않는다.
> - **D)** 활성화 함수로 시그모이드만 사용한다.
>
> **🇹🇷 Türkçe**
>
> ResNet'in temel fikri için en doğru olan hangisidir?
>
> - **A)** Artık bağlantılar (residual connection) sayesinde çok derin ağların eğitimini kolaylaştırır.
> - **B)** Evrişim olmadan yalnızca tam bağlı (fully connected) katmanlar üst üste yığılır.
> - **C)** Havuzlamayı (pooling) hiç kullanmaz.
> - **D)** Aktivasyon fonksiyonu olarak yalnızca sigmoid kullanır.
>
> **✅ Cevap:** **A** — Artık bağlantılar (residual connection) sayesinde çok derin ağların eğitimini kolaylaştırır.

---

> ### 13 · 🇰🇷 Güney Kore · KOAI 2026
>
> **❓ Soru** · `ko`
>
> PCA(주성분 분석)에 대한 설명으로 옳은 것은?
>
> - **A)** PCA의 주성분은 데이터 공분산 행렬의 고유벡터 중 큰 고유값에 해당하는 것이다.
> - **B)** PCA는 비선형 차원 축소 기법이다.
> - **C)** PCA는 항상 분류 정확도를 향상시킨다.
> - **D)** PCA를 적용하기 전에 데이터를 표준화할 필요는 전혀 없다.
>
> **🇹🇷 Türkçe**
>
> PCA (temel bileşen analizi) ile ilgili doğru olan hangisidir?
>
> - **A)** PCA'nın temel bileşenleri, veri kovaryans matrisinin büyük özdeğerlerine karşılık gelen özvektörleridir.
> - **B)** PCA doğrusal olmayan bir boyut indirgeme tekniğidir.
> - **C)** PCA her zaman sınıflandırma doğruluğunu artırır.
> - **D)** PCA uygulamadan önce veriyi standartlaştırmaya hiç gerek yoktur.
>
> **✅ Cevap:** **A** — PCA'nın temel bileşenleri, kovaryans matrisinin büyük özdeğerlerine karşılık gelen özvektörleridir.

---

> ### 14 · 🇰🇷 Güney Kore · KOAI 2026
>
> **❓ Soru** · `ko`
>
> ROC 곡선과 AUC에 대한 설명으로 옳은 것은?
>
> - **A)** ROC 곡선의 x축은 정밀도, y축은 재현율이다.
> - **B)** AUC=0.5는 무작위 분류기와 동일한 수준임을 의미한다.
> - **C)** AUC는 항상 0.5에서 1.0 사이의 값을 갖는다.
> - **D)** ROC 곡선은 회귀 모델 평가에 표준적으로 사용된다.
>
> **🇹🇷 Türkçe**
>
> ROC eğrisi ve AUC ile ilgili doğru olan hangisidir?
>
> - **A)** ROC eğrisinin x ekseni kesinlik (precision), y ekseni duyarlılıktır (recall).
> - **B)** AUC=0.5, rastgele bir sınıflandırıcıyla aynı düzeyde olduğu anlamına gelir.
> - **C)** AUC her zaman 0.5 ile 1.0 arasında bir değer alır.
> - **D)** ROC eğrisi regresyon modeli değerlendirmesinde standart olarak kullanılır.
>
> **✅ Cevap:** **B** — AUC=0.5, rastgele bir sınıflandırıcıyla aynı düzeyde olduğu anlamına gelir.

---

> ### 15 · 🇻🇳 Vietnam · VOAI 2025
>
> **❓ Soru** · `vi`
>
> Câu 20. Mô hình BERT nhận đầu vào là gì?
>
> - **A)** Vector ID, mặt nạ chú ý (attention mask), ID loại token
> - **B)** Chỉ văn bản thô (raw text)
> - **C)** Cặp câu với nhúng (embedding)
> - **D)** Từ rời rạc
>
> **🇹🇷 Türkçe**
>
> Soru 20. BERT modeli girdi olarak neyi alır?
>
> - **A)** Vektör ID, dikkat maskesi (attention mask), token tipi ID
> - **B)** Yalnızca ham metin (raw text)
> - **C)** Gömme (embedding) ile cümle çiftleri
> - **D)** Ayrık kelimeler
>
> **✅ Cevap:** **A** — Vektör ID, dikkat maskesi (attention mask), token tipi ID

---

> ### 16 · 🇻🇳 Vietnam · VOAI 2025
>
> **❓ Soru** · `vi`
>
> Câu 95. Mạng GAN bao gồm hai mạng chính nào?
>
> - **A)** Bộ phát hiện (Detector) và Bộ phân đoạn (Segmentor)
> - **B)** Bộ chuyển đổi (Transformer) và Cơ chế chú ý (Attention)
> - **C)** Bộ mã hóa (Encoder) và Bộ giải mã (Decoder)
> - **D)** Bộ tạo (Generator) và Bộ phân biệt (Discriminator)
>
> **🇹🇷 Türkçe**
>
> Soru 95. GAN ağı hangi iki ana ağdan oluşur?
>
> - **A)** Dedektör (Detector) ve Bölütleyici (Segmentor)
> - **B)** Dönüştürücü (Transformer) ve Dikkat mekanizması (Attention)
> - **C)** Kodlayıcı (Encoder) ve Kod çözücü (Decoder)
> - **D)** Üretici (Generator) ve Ayırt edici (Discriminator)
>
> **✅ Cevap:** **D** — Üretici (Generator) ve Ayırt edici (Discriminator)

---

> ### 17 · 🇻🇳 Vietnam · VOAI 2025
>
> **❓ Soru** · `vi`
>
> Câu 31. Chuẩn hóa rất quan trọng đối với k-NN vì
>
> - **A)** Giúp tránh được vấn đề một thuộc tính có thể đóng vai trò quyết định, lấn át các thuộc tính khác.
> - **B)** Nó biến đổi các giá trị thuộc tính thành phạm vi [0, 1] để dễ dàng tính toán.
> - **C)** Nó cho phép so sánh và phân tích có ý nghĩa giữa các biến.
> - **D)** Nó cần thiết để tính toán khoảng cách giữa các mẫu dữ liệu.
>
> **🇹🇷 Türkçe**
>
> Soru 31. Normalizasyon k-NN için çok önemlidir çünkü
>
> - **A)** Bir özniteliğin belirleyici rol oynayıp diğer öznitelikleri bastırması sorununu önlemeye yardımcı olur.
> - **B)** Öznitelik değerlerini, hesaplamayı kolaylaştırmak için [0, 1] aralığına dönüştürür.
> - **C)** Değişkenler arasında anlamlı karşılaştırma ve analize izin verir.
> - **D)** Veri örnekleri arasındaki mesafeyi hesaplamak için gereklidir.
>
> **✅ Cevap:** **A** — Bir özniteliğin belirleyici rol oynayıp diğerlerini bastırması sorununu önler.

---

> ### 18 · 🇻🇳 Vietnam · VOAI 2025
>
> **❓ Soru** · `vi`
>
> Câu 98. Mô hình DALL·E có khả năng đặc biệt nào?
>
> - **A)** Phân đoạn vật thể
> - **B)** Sinh ảnh từ mô tả văn bản
> - **C)** Nén ảnh thành vector
> - **D)** Sinh mô tả từ ảnh
>
> **🇹🇷 Türkçe**
>
> Soru 98. DALL·E modelinin özel yeteneği nedir?
>
> - **A)** Nesne bölütleme
> - **B)** Metin açıklamasından görüntü üretme
> - **C)** Görüntüyü vektöre sıkıştırma
> - **D)** Görüntüden açıklama üretme
>
> **✅ Cevap:** **B** — Metin açıklamasından görüntü üretme

---

> ### 19 · 🇭🇺 Macaristan · HAIO 2025
>
> **❓ Soru** · `hu`
>
> Melyik állítás igaz a dropout technikáról?
>
> - Minden lépésben ugyanazokat a súlyokat nullázza
> - A háló súlyainak egy részét véglegesen nullára állítja
> - A kimenet bizonyos részeit véglegesen nullára állítja
> - A háló egyes részeit ideiglenesen kikapcsolja tanítás közben
> - A tanulási rátát csökkenti lokálisan
>
> **🇹🇷 Türkçe**
>
> Dropout tekniği hakkında hangi ifade doğrudur?
>
> - Her adımda aynı ağırlıkları sıfırlar
> - Ağın ağırlıklarının bir kısmını kalıcı olarak sıfıra ayarlar
> - Çıktının belirli kısımlarını kalıcı olarak sıfıra ayarlar
> - Eğitim sırasında ağın bazı kısımlarını geçici olarak devre dışı bırakır
> - Öğrenme oranını yerel olarak azaltır
>
> **✅ Cevap:** Eğitim sırasında ağın bazı kısımlarını geçici olarak devre dışı bırakır

---

> ### 20 · 🇭🇺 Macaristan · HAIO 2025
>
> **❓ Soru** · `hu`
>
> Mely állítások igazak a súlyinicializálásra?
>
> - A súlyokat mindig nullára kell állítani
> - Általában a súlyokat véletlenszerűen inicializáljuk
> - A kezdőérték nem számít
> - A súlyokat újratanulásból is származtathatjuk (pl. transfer learning)
> - A bias értékek mindig 1-re vannak állítva
>
> **🇹🇷 Türkçe**
>
> Ağırlık başlatma (initialization) için hangi ifadeler doğrudur?
>
> - Ağırlıklar her zaman sıfıra ayarlanmalıdır
> - Genellikle ağırlıklar rastgele başlatılır
> - Başlangıç değeri önemli değildir
> - Ağırlıkları yeniden öğrenmeden de türetebiliriz (ör. transfer learning)
> - Bias değerleri her zaman 1'e ayarlanır
>
> **✅ Cevap:** Genellikle ağırlıklar rastgele başlatılır · Ağırlıkları yeniden öğrenmeden de türetebiliriz (transfer learning)

---

> ### 21 · 🇭🇺 Macaristan · HAIO 2025
>
> **❓ Soru** · `hu`
>
> Melyik állítás igaz az Attention mechanizmusra?
>
> - Képes kontextusfüggő reprezentációkat létrehozni
> - Egy token hatását a többi tokenhez viszonyítva súlyozza
> - Kizárólag képek feldolgozására használjuk
> - A tanulási ráta optimalizálására szolgál
> - Csak visszacsatolt hálókban alkalmazható
>
> **🇹🇷 Türkçe**
>
> Attention mekanizması hakkında hangi ifade doğrudur?
>
> - Bağlama duyarlı temsiller oluşturabilir
> - Bir token'ın etkisini diğer token'lara göre ağırlıklandırır
> - Yalnızca görüntü işlemede kullanılır
> - Öğrenme oranını optimize etmeye yarar
> - Yalnızca geri beslemeli (recurrent) ağlarda uygulanabilir
>
> **✅ Cevap:** Bağlama duyarlı temsiller oluşturabilir · Bir token'ın etkisini diğerlerine göre ağırlıklandırır

---

> ### 22 · 🇭🇺 Macaristan · HAIO 2025
>
> **❓ Soru** · `hu`
>
> Az alábbiak közül melyik nem biológiai ihletésű?
>
> - Hebb-i tanulás
> - ADAM
> - Önszervező térkép
> - Konvolúciós háló
> - Spike-time dependent plasticity
>
> **🇹🇷 Türkçe**
>
> Aşağıdakilerden hangisi biyolojik esinli DEĞİLDİR?
>
> - Hebb öğrenmesi
> - ADAM
> - Öz-örgütlemeli harita (SOM)
> - Evrişimli ağ (CNN)
> - Spike-time dependent plasticity
>
> **✅ Cevap:** ADAM

---

> ### 23 · 🇨🇳 Çin · NOAI 2024
>
> **❓ Soru** · `zh`
>
> Matplotlib 库中，哪种图表最适合展示数据的频率分布情况？
>
> - **A)** 折线图
> - **B)** 饼图
> - **C)** 直方图
> - **D)** 散点图
>
> **🇹🇷 Türkçe**
>
> Matplotlib kütüphanesinde, verinin frekans dağılımını göstermek için en uygun grafik hangisidir?
>
> - **A)** Çizgi grafiği
> - **B)** Pasta grafiği
> - **C)** Histogram
> - **D)** Dağılım grafiği (scatter)
>
> **✅ Cevap:** **C** — Histogram

---

> ### 24 · 🇨🇳 Çin · NOAI 2024
>
> **❓ Soru** · `zh`
>
> Pandas 中的 DataFrame 与 Series 的主要区别是什么？
>
> - **A)** DataFrame 只能存储数值数据，而 Series 可以存储任何类型的数据
> - **B)** DataFrame 不支持缺失值，而 Series 支持
> - **C)** DataFrame 是二维结构，可以包含多列数据，而 Series 是一维结构
> - **D)** DataFrame 是 Pandas 独有的，而 Series 是 NumPy 的特性
>
> **🇹🇷 Türkçe**
>
> Pandas'ta DataFrame ile Series arasındaki temel fark nedir?
>
> - **A)** DataFrame yalnızca sayısal veri saklayabilir, Series ise her türü saklayabilir
> - **B)** DataFrame eksik değerleri desteklemez, Series destekler
> - **C)** DataFrame iki boyutlu bir yapıdır ve birden çok sütun içerebilir, Series ise tek boyutludur
> - **D)** DataFrame Pandas'a özgüdür, Series ise NumPy'nin bir özelliğidir
>
> **✅ Cevap:** **C** — DataFrame iki boyutlu (çok sütunlu), Series ise tek boyutlu bir yapıdır

---

> ### 25 · 🇨🇳 Çin · NOAI 2025
>
> **❓ Soru** · `zh`
>
> 使用 for 循环遍历列表 nums = [1, 2, 3]，应使用的语法是：
>
> - **A)** for i in nums:
> - **B)** for nums in i:
> - **C)** while i in nums:
> - **D)** while nums in i:
>
> **🇹🇷 Türkçe**
>
> nums = [1, 2, 3] listesini for döngüsüyle dolaşmak için kullanılması gereken sözdizimi:
>
> - **A)** for i in nums:
> - **B)** for nums in i:
> - **C)** while i in nums:
> - **D)** while nums in i:
>
> **✅ Cevap:** **A** — `for i in nums:`

---

> ### 26 · 🇨🇳 Çin · NOAI 2025
>
> **❓ Soru** · `zh`
>
> 如果有列表 a[1, 2, 3, 4, 5]，以下哪个语句的结果是 [2, 3, 4]？
>
> - **A)** a[1:4]
> - **B)** a[2:4]
> - **C)** a[1:3]
> - **D)** a[2:3]
>
> **🇹🇷 Türkçe**
>
> a = [1, 2, 3, 4, 5] listesi varsa, aşağıdaki ifadelerden hangisinin sonucu [2, 3, 4]'tür?
>
> - **A)** a[1:4]
> - **B)** a[2:4]
> - **C)** a[1:3]
> - **D)** a[2:3]
>
> **✅ Cevap:** **A** — `a[1:4]`

---

> ### 27 · 🇸🇬 Singapur · NOAI 2026
>
> **❓ Soru** · `en`
>
> Supervised learning requires:
>
> - **A)** Unlabeled data only
> - **B)** Reinforcement signals
> - **C)** No data
> - **D)** Labeled training data
>
> **🇹🇷 Türkçe**
>
> Gözetimli öğrenme (supervised learning) neyi gerektirir:
>
> - **A)** Yalnızca etiketsiz veri
> - **B)** Pekiştirme sinyalleri
> - **C)** Hiç veri yok
> - **D)** Etiketli eğitim verisi
>
> **✅ Cevap:** **D** — Etiketli eğitim verisi

---

> ### 28 · 🇸🇬 Singapur · NOAI 2026
>
> **❓ Soru** · `en`
>
> What is an epoch in training?
>
> - **A)** One forward pass
> - **B)** One batch
> - **C)** One weight update
> - **D)** One complete pass through training dataset
>
> **🇹🇷 Türkçe**
>
> Eğitimde bir epoch nedir?
>
> - **A)** Bir ileri geçiş (forward pass)
> - **B)** Bir batch
> - **C)** Bir ağırlık güncellemesi
> - **D)** Eğitim veri kümesinden bir tam geçiş
>
> **✅ Cevap:** **D** — Eğitim veri kümesinden bir tam geçiş

---

> ### 29 · 🇸🇬 Singapur · NOAI 2026
>
> **❓ Soru** · `en`
>
> YOLO (You Only Look Once) is:
>
> - **A)** Classification model
> - **B)** Segmentation model
> - **C)** Single-stage real-time object detector
> - **D)** Two-stage detector
>
> **🇹🇷 Türkçe**
>
> YOLO (You Only Look Once) nedir:
>
> - **A)** Sınıflandırma modeli
> - **B)** Bölütleme (segmentation) modeli
> - **C)** Tek aşamalı gerçek zamanlı nesne dedektörü
> - **D)** İki aşamalı dedektör
>
> **✅ Cevap:** **C** — Tek aşamalı gerçek zamanlı nesne dedektörü

---

> ### 30 · 🇸🇬 Singapur · NOAI 2026
>
> **❓ Soru** · `en`
>
> LSTMs solve what RNN problem?
>
> - **A)** Slow training
> - **B)** Large memory
> - **C)** Long-term dependency/vanishing gradient
> - **D)** No problem
>
> **🇹🇷 Türkçe**
>
> LSTM'ler RNN'in hangi problemini çözer?
>
> - **A)** Yavaş eğitim
> - **B)** Büyük bellek
> - **C)** Uzun vadeli bağımlılık / kaybolan gradyan (vanishing gradient)
> - **D)** Problem yok
>
> **✅ Cevap:** **C** — Uzun vadeli bağımlılık / kaybolan gradyan

---

> ### 31 · 🇸🇬 Singapur · NOAI 2026
>
> **❓ Soru** · `en`
>
> Which matrix is symmetric?
>
> - **A)** [[1, 2], [3, 4]]
> - **B)** [[1, 2], [2, 3]]
> - **C)** [[1, 0], [1, 0]]
> - **D)** [[0, 1], [0, 0]]
>
> **🇹🇷 Türkçe**
>
> Hangi matris simetriktir?
>
> - **A)** [[1, 2], [3, 4]]
> - **B)** [[1, 2], [2, 3]]
> - **C)** [[1, 0], [1, 0]]
> - **D)** [[0, 1], [0, 0]]
>
> **✅ Cevap:** **B** — [[1, 2], [2, 3]]

---

> ### 32 · 🇸🇬 Singapur · NOAI 2026
>
> **❓ Soru** · `en`
>
> The standard deviation is:
>
> - **A)** Square of variance
> - **B)** Sum of deviations
> - **C)** Mean absolute deviation
> - **D)** Square root of variance
>
> **🇹🇷 Türkçe**
>
> Standart sapma nedir:
>
> - **A)** Varyansın karesi
> - **B)** Sapmaların toplamı
> - **C)** Ortalama mutlak sapma
> - **D)** Varyansın karekökü
>
> **✅ Cevap:** **D** — Varyansın karekökü

---

> ### 33 · 🇸🇬 Singapur · NOAI 2026
>
> **❓ Soru** · `en`
>
> Word embeddings represent:
>
> - **A)** Words as one-hot vectors
> - **B)** Words as strings
> - **C)** Words as images
> - **D)** Words as dense vectors
>
> **🇹🇷 Türkçe**
>
> Kelime gömmeleri (word embeddings) neyi temsil eder:
>
> - **A)** Kelimeleri one-hot vektörler olarak
> - **B)** Kelimeleri dizgi (string) olarak
> - **C)** Kelimeleri görüntü olarak
> - **D)** Kelimeleri yoğun (dense) vektörler olarak
>
> **✅ Cevap:** **D** — Kelimeleri yoğun (dense) vektörler olarak

---

> ### 34 · 🇸🇬 Singapur · NOAI 2026
>
> **❓ Soru** · `en`
>
> Multimodal models process:
>
> - **A)** One data type only
> - **B)** Only text
> - **C)** Multiple data types
> - **D)** Only images
>
> **🇹🇷 Türkçe**
>
> Çok kipli (multimodal) modeller neyi işler:
>
> - **A)** Yalnızca tek bir veri tipi
> - **B)** Yalnızca metin
> - **C)** Birden çok veri tipi
> - **D)** Yalnızca görüntü
>
> **✅ Cevap:** **C** — Birden çok veri tipi

---

> ### 35 · 🇸🇬 Singapur · NOAI 2026
>
> **❓ Soru** · `en`
>
> GPT-4 Vision (GPT-4V) can:
>
> - **A)** Process images and text together
> - **B)** Only process text
> - **C)** Only generate images
> - **D)** Only classify images
>
> **🇹🇷 Türkçe**
>
> GPT-4 Vision (GPT-4V) neyi yapabilir:
>
> - **A)** Görüntü ve metni birlikte işleyebilir
> - **B)** Yalnızca metin işler
> - **C)** Yalnızca görüntü üretir
> - **D)** Yalnızca görüntü sınıflandırır
>
> **✅ Cevap:** **A** — Görüntü ve metni birlikte işleyebilir

---

> ### 36 · 🇸🇬 Singapur · NOAI 2026
>
> **❓ Soru** · `en`
>
> Which is mutable in Python?
>
> - **A)** Tuple
> - **B)** String
> - **C)** List
> - **D)** Integer
>
> **🇹🇷 Türkçe**
>
> Python'da hangisi değiştirilebilirdir (mutable):
>
> - **A)** Tuple
> - **B)** String
> - **C)** List
> - **D)** Integer
>
> **✅ Cevap:** **C** — List

---

> ### 37 · 🇸🇬 Singapur · NOAI 2026
>
> **❓ Soru** · `en`
>
> Backpropagation is used to:
>
> - **A)** Initialise weights
> - **B)** Make predictions
> - **C)** Compute gradients via chain rule
> - **D)** Evaluate test accuracy
>
> **🇹🇷 Türkçe**
>
> Geri yayılım (backpropagation) ne için kullanılır:
>
> - **A)** Ağırlıkları başlatmak
> - **B)** Tahmin yapmak
> - **C)** Zincir kuralıyla (chain rule) gradyanları hesaplamak
> - **D)** Test doğruluğunu değerlendirmek
>
> **✅ Cevap:** **C** — Zincir kuralıyla gradyanları hesaplamak

---

> ### 38 · 🇸🇬 Singapur · NOAI 2026
>
> **❓ Soru** · `en`
>
> Transformers primarily use:
>
> - **A)** Recurrence (RNN)
> - **B)** Convolution (CNN)
> - **C)** Self-attention mechanisms
> - **D)** Fully connected layers only
>
> **🇹🇷 Türkçe**
>
> Transformer'lar öncelikle neyi kullanır:
>
> - **A)** Yineleme (RNN)
> - **B)** Evrişim (CNN)
> - **C)** Öz-dikkat (self-attention) mekanizmaları
> - **D)** Yalnızca tam bağlı (fully connected) katmanlar
>
> **✅ Cevap:** **C** — Öz-dikkat (self-attention) mekanizmaları

---

> ### 39 · 🇸🇬 Singapur · NOAI 2026
>
> **❓ Soru** · `en`
>
> Few-shot learning provides:
>
> - **A)** No examples
> - **B)** Full dataset
> - **C)** Only instructions
> - **D)** Small number of examples in prompt
>
> **🇹🇷 Türkçe**
>
> Az örnekli öğrenme (few-shot learning) neyi sağlar:
>
> - **A)** Hiç örnek yok
> - **B)** Tüm veri kümesi
> - **C)** Yalnızca talimatlar
> - **D)** İstem (prompt) içinde az sayıda örnek
>
> **✅ Cevap:** **D** — İstem (prompt) içinde az sayıda örnek

---

> ### 40 · 🇸🇬 Singapur · NOAI 2026
>
> **❓ Soru** · `en`
>
> The Hessian matrix contains:
>
> - **A)** First-order partial derivatives
> - **B)** Second-order partial derivatives
> - **C)** Eigenvalues
> - **D)** Gradients
>
> **🇹🇷 Türkçe**
>
> Hessian matrisi neyi içerir:
>
> - **A)** Birinci dereceden kısmi türevler
> - **B)** İkinci dereceden kısmi türevler
> - **C)** Özdeğerler
> - **D)** Gradyanlar
>
> **✅ Cevap:** **B** — İkinci dereceden kısmi türevler

---

> ### 41 · 🇸🇬 Singapur · NOAI 2026
>
> **❓ Soru** · `en`
>
> Cross-validation is used to:
>
> - **A)** Clean data
> - **B)** Select features
> - **C)** Normalise inputs
> - **D)** Estimate model performance on unseen data
>
> **🇹🇷 Türkçe**
>
> Çapraz doğrulama (cross-validation) ne için kullanılır:
>
> - **A)** Veriyi temizlemek
> - **B)** Öznitelik seçmek
> - **C)** Girdileri normalize etmek
> - **D)** Modelin görülmemiş veri üzerindeki performansını kestirmek
>
> **✅ Cevap:** **D** — Modelin görülmemiş veri üzerindeki performansını kestirmek

---

> ### 42 · 🇸🇬 Singapur · NOAI 2026
>
> **❓ Soru** · `en`
>
> ReLU activation function is:
>
> - **A)** max(0, x)
> - **B)** 1 / (1 + e^(-x))
> - **C)** tanh(x)
> - **D)** x²
>
> **🇹🇷 Türkçe**
>
> ReLU aktivasyon fonksiyonu nedir:
>
> - **A)** max(0, x)
> - **B)** 1 / (1 + e^(-x))
> - **C)** tanh(x)
> - **D)** x²
>
> **✅ Cevap:** **A** — max(0, x)

---

> ### 43 · 🇸🇬 Singapur · NOAI 2026
>
> **❓ Soru** · `en`
>
> What does loss.backward() do?
>
> - **A)** Reverses the forward pass
> - **B)** Updates weights
> - **C)** Computes gradients via backpropagation
> - **D)** Resets the model
>
> **🇹🇷 Türkçe**
>
> loss.backward() ne yapar:
>
> - **A)** İleri geçişi (forward pass) tersine çevirir
> - **B)** Ağırlıkları günceller
> - **C)** Geri yayılımla (backpropagation) gradyanları hesaplar
> - **D)** Modeli sıfırlar
>
> **✅ Cevap:** **C** — Geri yayılımla gradyanları hesaplar

---

> ### 44 · 🇸🇬 Singapur · NOAI 2026
>
> **❓ Soru** · `en`
>
> What is nn.Module in PyTorch?
>
> - **A)** Base class for all neural network modules
> - **B)** Activation function
> - **C)** Loss function
> - **D)** Optimiser
>
> **🇹🇷 Türkçe**
>
> PyTorch'ta nn.Module nedir:
>
> - **A)** Tüm sinir ağı modüllerinin temel sınıfı (base class)
> - **B)** Aktivasyon fonksiyonu
> - **C)** Kayıp (loss) fonksiyonu
> - **D)** Optimizer
>
> **✅ Cevap:** **A** — Tüm sinir ağı modüllerinin temel sınıfı

---

> ### 45 · 🇨🇦 Kanada · CAIO 2025
>
> **❓ Soru** · `en`
>
> Consider the following Python code:
>
> ```python
> import pandas as pd
>
> df = pd.DataFrame({
>     'A': [1, 2, 3, 4, 5],
>     'B': [10, 20, 30, 40, 50],
>     'C': [5, 4, 3, 2, 1]
> })
>
> print(df.loc[df['B'] > 20, ['A', 'C']].iloc[1, 1])
> ```
>
> What is the output?
>
> - **A)** 4
> - **B)** 2
> - **C)** 40
> - **D)** 3
> - **E)** 30
>
> **🇹🇷 Türkçe**
>
> Aşağıdaki Python kodunu inceleyin:
>
> ```python
> import pandas as pd
>
> df = pd.DataFrame({
>     'A': [1, 2, 3, 4, 5],
>     'B': [10, 20, 30, 40, 50],
>     'C': [5, 4, 3, 2, 1]
> })
>
> print(df.loc[df['B'] > 20, ['A', 'C']].iloc[1, 1])
> ```
>
> Çıktı nedir?
>
> - **A)** 4
> - **B)** 2
> - **C)** 40
> - **D)** 3
> - **E)** 30
>
> **✅ Cevap:** **B** — 2

---

## 🖼️ Bölüm 2 — Görselli Sorular

> ### 46 · 🇿🇦 Güney Afrika · SAAIO 2026 · 🖼️
>
> ![Güney Afrika görsel](gorseller/saaio-official-sample-r1-q3_1.jpg)
>
> **❓ Soru** · `en`
>
> The number sequence shown in the image has a rule. Find out what it is and select the missing number in the sequence.
>
> - A. 11
> - B. 13
> - C. 15
> - D. 17
> - E. 19
>
> **🇹🇷 Türkçe**
>
> Görseldeki sayı dizisinin bir kuralı vardır. Bu kuralı bulun ve dizideki eksik sayıyı seçin.
>
> - A. 11
> - B. 13
> - C. 15
> - D. 17
> - E. 19
>
> **✅ Cevap:** **C** — 15

---

> ### 47 · 🇮🇳 Hindistan · UAIO 2026 · 🖼️
>
> ![Hindistan görsel](gorseller/hindistan-unicus-uaio-sinif6-ornek-01_1.png)
>
> **❓ Soru** · `en`
>
> Linh uses a text-based AI tool to summarise a long chapter for her revision. What is the primary purpose of such an AI tool?
>
> - **A)** To play music for Linh
> - **B)** To translate the text into another language while preserving its meaning
> - **C)** To create a summary capturing the main points of the chapter
> - **D)** To translate the chapter into another language
>
> **🇹🇷 Türkçe**
>
> Linh, tekrar çalışması için uzun bir bölümü özetlemek üzere metin tabanlı bir AI aracı kullanıyor. Böyle bir AI aracının başlıca amacı nedir?
>
> - **A)** Linh için müzik çalmak
> - **B)** Metni anlamını koruyarak başka bir dile çevirmek
> - **C)** Bölümün ana noktalarını yakalayan bir özet oluşturmak
> - **D)** Bölümü başka bir dile çevirmek
>
> **✅ Cevap:** **C** — Bölümün ana noktalarını yakalayan bir özet oluşturmak

---

> ### 48 · 🇧🇷 Brezilya · ONIA · 🖼️
>
> ![Brezilya görsel](gorseller/brezilya-onia-2025-faz1-s05_1.png)
>
> **❓ Soru** · `pt`
>
> 5. Observe as imagens abaixo. Nela você pode notar uma diferença do polígono
> representado pela letra C dos demais. Qual seria esta distinção?
>
> - **A)** Tridimensionalidade.
> - **B)** Número de letras no nome.
> - **C)** Número de tons de cor.
> - **D)** Variação da claridade da cor.
> - **E)** Letra inicial da cor.
>
> **🇹🇷 Türkçe**
>
> 5. Aşağıdaki görselleri inceleyin. C harfiyle temsil edilen çokgenin diğerlerinden bir farkını görebilirsiniz. Bu ayrım ne olabilir?
>
> - **A)** Üç boyutluluk.
> - **B)** İsimdeki harf sayısı.
> - **C)** Renk tonu sayısı.
> - **D)** Rengin açıklık (parlaklık) değişimi.
> - **E)** Rengin baş harfi.
>
> **✅ Cevap:** **D** — Rengin açıklık (parlaklık) değişimi.

---

> ### 49 · 🇮🇳 Hindistan · UAIO 2026 · 🖼️
>
> ![Hindistan görsel](gorseller/hindistan-unicus-uaio-sinif6-ornek-16_1.png)
>
> **❓ Soru** · `en`
>
> Look at the image of a decision tree that Luca built to classify animals. What does the first node (root node) represent?
>
> - **A)** The first node or condition used to split the data
> - **B)** The final classification result
> - **C)** A leaf node with no further branches
> - **D)** A random data point from the training set
>
> **🇹🇷 Türkçe**
>
> Luca'nın hayvanları sınıflandırmak için kurduğu karar ağacının görselini inceleyin. İlk düğüm (kök düğüm) neyi temsil eder?
>
> - **A)** Veriyi bölmek için kullanılan ilk düğüm veya koşul
> - **B)** Nihai sınıflandırma sonucu
> - **C)** Daha fazla dallanması olmayan bir yaprak düğüm
> - **D)** Eğitim kümesinden rastgele bir veri noktası
>
> **✅ Cevap:** **A** — Veriyi bölmek için kullanılan ilk düğüm veya koşul

---

## ✍️ Bölüm 3 — Açık Uçlu Soru

> ### 50 · 🇷🇺 Rusya · VsOŞ-YZ 2025
>
> **❓ Soru** · `ru`
>
> Задание 4. Модели ИИ нужно последовательно выдать пять различных задач, и две из которых —
> тяжёлые. Планировщик экспериментов задаёт порядок выдачи этих пяти задач так, чтобы тяжёлые
> задачи не выдавались подряд. Сколькими способами он может это сделать?
>
> **🇹🇷 Türkçe**
>
> Görev 4. Bir AI modeline ardışık olarak beş farklı görev verilecek; bunlardan ikisi zor. Deney planlayıcısı, zor görevler art arda gelmeyecek şekilde bu beş görevin veriliş sırasını belirliyor. Bunu kaç farklı şekilde yapabilir?
>
> **✅ Cevap:** **72**

---

## 🧪 Bölüm 4 — Pratik / Kod Görevleri (çözümleriyle)

Olimpiyatların en seçkin bölümü: gerçek yarışma görevleri. Her biri ya **kodla doğrulanmış çözüm** ya da **resmî baseline** ile birlikte.

> ### 51 · 🇺🇸 ABD · USAAIO 2026 · 🧪
>
> **🎯 Bağlam:** USAAIO 2026 1. Tur açık uçlu görevi. Gerçek bir makine öğrenmesi pipeline'ı: tıbbi teşhis verisinde ikili sınıflandırma — ama yalnızca **k-En Yakın Komşu (kNN)** kullanma kısıtıyla. Veri seti kamuya açık.
>
> **❓ Görev** · `en`
>
> You are given the breast-cancer training set (30 numeric features, target ∈ {0,1}). Build a classifier that predicts the label on a hidden test set, evaluated by macro-F1. Constraint: among supervised models you may use **only kNN** (any preprocessing/pipeline is allowed).
>
> **🇹🇷 Türkçe**
>
> Breast-cancer eğitim verisi (30 sayısal öznitelik, hedef ∈ {0,1}) veriliyor. Gizli test kümesinde etiketi tahmin eden, makro-F1 ile ölçülen bir sınıflandırıcı kurun. Kısıt: gözetimli modellerden **yalnızca kNN** kullanılabilir (her türlü ön işleme/pipeline serbest).
>
> **📦 Veri seti:** https://huggingface.co/datasets/usaaio-official/2026_USAAIO_Round1_public
>
> **🔗 Kaynak:** https://www.usaaio.org/past-problems
>
> **🔑 Çözüm:** Anahtar içgörü: öznitelik ölçekleri çok farklı olduğundan **StandardScaler şart**. `StandardScaler → kNN(k=9, weights='distance')` pipeline'ı ile makro-F1 ham kNN'de 0.93 iken **0.97**'ye çıkar (5-kat çapraz doğrulama). Referans çözüm kodla çalıştırılıp doğrulandı.

---

> ### 52 · 🌐 Uluslararası · IOAI 2025 · 🧪
>
> **🎯 Bağlam:** IOAI 2025 (Pekin) Bireysel Yarışma pratik görevi. Bilgisayarla görü + **yoğunluk kestirimi (density estimation)**: bir sürüdeki tavukları saymak. Leaderboard'da ortalama bağıl hata ile puanlanır; herkese çalışan bir başlangıç kodu (baseline) verilir.
>
> **❓ Görev** · `en`
>
> You are given 100 training images of Silkie chickens, each with a ground-truth density map (180×320) whose sum equals the chicken count. Using a provided pretrained feature extractor, design and train a density-map decoder so that, for unseen images, the summed predicted map estimates the count. Scored by mean relative error.
>
> **🇹🇷 Türkçe**
>
> Her biri, toplamı tavuk sayısına eşit olan bir gerçek yoğunluk haritasına (180×320) sahip 100 eğitim görüntüsü veriliyor. Verilen önceden eğitilmiş öznitelik çıkarıcıyı kullanarak, görülmemiş görüntülerde tahmin haritasının toplamı sayıyı kestirecek şekilde bir yoğunluk-harita kod çözücüsü (decoder) tasarlayıp eğitin. Ortalama bağıl hata ile puanlanır.
>
> **📦 Veri seti:** https://github.com/IOAI-official/IOAI-2025
>
> **🔗 Kaynak:** https://ioai-official.org/china-2025
>
> **🔑 Çözüm:** Konvolüsyonel öznitelik çıkarıcının üstüne bir yoğunluk-decoder eklenir; çıktı 180×320'ye yeniden boyutlandırılır ve MSE ile eğitilir. **Resmî baseline skoru 0.71**, Bilim Kurulu'nun en iyisi **0.89**. Tam resmî baseline kodu veri setinde yer alır.

---

> ### 53 · 🇨🇦 Kanada · CAIO 2025 · 🧪
>
> **🎯 Bağlam:** Kanada ulusal elemesi (CAIO), 5 puanlık kısa hesap sorusu. Test ettiği kavram: doğrusal regresyonda modelin hatasını ölçen **maliyet (cost) fonksiyonu** — makine öğrenmesinin en temel yapı taşlarından biri. (Veri, soruda satır-içi verilir; harici veri seti yok.)
>
> **❓ Görev** · `en`
>
> A linear model f(x)=wx+b is set to w=6, b=4. On the 5 points (1,10), (2,17), (3,25), (4,32), (5,35), the cost is J = (1/2m)·Σ(f(xᵢ)−yᵢ)² with m=5. Compute J.
>
> **🇹🇷 Türkçe**
>
> Doğrusal model f(x)=wx+b, w=6, b=4 olarak ayarlanıyor. (1,10), (2,17), (3,25), (4,32), (5,35) noktalarında maliyet J = (1/2m)·Σ(f(xᵢ)−yᵢ)², m=5. J'yi hesaplayın.
>
> **🔗 Kaynak:** https://www.iaiocanada.com/prepare/
>
> **🔑 Çözüm:** Tahminler f(x)=6x+4 → 10, 16, 22, 28, 34. Kalıntıların kareleri: 0+1+9+16+1 = 27. **J = 27/(2·5) = 2.7.** (Adım adım ve kodla doğrulandı.)

---

> ### 54 · 🇨🇦 Kanada · CAIO 2025 · 🧪
>
> **🎯 Bağlam:** Kanada ulusal elemesi (CAIO), 5 puanlık kısa hesap sorusu. Test ettiği kavram: bir **karar ağacının** bir özniteliğe göre bölünmesinin ne kadar bilgi kazandırdığını ölçen **information gain** (entropi düşüşü). (Sınıf sayıları soruda verilir; harici veri yok.)
>
> **❓ Görev** · `en`
>
> A node contains 6 positive and 4 negative samples. Splitting on feature X yields a Left branch (4 positive, 1 negative) and a Right branch (2 positive, 3 negative). What is the Information Gain of this split? (log base 2)
>
> **🇹🇷 Türkçe**
>
> Bir düğümde 6 pozitif ve 4 negatif örnek var. X özniteliğine göre bölünce Sol dal (4 pozitif, 1 negatif) ve Sağ dal (2 pozitif, 3 negatif) oluşuyor. Bu bölünmenin Information Gain'i nedir? (log tabanı 2)
>
> **🔗 Kaynak:** https://www.iaiocanada.com/prepare/
>
> **🔑 Çözüm:** Entropi H = −Σ p·log₂p. Ebeveyn H=0.971; Sol H=0.722, Sağ H=0.971 → ağırlıklı çocuk entropisi = (5/10)·0.722 + (5/10)·0.971 = 0.846. **Information Gain = 0.971 − 0.846 = 0.12.** (Kodla doğrulandı.)

---

> ### 55 · 🇷🇴 Romanya · ONIA 2024 · 🧪
>
> **🎯 Bağlam:** Romanya ONIA (genişletilmiş takım). Test ettiği beceri: karmaşık modele sarılmadan **problemin geometrisini görmek**. Görev kendi içinde tam (harici veri yok).
>
> **❓ Görev** · `en`
>
> Points (X,Y) in [0,100]² are labeled 1 if inside an unknown axis-aligned rectangle, else 0. From labeled training points, build a classifier for any point in the region. Scored by accuracy.
>
> **🇹🇷 Türkçe**
>
> [0,100]² içindeki (X,Y) noktaları, bilinmeyen eksen-hizalı bir dikdörtgenin içindeyse 1, dışındaysa 0 etiketli. Etiketli eğitim noktalarından bölgedeki herhangi bir noktayı sınıflandıran bir model kurun. Doğrulukla puanlanır.
>
> **🔗 Kaynak:** https://roai.ro/
>
> **🔑 Çözüm:** Karar bölgesi bir dikdörtgen olduğundan karmaşık modele gerek yok: **pozitif noktaların sınırlayıcı kutusunu (bounding box)** al (min/maks X, min/maks Y); bir noktayı bu kutunun içindeyse pozitif de. **Doğrulama:** 200 rastgele dikdörtgen × 500 eğitim noktası → ortalama test doğruluğu **%99.3** (kodla ölçüldü).

---

> ### 56 · 🇬🇷 Yunanistan · PDTN (Talos) 2025 · 🧪
>
> **🎯 Bağlam:** Yunanistan ulusal olimpiyatı (Talos). Bir görüntüyü, çember üzerine gerilen **düz iplerle** (string art) yaklaşık oluşturma — şık bir doğrusal cebir uygulaması. (Açık uçlu optimizasyon görevi.)
>
> **❓ Görev** · `el`
>
> Approximate a target image using straight lines drawn over a circle (like thread/string art). Assign a darkness weight (0–100) to each candidate line so the composed result matches the target image as closely as possible.
>
> **🇹🇷 Türkçe**
>
> Bir hedef görüntüyü, çember üzerine çizilen düz çizgilerle (iplik/string art gibi) yaklaşık oluşturun. Her aday çizgiye 0–100 arası bir karartma ağırlığı atayın; öyle ki oluşan sonuç hedef görüntüye olabildiğince yakın olsun.
>
> **🔗 Kaynak:** https://pdp.pdtn.gr/
>
> **🔑 Çözüm:** Her çizgi, üzerinden geçtiği piksellere sabit bir karartma katkısı yapar → **görüntü = (çizgi-piksel matrisi) × (ağırlıklar)**. Hedefe en yakın sonucu veren 0–100 arası ağırlıklar **negatif-olmayan en küçük kareler (NNLS)** ile çözülür — yani problem şık biçimde doğrusal cebire indirgenir.

---


*Tam veri seti 1151 soru içerir ve iki süreç (kontrol + çeviri) tamamlandığında kamuya açılacaktır.*

## 📄 Lisans ve künye

- Kamuya açık olimpiyat materyallerinden **künye ile** derlenmiştir; amaç eğitim ve araştırmadır.
- Her sorunun kaynağı (yarışma, yıl) korunur; ticari/telifli materyal bilerek dışlanmıştır.
- Türkçe çeviriler **taslaktır**.
