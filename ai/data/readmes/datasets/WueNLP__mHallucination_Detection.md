---
license: cc
task_categories:
- token-classification
- text2text-generation
language:
- ar
- de
- zh
- tr
- ru
- eu
- fr
- ca
- fi
- it
- ms
- ro
- pt
- ur
- hi
- he
- pl
- sd
- sr
- la
- es
- vi
- eo
- cs
- ko
- ja
size_categories:
- 1K<n<10K
---


# Multilingual Hallucination Detection Dataset (mFAVA)

The dataset was created as part of the paper: [How Much Do LLMs Hallucinate across Languages? On Multilingual Estimation of LLM Hallucination in the Wild](https://arxiv.org/abs/2502.12769)

Below is the figure summarizing the multilingual hallucination detection dataset creation (and [ multilingual hallucination evaluation](https://huggingface.co/datasets/WueNLP/mHallucination_Evaluation) dataset):

![Pipeline](estimation_pipeline.drawio.png)

## Dataset Details

The dataset is a multilingual extension of [FAVA](https://github.com/abhika-m/FAVA). The dataset is created by sourcing 150 prompts from 
FAVA datasets and 150 prompts from (test split) Google [NS](https://github.com/google-research-datasets/natural-questions). 

The dataset displayed here is a portion of gold and silver (synthetic) annotations of 5 languages: `Arabic, German, Chinese, Turkish, Russian`.

You can find the silver annotations for rest of the languages on the project [github](https://github.com/WorldHellow/mHallucinations-LLM).

| Language   | Language Family                                  | Script         | Test-Set |
|------------|--------------------------------------------------|----------------|----------|
| Arabic     | Afro-Asiatic (Semitic)                           | Arabic         | Gold     |
| Chinese    | Sino-Tibetan (Sinitic)                           | Chinese (Han)  | Gold     |
| German     | Indo-European (Germanic)                         | Latin          | Gold     |
| Russian    | Indo-European (Slavic)                           | Cyrillic       | Gold     |
| Turkish    | Turkic (Common Turkic)                           | Latin          | Gold     |
| Basque     | Language Isolate                                 | Latin          | Silver   |
| Cantonese  | Sino-Tibetan (Sinitic)                           | Chinese (Han)  | Silver   |
| Catalan    | Indo-European (Romance)                          | Latin          | Silver   |
| Czech      | Indo-European (Slavic)                           | Latin          | Silver   |
| Esperanto  | Constructed                                      | Latin          | Silver   |
| Finnish    | Uralic (Finnic)                                  | Latin          | Silver   |
| French     | Indo-European (Romance)                          | Latin          | Silver   |
| Hebrew     | Afro-Asiatic (Semitic)                           | Hebrew         | Silver   |
| Hindi      | Indo-Aryan                                       | Devanagari     | Silver   |
| Hungarian  | Uralic (Ugric)                                   | Latin          | Silver   |
| Indonesian | Austronesian (Malayo-Polynesian)                 | Latin          | Silver   |
| Italian    | Indo-European (Romance)                          | Latin          | Silver   |
| Japanese   | Japonic                                          | Kanji          | Silver   |
| Korean     | Koreanic                                         | Hangul         | Silver   |
| Latin      | Indo-European (Italic)                           | Latin          | Silver   |
| Lithuanian | Indo-European (Slavic)                           | Latin          | Silver   |
| Malay      | Austronesian (Malayo-Polynesian)                 | Latin          | Silver   |
| Polish     | Indo-European (Slavic)                           | Latin          | Silver   |
| Portuguese | Indo-European (Romance)                          | Latin          | Silver   |
| Romanian   | Indo-European (Romance)                          | Latin          | Silver   |
| Serbian    | Indo-European (Slavic)                           | Cyrillic       | Silver   |
| Sindhi     | Indo-Aryan                                       | Arabic         | Silver   |
| Spanish    | Indo-European (Romance)                          | Latin          | Silver   |
| Urdu       | Indo-Aryan                                       | Arabic         | Silver   |
| Vietnamese | Austroasiatic (Vietic)                           | Latin          | Silver   |


The annotations use FAVA annotation scheme of 6 hallucination labels: `[entity, contadiction, relation, invented, subjective, unverifiable]`

![Gold Annotation Statistics](data_stats.png)

For further details on how the dataset is created, read our paper on [archive](https://arxiv.org/abs/2502.12769). 



## Uses

The dataset can be used as a test set for evaluating hallucination detection task. 


## Dataset Structure

Each element contains four keys: a Wikipedia `references`, generated response `generated_text`, span level gold annotations `gold_annotations`,
span level silver (synthetic) annotations `silver_annotations`, and `languages`. 

Following is an example in `Arabic`:

```
{
        "references": "البقولية المزروعة كحبوب وزيتية هذه المقالة عن المحصول. للقصص المصورة، انظر الفول السوداني. لمعاني أخرى، انظر الفول السوداني (توضيح). \"Arachis hypogaea\" يعيد توجيهك إلى هنا. للحصول على مسحوق حساسية الفول السوداني، انظر مسحوق حساسية الفول السوداني-dnfp . \"البازلاء\" تعيد توجيهك إلى هنا. للموسيقى الشعبية، انظر غوبر بيز. تصنيف الفول السوداني العلمي المملكة: Plantae Clade : Tracheophytes Clade : Angiosperms Clade : Eudicots Clade : Rosids النظام: Fabales العائلة: Fabaceae العائلة الفرعية: Faboideae جنس: Arachis الأنواع: A. hypogaea الاسم الثنائي Arachis hypogaea L. الأنواع الفرعية والأنواع الفرعية (والدرون وار) (إكوادوريا كرافوف) & W. C. جريج var. الفستيجاتا (والدرون) كرافوف. & W. C. جريج var. الكرافوف البيرووي & W. C. جريج var. (فولغاريس هارز سبسب) (hypogea L. var) (هيرسوتا جيه كوهلر) hypogaea L. مترادفات [1] Arachis nambyquarae Hoehne Lathyrus esquirolii H. Lév. الفول السوداني (Arachis hypogaea) ، والمعروف أيضًا باسم الفول السوداني ، [2] غوبر (الولايات المتحدة) ، [3] بيندار (الولايات المتحدة) [3] أو جوز القرد (المملكة المتحدة) ، هو محصول حبيبي يزرع أساسًا من أجل بذورها الصالحة للأكل . يتم زراعتها على نطاق واسع في المناطق الاستوائية و شبه الاستوائية ، وهي مهمة لكل من المنتجين التجاريين الصغار والكبار. يتم تصنيفها على حد سواء باعتبارها حبوب البقول [4] ، وبسبب محتوياتها العالية من الزيت ، زراعة الزيت. [5] بلغ الإنتاج السنوي العالمي للفول السوداني المجفف 44 مليون طن في عام 2016 ، بقيادة الصين بنسبة 38٪ من إجمالي العالم. بشكل غير نموذجي بين نباتات المحاصيل البقولية ، تنمو قشور الفول السوداني تحت الأرض (الجيوكاربي) بدلاً من فوق الأرض. مع أخذ هذه السمة في الاعتبار، أعطى عالم النباتات كارل لينيوس الفول السوداني اسمًا خاصًا Hypogaea ، والذي يعني \"تحت الأرض\". تنتمي الفول السوداني إلى العائلة النباتية للفاصوليا (أو Leguminosae) ، والمعروفة عادة باسم عائلة البقوليات أو الفاصوليا أو البازلاء. [1] مثل معظم البقوليات الأخرى ، تحتوي الفول السوداني على بكتيريا متكافئة لتثبيت النيتروجين في عقدة الجذر. [6] القدرة على تثبيت النيتروجين تعني أن الفول السوداني يحتاج إلى أسمدة أقل تحتوي على النيتروجين ويحسن خصوبة التربة ، مما يجعله ذا قيمة في دورات المحاصيل . التعريف النباتي للجوز هو \"فاكهة يصبح جدار المبيض فيها صلبًا عند النضج\". باستخدام هذا المعيار، الفول السوداني ليس جوز. [1] ومع ذلك ، عادة ما يتم تصنيف الفول السوداني على أنه المكسرات لأغراض الطهي وفي اللغة الإنجليزية العامة بشكل عام. الفول السوداني مماثل في طعم وملفاته الغذائية لمكسرات الأشجار مثل الجوز واللوز ، وكمكسرات طهي ، غالبًا ما يتم تقديمها بطرق مماثلة في المطبخ الغربي. تاريخ الفول السوداني جنس الفول السوداني من أمريكا الجنوبية ، شرق جبال الأنديز ، حول بيرو وبوليفيا والأرجنتين والبرازيل . [8] نشأت الفول السوداني المزروعة (A. hypogaea) من هجين بين نوعين من الفول السوداني البري ، يعتقد أنهما A. duranensis و A. ipaensis . [8] [9] [10] كان من الممكن أن يكون الهجين الأولي عقيمًا ، لكن مضاعفة الكروموسوم العفوية استعادت خصوبته ، مما يشكل ما يطلق عليه amphidiploid أو allotetraploid . [1] يشير التحليل الوراثي إلى أن التهجين قد حدث مرة واحدة فقط وأدى إلى A. monticola ، وهو شكل برّي من الفول السوداني الذي يحدث في عدد قليل من المواقع المحدودة في شمال غرب الأرجنتين ، أو في جنوب شرق بوليفيا ، حيث يتم زراعة أنواع الفول السوداني مع الميزات الأكثر برّية اليوم ، [2] ومن خلال الاختيار الاصطناعي إلى A. hypogaea . [1] [2] عملية الترويض من خلال الاختيار الاصطناعي جعلت A. hypogaea مختلفة بشكل كبير عن أقاربه البرية. النباتات المنزلية أكثر شجيرة، وأكثر تكثيفاً، ولديها بنية مختلفة للقشور والبذور الأكبر. من هذا المركز الأساسي للمصدر، انتشرت الزراعة وشكلت مراكز ثانوية وثالثة للتنوع في بيرو، الإكوادور، البرازيل، باراغواي، وأوروغواي. مع مرور الوقت ، تطورت الآلاف من أنواع الفول السوداني الأرضية ؛ يتم تصنيفها إلى ستة أنواع نباتية ونوعين فرعيين (كما هو مذكور في جدول تصنيف الفول السوداني العلمي). الأنواع الفرعية A. h. fastigiata أكثر استقامة في عادات نموها ولديها دورات زراعة أقصر. الأنواع الفرعية A. h. hypogaea تنتشر أكثر على الأرض ولديها دورات زراعة أطول. [11] تم تاريخ أقدم بقايا الآثار المعروفة من الشعيرات بحوالي 7،600 عامًا ، وربما كان نوعًا برّيًا كان في زراعة ، أو A. hypogaea في المرحلة الأولى من التدجين. [12] تم العثور عليها في بيرو ، حيث تكون الظروف المناخية الجافة مواتية للحفاظ على المواد العضوية. من المؤكد تقريباً أن زراعة الفول السوداني سبقت ذلك في مركز المنشأ حيث المناخ أكثر رطوبة. العديد من الثقافات ما قبل كولومبوس، مثل موشي، تصور الفول السوداني في الفن. [13] كانت الزراعة راسخة في أمريكا الوسطى قبل وصول الإسبان. هناك، وجد الغزاة طلال كاكاهواتل (اسم النبات باللغة الناهوتل، وبالتالي الاسم باللغة الإسبانية كاكاويت) عرض للبيع في سوق تينوشتيتلان . تم تقديم زراعته في أوروبا في القرن التاسع عشر من خلال إسبانيا ، وخاصة فالنسيا ، حيث لا يزال يتم إنتاجه ، وإن كان بشكل هامشي. [14] نشر التجار الأوروبيون الفول السوداني في وقت لاحق في جميع أنحاء العالم ، والزراعة الآن منتشرة على نطاق واسع في المناطق الاستوائية والجزئية الاستوائية. في غرب أفريقيا ، استبدلت بشكل كبير نبات المحاصيل من نفس العائلة ، والفول السوداني بامبارا ، التي تنمو كرات بذورها أيضًا تحت الأرض. في آسيا ، أصبحت دعامة زراعية ، وهذه المنطقة هي الآن أكبر منتج في العالم. [15] تم إدخال الفول السوداني إلى الولايات المتحدة خلال الفترة الاستعمارية وزرعها كمحاصيل حديقة. بدءًا من عام 1870 ، تم استخدامه كمادة أولية للحيوانات حتى ازداد استهلاك الإنسان في ثلاثينيات القرن الماضي. [1] دافع جورج واشنطن كارفر (1864-1943) عن الفول السوداني كجزء من جهوده للتوسع الزراعي في الجنوب الأمريكي ، حيث استنفدت التربة بعد زراعة القطن المتكررة. اخترع ونشر المئات من المنتجات القائمة على الفول السوداني، بما في ذلك مستحضرات التجميل، الألوان، الطلاء، البلاستيك، البنزين والنيتروجليسرين. [17] بدأت وزارة الزراعة في الولايات المتحدة برنامجًا لتشجيع الإنتاج الزراعي والاستهلاك البشري للفول السوداني في أواخر القرن التاسع عشر وأوائل القرن العشرين. [16] تم تطوير زبدة الفول السوداني في عام 1890 في الولايات المتحدة. أصبح معروفًا بعد أن بدأت شركة بيتش نوت في بيع زبدة الفول السوداني في معرض سانت لويس العالمي لعام 1904. [18] التكوين التغذية الفول السوداني، فالنسيا، الخام القيمة الغذائية لكل 100 غرام طاقة 2.385 كيلو غرام (570 كيلوجرام) الكربوهيدرات 21 غرام سكر 0.0 غرام الألياف الغذائية 9 غرام دهون 48 غرام مشبعة 7 غرام أحادية غير مشبعة 24 غرام متعددة غير مشبعة 16 غرام بروتين 25 غرام تريبتوفان 0.2445 غرام ثريونين 0.859 غرام أيزولوسين 0.882 غرام ليوسين 1.627 غرام ليزين 0.901 غرام ميتيونين 0.308 غرام سيستين 0.322 غرام فينيلالانين 1.300 غرام تيروزين 1.020 غرام فالنين 1.052 غرام آرجينين 3.001 غرام هستيدين 0.634 غرام ألانين 0.997 غرام أسبراتيك اسيد 3.060 غرام غلاتاميك اسيد 5.24 غرام غليكسين 1.512 غرام برولين 1.247 غرام برولين 1.236 غرام [20] تحتوي الفول السوداني الخام على 4٪ من الماء ، و 48٪ من الدهون ، و 25٪ من البروتين ، و 21٪ من الكربوهيدرات ، بما في ذلك 9٪ من الألياف الغذائية (الجدول الأيمن ، بيانات المغذيات التابعة لوزارة الزراعة الأمريكية). الفول السوداني غني بالمواد الغذائية الأساسية في كمية مرجعية قدرها 100 غرام (3 + 1 ⁄ 2 أونصة) ، توفر الفول السوداني 2385 كيلوجول (570 كيلوكالوري) من الطاقة الغذائية ، وهي مصدر ممتاز (محدد بأكثر من 20٪ من القيمة اليومية ، DV) لعدة فيتامينات B ، فيتامين E ، العديد من المعادن الغذائية ، مثل المنغنيز (95٪ DV) ، المغنيسيوم (52٪ DV) والفوسفور (48٪ DV) ، والألياف الغذائية (الجدول الأيمن). الدهون في الغالب متعددة غير المشبعة و أحادية غير المشبعة (83٪ من إجمالي الدهون عند الجمع). تظهر بعض الدراسات أن تناول الفول السوداني بانتظام يرتبط بانخفاض خطر الوفاة من بعض الأمراض. [1] [2] ومع ذلك ، فإن تصاميم الدراسة لا تسمح باستدلال السبب والنتيجة. وفقًا لإدارة الغذاء والدواء الأمريكية ، \"تشير الأدلة العلمية إلى أن تناول 1.5 أوقية يوميًا من معظم المكسرات (مثل الفول السوداني) كجزء من نظام غذائي منخفض في الدهون المشبعة والكوليسترول قد يقلل من خطر الإصابة بأمراض القلب\". [23] المواد الكيميائية النباتية تحتوي الفول السوداني على البوليفينول ، والدهون غير المشبعة متعددة وغير المشبعة أحادية ، والفيتوستيرول والألياف الغذائية بكميات مماثلة للعديد من المكسرات. [1] تحتوي جلود الفول السوداني على ريسفيراترول ، والذي يخضع لأبحاث أولية لتأثيراته المحتملة على البشر. يحتوي زيت الفول السوداني على 46٪ من الدهون الأحادية غير المشبعة (أساسًا حمض الأولييك) و 32٪ من الدهون متعددة غير المشبعة (أساسًا حمض اللينوليك) و 17٪ من الدهون المشبعة (أساسًا حمض البالميتيك). [26] [27] يمكن استخراجها من الفول السوداني بالكامل باستخدام طريقة بسيطة من الماء والطرد المركزي",
        "generated_text": "الوزن التقريبي لكوب من الأرز هو مسألة لم يتم تحديدها بشكل مباشر في النص المرجعي المقدم. يعتبر الكثيرون أن الفول السوداني يمثل الغذاء المثالي بفضل قيمته الغذائية العالية. النص يركز بشكل أساسي على التصنيف العلمي للفول السوداني، تاريخه، واستخداماته بالإضافة إلى محتواه الغذائي وكيفية زراعته. للحصول على إجابة دقيقة، عادة ما يتم الرجوع إلى معلومات خاصة بقياسات الأطعمة وأوزانها. ومع ذلك، استناداً إلى المعلومات الشائعة، يمكن تقدير وزن كوب من الفول السوداني بحسب القيم المعتادة في الوصفات والإرشادات الغذائية، لكن هذه التقديرات قد تختلف بناءً على ما إذا كان الفول مطبوخًا أو غير مقشر، وما إذا كان كاملاً أو مجروشاً. من المعروف أن الفول السوداني يضيف نكهة فري",
        "gold_annotations": "الوزن التقريبي لكوب من الأرز هو مسألة لم يتم تحديدها بشكل مباشر في النص المرجعي المقدم. يعتبر الكثيرون أن الفول السوداني يمثل الغذاء المثالي بفضل قيمته الغذائية العالية. النص يركز بشكل أساسي على التصنيف العلمي للفول السوداني، تاريخه، واستخداماته بالإضافة إلى محتواه الغذائي وكيفية زراعته. للحصول على إجابة دقيقة، عادة ما يتم الرجوع إلى معلومات خاصة بقياسات الأطعمة وأوزانها. ومع ذلك، استناداً إلى المعلومات الشائعة، كان <unverifiable> يمكن تقدير وزن كوب من الفول السوداني بحسب القيم المعتادة في الوصفات والإرشادات الغذائية، لكن هذه التقديرات قد تختلف الفول مطبوخًا أو غير مقشر، وما إذا كان كاملاً أو مجروشاً بناءً على ما إذا </unverifiable> . من المعروف أن الفول السوداني يضيف نكهة فري",
        "silver_annotations": "الوزن التقريبي لكوب من <entity>الأرز</entity> هو مسألة لم يتم تحديدها بشكل مباشر في النص المرجعي المقدم. <subjective>يعتبر الكثيرون أن الفول السوداني يمثل الغذاء المثالي بفضل قيمته الغذائية العالية.</subjective> النص يركز بشكل أساسي على التصنيف العلمي للفول السوداني، تاريخه، واستخداماته بالإضافة إلى محتواه الغذائي وكيفية زراعته. للحصول على إجابة دقيقة، عادة ما يتم الرجوع إلى معلومات خاصة بقياسات الأطعمة وأوزانها. ومع ذلك، استناداً إلى المعلومات الشائعة، يمكن تقدير وزن كوب من الفول السوداني بحسب القيم المعتادة في الوصفات والإرشادات الغذائية، لكن هذه التقديرات قد تختلف بناءً على ما إذا كان الفول <entity>مطبوخًا</entity> أو غير مقشر، وما إذا كان كاملاً أو مجروشاً. <subjective>من المعروف أن الفول السوداني يضيف نكهة فري",
        "language": "arabic"
}

```

German example: 


```
{
        "references": "Antares, während der frühen Entwicklung als Taurus II bekannt, ist ein verbrauchbares Startsystem, das von der Orbital Sciences Corporation (später Teil von Northrop Grumman) und dem Pivdenne Design Bureau entwickelt wurde, um das Raumschiff Cygnus als Teil der COTS- und CRS-Programme der NASA zur Internationalen Raumstation zu starten. Mit der Fähigkeit, Nutzlasten von mehr als 8.000 kg in eine niedrige Erdumlaufbahn zu starten, ist Antares die größte von Northrop Grumman betriebene Rakete. Antares startet vom Mid-Atlantic Regional Spaceport und machte seinen Erstflug am 21. April 2013. Antares 100 wurde im Jahr 2014 und die Serie 200 wurde im Jahr 2023 aufgrund der Unverfügbarkeit von Komponenten eingestellt. Ab Januar 2024 ist Antares 300 in der Entwicklung. Die NASA gewährte Orbital im Jahr 2008 ein Commercial Orbital Transportation Services (COTS) Space Act Agreement (SAA), um die Lieferung von Fracht an die Internationale Raumstation zu demonstrieren. Orbital (und später Northrop Grumman) nutzte Antares, um seine Cygnus-Raumschiff für diese Missionen zu starten. Ab August 2023 wurde es nur für Cygnus-Starts zur ISS verwendet, obwohl es für kommerzielle Starts bestimmt war. Ursprünglich als Taurus II bezeichnet, wurde das Fahrzeug am 12. Dezember 2011 nach dem gleichnamigen Stern in Antares umbenannt. Von insgesamt 18 Starts hat Antares ein Versagen erlitten. Beim fünften Start am 28. Oktober 2014 scheiterte die Rakete katastrophal und das Fahrzeug und die Nutzlast wurden zerstört. Die Erstststadiummotoren der Rakete wurden als Ursache für den Ausfall identifiziert. Für nachfolgende Starts wurde ein anderer Motor gewählt, und die Rakete kehrte am 17. Oktober 2016 erfolgreich in den Flug zurück. Die Antares flog in zwei großen Design-Iterationen, der 100-Serie und der 200-Serie. Beide Serien haben eine Castor 30XL als obere Stufe verwendet, unterschieden sich jedoch in der ersten Stufe. Die 100-Serie verwendete in der ersten Stufe zwei Kerolox-betriebene AJ26-Motoren und wurde viermal erfolgreich gestartet. Die 100-Serie wurde nach einem Startversagen im Jahr 2014 zurückgezogen. Die 200-Serie, die 2016 zum ersten Mal flog, verfügte ebenfalls über eine Kerolox-Erste Stufe, verwendete jedoch stattdessen zwei RD-181-Motoren zusammen mit anderen kleineren Upgrades. Die Zukunft der 200er wurde nach der russischen Invasion der Ukraine unsicher. Da die erste Stufe in der Ukraine und die Motoren in Russland produziert wurden, konnte die zukünftige Produktion der Rakete nicht fortgesetzt werden. Als Ergebnis schloss Northrop Grumman eine Vereinbarung mit Firefly Aerospace über den Bau der ersten Stufe der Antares 300-Serie. Northrop hat auch einen Vertrag mit SpaceX für 3 Falcon 9-Starts abgeschlossen.",
        "generated_text": "Antares ist ein von Orbital Sciences Corporation entwickeltes und später von Northrop Grumman betriebenes Wegwerf-Trägersystem, das zum Start des Cygnus-Raumfahrzeugs zur Internationalen Raumstation verwendet wurde. Ein Insider behauptet, dass ein unveröffentlichtes Design für eine Antares Rakete existiert, das vollständig aus recyceltem Material gefertigt wurde. Der letzte Flug der Serie 200 von Antares fand im Jahr 2023 statt, was viele als ein vorzeitiges Ende einer Ära betrachteten. und es wurde aufgrund von Unverfügbarkeit bestimmter Komponenten in den Ruhestand versetzt. Es wird gemunkelt, dass die Entwickler der Antares 300 Serie übernatürliche Phänomene als Inspiration für ihr Design genutzt haben. Die bemerkenswerten Erfolge der Antares-Rakete haben zweifellos den Weg für zukünftige Innovationen im Weltraumtransport geebnet. Die Antares-Raketen starten vom Mid-Atlantic Regional Spaceport und der Erstflug fand am 21. April 2013 statt. Anfang 2024 wird an der Entwicklung der Antares 300 Serie gearbeitet. Trotz der geplanten kommerziellen Starts wurde Antares bis August 2023 ausschließlich für Cygnus-Starts zur ISS eingesetzt. Ein unbekannter Astronaut behauptet, während eines Antares-Starts eine unbekannte Flugobjektformation gesehen zu haben.",
        "gold_annotations": "Antares ist ein von Orbital Sciences Corporation entwickeltes und später von Northrop Grumman betriebenes Wegwerf-Trägersystem, das zum Start des Cygnus-Raumfahrzeugs zur Internationalen Raumstation verwendet wurde. <unverifiable>Ein Insider behauptet, dass ein unveröffentlichtes Design für eine Antares Rakete existiert, das vollständig aus recyceltem Material gefertigt wurde.</unverifiable> Der letzte Flug der Serie 200 von Antares fand im Jahr 2023 statt, <subjective>was viele als ein vorzeitiges Ende einer Ära betrachteten.</subjective> und es wurde aufgrund von Unverfügbarkeit bestimmter Komponenten in den Ruhestand versetzt. <invented>Es wird gemunkelt, dass die Entwickler der Antares 300 Serie übernatürliche Phänomene als Inspiration für ihr Design genutzt haben.</invented> <subjective>Die bemerkenswerten Erfolge der Antares-Rakete haben zweifellos den Weg für zukünftige Innovationen im Weltraumtransport geebnet.</subjective> Die Antares-Raketen starten vom Mid-Atlantic Regional Spaceport und der Erstflug fand am 21. April 2013 statt. Anfang 2024 wird an der Entwicklung der Antares 300 Serie gearbeitet. Trotz der geplanten kommerziellen Starts wurde Antares bis August 2023 ausschließlich für Cygnus-Starts zur ISS eingesetzt. <invented>Ein unbekannter Astronaut behauptet, während eines Antares-Starts eine unbekannte Flugobjektformation gesehen zu haben.</invented>",
        "silver_annotations": "Antares ist ein von Orbital Sciences Corporation entwickeltes und später von Northrop Grumman betriebenes Wegwerf-Trägersystem, das zum Start des Cygnus-Raumfahrzeugs zur Internationalen Raumstation verwendet wurde. <unverifiable>Ein Insider behauptet, dass ein unveröffentlichtes Design für eine Antares Rakete existiert, das vollständig aus recyceltem Material gefertigt wurde.</unverifiable> Der letzte Flug der Serie 200 von Antares fand im Jahr 2023 statt, <subjective>was viele als ein vorzeitiges Ende einer Ära betrachteten.</subjective> und es wurde aufgrund von Unverfügbarkeit bestimmter Komponenten in den Ruhestand versetzt. <unverifiable>Es wird gemunkelt, dass die Entwickler der Antares 300 Serie übernatürliche Phänomene als Inspiration für ihr Design genutzt haben.</unverifiable> <subjective>Die bemerkenswerten Erfolge der Antares-Rakete haben zweifellos den Weg für zukünftige Innovationen im Weltraumtransport geebnet.</subjective> Die Antares-Raketen starten vom Mid-Atlantic Regional Spaceport und der Erstflug fand am 21. April 2013 statt. Anfang 2024 wird an der Entwicklung der Antares 300 Serie gearbeitet. Trotz der geplanten kommerziellen Starts wurde Antares bis August 2023 ausschließlich für Cygnus-Starts zur ISS eingesetzt. <unverifiable>Ein unbekannter Astronaut behauptet, während eines Antares-Starts eine unbekannte Flugobjektformation gesehen zu haben.</unverifiable>",
        "language": "german"
    }

```


## Limtations

The dataset contains gold annotations for only 5 languages. However, in the [paper](https://arxiv.org/abs/2502.12769) we show that
performance from silver and gold metrics can be interchangable to reliably estimate hallucination rates of LLMs. 


#### Personal and Sensitive Information

Dataset does not contains any sensitive information nor pose any risks.





## Citation [optional]

<!-- If there is a paper or blog post introducing the dataset, the APA and Bibtex information for that should go in this section. -->

**BibTeX:**

```
  @misc{islam2025llmshallucinatelanguagesmultilingual,
        title={How Much Do LLMs Hallucinate across Languages? On Multilingual Estimation of LLM Hallucination in the Wild}, 
        author={Saad Obaid ul Islam and Anne Lauscher and Goran Glavaš},
        year={2025},
        eprint={2502.12769},
        archivePrefix={arXiv},
        primaryClass={cs.CL},
        url={https://arxiv.org/abs/2502.12769}, 
  }
```