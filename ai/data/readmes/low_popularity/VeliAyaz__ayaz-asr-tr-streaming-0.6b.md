---
license: other
license_name: openmdw-1.1
license_link: LICENSE
base_model: nvidia/nemotron-3.5-asr-streaming-0.6b
base_model_relation: finetune
pipeline_tag: automatic-speech-recognition
library_name: nemo
language:
- tr
- de
- en
- fr
- es
- it
- pt
- nl
- ru
- uk
- pl
- cs
- sk
- sl
- hr
- bg
- ro
- hu
- fi
- et
- lv
- lt
- sv
- da
- 'no'
- el
- ar
- he
- hi
- ja
- ko
- vi
- zh
tags:
- speech
- asr
- streaming
- turkish
- multilingual
- fastconformer
- rnnt
---

*Bu kart Türkçe ve İngilizcedir; İngilizcesi Türkçesinden sonra gelir. · This card is in Turkish and English; the English version follows the Turkish one.*

# Ayaz ASR — Türkçesi geliştirilmiş, akışlı, çok dilli konuşma tanıma (v0.2)

*Ayazda ses uzağa gider.*

Bu model, NVIDIA'nın `nvidia/nemotron-3.5-asr-streaming-0.6b` modeli [1] üzerinden Türkçe için ince ayarlanmıştır. Temel modelin lisansı OpenMDW-1.1'dir [2]. Bu çalışma NVIDIA tarafından onaylanmış ya da desteklenmiş değildir.

**Bu sürüm v0.2'dir.** v0.1'e göre günlük konuşmada, sesli mesajlarda ve YouTube konuşmasında hata düştü. Bu kazancın ölçüsü kısmen şişkindir: sesli mesaj ve geliştirici sınavlarının konuşmacıları eğitimde de var ve bu kümeler seçimde kullanıldı. Yeni konuşmacıya en yakın ölçüm YouTube videolarıdır: hata %20,45'ten %17,63'e indi. Okunmuş Türkçe PyTorch'ta temel modelle aynı düzeyde kaldı, cihaz içi int8 biçimde temel modelden +0,49 puan kötü; kısa komutlarda v0.1'e göre kazanç yok. Söz içermeyen seste metin üretme temel modele göre arttı, öteki dillerde kayıp arttı. Bu sürüm kabul ölçütlerinden birinde kaldı ve bilerek yayımlandı. Ölçümler aşağıda. v0.1'in dosyaları depoda `v0.1` etiketiyle duruyor.

## Neden bu model?

Denediğimiz çok dilli konuşma tanıma modelleri günlük Türkçede zayıf kaldı. Kısa Türkçe komutları başka bir dilde duydular; uzun konuşmada sözcükleri yanlış dile döktüler.

Yalnız Türkçeyle yapılan ince ayar ise çoğu zaman ters yönde bozuyor: model Türkçeyi öğrenirken öteki dilleri unutuyor. Makine öğrenmesinde bu olgunun adı yıkıcı unutmadır [3, 4]. Kendi ilk denememizde yalnız Türkçeyle eğitilen sürüm, FLEURS sınavının [5] 34 dilinin 32'sinde anlamlı biçimde geriledi. Almancada hata oranı 38 puan arttı.

Ayaz ASR bu iki sorunu birlikte çözmeye çalışıyor.

## Hedefler

- **Akış (streaming).** Konuşma sürerken metin üretmek; cümlenin bitmesini beklememek. Temel model bunu önbellekli FastConformer ve RNN-T yapısıyla destekliyor [1].
- **İyi Türkçe.** Günlük konuşmada, sesli mesajlarda ve kısa komutlarda.
- **Aynı konuşmada birden çok dil.** Türkçe öğrenilirken öteki diller korunmalı. Böylece bir konuşmanın bir sözü Türkçe, sonraki sözü Almanca ya da İngilizce olabilir.

Bunlar hedeflerdir. Ölçtüklerimizi aşağıda ayrıca veriyoruz; ölçmediğimiz bir şeyi vaat etmiyoruz.

## Ölçülen

**Nasıl ölçüldü.**
- Bu bölümün tabloları PyTorch'ta, akış kipinde, 560 ms'lik bağlamla ölçüldü (Kasım 2026). Dil her sınavda baştan verildi (Türkçe sınavlarda `tr-TR`). Türkçe tablodaki üç model aynı gün ölçüldü. Cihaz içi int8 biçimin ölçümü ayrı başlıkta.
- Ölçü sözcük hata oranıdır (WER, %). Japonca, Korece, Tayca ve Çincede harf hata oranıdır (CER, %).
- Karşılaştırmadan önce metin normalleştirilir. Türkçede: Unicode NFC; rakamlar Türkçe sözcüğe çevrilir (eğitim etiketlerinde de böyle yapıldı); Türkçe büyük-küçük harf kuralı (I → ı, İ → i); kesme işareti silinir; noktalama ve simgeler boşluğa döner. Öteki dillerde: Unicode NFKC, harfler küçültülür, noktalama ve simgeler boşluğa döner.
- **Sınav kayıtları eğitimde yok, ama seçimde kullanıldı.** Hiçbir sınav kaydı model ağırlıklarının eğitiminde kullanılmadı. Buna karşılık geliştirici kümesi eğitim adımını seçmede, sesli mesaj kümeleri adayı seçmede kullanıldı; FLEURS Türkçenin 150 kayıtlık bir alt kümesi de ara ölçütteydi. Aday ve paket kararında ayrıca FLEURS Türkçenin tamamı ve komut sınavı eşik olarak, bir gönüllünün eğitime girmeyen 186 kaydı da kazanç ölçüsü olarak kullanıldı. Bu yüzden geliştirici ve sesli mesaj satırları yansız değildir, iyimserdir.
- **Ayrım.** YODAS'ın 30 videosu video düzeyinde ayrıldı; kanal düzeyinde ayrım yapılmadı, yani bir konuşmacının eğitimdeki başka bir videoda bulunmadığı garanti değildir. Geliştiricinin sınav konuşmaları eğitim verisinden ayrı günlerden seçildi, ama konuşmacı eğitimde var. Sesli mesaj sınavı mesaj düzeyinde ayrıldı (6 mesaj, 4 konuşmacı): bu mesajlar eğitimde yok, ama 4 konuşmacının hepsinin başka mesajları hem v0.1'in hem v0.2'nin eğitiminde var.
- **Komutlar.** Okuma komutlarının sınav kayıtları eğitimdeki komut kayıtlarından ayrıdır, ama 20 komut metninin 17'si eğitimde başka kayıtlarla geçiyor; yani komut satırları görülmemiş sözü ölçmez. 20 kaydın 2'si Almancadır; int8 tablosunda yalnız Türkçe 18 kayıt var.
- **Küçük kümeler.** Sesli mesaj satırı 889 sözcük, geliştirici satırı tek kişiden 523 sözcük. Kısa söz ve komut satırlarındaki bir kayıtlık farklar (15 ile 14, 18 ile 17, 4 ile 3) fark sayılmamalıdır.

### Türkçe

| Sınav | Ne ölçer | Parça | Temel model | v0.1 | v0.2 |
|---|---|---|---|---|---|
| FLEURS tr, sınav bölümü [5, 6] | okunmuş genel Türkçe | 743 | 11,96 | 12,18 | 11,79 |
| YODAS Türkçe, ayrılmış 30 video [7–9] | YouTube konuşması | 705 | 39,17 | 20,45 | 17,63 |
| Sesli mesajlar | rıza veren gönüllülerin günlük konuşması; birden çok konuşmacı | 124 | 63,33 | 33,41 | 22,38 |
| Geliştiricinin günlük konuşması | tek konuşmacı, gerçek kullanım | 85 | 49,33 | 28,11 | 20,27 |
| Kısa sözler | 15 kısa söz (çoğu bir ya da iki sözcük, en uzunu sekiz; toplam yaklaşık 40 sözcük) ve söz içermeyen 1 parça | 16 | 95,0 (8'i boş) | 77,5 (2'si boş) | 77,5 (1'i boş) |
| Kısa sözler, sessizlik dolgulu | aynı parçalar; önüne 1,0, arkasına 1,2 saniye sessizlik eklenmiş | 16 | 90,0 (6'sı boş) | 80,0 (4'ü boş) | 80,0 (3'ü boş) |
| Okuma komutları | geliştiricinin 20 kısa komut kaydı; komutun doğru tanındığı kayıt sayısı (hata oranı değil) | 20 | 1 | 15 | 14 |
| Okuma komutları, sessizlik dolgulu | aynı kayıtlar, dolgulu | 20 | 7 | 18 | 17 |

Kısa söz satırlarında 16 parçanın biri söz içermez, doğru çıktısı boştur. Hata oranı yalnız 15 sözle hesaplanır; boş sayıları bu parçayı da içerir (bu parça her modelde, her iki satırda boş çıktı).

v0.2'nin kazancı günlük konuşmada, sesli mesajlarda ve YouTube konuşmasında. Okunmuş Türkçede temel modelle aynı düzeyde; kısa söz ve komut satırlarında v0.1'den iyi değil.

**Bu kazanç nasıl okunmalı.** v0.1 ile v0.2 arasındaki kazanç kısmen şişkindir. Sesli mesaj ve geliştirici satırlarının konuşmacıları eğitimde var ve bu kümeler seçimde kullanıldı. Eğitimdeki sesli mesaj 881 parçadan 3.863 parçaya, gönüllü sayısı 11'den 34'e çıktı; sınavdaki 4 konuşmacının üçünü v0.2 daha çok duydu. Bu yüzden yeni bir konuşmacı için geçerli kazanç bu satırlardan küçük olabilir. En temiz ölçüm YODAS satırıdır: hata %20,45'ten %17,63'e indi, göreli %13,8. Eğitimdeki YODAS verisi de 14.387 parçadan (24,6 saat) 87.189 parçaya (149,4 saat) çıktı. Sesli mesajda göreli kazanç %33,0, geliştiricide %27,9.

**v0.1'den v0.2'ye fark** (puan; farklar yuvarlanmamış değerlerden; parantezde %95 aralık, parça düzeyinde eşli önyükleme, 2.000 tekrar): FLEURS −0,40 (−0,80 … −0,02) · YODAS −2,82 (−3,49 … −2,13), video düzeyinde (30 video) −2,82 (−3,77 … −1,94) · sesli mesajlar −11,02 (−14,45 … −7,88), mesaj düzeyinde (6 mesaj) −11,02 (−14,25 … −5,71) · geliştirici −7,84 (−11,59 … −4,55). Bu aralıklar yalnız örnekleme belirsizliğini gösterir; yukarıdaki iyimserliği gidermez.

NVIDIA'nın kendi kartında temel modelin Türkçe FLEURS hatası %11,34'tür [1]. Bizim normalleştirmemizle aynı model %11,96 ölçüldü. Fark, metin normalleştirmesinin ayrıntılarından gelir. Bu yüzden karşılaştırmayı hep aynı ölçüm düzeninde, temel modelle yan yana veriyoruz.

### Öteki diller

FLEURS sınav bölümünde, Türkçe dışındaki 33 dilde temel modelle karşılaştırma. Fark puan olarak verilir; artı işareti hatanın arttığı anlamına gelir. "Anlamlı" demek, sözce düzeyinde eşli önyükleme (1.000 tekrar) ile bulunan %95 güven aralığının tamamen sıfırın üstünde (gerileme) ya da altında (iyileşme) olması demektir.

**Özet.**
- Almanca +0,5 · İngilizce +0,1 · Fransızca +0,3. İngilizcede anlamlı fark yok; Almancada ve Fransızcada anlamlı gerileme var.
- Türkçe dışındaki dillerin ortanca farkı +1,0 puan (v0.1'de +0,8).
- 28 dilde anlamlı gerileme (v0.1'de 23). Puan olarak en çok gerileyenler Letonca (+3,8), Rumence (+3,5) ve Hintçe (+2,9); göreli olarak Hintçe (%19,4), Japonca (%14,6) ve Rumence (%11,4). 33 dilin 20'sinde v0.2'nin hatası v0.1'inkinden yüksek.
- 3 dilde anlamlı fark yok; 2 dilde anlamlı iyileşme (İbranice ve Tayca).
- Tayca temel modelde de çalışmıyor (CER %99); değerlendirmenin dışında tutulur.

**Dil dil sonuçlar.** ★ işaretli 29 dil, kabul ölçütündeki ana dil grubudur.

| Dil | Ölçü | Sözce | Temel | v0.2 | Fark | %95 aralık | Hüküm |
|---|---|---|---|---|---|---|---|
| Almanca ★ | WER | 862 | 10,57 | 11,06 | +0,5 | +0,1 … +0,8 | gerileme |
| İngilizce ★ | WER | 647 | 10,79 | 10,85 | +0,1 | −0,4 … +0,5 | fark yok |
| Fransızca ★ | WER | 676 | 11,19 | 11,51 | +0,3 | +0,0 … +0,6 | gerileme |
| İspanyolca ★ | WER | 908 | 6,49 | 6,76 | +0,3 | +0,1 … +0,4 | gerileme |
| İtalyanca ★ | WER | 865 | 6,00 | 6,34 | +0,3 | +0,1 … +0,6 | gerileme |
| Portekizce ★ | WER | 919 | 8,67 | 8,98 | +0,3 | +0,1 … +0,5 | gerileme |
| Felemenkçe ★ | WER | 364 | 14,23 | 14,81 | +0,6 | +0,1 … +1,1 | gerileme |
| Rusça ★ | WER | 775 | 12,87 | 13,27 | +0,4 | +0,1 … +0,7 | gerileme |
| Ukraynaca ★ | WER | 750 | 15,56 | 16,64 | +1,1 | +0,7 … +1,5 | gerileme |
| Lehçe ★ | WER | 758 | 19,40 | 19,90 | +0,5 | +0,1 … +0,9 | gerileme |
| Çekçe ★ | WER | 723 | 23,69 | 25,22 | +1,5 | +1,0 … +2,0 | gerileme |
| Slovakça ★ | WER | 792 | 24,51 | 25,81 | +1,3 | +0,8 … +1,8 | gerileme |
| Slovence ★ | WER | 834 | 51,74 | 53,67 | +1,9 | +1,3 … +2,5 | gerileme |
| Hırvatça ★ | WER | 914 | 27,39 | 27,89 | +0,5 | +0,0 … +1,0 | gerileme |
| Bulgarca ★ | WER | 658 | 22,94 | 24,16 | +1,2 | +0,7 … +1,8 | gerileme |
| Rumence ★ | WER | 883 | 30,24 | 33,70 | +3,5 | +2,9 … +4,0 | gerileme |
| Macarca ★ | WER | 905 | 32,80 | 35,16 | +2,4 | +1,8 … +2,9 | gerileme |
| Fince ★ | WER | 918 | 22,24 | 23,43 | +1,2 | +0,7 … +1,7 | gerileme |
| Estonca ★ | WER | 893 | 32,74 | 35,00 | +2,3 | +1,5 … +3,0 | gerileme |
| Letonca ★ | WER | 851 | 52,61 | 56,39 | +3,8 | +3,0 … +4,5 | gerileme |
| Litvanca ★ | WER | 986 | 50,00 | 52,74 | +2,7 | +2,2 … +3,3 | gerileme |
| İsveççe ★ | WER | 759 | 25,02 | 26,40 | +1,4 | +0,9 … +1,9 | gerileme |
| Danca ★ | WER | 930 | 29,93 | 31,10 | +1,2 | +0,8 … +1,6 | gerileme |
| Norveççe | WER | 357 | 19,80 | 19,91 | +0,1 | −0,5 … +0,7 | fark yok |
| Yunanca ★ | WER | 650 | 46,08 | 47,05 | +1,0 | +0,5 … +1,4 | gerileme |
| Arapça ★ | WER | 428 | 15,86 | 16,84 | +1,0 | +0,5 … +1,5 | gerileme |
| İbranice | WER | 792 | 47,84 | 45,43 | −2,4 | −3,1 … −1,7 | iyileşme |
| Hintçe ★ | WER | 418 | 15,17 | 18,11 | +2,9 | +2,2 … +3,7 | gerileme |
| Japonca ★ | CER | 650 | 13,81 | 15,83 | +2,0 | +1,4 … +2,7 | gerileme |
| Korece ★ | CER | 382 | 8,94 | 9,48 | +0,5 | +0,3 … +0,8 | gerileme |
| Vietnamca ★ | WER | 857 | 14,71 | 16,22 | +1,5 | +1,2 … +1,9 | gerileme |
| Çince | CER | 945 | 19,45 | 19,31 | −0,1 | −0,6 … +0,3 | fark yok |
| Tayca | CER | 1.021 | 99,35 | 96,27 | −3,1 | −3,5 … −2,7 | (değerlendirme dışı) |

Aralığın bir ucu ±0,0 görünen satırlarda, sınır yuvarlamadan önce sıfırın hangi yanındaysa hüküm ona göredir.

### Cihaz içi biçim (int8)

Model sherpa-onnx [10] için int8'e dönüştürüldü. Bu depoda iki paket var: `sherpa-onnx-int8-560ms/` ve `sherpa-onnx-int8-1120ms/`. Aşağıdaki ölçümler 1.120 ms'lik paketle, gerçek bir sesli asistanın çözme koduyla yapıldı (Apple M4, yalnız işlemci; dil Türkçeye sabit). Çözme ayarı: sözün önüne 1,0, arkasına 1,8 saniye gürültü dolgusu (−70 dBFS) ve boş cezası (blank penalty) 1,5. Temel model, sherpa-onnx'in yayımladığı 1.120 ms'lik int8 paketiyle, aynı ayarla ölçüldü.

| Sınav | Parça | Temel model | v0.1 | v0.2 |
|---|---|---|---|---|
| FLEURS tr, sınav bölümü | 743 | 13,94 | 14,52 | 14,43 |
| YODAS Türkçe, ayrılmış 30 video | 705 | 33,64 | 20,17 | 18,23 |
| Geliştiricinin günlük konuşması | 85 | 46,08 | 28,30 | 21,80 |
| Sesli mesajlar (üç sınav kümesi birlikte, kırpılması giderilmiş ses) | 652 | 60,50 | 37,08 | 30,49 |
| Okuma komutları, Türkçe; komutun tam doğru yazıldığı kayıt sayısı (hata oranı değil) | 18 | 4 | 17 | 17 |

v0.1'den v0.2'ye fark (puan; parantezde %95 aralık): FLEURS −0,09 (−0,57 … +0,40) · YODAS −1,94 (−2,62 … −1,28) · geliştirici −6,50 (−9,85 … −3,50).

Sesli mesaj satırı üç sınav kümesinin (124, 137 ve 391 parça) toplamıdır: 652 parça, 124 mesaj, 23 konuşmacı. Kümeler mesaj düzeyinde ayrıldı; bu mesajlar eğitimde yok, ama 23 konuşmacının hepsinin başka mesajları eğitimde var. Bu satırda, dönüştürmede oluşan kırpılmanın giderildiği ses kopyası kullanıldı; son aşamanın eğitimi ve önceki iki ince ayardan biri de böyle sesle yapıldı. PyTorch tablosundaki sesli mesaj satırı ise işlenmemiş sesle ölçüldü.

Dil otomatik bırakılırsa sesli mesaj satırı temel modelde %76,34, v0.1'de %39,82, v0.2'de %31,23; komut satırı 4, 15, 15.

Tanıma süresi, dolgu dahil sesin süresinin ortalama 0,05'i oldu. Bu ayarlarla 1.120 ms'lik paket sesli mesajlarda daha doğru sonuç verdi, ama sonucu daha geç verir: 560 ms'lik paketle, varsayılan çözümle (dolgusuz, boş cezasız), aynı üç sesli mesaj kümesinde v0.2'nin hatası %33,54. Dil otomatik bırakılırsa kısa sözlerde hata artıyor: geliştiricinin 247 kısa sözünde (bunlar eğitimde de var) Türkçeye sabitken %28,66, otomatik dilde %34,85.

### Kabul ölçütleri

Bir aday ancak iki hükmü birden geçerse yayına girebilir.

**Türkçe hükmü:**
- Geliştiricinin günlük konuşmasında en az %10 göreli iyileşme.
- FLEURS Türkçede en çok +0,5 puan bozulma.
- Sessizlik dolgulu kısa söz sınavında en çok 2 boş çıktı.
- Eğitim sırasındaki ara ölçümde Almanca ve İngilizcede en çok +1,5 puan.

**Çok dil hükmü:**
- Almanca ve İngilizcede en çok +1,0 puan.
- ★ işaretli 29 dilin ortancası en çok +2,0 puan.
- Tayca dışında hiçbir dil +5,0 puanın üstünde değil.

Bu sürüm çok dil hükmünü geçti: Almanca +0,5, İngilizce +0,1; 29 dilin ortancası +1,2; en kötü dil Letonca (+3,8). Türkçe hükmünün dört ölçütünden üçünü geçti: günlük konuşmada göreli iyileşme %58,9 (seçimde kullanılan, iyimser bir küme); FLEURS Türkçe −0,2 puan; ara ölçümde temel modele göre Almanca +0,2, İngilizce +0,1. Dördüncü ölçütte kaldı: sessizlik dolgulu kısa söz sınavında 3 boş çıktı (sınır 2; v0.1'de 4). Bu üç boştan biri söz içermeyen parçadır, orada boş çıktı doğrudur; ölçüt yazıldığı gibi sayıldı, sonradan değiştirilmedi.

**Kuraldan bilerek saptık.** Yukarıdaki kurala göre iki hükmü birden geçmeyen aday yayına girmez; bu sürüm bir ölçütte kaldı ve yine de yayımlandı. v0.1 de dolgulu ölçümde aynı ölçütte kalmıştı. Gerekçemiz günlük konuşmadaki ve YouTube konuşmasındaki kazançtır; bu kazancın büyük bölümü yukarıda anlatılan iyimser kümelerden gelir, YouTube'daki kazanç daha küçük ama aralığı sıfırı içermiyor. Cihaz içi int8 biçimde FLEURS Türkçe farkı temel modele göre +0,49 puandır, yani +0,5 sınırının hemen altında. Aynı koşunun 7.000. adımı dördüncü ölçütü geçiyordu (dolgulu kısa sözde 2 boş; dolgulu komutta 18/20, 8.000. adımda 17/20), ama geliştirici hatası daha yüksekti (%21,99; 8.000. adımda %20,27). Seçim kuralı geliştirici hatasına baktığı için 8.000. adım seçildi. 7.000. adımın ağırlıkları saklanmadı; tam FLEURS Türkçe ve çok dil ölçümü de yapılmadı.

## Nasıl eğitildi

- **Taban ve araç.** `nvidia/nemotron-3.5-asr-streaming-0.6b` [1], NeMo 3.0.0 [11] ile eğitildi. NVIDIA'nın ince ayar rehberinden [12] yola çıkıldı.
- **Üç aşama.** Önce temel modelden iki ayrı ince ayar yapıldı: tarifleri v0.1'inki, verileri onun genişletilmiş hâliydi, ikincisinde sesli mesajların sesi temizlendi. Sonra iki modelin ağırlıkları yarı yarıya ortalandı (model çorbası [13]). Son aşamada bu ortalama model, aşağıdaki tam veriyle ve sesli mesajların temizlenmiş sesiyle yeniden ince ayarlandı.
- **Açık katmanlar.** Kodlayıcının son 8 katmanı, tahmin ağı, ortak katman ve dil istemi modülü eğitildi; yaklaşık 230 milyon parametre. Kodlayıcının geri kalanı donduruldu.
- **Ayar (son aşama).** AdamW, öğrenme oranı 1,5·10⁻⁵; parti başına 20 saniye ses; hedef 11.000 adım, her 1.000 adımda ölçüm. Bu sürüm 8.000. adımdır. Ara seçimde kısa söz ve komut ölçütleri kapalıydı: FLEURS Türkçenin alt kümesine, yankı kayıtlarına, Almanca ve İngilizce koruma ölçütüne uyan adımlar içinde geliştiricinin konuşmasında en düşük hatayı verdiği için seçildi. Sessizlik dolgulu kısa söz ölçütüne seçimde bakılmadı, sonraki ölçümde o ölçütte kaldı (bkz. Kabul ölçütleri). Önceki iki ince ayarda öğrenme oranı 3·10⁻⁵ idi.
- **Unutmaya karşı iki önlem.**
  - *Prova.* 32 dilden FLEURS eğitim bölümü kayıtları [5, 6] karışıma girer. Etiketleri, temel modelin aynı kayıtlar için ürettiği metindir; buna öz damıtma denir. Robins, yıkıcı unutmaya karşı provayı ve sözde provayı ele alır [4].
  - *Çapa (L2-SP).* Ağırlıklar her 10 adımda bir başlangıç modelinin ağırlıklarına doğru çekilir [14]. Son aşamada çapa, ortalama modeldir.
- **Boş örnekler.** Sessizlik ve gürültüden oluşan, hedefi boş metin olan örnekler. Model boş sese metin uydurmasın diye.
- **Donanım.** Tek bir Apple M4 Mac (24 GB bellek), Metal (MPS). Son aşama, ölçümler dahil yaklaşık 7,5 saat sürdü; önceki iki ince ayar da aynı makinede yapıldı (ölçümler dahil yaklaşık 9,3 ve 7,4 saat).
- **Tarif.** Eğitim tarifinin deposundaki betikler v0.1'in yoludur; v0.2'nin ayarları oradaki `configs/v0.2.yaml` dosyasında. Ortalama adımının betiği depoda yok.

## Veri

| Kaynak | Miktar | Lisans ya da rıza | Etiket |
|---|---|---|---|
| YODAS Türkçe, OWSM v4'ün temizlenmiş sürümü [7–9] | 87.189 parça, 149,4 saat, 3.848 video | CC-BY-3.0 [9] | videonun elle yazılmış alt yazısı |
| Geliştiricinin günlük konuşması | 215 parça | geliştiricinin kendi sesi | iki öğretmen modelin anlaştığı metin |
| Rıza veren gönüllülerin sesli mesajları | 3.863 parça, 5,8 saat, yaklaşık 660 mesaj, 34 konuşmacı | konuşmacıların yazılı rızası (yayın ve ticari kullanım dahil) | iki öğretmen modelin anlaştığı metin |
| Kısa söz ve komut kayıtları | 960 söz, 18,0 dakika, iki konuşmacı | konuşmacıların kendi kayıtları, yayın için rızayla | öğretmen modeller ve elle gözden geçirme |
| Boş örnekler | 3.285 parça, 1,7 saat | — | boş metin |
| Prova: FLEURS eğitim bölümü, 32 dil [5, 6] | 12.649 parça, 28,0 saat | CC-BY-4.0 [6] | temel modelin kendi çıktısı |

- **Karışım.** Son aşamanın karışımı 132.667 satır, 207,61 saattir. Küçük kaynaklar kopyalanarak ağırlıklandırıldı: sesli mesajlar 3 kopya (17,5 saat), kısa söz ve komutlar 15 kopya (4,5 saat), geliştiricinin konuşması 5 kopya, provada Almanca ve İngilizce 2 kopya (bütün prova 15.129 satır, 33,5 saat). Süreye göre paylar: YODAS %72,0, prova %16,1, sesli mesaj %8,4, kısa söz %2,2; kalan %1,3 geliştiricinin konuşması ve boş örnekler. Tablodaki miktarlar kopyasız sayılardır.
- **Öğretmen modeller.** Whisper large-v3-turbo [15, 16] birincil öğretmendir (MIT). Qwen3-ASR [17] ikinci görüştür (Apache-2.0). Whisper medium [15] üçüncü görüştür (MIT). En az iki öğretmenin anlaşmadığı parçalar eğitime girmedi.
- **Ham ses ve metin yayımlanmaz.** Bu depoda yalnız model ağırlıkları vardır.

## Sınırlar

- **Kısa sözler hâlâ zayıf.** Kısa söz sınavında hata %77,5; sessizlik dolgusuyla %80,0 ve 16 parçanın 3'ünde boş çıktı (biri söz içermeyen parça). Sınav küçüktür: 15 söz, yaklaşık 40 sözcük. Okuma komutlarında v0.2, v0.1'den iyi değil. Bu, modelin zayıf yanlarından biridir.
- **Konuşmacı çeşitliliği dar.** Türkçe kazancın bir kısmı tek bir konuşmacıya, geliştiriciye aittir. Çok konuşmacılı sınavlar Türkçenin ağız çeşitliliğini temsil etmiyor. Sesli mesaj sınavlarındaki 23 konuşmacının hepsi başka mesajlarıyla eğitimde var, bu yüzden o satırlar yeni konuşmacıya genellemeyi göstermez. En temiz kanıt ayrılmış YouTube videolarıdır, ama orada da konuşmacı ayrımı garanti değildir. FLEURS Türkçe sınavındaki 743 kaydın hepsi veri dosyasında erkek konuşmacı olarak işaretli [6].
- **Aynı konuşmada dil değişimi ölçülmedi.** Bu karttaki ölçümlerde dil her kayıt için baştan verildi; int8 tablosunun altında Türkçe kayıtlarda otomatik dil de ölçüldü. Bir sözden ötekine ya da cümlenin içinde dil değişimini ölçen bir sınavımız yok.
- **Öteki dillerde kayıplar var ve v0.1'e göre arttı.** 28 dilde anlamlı ama en çok 3,8 puanlık gerileme (v0.1'de 23 dil, en çok 3,5 puan). Puan küçük görünse de göreli artış bazı dillerde küçük değildir: Hintçede %19,4, Japoncada %14,6, Rumencede %11,4. Türkçe eğitimin bir yan etkisi olarak öteki dillerin çıktısına, doğru metinde olmayan Türkçe harfler (ç, ğ, ı, İ, ş) karışabiliyor: Türkçe dışındaki 25.070 FLEURS sözcesinin 89'unda; en çok Rumencede (883 sözcenin 44'ünde) ve Macarcada (905 sözcenin 23'ünde). Temel modelde aynı sözcelerden 6'sında görülüyor; bunların hiçbirinde ı, İ ya da ğ yok. Türkçe dil etiketi (`<tr-TR>`) de bu sözcelerin 19'unda çıktıya karışıyor.
- **Okunmuş Türkçede kazanç yok.** FLEURS Türkçede PyTorch'ta temel modelle aynı düzeyde (−0,2 puan); cihaz içi int8 biçimde temel modelden +0,49 puan kötü (sınır +0,5).
- **int8 sonuçları PyTorch sonuçlarından farklıdır.** Dışa aktarma, nicemleme ve çözme ayarı sonucu değiştirir: aynı model FLEURS Türkçede PyTorch'ta %11,79, int8 1.120 ms'lik pakette %14,43. Temel modelde de aynı yönde fark var (%11,96 ile %13,94). Bağlam da farklıdır: PyTorch ölçümleri 560 ms'lik bağlamla, bu paket 1.120 ms'lik bağlamla yapıldı.
- **Söz içermeyen seste metin üretme arttı.** PyTorch'ta 263 sözsüz kayıtta (sessizlik, gürültü, oda, yankı ve karışık ses) metin çıkan kayıt sayısı temel modelde 46 (%17,5), v0.1'de 89 (%33,8), v0.2'de 96 (%36,5). int8 biçimde, yukarıdaki dolgu ve boş cezasıyla, 282 sözsüz kaydın 150'sinde (dil otomatik) ya da 153'ünde (dil Türkçeye sabit) metin çıktı (%53–54); bu sınama yalnız v0.2'de yapıldı, int8'de temel model ve v0.1 ile karşılaştırma yok. Uygulama önüne bir ses etkinliği algılayıcısı koymalıdır.
- **Uzun canlı deneme yok.** int8 biçim sınav kümelerinde ölçüldü, ama v0.2 gerçek bir sohbette henüz denenmedi.
- **Argo ve küfür.** Model gerçek günlük konuşmayla eğitildi; söyleneni sansürlemeden yazar. Yayından önce int8 biçimde 541 kayıtla, otomatik dilde ve Türkçeye sabit, iki kipte sınandı. Sınamanın otomatik hükmü GEÇMEDİ, çünkü ölçüt sıfır vakaydı. Vakaların hepsi sentetik sesli Türkçe cümlelerdedir, tek tek incelendi: küfre benzeyen masum bir sözcüğü temiz seste bir harf eksik yazdı ve çıktı küfür gibi okunuyor, aynı sözcüğün gürültülü kopyasını doğru yazdı; ada benzeyen bir söz öbeğinde temel modelin yaptığı yanlışı yaptı. Söz içermeyen 282 kayıtta küfür ya da eğitim verisinde sık geçen bir özel ad üretmedi; tek istisna, Türkçeye sabit kipte bir gürültü kaydında çıkan hafif bir argo sözcük.
- **Alan.** YODAS'taki videoların çoğu ders anlatımıdır. Model sayıları genellikle sözcükle yazar (eğitim etiketlerinde rakamlar sözcüğe çevrildi); rakam bekleyen bir uygulama çıktıyı ayrıca dönüştürmelidir.

## Kullanım

**NeMo ile:**

```python
from huggingface_hub import hf_hub_download
import nemo.collections.asr as nemo_asr

path = hf_hub_download("VeliAyaz/ayaz-asr-tr-streaming-0.6b", "ayaz-asr-tr-streaming-0.6b.nemo")
asr_model = nemo_asr.models.ASRModel.restore_from(path)
```

Model böyle yüklenir; `restore_from` yayından önce bu dosyayla sınandı. v0.1 için `hf_hub_download` çağrısına `revision="v0.1"` ekleyin. Tanıma, dil seçimi, akış kipi ve parça uzunluğu için temel modelin kartındaki NeMo örnekleri geçerlidir [1].

**sherpa-onnx ile (cihaz içi, int8):** `sherpa-onnx-int8-560ms/` ve `sherpa-onnx-int8-1120ms/` klasörlerindeki `encoder.int8.onnx`, `decoder.int8.onnx`, `joiner.int8.onnx` ve `tokens.txt`, sherpa-onnx'in [10] Nemotron 3.5 ASR akışlı modeli için yayımladığı paketlerle aynı düzende ve aynı üst veriyle hazırlandı. Ölçümlerimizdeki çözme ayarı "Cihaz içi biçim" başlığında.

Bu depo Transformers biçimini içermez.

## Lisans

- Model ağırlıkları OpenMDW-1.1 lisansıyla yayımlanır [2]. Lisans metni ve temel modelin köken bildirimleri depodaki `LICENSE` ve `NOTICE` dosyalarındadır. Ticari kullanım serbesttir.
- Eğitim tarifi Apache-2.0 lisansıyla ayrı bir depoda yayımlandı: https://github.com/veliayaz71/ayaz-asr
- Veri kaynaklarının atıfları yukarıdaki tabloda ve kaynak listesindedir.

## Destek

Bir mühendis arkadaşım lastikçi dükkânı açtı. Şaşıranlara "Mühendislikten fazla kazanıyorum, lastikçiliği hobi olarak yapıyorum" diyor. Ben de bu modeli hobi olarak yapıyorum; yalnız benim hobim lastikçilik kadar kazandırmıyor. Bugüne kadarki toplam gelir: sıfır avro.

Fona da başvurmadım. Fon bulmayı bilenler zaten bulmuş, birkaç yılda milyarder olmuşlar; benim ekran okuyucum o hızda okuyamıyor.

Bu model, ekranı göremeyen biri tarafından, kulakla dinlenerek ve evdeki bir Mac'in gece mesaisiyle eğitildi. Neden var olduğunu yukarıda anlattım: Türkçeyi iyi duyan ve öteki dilleri korumaya çalışan bir model. Bağış yaparsanız GPU saatine, daha iyi bir mikrofona ve Türkçe konuşma verisinin temizlenmesine gider. Bağış yapamıyorsanız modeli deneyip yanlış duyduğu sözcükleri bildirmeniz de aynı değerde. Lastikçi arkadaşıma sorarsanız o da öyle der: önemli olan havanın kaçmaması.

Bağış bağlantıları yakında bu bölüme eklenecek. Ticari destek, entegrasyon ya da alana özel ince ayar için deponun Community sekmesinden yazabilirsiniz.

## Katkı

Bu modeli bir kişi geliştiriyor; topluluğun katkısıyla daha iyi olmasını istiyoruz. Katkının yolları şunlar:

- **Yanlış duyulan sözleri bildirmek.** Deponun Community (tartışma) sekmesinde yeni bir başlık açın. Ne söylediğinizi, modelin ne yazdığını, hangi dilde konuştuğunuzu ve ortamı (sessiz oda, sokak, telefon) yazın. Ses dosyası eklemeyin: sesiniz kişisel veridir ve tartışma sayfaları herkese açıktır.
- **Gerçek kullanımda denemek.** Ekran okuyucuyla ya da sesle çalışan görme engelli kullanıcıların ve farklı yörelerden konuşanların denemeleri özellikle değerli. Modelin hangi ağızda, hangi tür sözde zorlandığını bildirin.
- **Cihaz içi biçimler.** int8 sherpa-onnx biçimi bu depoda. Onu kendi verinizde ölçmek ya da modeli CoreML gibi başka biçimlere dönüştürüp ölçmek çok değerli. Sonuçları ölçüm düzeniyle birlikte paylaşın; karşılaştırma ancak aynı düzende anlamlıdır.
- **Daha büyük eğitimler.** Güçlü grafik işlemcisi olanlar eğitim tarifini (https://github.com/veliayaz71/ayaz-asr) daha çok veriyle ya da daha uzun koşturabilir. Sonucu yukarıdaki iki hükümle (Türkçe ve çok dil) ölçüp paylaşırsanız bu karta eklenebilir.
- **Karşılaştırma.** Herkese açık başka Türkçe modelleri aynı Türkçe sınavlardan ve 34 dillik FLEURS sınavından geçirmek. Hangi yaklaşımın öteki dilleri koruduğunu böyle öğrenebiliriz.
- **Ses bağışı.** Türkçe konuşmanızı bağışlamak isterseniz Mozilla'nın Common Voice projesine katılın [18]. Orada bağışlar projenin koşullarıyla yapılır ve kayıtlar herkese açık bir veri kümesi olarak yayımlanır; Türkçe kümesi de vardır [19]. Bu depo ses kaydı kabul etmez.
- **Kod.** Eğitim tarifi Apache-2.0 lisansıyla ayrı bir depoda: https://github.com/veliayaz71/ayaz-asr. Kod katkıları oraya gider.

Sesli mesajlarını bu modelin eğitimine bağışlayan gönüllülere teşekkür ederiz. Kişisel verilerini korumak için adlarını anmıyoruz.

## Atıf

Ayaz V. Ayaz ASR: Türkçesi geliştirilmiş, akışlı, çok dilli konuşma tanıma modeli, sürüm 0.2 [internet]. Hugging Face; 2026. Erişim adresi: https://huggingface.co/VeliAyaz/ayaz-asr-tr-streaming-0.6b

Geliştirici: Veli Ayaz · ORCID: https://orcid.org/0009-0009-5479-9464

```bibtex
@misc{ayaz2026ayazasr,
  author       = {Ayaz, Veli},
  title        = {Ayaz ASR: streaming, multilingual speech recognition with improved Turkish, version 0.2},
  year         = {2026},
  howpublished = {Hugging Face},
  url          = {https://huggingface.co/VeliAyaz/ayaz-asr-tr-streaming-0.6b}
}
```

## Kaynaklar

[1] NVIDIA. nvidia/nemotron-3.5-asr-streaming-0.6b — model kartı ve dosyalar [internet]. Hugging Face; 2026 [erişim 29.09.2026]. Erişim adresi: https://huggingface.co/nvidia/nemotron-3.5-asr-streaming-0.6b

[2] OpenMDW. OpenMDW License Agreement, sürüm 1.1 [internet]. [erişim 11.10.2026]. Erişim adresi: https://openmdw.ai/license/1-1/

[3] McCloskey M, Cohen NJ. Catastrophic interference in connectionist networks: the sequential learning problem. In: Bower GH, editor. Psychology of Learning and Motivation. Vol. 24. San Diego: Academic Press; 1989. p. 109–65.

[4] Robins A. Catastrophic forgetting, rehearsal and pseudorehearsal. Connection Science. 1995;7(2):123–46.

[5] Conneau A, Ma M, Khanuja S, Zhang Y, Axelrod V, Dalmia S, et al. FLEURS: few-shot learning evaluation of universal representations of speech. In: 2022 IEEE Spoken Language Technology Workshop (SLT); 2023. p. 798–805.

[6] Google. google/fleurs — veri kartı ve dosyalar [internet]. Hugging Face [erişim 02.10.2026]. Erişim adresi: https://huggingface.co/datasets/google/fleurs

[7] Li X, Takamichi S, Saeki T, Chen W, Shiota S, Watanabe S. YODAS: YouTube-oriented dataset for audio and speech. In: 2023 IEEE Automatic Speech Recognition and Understanding Workshop (ASRU); 2023. arXiv:2406.00899.

[8] Peng Y, Muhammad S, Sudo Y, Chen W, Tian J, Lin CJ, et al. OWSM v4: improving open Whisper-style speech models via data scaling and cleaning [ön baskı]. arXiv:2506.00338; 2025.

[9] ESPnet. espnet/yodas_owsmv4 — veri kartı [internet]. Hugging Face [erişim 28.09.2026]. Erişim adresi: https://huggingface.co/datasets/espnet/yodas_owsmv4

[10] k2-fsa. sherpa-onnx [internet]. GitHub [erişim 13.10.2026]. Erişim adresi: https://github.com/k2-fsa/sherpa-onnx

[11] NVIDIA-NeMo. NeMo v3.0.0 [internet]. GitHub; 07.08.2026 [erişim 28.09.2026]. Erişim adresi: https://github.com/NVIDIA-NeMo/NeMo/releases/tag/v3.0.0

[12] NVIDIA. How to fine-tune Nemotron 3.5 ASR for your language, domain, or accent [internet]. Hugging Face Blog; 04.06.2026 [erişim 28.09.2026]. Erişim adresi: https://huggingface.co/blog/nvidia/fine-tuning-nemotron-35-asr

[13] Wortsman M, Ilharco G, Gadre SY, Roelofs R, Gontijo-Lopes R, Morcos AS, et al. Model soups: averaging weights of multiple fine-tuned models improves accuracy without increasing inference time. In: Proceedings of the 39th International Conference on Machine Learning (ICML 2022). PMLR 162; 2022. p. 23965–98.

[14] Li X, Grandvalet Y, Davoine F. Explicit inductive bias for transfer learning with convolutional networks. In: Proceedings of the 35th International Conference on Machine Learning (ICML 2018); 2018. p. 2825–34.

[15] Radford A, Kim JW, Xu T, Brockman G, McLeavey C, Sutskever I. Robust speech recognition via large-scale weak supervision. In: Proceedings of the 40th International Conference on Machine Learning (ICML 2023). PMLR 202; 2023. p. 28492–518.

[16] OpenAI. openai/whisper-large-v3-turbo — model kartı [internet]. Hugging Face [erişim 02.10.2026]. Erişim adresi: https://huggingface.co/openai/whisper-large-v3-turbo

[17] Qwen. Qwen/Qwen3-ASR-1.7B — model kartı [internet]. Hugging Face [erişim 02.10.2026]. Erişim adresi: https://huggingface.co/Qwen/Qwen3-ASR-1.7B

[18] Mozilla Foundation. Common Voice [internet]. [erişim 12.10.2026]. Erişim adresi: https://commonvoice.mozilla.org/tr

[19] Mozilla Data Collective. Common Voice Scripted Speech 25.0 – Turkish [internet]. [erişim 12.10.2026]. Erişim adresi: https://mozilladatacollective.com/datasets/cmn2e7kbl01k2mm07gm5n1bc9

---

---

# Ayaz ASR — streaming, multilingual speech recognition with improved Turkish (v0.2)

*On a frosty night, sound carries far.* ("Ayaz" is Turkish for a clear, frosty night; it is also the developer's surname.)

This model is fine-tuned for Turkish from NVIDIA's `nvidia/nemotron-3.5-asr-streaming-0.6b` [1]. The base model is licensed under OpenMDW-1.1 [2]. This work is not endorsed or supported by NVIDIA.

**This is version 0.2.** Compared with v0.1, the error fell on everyday speech, voice messages and YouTube speech. This gain is partly inflated: the speakers of the voice-message and developer tests are also in training, and those sets were used in selection. The closest measure for a new speaker is the YouTube videos: the error fell from 20.45% to 17.63%. Read Turkish stayed level with the base model in PyTorch and is +0.49 points worse in the int8 on-device format; short commands did not improve compared with v0.1. Text output on non-speech audio rose compared with the base model, and the loss in other languages grew. This release failed one acceptance criterion and was published knowingly. The measurements are below. The v0.1 files remain in the repository under the tag `v0.1`.

## Why this model?

In our tests, the multilingual speech recognisers we tried were weak in everyday Turkish. They heard short Turkish commands as another language, and in longer speech they spilled words into the wrong language.

Fine-tuning on Turkish alone tends to fail in the opposite direction: while the model learns Turkish, it forgets the other languages. Machine learning calls this catastrophic forgetting [3, 4]. In our own first attempt, a version trained on Turkish only regressed significantly in 32 of the 34 FLEURS [5] languages; its German error rate rose by 38 points.

Ayaz ASR tries to address both problems at once.

## Goals

- **Streaming.** Produce text while the person is still speaking, without waiting for the sentence to end. The base model supports this with its cache-aware FastConformer and RNN-T design [1].
- **Good Turkish.** In everyday speech, voice messages and short commands.
- **Several languages in one conversation.** Keep the other languages while learning Turkish, so that one utterance can be Turkish and the next German or English.

These are goals. What we measured is listed separately below; we do not promise anything we have not measured.

## Measured

**How it was measured.**
- The tables in this section were measured in PyTorch, in streaming mode, with a 560 ms context (November 2026). The language was given up front for every test (`tr-TR` on the Turkish tests). The three models in the Turkish table were measured on the same day. The int8 on-device format has its own heading.
- The metric is word error rate (WER, %); for Japanese, Korean, Thai and Chinese it is character error rate (CER, %).
- Before comparison, text is normalised. Turkish: Unicode NFC; digits are spelled out as Turkish words (as in the training labels); Turkish casing (I → ı, İ → i); apostrophes are deleted; punctuation and symbols become spaces. Other languages: Unicode NFKC, lower-cased, punctuation and symbols become spaces.
- **Test recordings are not in training, but they were used in selection.** No test recording was used to train the weights. However, the developer set was used to choose the training step and the voice-message sets to choose the candidate, and a 150-recording subset of FLEURS Turkish was part of the interim criteria. The candidate and package decisions also used full FLEURS Turkish and the command test as thresholds, and 186 recordings of one volunteer that stayed out of training as a measure of gain. The developer and voice-message rows are therefore not unbiased; they are optimistic.
- **Separation.** Thirty YODAS videos were held out at video level, not channel level, so it is not guaranteed that a speaker is absent from other training videos. The developer's test speech comes from days not used for training, but the speaker is in training. The voice-message test was held out at message level (6 messages, 4 speakers): these messages are not in training, but all 4 speakers have other messages in the training data of both v0.1 and v0.2.
- **Commands.** The reading-command test recordings are separate from the command recordings used in training, but 17 of the 20 command texts occur in training in other recordings, so the command rows do not measure unseen wording. Two of the 20 recordings are in German; the int8 table holds only the 18 Turkish ones.
- **Small sets.** The voice-message row has 889 words, and the developer row 523 words from one person. One-recording differences in the short-utterance and command rows (15 and 14, 18 and 17, 4 and 3) should not be read as differences.

### Turkish

| Test | What it measures | Clips | Base model | v0.1 | v0.2 |
|---|---|---|---|---|---|
| FLEURS tr, test split [5, 6] | read general Turkish | 743 | 11.96 | 12.18 | 11.79 |
| YODAS Turkish, 30 held-out videos [7–9] | YouTube speech | 705 | 39.17 | 20.45 | 17.63 |
| Voice messages | everyday speech of consenting volunteers; several speakers | 124 | 63.33 | 33.41 | 22.38 |
| Developer's everyday speech | one speaker, real use | 85 | 49.33 | 28.11 | 20.27 |
| Short utterances | 15 short utterances (mostly one or two words, the longest eight; about 40 words in all) and 1 clip without speech | 16 | 95.0 (8 empty) | 77.5 (2 empty) | 77.5 (1 empty) |
| Short utterances, silence-padded | the same clips with 1.0 s of silence before and 1.2 s after | 16 | 90.0 (6 empty) | 80.0 (4 empty) | 80.0 (3 empty) |
| Reading commands | the developer's 20 short command recordings; number recognised as the right command (not an error rate) | 20 | 1 | 15 | 14 |
| Reading commands, silence-padded | the same recordings, padded | 20 | 7 | 18 | 17 |

In the short-utterance rows, one of the 16 clips contains no speech and its correct output is empty. The error rate uses only the 15 utterances; the empty counts include this clip (it came out empty for every model in both rows).

The gain of v0.2 is in everyday speech, voice messages and YouTube speech. On read Turkish it is level with the base model; on short utterances and commands it is no better than v0.1.

**How to read this gain.** The gain from v0.1 to v0.2 is partly inflated. The speakers of the voice-message and developer rows are in training, and those sets were used in selection. Voice-message training data grew from 881 to 3,863 clips and from 11 to 34 volunteers, so v0.2 heard three of the four test speakers more. The gain for a new speaker may therefore be smaller than these rows suggest. The cleanest measure is the YODAS row: the error fell from 20.45% to 17.63%, 13.8% in relative terms. YODAS training data also grew from 14,387 clips (24.6 h) to 87,189 clips (149.4 h). The relative gain is 33.0% on voice messages and 27.9% on the developer's speech.

**Difference from v0.1 to v0.2** (points; computed from unrounded values; 95% interval in brackets, paired bootstrap at clip level, 2,000 resamples): FLEURS −0.40 (−0.80 … −0.02) · YODAS −2.82 (−3.49 … −2.13), at video level (30 videos) −2.82 (−3.77 … −1.94) · voice messages −11.02 (−14.45 … −7.88), at message level (6 messages) −11.02 (−14.25 … −5.71) · developer −7.84 (−11.59 … −4.55). These intervals show sampling uncertainty only; they do not remove the optimism described above.

NVIDIA's own card gives the base model's Turkish FLEURS error as 11.34% [1]. With our normalisation the same model measures 11.96%. The difference comes from normalisation details, which is why we always report against the base model under the same set-up.

### Other languages

FLEURS test split, 33 languages other than Turkish, compared with the base model. Differences are in points; a plus sign means the error went up. "Significant" means the 95% interval from a paired, utterance-level bootstrap (1,000 resamples) lies entirely above zero (regression) or below zero (improvement).

**Summary.**
- German +0.5 · English +0.1 · French +0.3. No significant difference in English; a significant regression in German and French.
- Median difference across the non-Turkish languages: +1.0 points (+0.8 in v0.1).
- Significant regression in 28 languages (23 in v0.1). The largest in points are Latvian (+3.8), Romanian (+3.5) and Hindi (+2.9); in relative terms Hindi (19.4%), Japanese (14.6%) and Romanian (11.4%). In 20 of the 33 languages the error of v0.2 is higher than that of v0.1.
- No significant difference in 3 languages; significant improvement in 2 (Hebrew and Thai).
- Thai does not work in the base model either (CER 99%) and is excluded from the verdict.

**Per language.** The 29 languages marked ★ form the main group used in the acceptance criteria.

| Language | Metric | Utterances | Base | v0.2 | Diff. | 95% interval | Verdict |
|---|---|---|---|---|---|---|---|
| German ★ | WER | 862 | 10.57 | 11.06 | +0.5 | +0.1 … +0.8 | regression |
| English ★ | WER | 647 | 10.79 | 10.85 | +0.1 | −0.4 … +0.5 | no difference |
| French ★ | WER | 676 | 11.19 | 11.51 | +0.3 | +0.0 … +0.6 | regression |
| Spanish ★ | WER | 908 | 6.49 | 6.76 | +0.3 | +0.1 … +0.4 | regression |
| Italian ★ | WER | 865 | 6.00 | 6.34 | +0.3 | +0.1 … +0.6 | regression |
| Portuguese ★ | WER | 919 | 8.67 | 8.98 | +0.3 | +0.1 … +0.5 | regression |
| Dutch ★ | WER | 364 | 14.23 | 14.81 | +0.6 | +0.1 … +1.1 | regression |
| Russian ★ | WER | 775 | 12.87 | 13.27 | +0.4 | +0.1 … +0.7 | regression |
| Ukrainian ★ | WER | 750 | 15.56 | 16.64 | +1.1 | +0.7 … +1.5 | regression |
| Polish ★ | WER | 758 | 19.40 | 19.90 | +0.5 | +0.1 … +0.9 | regression |
| Czech ★ | WER | 723 | 23.69 | 25.22 | +1.5 | +1.0 … +2.0 | regression |
| Slovak ★ | WER | 792 | 24.51 | 25.81 | +1.3 | +0.8 … +1.8 | regression |
| Slovenian ★ | WER | 834 | 51.74 | 53.67 | +1.9 | +1.3 … +2.5 | regression |
| Croatian ★ | WER | 914 | 27.39 | 27.89 | +0.5 | +0.0 … +1.0 | regression |
| Bulgarian ★ | WER | 658 | 22.94 | 24.16 | +1.2 | +0.7 … +1.8 | regression |
| Romanian ★ | WER | 883 | 30.24 | 33.70 | +3.5 | +2.9 … +4.0 | regression |
| Hungarian ★ | WER | 905 | 32.80 | 35.16 | +2.4 | +1.8 … +2.9 | regression |
| Finnish ★ | WER | 918 | 22.24 | 23.43 | +1.2 | +0.7 … +1.7 | regression |
| Estonian ★ | WER | 893 | 32.74 | 35.00 | +2.3 | +1.5 … +3.0 | regression |
| Latvian ★ | WER | 851 | 52.61 | 56.39 | +3.8 | +3.0 … +4.5 | regression |
| Lithuanian ★ | WER | 986 | 50.00 | 52.74 | +2.7 | +2.2 … +3.3 | regression |
| Swedish ★ | WER | 759 | 25.02 | 26.40 | +1.4 | +0.9 … +1.9 | regression |
| Danish ★ | WER | 930 | 29.93 | 31.10 | +1.2 | +0.8 … +1.6 | regression |
| Norwegian | WER | 357 | 19.80 | 19.91 | +0.1 | −0.5 … +0.7 | no difference |
| Greek ★ | WER | 650 | 46.08 | 47.05 | +1.0 | +0.5 … +1.4 | regression |
| Arabic ★ | WER | 428 | 15.86 | 16.84 | +1.0 | +0.5 … +1.5 | regression |
| Hebrew | WER | 792 | 47.84 | 45.43 | −2.4 | −3.1 … −1.7 | improvement |
| Hindi ★ | WER | 418 | 15.17 | 18.11 | +2.9 | +2.2 … +3.7 | regression |
| Japanese ★ | CER | 650 | 13.81 | 15.83 | +2.0 | +1.4 … +2.7 | regression |
| Korean ★ | CER | 382 | 8.94 | 9.48 | +0.5 | +0.3 … +0.8 | regression |
| Vietnamese ★ | WER | 857 | 14.71 | 16.22 | +1.5 | +1.2 … +1.9 | regression |
| Chinese | CER | 945 | 19.45 | 19.31 | −0.1 | −0.6 … +0.3 | no difference |
| Thai | CER | 1,021 | 99.35 | 96.27 | −3.1 | −3.5 … −2.7 | (excluded) |

Where one end of an interval shows as ±0.0, the verdict follows the side of zero the unrounded bound lies on.

### On-device format (int8)

The model was converted to int8 for sherpa-onnx [10]. This repository holds two packages: `sherpa-onnx-int8-560ms/` and `sherpa-onnx-int8-1120ms/`. The measurements below used the 1,120 ms package and the decoding code of a real voice assistant (Apple M4, CPU only; language fixed to Turkish). Decoding settings: 1.0 s of noise padding before the utterance and 1.8 s after it (−70 dBFS), blank penalty 1.5. The base model was measured with the 1,120 ms int8 package published by sherpa-onnx, under the same settings.

| Test | Clips | Base model | v0.1 | v0.2 |
|---|---|---|---|---|
| FLEURS tr, test split | 743 | 13.94 | 14.52 | 14.43 |
| YODAS Turkish, 30 held-out videos | 705 | 33.64 | 20.17 | 18.23 |
| Developer's everyday speech | 85 | 46.08 | 28.30 | 21.80 |
| Voice messages (three test sets together, audio with clipping removed) | 652 | 60.50 | 37.08 | 30.49 |
| Reading commands, Turkish; number of recordings transcribed exactly right (not an error rate) | 18 | 4 | 17 | 17 |

Difference from v0.1 to v0.2 (points; 95% interval in brackets): FLEURS −0.09 (−0.57 … +0.40) · YODAS −1.94 (−2.62 … −1.28) · developer −6.50 (−9.85 … −3.50).

The voice-message row pools three test sets (124, 137 and 391 clips): 652 clips, 124 messages, 23 speakers. The sets were held out at message level; these messages are not in training, but all 23 speakers have other messages there. This row uses the copy of the audio with conversion clipping removed; the last training stage and one of the two earlier fine-tuning runs also used such audio. The voice-message row of the PyTorch table used unprocessed audio.

If the language is left on automatic, the voice-message row is 76.34% for the base model, 39.82% for v0.1 and 31.23% for v0.2; the command row is 4, 15 and 15.

Recognition took on average 0.05 of the audio's duration, padding included. With these settings the 1,120 ms package was more accurate on voice messages, but it returns results later: with the 560 ms package and default decoding (no padding, no blank penalty), the error of v0.2 on the same three voice-message sets is 33.54%. If the language is left on automatic, the error on short utterances rises: on the developer's 247 short utterances (these are also in training) it is 28.66% with the language fixed to Turkish and 34.85% on automatic.

### Acceptance criteria

A candidate may be released only if it passes both verdicts.

**Turkish verdict:**
- At least 10% relative improvement on the developer's everyday speech.
- At most +0.5 points on FLEURS Turkish.
- At most 2 empty outputs on the silence-padded short-utterance test.
- At most +1.5 points on German and English in the in-training check.

**Multilingual verdict:**
- At most +1.0 points on German and English.
- Median of the 29 ★ languages at most +2.0 points.
- No language above +5.0 points, Thai excepted.

This release passed the multilingual verdict: German +0.5, English +0.1; median of the 29 languages +1.2; worst language Latvian (+3.8). It passed three of the four Turkish criteria: 58.9% relative improvement on everyday speech (an optimistic set that was used in selection); FLEURS Turkish −0.2 points; in the in-training check, against the base model, German +0.2 and English +0.1. It failed the fourth: 3 empty outputs on the silence-padded short-utterance test (limit 2; 4 in v0.1). One of these three is the clip without speech, where an empty output is correct; the criterion was counted as written and was not changed afterwards.

**We departed from the rule knowingly.** By the rule above, a candidate that does not pass both verdicts is not released; this release failed one criterion and is published anyway. v0.1 also failed this criterion on the padded measurement. Our reason is the gain on everyday and YouTube speech; most of it comes from the optimistic sets described above, while the YouTube gain is smaller but its interval excludes zero. In the int8 on-device format the FLEURS Turkish difference from the base model is +0.49 points, just under the +0.5 limit. Step 7,000 of the same run passed the fourth criterion (2 empty outputs on padded short utterances; 18/20 padded commands, against 17/20 at step 8,000), but its developer error was higher (21.99%, against 20.27% at step 8,000). The selection rule looks at developer error, so step 8,000 was chosen. The weights of step 7,000 were not kept, and full FLEURS Turkish and multilingual measurements were not run for it.

## How it was trained

- **Base and toolkit.** `nvidia/nemotron-3.5-asr-streaming-0.6b` [1], trained with NeMo 3.0.0 [11], starting from NVIDIA's fine-tuning guide [12].
- **Three stages.** First, two separate fine-tuning runs from the base model: the recipe of v0.1 on an extended version of its data, with cleaned voice-message audio in the second run. Then the weights of the two models were averaged half and half (a model soup [13]). In the last stage this averaged model was fine-tuned again on the full data listed below, again with cleaned voice-message audio.
- **Trainable layers.** The last 8 encoder layers, the prediction network, the joint network and the language-prompt module, about 230 million parameters. The rest of the encoder was frozen.
- **Settings (last stage).** AdamW, learning rate 1.5·10⁻⁵; 20 seconds of audio per batch; target 11,000 steps, measured every 1,000 steps. This release is step 8,000. The short-utterance and command gates were off in the interim selection: among the steps that met the criteria on the FLEURS Turkish subset, the echo recordings and the German and English guard, it had the lowest error on the developer's speech. The silence-padded short-utterance criterion played no part in this choice, and the later measurement failed it (see Acceptance criteria). The learning rate in the two earlier runs was 3·10⁻⁵.
- **Two safeguards against forgetting.**
  - *Rehearsal.* FLEURS training-split recordings in 32 languages [5, 6] are mixed in. Their labels are the base model's own transcripts of the same recordings (self-distillation). Robins discusses rehearsal and pseudorehearsal as remedies for catastrophic forgetting [4].
  - *Anchor (L2-SP).* Every 10 steps the weights are pulled towards the starting model's weights [14]. In the last stage the anchor is the averaged model.
- **Empty examples.** Silence and noise with an empty target, so the model does not invent text for non-speech.
- **Hardware.** A single Apple M4 Mac (24 GB memory), Metal (MPS). The last stage took about 7.5 hours including measurements; the two earlier runs were also done on the same machine (about 9.3 and 7.4 hours including measurements).
- **Recipe.** The scripts in the training-recipe repository follow the v0.1 path; the settings of v0.2 are in `configs/v0.2.yaml` there. The averaging step has no script in that repository.

## Data

| Source | Amount | Licence or consent | Labels |
|---|---|---|---|
| YODAS Turkish, cleaned OWSM v4 release [7–9] | 87,189 clips, 149.4 h, 3,848 videos | CC-BY-3.0 [9] | the video's manually written subtitles |
| Developer's everyday speech | 215 clips | the developer's own voice | text on which two teacher models agree |
| Voice messages from consenting volunteers | 3,863 clips, 5.8 h, about 660 messages, 34 speakers | speakers' written consent (including publication and commercial use) | text on which two teacher models agree |
| Short-utterance and command recordings | 960 utterances, 18.0 min, two speakers | the speakers' own recordings, with consent for release | teacher models plus manual review |
| Empty examples | 3,285 clips, 1.7 h | — | empty text |
| Rehearsal: FLEURS training split, 32 languages [5, 6] | 12,649 clips, 28.0 h | CC-BY-4.0 [6] | the base model's own output |

- **Mixture.** The mixture of the last stage has 132,667 rows and 207.61 hours. Small sources were weighted by copying: voice messages 3 copies (17.5 h), short utterances and commands 15 copies (4.5 h), the developer's speech 5 copies, German and English rehearsal 2 copies (all rehearsal 15,129 rows, 33.5 h). Shares by duration: YODAS 72.0%, rehearsal 16.1%, voice messages 8.4%, short utterances 2.2%; the remaining 1.3% is the developer's speech and empty examples. The amounts in the table are counted without copies.
- **Teacher models.** Whisper large-v3-turbo [15, 16] is the primary teacher (MIT). Qwen3-ASR [17] is the second opinion (Apache-2.0). Whisper medium [15] is the third opinion (MIT). Clips on which at least two teachers did not agree were left out.
- **No raw audio or text is published.** This repository contains model weights only.

## Limitations

- **Short utterances are still weak.** Error on the short-utterance test is 77.5%; with silence padding it is 80.0%, with 3 of 16 outputs empty (one of them the clip without speech). The test is small: 15 utterances, about 40 words. On reading commands v0.2 is no better than v0.1. This is one of the model's weak points.
- **Narrow speaker diversity.** Part of the Turkish gain belongs to a single speaker, the developer. Multi-speaker tests do not represent the range of Turkish accents. All 23 speakers in the voice-message tests have other messages in training, so those rows do not show generalisation to new speakers. The cleanest evidence is the held-out YouTube videos, but speaker separation is not guaranteed there either. All 743 recordings in the FLEURS Turkish test split are marked as male speakers in the dataset files [6].
- **Language switching within a conversation was not measured.** In the measurements on this card the language was given up front for every recording; below the int8 table, automatic language was also measured on Turkish recordings. We have no test of switching language from one utterance to the next or inside a sentence.
- **Losses in other languages, larger than in v0.1.** Significant regression in 28 languages, at most 3.8 points (23 languages and at most 3.5 points in v0.1). Though small in points, the relative rise is not small in some languages: 19.4% in Hindi, 14.6% in Japanese, 11.4% in Romanian. As a side effect of the Turkish training, Turkish letters (ç, ğ, ı, İ, ş) that are not in the reference transcript sometimes appear in the output of other languages: in 89 of 25,070 non-Turkish FLEURS utterances, most often Romanian (44 of 883) and Hungarian (23 of 905). On the same utterances the base model does this in 6, none of them with ı, İ or ğ. The Turkish language tag (`<tr-TR>`) also leaks into the output of 19 of these utterances.
- **No gain on read Turkish.** Level with the base model on FLEURS Turkish in PyTorch (−0.2 points); in the int8 on-device format +0.49 points worse than the base model (limit +0.5).
- **int8 results differ from PyTorch results.** Export, quantisation and decoding settings change the result: on FLEURS Turkish the same model gives 11.79% in PyTorch and 14.43% with the int8 1,120 ms package. The base model shows a difference in the same direction (11.96% and 13.94%). The context also differs: the PyTorch measurements used 560 ms, this package 1,120 ms.
- **Text output on non-speech audio rose.** In PyTorch, on 263 recordings without speech (silence, noise, room, echo and mixed sound), the number with text output is 46 (17.5%) for the base model, 89 (33.8%) for v0.1 and 96 (36.5%) for v0.2. In int8, with the padding and blank penalty above, 150 (language automatic) or 153 (language fixed to Turkish) of 282 non-speech recordings produced text (53–54%); this test was run for v0.2 only, so int8 has no comparison with the base model or v0.1. An application should put a voice activity detector in front of the model.
- **No long live trial.** The int8 format was measured on the test sets, but v0.2 has not yet been tried in a real conversation.
- **Slang and profanity.** The model was trained on real everyday speech and transcribes what is said without censoring it. Before release it was tested on 541 recordings in int8 format, in two modes: automatic language and fixed to Turkish. The automatic verdict of this test was NOT PASSED, because the criterion was zero cases. All cases are in synthetic Turkish sentences and were reviewed one by one: it wrote an innocent word that sounds like profanity one letter short on clean audio, and the output reads like profanity, while it wrote the noisy copy of the same word correctly; on a phrase that sounds like a name it made the same mistake as the base model. On 282 recordings without speech it produced no profanity and no proper name that is frequent in its training data, with one exception: a mild slang word on one noise recording with the language fixed to Turkish.
- **Domain.** Most YODAS videos are lectures. The model usually writes numbers as words (digits were spelled out in the training labels); an application that expects digits has to convert the output.

## Usage

**With NeMo:**

```python
from huggingface_hub import hf_hub_download
import nemo.collections.asr as nemo_asr

path = hf_hub_download("VeliAyaz/ayaz-asr-tr-streaming-0.6b", "ayaz-asr-tr-streaming-0.6b.nemo")
asr_model = nemo_asr.models.ASRModel.restore_from(path)
```

This is how the model loads; `restore_from` was tested with this file before release. For v0.1, add `revision="v0.1"` to the `hf_hub_download` call. For transcription, language selection, streaming mode and chunk size, the NeMo examples in the base model's card apply [1].

**With sherpa-onnx (on-device, int8):** `encoder.int8.onnx`, `decoder.int8.onnx`, `joiner.int8.onnx` and `tokens.txt` in the `sherpa-onnx-int8-560ms/` and `sherpa-onnx-int8-1120ms/` folders were prepared with the same layout and metadata as the packages sherpa-onnx [10] publishes for the Nemotron 3.5 ASR streaming model. The decoding settings of our measurements are under "On-device format".

This repository does not include a Transformers format.

## Licence

- Model weights are released under OpenMDW-1.1 [2]. The licence text and the base model's notices of origin are in the repository's `LICENSE` and `NOTICE` files. Commercial use is permitted.
- The training recipe is released under Apache-2.0 in a separate repository: https://github.com/veliayaz71/ayaz-asr
- Data sources are credited in the table above and in the reference list.

## Support

An engineer friend of mine opened a tyre shop. When people look surprised, he says: "It pays better than engineering, so now I do tyres as a hobby." I build this model as a hobby too. The difference is that my hobby doesn't pay like his: total income so far, zero euros.

I didn't apply for funding either. The people who know how to find funds found them long ago and became billionaires in a few years; my screen reader can't read that fast.

This model was trained by someone who cannot see the screen, by ear, on a home Mac working night shifts. Why it exists is explained above: a model that hears Turkish well and tries to keep the other languages. Donations go to GPU hours, a better microphone and cleaning Turkish speech data. If you can't donate, trying the model and reporting the words it gets wrong is worth just as much. Ask my tyre-shop friend and he'll say the same: what matters is that the air doesn't leak out.

Donation links will be added to this section soon. For commercial support, integration or domain-specific fine-tuning, please write in the repository's Community tab.

## Contributing

One person develops this model; we would like it to get better with the community's help. Ways to contribute:

- **Report misrecognitions.** Open a new thread in the repository's Community tab. Write what you said, what the model wrote, which language you were speaking and the setting (quiet room, street, phone). Do not attach audio: your voice is personal data, and discussion pages are public.
- **Try it in real use.** Tests by blind and low-vision users who work with a screen reader or by voice, and by speakers from different regions, are especially valuable. Tell us which accents and kinds of utterance the model struggles with.
- **On-device formats.** The int8 sherpa-onnx format is in this repository. Measuring it on your own data, or converting the model to other formats such as CoreML and measuring it there, is very valuable. Share the results together with your measurement set-up; comparisons only make sense under the same set-up.
- **Larger training runs.** People with strong GPUs can run the training recipe (https://github.com/veliayaz71/ayaz-asr) with more data or for longer. If you measure the result against the two verdicts above (Turkish and multilingual) and share it, it can be added to this card.
- **Comparisons.** Run other public Turkish models through the same Turkish tests and the 34-language FLEURS test. This is how we can learn which approaches keep the other languages.
- **Donate your voice.** If you would like to donate Turkish speech, join Mozilla's Common Voice project [18]. Contributions there are made under the project's terms, and the recordings are published as an open dataset; there is a Turkish dataset too [19]. This repository does not accept voice recordings.
- **Code.** The training recipe is in a separate repository under Apache-2.0: https://github.com/veliayaz71/ayaz-asr. Code contributions go there.

We thank the volunteers who donated their voice messages to train this model. We do not name them, to protect their personal data.

## Citation

Ayaz V. Ayaz ASR: streaming, multilingual speech recognition with improved Turkish, version 0.2 [Internet]. Hugging Face; 2026. Available from: https://huggingface.co/VeliAyaz/ayaz-asr-tr-streaming-0.6b

Developer: Veli Ayaz · ORCID: https://orcid.org/0009-0009-5479-9464

*(The BibTeX entry is given in the Turkish section above.)*

## References

[1] NVIDIA. nvidia/nemotron-3.5-asr-streaming-0.6b — model card and files [Internet]. Hugging Face; 2026 [cited 2026 Sep 29]. Available from: https://huggingface.co/nvidia/nemotron-3.5-asr-streaming-0.6b

[2] OpenMDW. OpenMDW License Agreement, version 1.1 [Internet]. [cited 2026 Oct 11]. Available from: https://openmdw.ai/license/1-1/

[3] McCloskey M, Cohen NJ. Catastrophic interference in connectionist networks: the sequential learning problem. In: Bower GH, editor. Psychology of Learning and Motivation. Vol. 24. San Diego: Academic Press; 1989. p. 109–65.

[4] Robins A. Catastrophic forgetting, rehearsal and pseudorehearsal. Connection Science. 1995;7(2):123–46.

[5] Conneau A, Ma M, Khanuja S, Zhang Y, Axelrod V, Dalmia S, et al. FLEURS: few-shot learning evaluation of universal representations of speech. In: 2022 IEEE Spoken Language Technology Workshop (SLT); 2023. p. 798–805.

[6] Google. google/fleurs — dataset card and files [Internet]. Hugging Face [cited 2026 Oct 2]. Available from: https://huggingface.co/datasets/google/fleurs

[7] Li X, Takamichi S, Saeki T, Chen W, Shiota S, Watanabe S. YODAS: YouTube-oriented dataset for audio and speech. In: 2023 IEEE Automatic Speech Recognition and Understanding Workshop (ASRU); 2023. arXiv:2406.00899.

[8] Peng Y, Muhammad S, Sudo Y, Chen W, Tian J, Lin CJ, et al. OWSM v4: improving open Whisper-style speech models via data scaling and cleaning [Preprint]. arXiv:2506.00338; 2025.

[9] ESPnet. espnet/yodas_owsmv4 — dataset card [Internet]. Hugging Face [cited 2026 Sep 28]. Available from: https://huggingface.co/datasets/espnet/yodas_owsmv4

[10] k2-fsa. sherpa-onnx [Internet]. GitHub [cited 2026 Oct 13]. Available from: https://github.com/k2-fsa/sherpa-onnx

[11] NVIDIA-NeMo. NeMo v3.0.0 [Internet]. GitHub; 2026 Aug 7 [cited 2026 Sep 28]. Available from: https://github.com/NVIDIA-NeMo/NeMo/releases/tag/v3.0.0

[12] NVIDIA. How to fine-tune Nemotron 3.5 ASR for your language, domain, or accent [Internet]. Hugging Face Blog; 2026 Jun 4 [cited 2026 Sep 28]. Available from: https://huggingface.co/blog/nvidia/fine-tuning-nemotron-35-asr

[13] Wortsman M, Ilharco G, Gadre SY, Roelofs R, Gontijo-Lopes R, Morcos AS, et al. Model soups: averaging weights of multiple fine-tuned models improves accuracy without increasing inference time. In: Proceedings of the 39th International Conference on Machine Learning (ICML 2022). PMLR 162; 2022. p. 23965–98.

[14] Li X, Grandvalet Y, Davoine F. Explicit inductive bias for transfer learning with convolutional networks. In: Proceedings of the 35th International Conference on Machine Learning (ICML 2018); 2018. p. 2825–34.

[15] Radford A, Kim JW, Xu T, Brockman G, McLeavey C, Sutskever I. Robust speech recognition via large-scale weak supervision. In: Proceedings of the 40th International Conference on Machine Learning (ICML 2023). PMLR 202; 2023. p. 28492–518.

[16] OpenAI. openai/whisper-large-v3-turbo — model card [Internet]. Hugging Face [cited 2026 Oct 2]. Available from: https://huggingface.co/openai/whisper-large-v3-turbo

[17] Qwen. Qwen/Qwen3-ASR-1.7B — model card [Internet]. Hugging Face [cited 2026 Oct 2]. Available from: https://huggingface.co/Qwen/Qwen3-ASR-1.7B

[18] Mozilla Foundation. Common Voice [Internet]. [cited 2026 Oct 12]. Available from: https://commonvoice.mozilla.org/en

[19] Mozilla Data Collective. Common Voice Scripted Speech 25.0 – Turkish [Internet]. [cited 2026 Oct 12]. Available from: https://mozilladatacollective.com/datasets/cmn2e7kbl01k2mm07gm5n1bc9

---
