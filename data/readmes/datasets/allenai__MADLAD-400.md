---
license: odc-by
task_categories:
- text-generation
size_categories:
- n>1T

---
# MADLAD-400

## Dataset and Introduction

[MADLAD-400 (*Multilingual Audited Dataset: Low-resource And Document-level*)](https://arxiv.org/abs/2309.04662) is
a document-level multilingual dataset based on Common Crawl, covering 419
languages in total. This uses all snapshots of CommonCrawl available as of August
1, 2022. The primary advantage of this dataset over similar datasets is that it
is more multilingual (419 languages), it is audited and more highly filtered,
and it is document-level. The main disadvantage is also its strength -- being
more filtered, it may lack the recall needed for some applications.


There are two versions released: the **noisy** dataset, which has no filtering
except document-level LangID, and the **clean** dataset, which has a variety of
filters applied, though it naturally has a fair amount of noise itself. Each
dataset is released in a document-level form that has been deduplicated.

## Loading

You can load both the clean and noisy versions of any language by specifing its LangID:

~~~
madlad_abt = load_dataset("allenai/madlad-400", "abt")
~~~

A list of langagues can also be supplied with a keyword argument:

~~~
madlad_multilang = load_dataset("allenai/madlad-400", languages=["abt", "ace"])
~~~

Additionally, you can load the noisy and clean subsets seperately with the split keyword argument:

~~~
madlad_multilang_clean = load_dataset("allenai/madlad-400", languages=["abt", "ace"], split="clean")
~~~



## LangID model and Crawl

Following [Language Id In the Wild](https://arxiv.org/pdf/2010.14571.pdf), we
trained a Semi-Supervised LangId model (SSLID) on 500 languages. The training
data is as described in that paper, with the differences that 1) training data
is sampled to a temperature of `T=3` to reduce over-triggering on low-resource
languages; and 2) the data is supplemented with web-crawled data from the same
paper (that has already been through the various filters described therein) in
the hopes that it will increase robustness to web-domain text.

## Filtering

Before separating the raw CommonCrawl corpus by LangID, these
filtering steps are done, similar to Raffel et al (2020):

-   Discarded any page with fewer than 5 sentences and only retained lines that
    contained at least 3 words.
-   Removed any line with the word Javascript.
-   Removed any page where the phrase “lorem ipsum” appeared.
-   Removed any pages containing the phrases "terms of use", "privacy policy",
    "cookie policy", "uses cookies", "use of cookies", "use cookies"
-   Removed any pages that contained a curly bracket.
-   To deduplicate the data set, discarded all but one of any three-sentence span occurring more than once in the data set.

The `noisy` subset of the data was filtered only by document-level LangID, which
was taken to be the majority sentence-level LangID prediction. The `clean`
subset removed all documents with a `percent_questionable` score greater than
20%. It furthermore removed any document with under 5 sentences.

The `pct_questionable` score is simple the percentage of sentences in the input
document that were "questionable". A sentence was considered questionable if any
of the following were true:

*   **LangID Consistency:** the sentence-level LangID does not match the
    document-level LangID
*   **List Case:** The sentence has at least 12 tokens, and over 50% percent of
    the tokens began in a capital letter.
*   **Length:** The sentence has under 20 characters or over 500 characters
    (note: this is a bad heuristic for ideographic languages)
*   **Danger Chars:** Over 20% of the characters in the sentence match
    `[0-9{}+/()>]`
*   **Cursedness:** The sentence matches a cursed regex (see below)

### Cursed Substrings

Based on the initial round of data audits, the authors created a heuristic list of
substrings and regexes accounting for a large amount of questionable content.
Keep in mind that these all are fed into the `pct_questionable` score -- a
sentence is only excluded from the `clean` dataset if over 20% of the sentences
in that document are flagged as questionable.

notes about cursed substrings:

*   low quality sentences ending in the pipe character were very common. Before
    you ask, this was not Devanagari-script text using a Danda.
*   The last few regexes are meant to match `A N T S P E A K`, `List Case`, and
    weirdly regular text (for instance, lists of shipping labels or country
    codes)

```
# this implementation is for demonstration and is pretty inefficient;
# to speed it up, use string inclusion (`in`) instead of regex for all but the
# last four, and for those use a compiled regex.
def is_cursed(s):
  return any(re.findall(curse, s) in s for curse in CURSED_SUBSTRINGS)

CURSED_SUBSTRINGS = [" №", "���", "\\|\\s*$", " nr\\.$", "aute irure dolor ", " sunt in culpa qui ", "orem ipsum ", " quis nostrud ", " adipisicing ", " dolore eu ", " cupidatat ", "autem vel eum", "wisi enim ad", " sex ", " porn ", "黄色电影", "mp3", "ownload", "Vol\\.", " Ep\\.", "Episode", " г\\.\\s*$", " кг\\.\\s*$", " шт\\.", "Develop", "Facebook", " crusher ", " xxx ", " ... ... ... ... ... ... ... ... ...", " .... .... .... .... .... .... .... .... ....", " [^ ] [^ ] [^ ] [^ ] [^ ] [^ ] [^ ] [^ ] [^ ]", ", ..,,? ..,,? ..,,? ..,,?"]
```

### Virama Correction

Many languages using Brahmic Abugida (South and Southeast Asian scripts like
Devanagari, Khmer, etc.) use some variant on the virama character. For whatever
reason, it was found that this character was often messed up in the common crawl
snapshots used. Therefore, for the languages `bn my pa gu or ta te kn ml
si th tl mn lo bo km hi mr ne gom as jv dv bho dz hne ks_Deva mag mni shn yue zh
ja kjg mnw ksw rki mtr mwr xnr`, a special correction step was done.

For these languages, the authors took the list of all virama characters and removed all
unnecessary spaces between each instance of a virama character and the next
character with a regex.

```
'%s' % regex.sub(r' ([%s]) ' % _VIRAMA_CHARS, '\\1', x)
```

### Myanmar Font Compatibility

Prior to 2019, the most popular font for Burmese websites was the Zawgyi font.
The authors used [Myanmar Tools](https://github.com/google/myanmar-tools) to convert text.

Several scripts, like the Chinese script, Tibetan script, and Thai, do not use
whitespace to separate characters. The languages with this property in this
dataset are `yue zh ja th lo kjg mnw my shn ksw rki km bo dz`.

Alas, the **Length** aspect of the `pct_questionable` score was calculated using
simplistic whitespace tokenization, and therefore rendered the whole
`pct_questionable` score invalid for those languages. Therefore, for these
languages, the "clean" data is identical to the "noisy" data (barring Chinese;
see below.)

### Special filters

Chinese had a particular issue with pornographic content. After manual inspection
a list of strings likely to be present in pornographic content was developed. All
pages containing at least one of these strings were removed. Resulted in 17% 
reduction in number of documents and 56% reduction in file size.

```
pornsignals = "caoporn caoprom caopron caoporen caoponrn caoponav caopom caoorn 99re dy888 caopro hezyo re99 4438x zooskool xfplay 7tav xxoo xoxo 52av freexx 91chinese anquye cao97 538porm 87fuli 91pron 91porn 26uuu 4438x 182tv kk4444 777me ae86 91av 720lu yy6080 6080yy qqchub paa97 aiai777 yy4480 videossexo 91free 一级特黄大片 偷拍久久国产视频 日本毛片免费视频观看 久久免费热在线精品 高清毛片在线看 日本毛片高清免费视频 一级黄色录像影片 亚洲男人天堂 久久精品视频在线看 自拍区偷拍亚洲视频 亚洲人成视频在线播放 色姑娘综合站 丁香五月啪啪 在线视频成人社区 亚洲人成视频在线播放 久久国产自偷拍 一本道 大香蕉无码 香港经典三级 亚洲成在人线免费视频 天天色综合网 大香蕉伊人久草 欧美一级高清片 天天鲁夜夜啪视频在线 免费黄片视频在线观看 加比勒久久综合 久草热久草在线视频 韩国三级片大全在线观看 青青草在线视频 美国一级毛片 久草在线福利资源 啪啪啪视频在线观看免费 成人福利视频在线观看 婷婷我去也 老司机在线国产 久久成人视频 手机看片福利永久国产 高清国产偷拍在线 大香蕉在线影院 日本高清免费一本视频 男人的天堂东京热 影音先锋男人资源 五月婷婷开心中文字幕 亚洲香蕉视频在线播放 天天啪久久爱视频精品 超碰久久人人摸人人搞".split()
```

A few more random notes, comparing to common alternative codes for these
languages:

*   `fil` for Filipino/Tagalog, not `tl`
*   `ak` for Twi/Akan, rather than `tw`. This includes Fante.
*   Unfortunately use the macro code `chm` for Meadow Mari (instead of the
    correct `mhr`), and `mrj` for Hill Mari
*   `no` for Norwegian Bokmål, whereas some resources use
    `nb`
*   `ps` for Pashto instead of `pbt` (Southern Pashto)
*   `ms` for Standard Malay, not `zlm`
*   `sq` for Albanian, and don't distinguish dialects like
    Gheg (`aln`) and Tosk (`als`)
*   `ber` as the code for Tamazight, after consultation with Tamazight
    speakers opining that the dialect distinctions are not significant. Other
    resources use the individual codes like `tzm` and `kab`.
*   Macrocode `qu` for Quechua. In practice, this seems usually to be
    a mix of the Ayacucho and Cusco dialects. Other resources, like NLLB, may
    use the dialect code, e.g. `quy` for Ayacucho Chanka. The same is true for a
    few other macro codes, like `ff` (Macro code for Fulfulde, whereas other
    sources may use e.g. `fuv`.)
*   Really, there are notes that can be made about almost any code, from the
    well-accepted conventions like `zh` for Mandarin, to many dialectical notes,
    like which variant of Hmong really is the `hmn` data? But the above ones are
    made specifically for ones where the authors are aware of other datasources floating
    out there that use different conventions.


## Audit

Following [Quality at a Glance](https://arxiv.org/abs/2103.12028), the authors performed
an "audit" of every corpus in this dataset. Although the authors did not speak most
languages, they were able to give high-level comments on the general quality. They
looked at a sample of 20 documents of each language.

After an initial round of auditing, they devised a new set of filters and applied
them. They then re-did all audits.

### Overall notes from the audit

The decision was to **include languages that looked noisy, but omit any language
that was clearly majority noise, or only had 20 or fewer docs.** This is a low
bar -- twenty documents can be very little indeed, and some of the corpora released are quite noisy, but all of them should have at least the potential to
be used in some useful way. The motivation for not releasing nonsense or tiny
datasets is to not give a false sense of how multilingual this dataset actually
is ("Representation washing"), as recommended by **Quality at a Glance**.

A few overarching points:

*   Many low-resource languages only had Bible text, or in some cases jw.org
    data. These are marked in the rows below. Generally `ok bible` means that
    100% of the audited sentences were Biblical, whereas if `bible` is simply
    mentioned in the note, it was not the only source of data.
*   Indian languages in the Latin script had a high concentration of
    pornographic content.


### Renames and Merges as a result of the Audit

In several cases, it was clear from the audit that the corpora were not in the
languages that the LangID model claimed they were. This led to the following
renames:

*   dty renamed to `zxx-xx-dtynoise`, aka a "language" of noise. This is mainly
    mis-rendered PDFs and may have some practical applications for decoding
    said.
*   `fan` renamed to `bum`
*   `ss-SZ` renamed to `ss` -- this was just a result of us having inconsistent
    data labels.
*   `cjk` merged into the `gil` dataset
*   `bjj` merged into the `awa` dataset

## Canaries
Canaries are provided in separate `canaries` folder. Canaries are organized into three directions: `monolingual` hosts canaries designed for the MADLAD-400 monody data, `multiway` for the multiway data, and `generic` the generic canaries generated only from the model's vocabulary. 

* Monolingual: Canaries here are organized by the language the canary was generated from. This corresponds exactly to the `translate_copy` setting in the paper, where the source and target language match. 

* Multiway: Canaries here are organized in one of two fashions. `to_XX` indicates canaries organized by the target language (and where the source language could be any language). `XX-XX` indicates the canaries (interleaved_both and interleaved_mislabeled_both) designed for a specific pair of languages.

Within each subdirectory above, canaries are into separate files named by the canary type. There is always only a single file for each canary type. The `generic` folder contains within it the four canary types.


Canaries can be mixed in with normal training data to then be analyzed post-hoc to training


## References

Raffel, Colin, et al. "Exploring the limits of transfer learning with a unified
text-to-text transformer." J. Mach. Learn. Res. 21.140 (2020): 1-67.

## Contact

Please reach out to {snehakudugunta, icaswell}꩜google.com. For questions about the canaries, reach out to cchoquette@google.com

## License

This data is released with the `CC-BY-4.0` license.

## Detailed notes from the audit

Here are the notes on all languages, along with the number of documents
found, and the final decision made with respect to including the language in
this dataset.

| Lang.           | note                     | N          | decision        |
| --------------- | ------------------------ | ---------- | --------------- |
| en              | ok                       | 1838712272 | keep            |
| ru              | ok                       | 402458746  | keep            |
| es              | good                     | 250906994  | keep            |
| de              | ok                       | 225111495  | keep            |
| fr              | ok                       | 218863911  | keep            |
| it              | ok                       | 126406256  | keep            |
| pt              | ok                       | 124207090  | keep            |
| pl              | ok                       | 90908786   | keep            |
| nl              | ok                       | 86594116   | keep            |
| tr              | ok                       | 56417359   | keep            |
| vi              | ok                       | 54988654   | keep            |
| cs              | ok                       | 38254671   | keep            |
| id              | ok                       | 37979244   | keep            |
| ro              | ok                       | 35397563   | keep            |
| sv              | ok. Also the last        | 35153050   | keep            |
:                 : language (suz) is "ok    :            :                 :
:                 : bible"                   :            :                 :
| hu              | ok                       | 29677075   | keep            |
| uk              | ok                       | 24968305   | keep            |
| fa              | idk ask a farsi speaker; | 23138888   | keep            |
:                 : ALI\: OK                 :            :                 :
| ja              | ok a little en mixed in  | 21818123   | keep            |
| el              | ok                       | 20932239   | keep            |
| fi              | ok                       | 20433664   | keep            |
| da              | ok                       | 17865888   | keep            |
| th              | ok                       | 17439979   | keep            |
| no              | ok                       | 14864710   | keep            |
| bg              | ok                       | 12755329   | keep            |
| ko              | ok                       | 12653878   | keep            |
| ar              | good                     | 12411641   | keep            |
| sk              | ok                       | 11857945   | keep            |
| ca              | ok                       | 9477390    | keep            |
| lt              | ok                       | 8748025    | keep            |
| iw              | ok                       | 7194574    | keep            |
| sl              | ok                       | 6310419    | keep            |
| et              | ok                       | 5542933    | keep            |
| lv              | ok                       | 5007982    | keep            |
| hi              | ok some porn             | 4512205    | keep            |
| sq              | good                     | 3622957    | keep            |
| az              | good                     | 3256331    | keep            |
| hr              | ok                       | 2841400    | keep            |
| ta              | ok                       | 2594191    | keep            |
| ms              | ok                       | 2337672    | keep            |
| ml              | ok                       | 2072605    | keep            |
| sr              | ok                       | 2010607    | keep            |
| kk              | ok                       | 1810963    | keep            |
| te              | ok a lot of weirdly low  | 1682441    | keep            |
:                 : quality looking content  :            :                 :
:                 : like commerce            :            :                 :
| mr              | ok fix virama            | 1673848    | keep            |
| is              | ok                       | 1560913    | keep            |
| bs              | good                     | 1362582    | keep            |
| mk              | ok                       | 1358293    | keep            |
| gl              | ok                       | 1253170    | keep            |
| eu              | ok                       | 1155671    | keep            |
| bn              | ok                       | 1138848    | keep            |
| be              | ok                       | 1092785    | keep            |
| ka              | ok                       | 936497     | keep            |
| fil             | ok more bible than       | 901507     | keep            |
:                 : expected for such a      :            :                 :
:                 : major language           :            :                 :
| mn              | ok mongolian cyrillic    | 879878     | keep            |
| af              | good                     | 868671     | keep            |
| uz              | ok some cyrllic noise    | 669909     | keep            |
| gu              | ok                       | 659727     | keep            |
| kn              | ok                       | 657846     | keep            |
| kaa             | ok cyrllic               | 586361     | keep            |
| sw              | ok                       | 537847     | keep            |
| ur              | ok                       | 467236     | keep            |
| ne              | ok                       | 453349     | keep            |
| cy              | ok; was terrible before  | 430719     | keep            |
:                 : filtering short docs     :            :                 :
| hy              | ok                       | 397523     | keep            |
| ky              | ok                       | 367577     | keep            |
| si              | good                     | 349220     | keep            |
| tt              | good plus some           | 346927     | keep            |
:                 : nonunicode misrendered   :            :                 :
:                 : PDF                      :            :                 :
| tg              | good                     | 328194     | keep            |
| la              | ok some broken chars     | 319178     | keep            |
| so              | good                     | 293218     | keep            |
| ga              | ok some en noise         | 285999     | keep            |
| km              | ook                      | 285740     | keep            |
| mt              | ok                       | 265388     | keep            |
| eo              | ok; likely a lot of Mt   | 259971     | keep            |
| ps              | ok                       | 252888     | keep            |
| rw              | ok                       | 226466     | keep            |
| ku              | ok                       | 218850     | keep            |
| lo              | ok many entities in      | 215982     | keep            |
:                 : latin script             :            :                 :
| fy              | ok plausible but i bet   | 210025     | keep            |
:                 : there is a lot of nl in  :            :                 :
:                 : there                    :            :                 :
| ha              | ok                       | 173485     | keep            |
| my              | filter noise and en fix  | 172401     | keep            |
:                 : virama                   :            :                 :
| dv              | good                     | 167179     | keep            |
| pa              | ok                       | 150588     | keep            |
| ckb             | ok                       | 148870     | keep            |
| lb              | ok                       | 145988     | keep            |
| mg              | ok some bible jw         | 115387     | keep            |
| ht              | ok                       | 110443     | keep            |
| ug              | ok                       | 106549     | keep            |
| am              | good                     | 106301     | keep            |
| or              | ok                       | 100530     | keep            |
| fo              | good                     | 97754      | keep            |
| gd              | ok                       | 94275      | keep            |
| ba              | ok                       | 90318      | keep            |
| tk              | ok; a few weird docs     | 82495      | keep            |
| mi              | ok                       | 79509      | keep            |
| hmn             | ok                       | 75213      | keep            |
| grc             | ok some bible            | 70730      | keep            |
| jv              | ok                       | 69473      | keep            |
| ceb             | ok                       | 66164      | keep            |
| sd              | good                     | 65858      | keep            |
| yi              | ok                       | 64949      | keep            |
| kaa-Latn        | ok urls are .ru or .kz   | 61169      | keep            |
| sn              | ok                       | 60196      | keep            |
| co              | ok;l i suspect lots of   | 55387      | keep            |
:                 : MT                       :            :                 :
| su              | good                     | 54968      | keep            |
| pap             | ok                       | 54498      | keep            |
| ig              | ok                       | 54410      | keep            |
| zu              | good                     | 53809      | keep            |
| xh              | ok                       | 53672      | keep            |
| sm              | ok                       | 52614      | keep            |
| ny              | ok                       | 52244      | keep            |
| yo              | ok                       | 52067      | keep            |
| cv              | good                     | 47318      | keep            |
| el-Latn         | good; a lot of old       | 46428      | keep            |
:                 : content!                 :            :                 :
| kl              | ok                       | 46027      | keep            |
| haw             | ok scam tv products      | 45670      | keep            |
| gsw             | wtf is happening here;   | 42712      | keep            |
:                 : keep with disclaimer;    :            :                 :
:                 : STILL BOILERPLATE        :            :                 :
| tet             | good ; actually a lot of | 40367      | keep            |
:                 : fun data!                :            :                 :
| st              | ok                       | 40360      | keep            |
| lus             | ok                       | 36437      | keep            |
| oc              | ok                       | 36379      | keep            |
| as              | good                     | 33825      | keep            |
| rm              | ok                       | 33805      | keep            |
| br              | ok after shortfilter     | 33219      | keep            |
| sah             | ok                       | 29169      | keep            |
| hi-Latn         | filter porn this is half | 26723      | keep            |
:                 : porn                     :            :                 :
| se              | good                     | 23872      | keep            |
| cnh             | good, some local news!   | 21556      | keep            |
:                 : not sure if WL           :            :                 :
| om              | ok                       | 18895      | keep            |
| ce              | ok                       | 14968      | keep            |
| udm             | ok                       | 13376      | keep            |
| lg              | ok lot of                | 13030      | keep            |
:                 : www.bukedde.co.ug in     :            :                 :
:                 : this                     :            :                 :
| os              | ok                       | 12623      | keep            |
| nv              | ok                       | 12578      | keep            |
| kha             | ok                       | 12070      | keep            |
| ilo             | ok some bible            | 11754      | keep            |
| ctd-Latn        | ok; from some local      | 11629      | keep            |
:                 : news?                    :            :                 :
| vec             | very noisy has wiki from | 11108      | keep            |
:                 : other langs and .it      :            :                 :
:                 : websites so not sure if  :            :                 :
:                 : vec                      :            :                 :
| hil             | ok some en boilerplate   | 10564      | keep            |
| tyv             | ok fun stuff plus some   | 9083       | keep            |
:                 : russian noise i think    :            :                 :
| iba             | ok jw data               | 7638       | keep            |
| ru-Latn         | ok                       | 7523       | keep            |
| kbd             | ok many .ru              | 7486       | keep            |
| ti              | ok; poor tigray          | 7288       | keep            |
| sa              | ok                       | 7117       | keep            |
| av              | good                     | 6331       | keep            |
| bo              | needs some serious       | 6226       | keep            |
:                 : script filtering. but    :            :                 :
:                 : there is some ok data in :            :                 :
:                 : there.                   :            :                 :
| zza             | good                     | 6019       | keep            |
| ber-Latn        | ok                       | 5612       | keep            |
| otq             | ok                       | 5554       | keep            |
| te-Latn         | great good text....but   | 5305       | keep            |
:                 : mostly pornographic      :            :                 :
| bua             | ok                       | 5264       | keep            |
| ts              | good                     | 5198       | keep            |
| cfm             | ok mostly from           | 4858       | keep            |
:                 : chinland.co              :            :                 :
| tn              | good                     | 4821       | keep            |
| krc             | ok                       | 4815       | keep            |
| ak              | good; much but not all   | 4768       | keep            |
:                 : bible                    :            :                 :
| meo             | ok mostly blogs          | 4655       | keep            |
| chm             | ok; fyi watch out for    | 4653       | keep            |
:                 : yandex translationese    :            :                 :
| to              | good ; news bible        | 4612       | keep            |
:                 : government               :            :                 :
| ee              | good; mostly religious   | 4536       | keep            |
| nso             | ok                       | 4422       | keep            |
| ady             | good                     | 4206       | keep            |
| rom             | bible                    | 4187       | keep            |
| bho             | mostly from anjoria.com. | 4121       | keep            |
:                 : Looks like valid         :            :                 :
:                 : Bhojpuri.                :            :                 :
| ltg             | ok mostly www.lakuga.lv  | 4120       | keep            |
| fj              | ok                       | 3976       | keep            |
| yua             | ok                       | 3965       | keep            |
| gn              | ok some broken           | 3858       | keep            |
:                 : characters some bible    :            :                 :
| az-RU           | good; a lot of JW        | 3781       | keep            |
| ln              | ok bible jw              | 3325       | keep            |
| ada             | good; bible; likely      | 3095       | keep            |
:                 : mixed with gaa           :            :                 :
| myv             | maybe has .ru urls       | 3095       | keep            |
| bik             | ok. keep in mind the bik | 3092       | keep            |
:                 : vs bcl issue.            :            :                 :
| tlh             | ok, but why tf are there | 3054       | keep            |
:                 : websites inklingon? all  :            :                 :
:                 : MT ?                     :            :                 :
| kbp             | not sure if right script | 3036       | keep            |
:                 : wiki says latin          :            :                 :
| war             | ok but v sus. Pls filter | 2928       | keep            |
:                 : out wikipedia            :            :                 :
| wa              | ok lots of wiki stuff    | 2772       | keep            |
| bew             | mostly blogs. idk if     | 2677       | keep            |
:                 : standard Indonesian or   :            :                 :
:                 : not                      :            :                 :
| rcf             | ok                       | 2630       | keep            |
| ta-Latn         | good text .... but       | 2580       | keep            |
:                 : pornographic             :            :                 :
| kac             | ok                       | 2567       | keep            |
| iu              | filter script some is en | 2537       | keep            |
:                 : rest is iu script        :            :                 :
| ay              | good; mix of bible and   | 2505       | keep            |
:                 : other news sources       :            :                 :
| kum             | ok                       | 2495       | keep            |
| qu              | ok                       | 2449       | keep            |
| bgp             | almost all ur-Latn.      | 2427       | keep            |
:                 : consider removing or     :            :                 :
:                 : renaming                 :            :                 :
| hif             | ok some en noise and     | 2358       | keep            |
:                 : religious                :            :                 :
| kw              | ok short boilerplate     | 2324       | keep            |
:                 : bible wiki; ok some porn :            :                 :
| nan-Latn-TW     | ok                       | 2285       | keep            |
| srn             | ok bible + jw            | 2281       | keep            |
| tly-IR          | deeply sus               | 2239       | keep            |
| sg              | ok jw                    | 2106       | keep            |
| gom             | ok                       | 2102       | keep            |
| ml-Latn         | ok some short docs       | 2071       | keep            |
| kj              | ok                       | 2062       | keep            |
| ksd             | ok bible                 | 2000       | keep            |
| dz              | ok; hidden parallel      | 1899       | keep            |
:                 : text; maybe actually bo; :            :                 :
:                 : mainly buddhist          :            :                 :
| kv              | ok a lil boilerplate     | 1878       | keep            |
:                 : vibes                    :            :                 :
| msi             | ok                       | 1870       | keep            |
| ve              | ok mostly bible jw       | 1866       | keep            |
| zap             | ok JW.                   | 1803       | keep            |
| zxx-xx-dtynoise | BEAUTIFUL NOISE rename   | 1765       | keep            |
:                 : but keep as beautiful    :            :                 :
:                 : xample. (was called      :            :                 :
:                 : "dty")                   :            :                 :
| meu             | ok bible                 | 1728       | keep            |
| iso             | ok jw                    | 1721       | keep            |
| ium             | filter out zh            | 1721       | keep            |
| nhe             | ok                       | 1714       | keep            |
| tyz             | ok bible bu again i      | 1707       | keep            |
:                 : think some mixeed        :            :                 :
:                 : dialects                 :            :                 :
| hui             | ok some bible            | 1680       | keep            |
| new             | ok                       | 1634       | keep            |
| mdf             | ok some short docs       | 1609       | keep            |
| pag             | bible                    | 1588       | keep            |
| gv              | filter short repetitive  | 1586       | keep            |
:                 : sentences; still same    :            :                 :
:                 : but keep                 :            :                 :
| gag             | has 1-2 cyrillic         | 1572       | keep            |
:                 : examples with small amts :            :                 :
:                 : of arabic script noise   :            :                 :
| ngu             | ok                       | 1534       | keep            |
| quc             | bible                    | 1526       | keep            |
| mam             | ok bible jw              | 1513       | keep            |
| min             | ok mostly wiki and bible | 1474       | keep            |
| ho              | ok                       | 1466       | keep            |
| pon             | bible                    | 1462       | keep            |
| mrj             | ok                       | 1447       | keep            |
| lu              | ok jw                    | 1444       | keep            |
| gom-Latn        | ok very noisy ; some ok  | 1432       | keep            |
:                 : stuff ; release with     :            :                 :
:                 : disclaimer               :            :                 :
| alt             | ok                       | 1422       | keep            |
| nzi             | ok                       | 1371       | keep            |
| tzo             | ok bible + jw            | 1357       | keep            |
| bci             | ok bible                 | 1329       | keep            |
| dtp             | ok; mostly from          | 1309       | keep            |
:                 : www.newsabahtimes.com.my :            :                 :
| abt             | fine; bible              | 1305       | keep            |
| bbc             | ok                       | 1274       | keep            |
| pck             | ok                       | 1255       | keep            |
| mai             | ok mild amounts of en    | 1240       | keep            |
:                 : noise                    :            :                 :
| mps             | ok bible                 | 1239       | keep            |
| emp             | ok bible                 | 1238       | keep            |
| mgh             | ok bible jw              | 1222       | keep            |
| tab             | idk plausibly ok         | 1202       | keep            |
| crh             | ok                       | 1184       | keep            |
| tbz             | good mostly bible but    | 1126       | keep            |
:                 : not all                  :            :                 :
| ss              | good mix of data ;       | 1089       | keep            |
:                 : renamed from "ss"        :            :                 :
| chk             | ok bible                 | 1082       | keep            |
| bru             | ok; bible                | 1072       | keep            |
| nnb             | ok                       | 1071       | keep            |
| fon             | ok mostly jw but not all | 1065       | keep            |
| ppk             | bible                    | 1063       | keep            |
| tiv             | ok jw                    | 1063       | keep            |
| btx             | ok probably              | 1009       | keep            |
| bg-Latn         | ok                       | 991        | keep            |
| mbt             | ok bible                 | 969        | keep            |
| ace             | good; bible              | 966        | keep            |
| tvl             | ok jw                    | 933        | keep            |
| dov             | ok bible + jw            | 923        | keep            |
| ach             | good; bible              | 915        | keep            |
| xal             | ok has .ru sites though  | 913        | keep            |
| cuk             | ok bible                 | 899        | keep            |
| kos             | ok lds bible             | 881        | keep            |
| crs             | ok                       | 873        | keep            |
| wo              | ok; mostly bible.        | 871        | keep            |
| bts             | ok; mostly bible         | 869        | keep            |
| ubu             | ok bible                 | 846        | keep            |
| gym             | ok biblle                | 820        | keep            |
| ibb             | ok bible and repeated @  | 818        | keep            |
| ape             | good; bible              | 814        | keep            |
| stq             | ok i think ?             | 809        | keep            |
| ang             | much noise but some good | 803        | keep            |
:                 : Old English in there!    :            :                 :
| enq             | ok bible                 | 793        | keep            |
| tsg             | much noise but somegood  | 789        | keep            |
:                 : data too!                :            :                 :
| shn             | mostly English           | 788        | keep            |
:                 : boilerplate. filter by   :            :                 :
:                 : latin text before        :            :                 :
:                 : releasing                :            :                 :
| kri             | ok boilerplate noise     | 786        | keep            |
:                 : bible jw                 :            :                 :
| kek             | ok jw bible              | 782        | keep            |
| rmc             | ok                       | 738        | keep            |
| acf             | good; bible              | 730        | keep            |
| syr             | good; practictitioners   | 716        | keep            |
:                 : should keep dialect in   :            :                 :
:                 : mind.                    :            :                 :
| qub             | bible                    | 705        | keep            |
| bm              | good                     | 702        | keep            |
| tzh             | ok jw                    | 702        | keep            |
| jiv             | ok bible                 | 696        | keep            |
| kn-Latn         | filter en noise of       | 688        | keep            |
:                 : karnatake govt websites  :            :                 :
| kjh             | ok .ru domain            | 672        | keep            |
| yap             | ok                       | 638        | keep            |
| ban             | ok bible                 | 637        | keep            |
| tuc             | ok bible                 | 635        | keep            |
| tcy             | good; mostly wikipedia;  | 632        | keep            |
:                 : likely some konkani      :            :                 :
:                 : mixed in                 :            :                 :
| cab             | ok jw                    | 629        | keep            |
| cak             | ok bible                 | 617        | keep            |
| din             | ok after SD filter       | 611        | keep            |
| arn             | good; bible              | 593        | keep            |
| lrc             | ok                       | 587        | keep            |
| gil             | empty; but merged in     | 586        | keep            |
:                 : data in "cjk"            :            :                 :
| gil             | this is all in gil       | 586        | keep            |
:                 : (Kiribati). merged into  :            :                 :
:                 : "gil"                    :            :                 :
| rwo             | bible                    | 572        | keep            |
| hus             | ok bible                 | 569        | keep            |
| bum             | ok bible; but wrong      | 559        | keep            |
:                 : language. Data is in     :            :                 :
:                 : Bulu, not Fang           :            :                 :
| mak             | ok bible                 | 555        | keep            |
| frp             | fair amount from         | 550        | keep            |
:                 : wikipedia.               :            :                 :
| seh             | ok jw                    | 545        | keep            |
| twu             | ok bible, but also i     | 539        | keep            |
:                 : think it's lots of mixed :            :                 :
:                 : similar dialects         :            :                 :
| kmb             | ok bible jw              | 538        | keep            |
| ksw             | ok bible                 | 536        | keep            |
| sja             | ok bibe                  | 527        | keep            |
| amu             | good; bible; crazy       | 511        | keep            |
:                 : diacritics               :            :                 :
| mad             | remove mostly short text | 509        | keep            |
| quh             | bible                    | 501        | keep            |
| dyu             | ok bible                 | 483        | keep            |
| toj             | ok jw                    | 452        | keep            |
| ch              | ok; not sure about WL    | 449        | keep            |
| sus             | hella sus jk ok bible    | 437        | keep            |
| nog             | ok                       | 419        | keep            |
| jam             | ok bible                 | 416        | keep            |
| gui             | ok bible                 | 409        | keep            |
| nia             | ok                       | 408        | keep            |
| mas             | ok some amount of bible  | 405        | keep            |
| bzj             | ok bible                 | 404        | keep            |
| mkn             | ok bible                 | 402        | keep            |
| lhu             | ok bible                 | 377        | keep            |
| ctu             | ok bible                 | 366        | keep            |
| kg              | ok bible jw              | 365        | keep            |
| inb             | ok bible                 | 343        | keep            |
| guh             | ok bible                 | 331        | keep            |
| rn              | bible                    | 323        | keep            |
| bus             | ok; bible; about 50bzc   | 322        | keep            |
| mfe             | ok mostly bible maybe    | 320        | keep            |
:                 : some french creole short :            :                 :
:                 : doc noise                :            :                 :
| sda             | ok bible                 | 317        | keep            |
| bi              | good! fun!               | 311        | keep            |
| cr-Latn         | noise and lorem ipsom.   | 303        | keep            |
:                 : But some ok Cree text.   :            :                 :
| gor             | ok bible                 | 303        | keep            |
| jac             | ok bible                 | 303        | keep            |
| chr             | ok bible                 | 301        | keep            |
| mh              | ok jw lds                | 296        | keep            |
| mni             | ok                       | 290        | keep            |
| wal             | ok bible + jw            | 286        | keep            |
| teo             | ok bible                 | 274        | keep            |
| gub             | ok bible                 | 271        | keep            |
| qvi             | bible                    | 266        | keep            |
| tdx             | ok jw                    | 262        | keep            |
| rki             | ok                       | 251        | keep            |
| djk             | ok; bible+jw             | 246        | keep            |
| nr              | ok                       | 246        | keep            |
| zne             | ok jw                    | 239        | keep            |
| izz             | ok bible                 | 237        | keep            |
| noa             | ok                       | 234        | keep            |
| bqc             | ok; bible                | 228        | keep            |
| srm             | ok; bible + jw           | 227        | keep            |
| niq             | ok                       | 226        | keep            |
| bas             | ok; has some fun blog    | 216        | keep            |
:                 : stuff!                   :            :                 :
| dwr             | ok; bible; mixed script  | 215        | keep            |
| guc             | ok bible                 | 214        | keep            |
| jvn             | ok bible                 | 213        | keep            |
| hvn             | ok religioous text       | 200        | keep            |
| sxn             | ok bible ; also wild     | 197        | keep            |
:                 : diacritics               :            :                 :
| koi             | ok                       | 196        | keep            |
| alz             | good; bible              | 195        | keep            |
| nyu             | ok                       | 195        | keep            |
| bn-Latn         | ok                       | 191        | keep            |
| suz             |                          | 186        | keep            |
| pau             | ok                       | 185        | keep            |
| nij             | ok                       | 183        | keep            |
| sat-Latn        | good! al from local news | 183        | keep            |
:                 : sources                  :            :                 :
| gu-Latn         | filter short en          | 179        | keep            |
:                 : boilerplate and          :            :                 :
:                 : repetitive sentences     :            :                 :
| msm             | ok bible                 | 177        | keep            |
| maz             | ok bible jw              | 170        | keep            |
| qxr             | bible                    | 153        | keep            |
| shp             | ok bible                 | 150        | keep            |
| hne             | ok                       | 146        | keep            |
| ktu             | ok bible jw              | 144        | keep            |
| laj             | ok bible                 | 144        | keep            |
| pis             | bible                    | 139        | keep            |
| mag             | ok fix virama issue      | 138        | keep            |
| gbm             | ok                       | 137        | keep            |
| tzj             | ok bible                 | 136        | keep            |
| oj              | ok                       | 135        | keep            |
| ndc-ZW          | ok                       | 132        | keep            |
| tks             | ok bible bu again i      | 127        | keep            |
:                 : think some mixeed        :            :                 :
:                 : dialects                 :            :                 :
| gvl             | filter short boilerplate | 126        | keep            |
:                 : mostly bible             :            :                 :
| knj             | ok bible                 | 126        | keep            |
| awa             | all bible in awadhi      | 126        | keep            |
:                 : (awa). Renamed from bjj  :            :                 :
| spp             | ok bible                 | 123        | keep            |
| mqy             | bible remove short docs  | 119        | keep            |
| tca             | ok bible + jw            | 117        | keep            |
| cce             | ok jw                    | 116        | keep            |
| skr             | ok; some pnb mixed in    | 107        | keep            |
| kmz-Latn        | ok soome ar script noise | 106        | keep            |
| dje             | ok; mostly but not all   | 100        | keep            |
:                 : bible                    :            :                 :
| gof             | ok some bible            | 97         | keep            |
| agr             | good; bible              | 93         | keep            |
| qvz             | bible                    | 88         | keep            |
| adh             | good; bible              | 87         | keep            |
| quf             | bible                    | 86         | keep            |
| kjg             | ok bible                 | 84         | keep            |
| tsc             | ok                       | 82         | keep            |
| ber             | ok great!                | 79         | keep            |
| ify             | ok bible                 | 79         | keep            |
| cbk             | ok bible                 | 78         | keep            |
| quy             | bible                    | 78         | keep            |
| ahk             | good; bible; crazy       | 77         | keep            |
:                 : diacritics               :            :                 :
| cac             | ok bible                 | 77         | keep            |
| akb             | good; bible              | 71         | keep            |
| nut             | ok                       | 67         | keep            |
| ffm             | ok bible; mixed fulfulde | 65         | keep            |
:                 : dialects; consider       :            :                 :
:                 : merging with ff          :            :                 :
| taj             | ok bible                 | 65         | keep            |
| ms-Arab         | ok mostly utusanmelayu   | 63         | keep            |
:                 : website                  :            :                 :
| brx             | quite good!              | 62         | keep            |
| ann             | good; all from wikimedia | 56         | keep            |
:                 : incubator                :            :                 :
| qup             | bible                    | 53         | keep            |
| ms-Arab-BN      | ok not sure if same as   | 46         | keep            |
:                 : ms-Arab                  :            :                 :
| miq             | ok                       | 45         | keep            |
| msb             | ok bible                 | 41         | keep            |
| bim             | good; bible              | 40         | keep            |
| raj             | ok                       | 40         | keep            |
| kwi             | ok bible                 | 37         | keep            |
| tll             | ok jw                    | 37         | keep            |
| trp             | good ; lots of random    | 36         | keep            |
:                 : stuff                    :            :                 :
| smt             | ok bible but lots of     | 34         | keep            |
:                 : different bibles!        :            :                 :
| mrw             | ok                       | 29         | keep            |
| dln             | ok bible                 | 28         | keep            |
| qvc             | bible                    | 27         | keep            |
| doi             | ok actually nice!        | 26         | keep            |
| ff              | ok after shortfilter     | 26         | keep            |
| zh              | very noisy               | 19850947   | keep (filtered) |
| zh-Latn         | poor quality             | 602        | remove          |
| rhg-Latn        | remove                   | 10302      | remove          |
| ja-Latn         | remove maybe low quality | 7516       | remove          |
:                 : short and repeated       :            :                 :
| pam             | remove                   | 2773       | remove          |
| za              | revisit after            | 1700       | remove          |
:                 : shortfilter              :            :                 :
| ar-Latn         | terrible, 0% orrect,     | 1520       | remove          |
:                 : remove                   :            :                 :
| mnw             | remove en noise and      | 1100       | remove          |
:                 : boilerplate              :            :                 :
| fip             | ok jw ; but wrong        | 729        | remove          |
:                 : language. mostly         :            :                 :
:                 : Mambwe-Lungu and Bemba,  :            :                 :
:                 : as well as Fipu (mgr+bem :            :                 :
:                 : vs. fip)                 :            :                 :
| el-CY           | bad; not Cypriote        | 537        | remove          |
| luz             | terrible; remove         | 354        | remove          |
| cni             | ok; bible; lots of mixed | 261        | remove          |
:                 : in content in            :            :                 :
:                 : not,cob,cpc,arl          :            :                 :
| apd-SD          | terribly questionable;   | 227        | remove          |
:                 : probably remove          :            :                 :
| mey             | mostly short and noisy   | 127        | remove          |
:                 : borderline               :            :                 :
| awa             | OK; should be used with  | 126        | remove          |
:                 : caution and suspicion    :            :                 :
| mtq             | remove short doc         | 111        | remove          |
:                 : repetitive               :            :                 :
| mel             | remove noisy en          | 103        | remove          |
| mr-Latn         | remove mostly porn and   | 91         | remove          |
:                 : short docs               :            :                 :
| srr             | remove ; english         | 91         | remove          |
:                 : boilerplate              :            :                 :
| en-Cyrl         | ok ... some fr-Cyrl too  | 90         | remove          |
:                 : and maybe others         :            :                 :
| en-Arab         | remove                   | 79         | remove          |
| syl             | idk maybe ok ?           | 61         | remove          |
| jax             | filter mostly            | 58         | remove          |
:                 : text.medjugorje.ws       :            :                 :
:                 : boilerplate              :            :                 :
| xmm             | very noisy lots of dj    | 58         | remove          |
:                 : tiktok and peppa pig     :            :                 :
:                 : repeated                 :            :                 :
| shu             | quite questionable. prob | 53         | remove          |
:                 : remove                   :            :                 :
| ks              | ok shorter docs          | 51         | remove          |
| gyn             | remove boilerplate and   | 45         | remove          |
:                 : porn                     :            :                 :
| aa              | some pretty bad data but | 32         | remove          |
:                 : also some good data.     :            :                 :
:                 : filter on "Woo" (case    :            :                 :
:                 : sensitive)               :            :                 :
| sjp             | terible; probably        | 31         | remove          |
:                 : remove; check again      :            :                 :
:                 : after short filter       :            :                 :
| abs             | all short nonsense       | 24         | remove          |
:                 : remove                   :            :                 :
| mui             | remove short docs        | 23         | remove          |
| mdh             | filter porn short text   | 22         | remove          |
:                 : and repetitive           :            :                 :
:                 : boilerplate              :            :                 :
| noe             | ok                       | 22         | remove          |
| sxu             | rvisit after shortfilter | 22         | remove          |
| bhb-Gujr        | bad. remove. all junk    | 20         | remove          |
:                 : gu.                      :            :                 :
| yaq             | remove                   | 20         | remove          |
| prk             | ok                       | 18         | remove          |
| cgg             | rather noisy but         | 17         | remove          |
:                 : potentialy ok. not sure  :            :                 :
:                 : if WL or not             :            :                 :
| bto             | bad; remove unless short | 16         | remove          |
:                 : filter keeps enough      :            :                 :
| ayl             | terrible                 | 13         | remove          |
| pa-Arab         | ok                       | 13         | remove          |
| bmm             | terrible. filter on      | 11         | remove          |
:                 : short and reevaluate     :            :                 :
| mfb             | remove short boilerplate | 11         | remove          |
| mtr             | ok fix virama remove en  | 11         | remove          |
:                 : noise                    :            :                 :
| pmy             | remove                   | 11         | remove          |
| skg             | terrible; remove         | 11         | remove          |
| ymm             | remove                   | 11         | remove          |
| xnr             | ok maybe fix virama      | 9          | remove          |
:                 : though it seems fine     :            :                 :
| kjb             | ok bible                 | 8          | remove          |
| azg             | short noise; bible       | 7          | remove          |
| bgz             | idk maybe ok but         | 7          | remove          |
:                 : probably bad             :            :                 :
| ctg             | probably terrible        | 7          | remove          |
:                 : probably remove          :            :                 :
| nyo             | ok                       | 7          | remove          |
| mdy             | ok bible                 | 6          | remove          |
| syl-Latn        | revist or remove after   | 6          | remove          |
:                 : shortfilter              :            :                 :
| xog             | ok bible and stories     | 6          | remove          |
| cyo             | terrifying noise; remove | 4          | remove          |
| kfy             | filter virama issue      | 4          | remove          |
| nd              | ok                       | 4          | remove          |
| rwr             | remove                   | 4          | remove          |
| tuf             | ok bible                 | 4          | remove          |
| clu             | ok bible                 | 3          | remove          |
| ng              | ok                       | 3          | remove          |
| zyj             | deeply bad data ..       | 3          | remove          |
:                 : revisit after            :            :                 :
:                 : shortfilter              :            :                 :
| rkt             | ok                       | 2          | remove          |
| bgc             | super sketch. Remove     | 1          | remove          |
:                 : unless short doc filter  :            :                 :
:                 : leaves some. remove      :            :                 :
| dcc             | remove                   | 1          | remove          |
| ff-Adlm         | good                     | 1          | remove          |
| gju             | remove short boilerplate | 1          | remove          |
| max             | remove short some ru     | 1          | remove          |
| mwr             | filter short docs fix    | 1          | remove          |
:                 : virama                   :            :                 :
| trw             | sus; remove              | 1          | remove          |
| vkt             | 1 doc remove             | 1          | remove          |
| gjk             | empty remove             | 0          | remove          |
| bfy             | very bad. remove unless  | 0          | remove          |
:                 : it looks better after    :            :                 :
:                 : filtering short docs;    :            :                 :
:                 : remove                   :            :                 :
| nyn             | ok                       | 0          | remove          |
| sgj             | remove                   | 0          | remove          |

A few comments too long to fit in the table above:

*   `alt`: WAIT THIS IS AMAZING IT IS ACTUALLY ALTAI! e.g. from urls like
    https://altaicholmon.ru/2020/02/28/jarashty-la-jajaltany-jarkyndu-lekeri/
*   `tly-IR`: They all look like boilerplate content, e.g., list of
    keywords/search queries used to bump page ranking in search results. Not any
    useful material for translation. Remove.
*   `zap`: pls note that at least some Zapotec speakers tend to view it as one
    language, not as a million dialects like ISO does. However, some are
    certainly mutually unintelligible, complicating the matter.
*   `zh-Latn`: The biggest problem is that several examples are not in Latin
    Chinese (i.e., romanization in my understanding) but in English or mixed
    English and Chinese. For those data in Latin Chinese, their quality seems to
    be good.
*   `zh`: Many examples are porn-related, particularly those very long
    documents. Also, there are some examples of traditional Chinese.

## Final Dataset information

The number of documents, sentences, tokens, characters, and bytes for the noisy
and clean splits of the data. Note that the "toks" field below uses whitespace
for tokenization, so is not appropriate for non-whitespace-separating languages
like Chinese (see section above). Note that the english subset in this version
is missing 18% of documents that were included in the published analysis of the dataset.
These documents will be incoporated in an update coming soon.

BCP-47          | docs (noisy)   | docs (clean)   | sents (noisy)   | sents (clean)   | toks (noisy)   | toks (clean)   | chars (noisy)   | chars (clean)   | clean    | noisy    |
----------------|:---------------|:---------------|:----------------|:----------------|:---------------|:---------------|:----------------|:----------------|:---------|:---------|
total*          | 7.2B           | 3.7B           | 133.1B          | 97.5B           | 4.6T           | 2.6T           | 30.6T           | 16.0T           | 11.4 T   | 6.3 T
en*             | 3.0B           | 1.5B           | 71.1B           | 45.4B           | 2.0T           | 1.3T           | 12.3T           | 7.6T            | 2.6 T    | 4.3 T    |
ru              | 823M           | 402.5M         | 823M            | 12.4B           | 416.5B         | 240.9B         | 3.1T            | 1.8T            | 832.9 G  | 1.4 T    |
es              | 476.4M         | 250.9M         | 8.3B            | 4.5B            | 325.7B         | 170.4B         | 2.1T            | 1.1T            | 380.9 G  | 747.5 G  |
de              | 478.6M         | 225.1M         | 11.5B           | 6B              | 299.5B         | 139.6B         | 2.2T            | 1T              | 370.6 G  | 815.5 G  |
fr              | 384.2M         | 218.9M         | 7.9B            | 5B              | 307.1B         | 165.2B         | 2T              | 1T              | 370.4 G  | 699.1 G  |
it              | 238.9M         | 126.4M         | 4.5B            | 2.5B            | 180.1B         | 83.6B          | 1.2T            | 553.1B          | 198.4 G  | 429.6 G  |
pt              | 209.2M         | 124.2M         | 4B              | 2.4B            | 123.2B         | 79.2B          | 791.5B          | 499.8B          | 183.1 G  | 289.6 G  |
pl              | 145.1M         | 90.9M          | 3.3B            | 2.4B            | 68.9B          | 49.2B          | 505B            | 356.4B          | 140.7 G  | 202.5 G  |
nl              | 134.5M         | 86.6M          | 134.5M          | 2.3B            | 104.4B         | 51.6B          | 698.5B          | 334.5B          | 118.2 G  | 247.5 G  |
tr              | 107M           | 56.4M          | 107M            | 1.2B            | 41.9B          | 25B            | 328.8B          | 198.9B          | 73.7 G   | 123.9 G  |
vi              | 92.8M          | 55M            | 1.6B            | 1B              | 71.5B          | 48.7B          | 342B            | 228.8B          | 88.8 G   | 133.9 G  |
cs              | 72.1M          | 38.3M          | 1.7B            | 1B              | 40.8B          | 22.1B          | 272.2B          | 147.9B          | 62.1 G   | 112.7 G  |
id              | 120.9M         | 38M            | 2.2B            | 747.5M          | 60.4B          | 20.2B          | 443B            | 148.3B          | 48.5 G   | 148.7 G  |
ro              | 60.8M          | 35.4M          | 60.8M           | 746.4M          | 37.1B          | 22.9B          | 244.1B          | 148.2B          | 55.5 G   | 90.3 G   |
sv              | 65.2M          | 35.2M          | 65.2M           | 1B              | 62.1B          | 23.9B          | 422.6B          | 153.7B          | 57.0 G   | 149.9 G  |
hu              | 47.6M          | 29.7M          | 1.3B            | 806.3M          | 29.8B          | 17.8B          | 223.6B          | 134.9B          | 53.5 G   | 86.8 G   |
uk              | 46.6M          | 25M            | 1B              | 599.9M          | 21.6B          | 12.8B          | 164.2B          | 95.2B           | 45.1 G   | 75.8 G   |
fa              | 58.1M          | 23.1M          | 920.6M          | 493.5M          | 40.6B          | 18.4B          | 220.4B          | 96.7B           | 43.4 G   | 97.4 G   |
ja              | 23.3M          | 21.8M          | 326M            | 321.6M          | 10.9B          | 10.9B          | 133.3B          | 132.2B          | 98.7 G   | 99.7 G   |
el              | 52.4M          | 20.9M          | 808M            | 445.4M          | 25B            | 12B            | 173.2B          | 80.9B           | 37.9 G   | 80.8 G   |
fi              | 35.8M          | 20.4M          | 1B              | 650.3M          | 23.8B          | 11.5B          | 202.2B          | 101.1B          | 37.6 G   | 74.1 G   |
zh              | 29.3M          | 19.9M          | 492.3M          | 298.8M          | 19.2B          | 10B            | 333B            | 142.3B          | 109.9 G  | 191.8 G  |
da              | 38.5M          | 17.9M          | 1.1B            | 508M            | 37.7B          | 13B            | 252B            | 83.1B           | 29.4 G   | 89.5 G   |
th              | 19M            | 17.4M          | 19M             | 385.8M          | 8.9B           | 8.9B           | 118.6B          | 117.6B          | 57.6 G   | 58.2 G   |
no              | 34.7M          | 14.9M          | 34.7M           | 498.7M          | 46.6B          | 11.8B          | 305.6B          | 74.8B           | 27.3 G   | 109.8 G  |
bg              | 27.2M          | 12.8M          | 599.4M          | 360.3M          | 14.4B          | 8.8B           | 95.6B           | 57.8B           | 26.0 G   | 42.8 G   |
ko              | 19.7M          | 12.7M          | 628.6M          | 471.8M          | 13.3B          | 9.3B           | 65.9B           | 43.8B           | 34.2 G   | 49.1 G   |
ar              | 67.6M          | 12.4M          | 876.6M          | 182.6M          | 39B            | 7.1B           | 243B            | 43.2B           | 20.9 G   | 115.9 G  |
sk              | 23.2M          | 11.9M          | 487.9M          | 300.6M          | 11.3B          | 6.7B           | 77.8B           | 45.7B           | 18.8 G   | 31.9 G   |
ca              | 17.9M          | 9.5M           | 258.6M          | 153M            | 8.9B           | 5.6B           | 56.5B           | 34.6B           | 12.6 G   | 20.8 G   |
lt              | 15.3M          | 8.7M           | 374M            | 256.9M          | 7.5B           | 5.3B           | 58.6B           | 41.3B           | 15.7 G   | 22.3 G   |
he              | 14.1M          | 7.2M           | 302.2M          | 196.8M          | 9.2B           | 5.2B           | 54.9B           | 30.5B           | 14.8 G   | 26.3 G   |
sl              | 12M            | 6.3M           | 316M            | 180M            | 6.9B           | 4.5B           | 47.8B           | 30.5B           | 11.5 G   | 18.0 G   |
et              | 8.8M           | 5.5M           | 223.8M          | 176.3M          | 5B             | 3.6B           | 40.1B           | 28.7B           | 10.7 G   | 15.0 G   |
lv              | 8.4M           | 5M             | 186.1M          | 138.5M          | 4.8B           | 3.2B           | 36.7B           | 23.9B           | 9.1 G    | 13.8 G   |
hi              | 9.9M           | 4.5M           | 254.4M          | 152M            | 7.4B           | 3.8B           | 39.9B           | 20.1B           | 9.9 G    | 19.7 G   |
sq              | 5.5M           | 3.6M           | 5.5M            | 56.1M           | 2.7B           | 2.1B           | 17B             | 12.7B           | 4.8 G    | 6.6 G    |
az              | 5.2M           | 3.3M           | 90.3M           | 70.9M           | 2.1B           | 1.5B           | 16.3B           | 11.9B           | 4.5 G    | 6.3 G    |
hr              | 23M            | 2.8M           | 476.6M          | 53M             | 12.6B          | 1.4B           | 85.1B           | 9.6B            | 3.7 G    | 33.5 G   |
ta              | 5.6M           | 2.6M           | 122.5M          | 81.9M           | 2.1B           | 1.1B           | 19.2B           | 10.6B           | 4.9 G    | 8.8 G    |
ms              | 14.1M          | 2.3M           | 14.1M           | 55.2M           | 8B             | 1.7B           | 58.8B           | 12.5B           | 4.0 G    | 20.4 G   |
ml              | 3.7M           | 2.1M           | 75M             | 52M             | 1B             | 603.3M         | 10.5B           | 6.3B            | 3.0 G    | 5.1 G    |
sr              | 4.7M           | 2M             | 4.7M            | 64M             | 2.7B           | 1.6B           | 18.6B           | 11B             | 5.1 G    | 8.7 G    |
kk              | 3.1M           | 1.8M           | 87.4M           | 59.1M           | 1.6B           | 1B             | 13.4B           | 8.6B            | 3.8 G    | 5.8 G    |
te              | 2.5M           | 1.7M           | 59M             | 46.4M           | 900.2M         | 618.5M         | 7.4B            | 5.1B            | 2.6 G    | 3.8 G    |
mr              | 2.9M           | 1.7M           | 2.9M            | 50M             | 1.2B           | 776.9M         | 8.7B            | 5.5B            | 2.8 G    | 4.4 G    |
is              | 2.9M           | 1.6M           | 73.7M           | 39.3M           | 2.1B           | 979.2M         | 14.9B           | 6.4B            | 2.5 G    | 5.9 G    |
bs              | 12.9M          | 1.4M           | 163.6M          | 9M              | 5.9B           | 490.9M         | 39.5B           | 3.3B            | 1.3 G    | 15.6 G   |
mk              | 2.9M           | 1.4M           | 41.3M           | 22.6M           | 1.3B           | 685.9M         | 9.1B            | 4.5B            | 2.0 G    | 4.0 G    |
gl              | 4.2M           | 1.3M           | 45.3M           | 18.8M           | 2.3B           | 748.4M         | 15.6B           | 4.8B            | 1.7 G    | 5.5 G    |
eu              | 2.1M           | 1.2M           | 41.7M           | 24.8M           | 827.5M         | 525.3M         | 6.9B            | 4.3B            | 1.5 G    | 2.4 G    |
bn              | 4.3M           | 1.1M           | 151.2M          | 38.6M           | 2.5B           | 645.7M         | 16.8B           | 4.3B            | 2.2 G    | 8.7 G    |
be              | 2M             | 1.1M           | 48.8M           | 31.3M           | 981M           | 632.9M         | 7.2B            | 4.6B            | 2.2 G    | 3.5 G    |
ka              | 3.1M           | 936.5K         | 53.7M           | 26.6M           | 1.2B           | 460.8M         | 10.3B           | 3.8B            | 1.9 G    | 5.0 G    |
fil             | 4.2M           | 901.5K         | 67.4M           | 19.2M           | 2.2B           | 741.7M         | 14.6B           | 4.7B            | 1.5 G    | 5.0 G    |
mn              | 2.2M           | 879.9K         | 43.3M           | 24M             | 1.1B           | 487.5M         | 7.9B            | 3.5B            | 1.6 G    | 3.5 G    |
af              | 2.9M           | 868.7K         | 51.9M           | 30M             | 1.7B           | 795M           | 11.8B           | 4.8B            | 1.8 G    | 4.2 G    |
uz              | 1.4M           | 669.9K         | 25.7M           | 17.5M           | 605.9M         | 388.3M         | 5.2B            | 3.3B            | 1.1 G    | 1.9 G    |
gu              | 1.3M           | 659.7K         | 28.9M           | 18.1M           | 634.4M         | 345.9M         | 3.9B            | 2.1B            | 1.1 G    | 2.0 G    |
kn              | 1.6M           | 657.8K         | 32.9M           | 19.2M           | 546.4M         | 258.6M         | 4.6B            | 2.2B            | 1.1 G    | 2.3 G    |
kaa             | 1.1M           | 586.4K         | 19.8M           | 13.3M           | 455.9M         | 269M           | 3.8B            | 2.2B            | 990.2 M  | 1.6 G    |
sw              | 1.3M           | 537.8K         | 1.3M            | 9.5M            | 660.7M         | 345.8M         | 4.6B            | 2.4B            | 826.1 M  | 1.6 G    |
ur              | 967.2K         | 467.2K         | 29M             | 18.4M           | 1B             | 562.5M         | 5.2B            | 2.7B            | 1.2 G    | 2.4 G    |
ne              | 876.4K         | 453.3K         | 876.4K          | 20.4M           | 585M           | 345.3M         | 3.9B            | 2.2B            | 1.1 G    | 1.9 G    |
cy              | 4.9M           | 430.7K         | 68.3M           | 7.4M            | 3.6B           | 275.6M         | 26.4B           | 1.7B            | 609.5 M  | 10.0 G   |
hy              | 2M             | 397.5K         | 31.1M           | 9.9M            | 1B             | 190.9M         | 8.1B            | 1.5B            | 678.9 M  | 3.6 G    |
ky              | 751.1K         | 367.6K         | 14.3M           | 9.6M            | 303.4M         | 181.6M         | 2.5B            | 1.4B            | 665.1 M  | 1.1 G    |
si              | 788K           | 349.2K         | 22.1M           | 16M             | 507.3M         | 293.3M         | 3.4B            | 1.9B            | 1023.6 M | 1.8 G    |
tt              | 2.1M           | 346.9K         | 60.2M           | 8.6M            | 1B             | 135M           | 12.1B           | 1B              | 494.1 M  | 4.6 G    |
tg              | 789.2K         | 328.2K         | 789.2K          | 7.4M            | 363.8M         | 208.8M         | 2.6B            | 1.4B            | 635.7 M  | 1.1 G    |
la              | 2.9M           | 319.2K         | 85.7M           | 13.8M           | 1.1B           | 218.4M         | 8.2B            | 1.5B            | 550.6 M  | 2.9 G    |
so              | 729.2K         | 293.2K         | 729.2K          | 3.1M            | 294.8M         | 146.3M         | 2.1B            | 992.4M          | 350.8 M  | 746.2 M  |
ga              | 5.3M           | 286K           | 31.7M           | 6.9M            | 4.2B           | 229.3M         | 30.6B           | 1.4B            | 500.7 M  | 9.8 G    |
km              | 297.8K         | 285.7K         | 5M              | 5M              | 53M            | 52.6M          | 1.1B            | 1.1B            | 566.2 M  | 570.0 M  |
mt              | 1.2M           | 265.4K         | 1.2M            | 5.6M            | 390.4M         | 171.5M         | 3.2B            | 1.3B            | 467.4 M  | 1.1 G    |
eo              | 1.4M           | 260K           | 33.9M           | 9.3M            | 745.1M         | 253.1M         | 5.5B            | 1.7B            | 627.6 M  | 1.9 G    |
ps              | 429.9K         | 252.9K         | 5.1M            | 3.6M            | 293.9M         | 177.5M         | 1.4B            | 848.9M          | 403.5 M  | 682.9 M  |
rw              | 681.8K         | 226.5K         | 681.8K          | 1.9M            | 225M           | 99.8M          | 1.7B            | 749.1M          | 264.8 M  | 702.4 M  |
ku              | 671.9K         | 218.9K         | 10.7M           | 4.9M            | 305.3M         | 143.8M         | 2.1B            | 849.9M          | 335.3 M  | 791.9 M  |
lo              | 229.1K         | 216K           | 2.9M            | 2.8M            | 41.7M          | 41.1M          | 706.9M          | 697.6M          | 365.3 M  | 370.8 M  |
fy              | 1.7M           | 210K           | 12.1M           | 3.7M            | 506.9M         | 94M            | 3.7B            | 592.3M          | 223.0 M  | 1.2 G    |
ha              | 443.9K         | 173.5K         | 4.5M            | 2.4M            | 206.5M         | 109.3M         | 1.3B            | 630.2M          | 219.0 M  | 478.1 M  |
my              | 176.5K         | 172.4K         | 176.5K          | 10.1M           | 96.6M          | 96.3M          | 1.3B            | 1.3B            | 648.8 M  | 650.4 M  |
dv              | 264.4K         | 167.2K         | 4.3M            | 3.5M            | 92.8M          | 64M            | 877.3M          | 603.1M          | 238.3 M  | 343.2 M  |
pa              | 368.2K         | 150.6K         | 368.2K          | 6M              | 306M           | 152.8M         | 1.6B            | 797.1M          | 414.1 M  | 857.6 M  |
ckb             | 622.7K         | 148.9K         | 5.6M            | 2.5M            | 312.7M         | 83.3M          | 2.2B            | 572.7M          | 265.0 M  | 1011.1 M |
lb              | 7.6M           | 146K           | 47.1M           | 3.4M            | 7.5B           | 85M            | 58.4B           | 575.5M          | 218.4 M  | 22.2 G   |
mg              | 295.2K         | 115.4K         | 4.5M            | 2.6M            | 189.4M         | 75.5M          | 1.3B            | 548.5M          | 179.0 M  | 429.3 M  |
ht              | 425.6K         | 110.4K         | 6.7M            | 2.6M            | 163M           | 84.3M          | 994.5M          | 461.5M          | 168.2 M  | 361.5 M  |
ug              | 227.1K         | 106.5K         | 4.5M            | 3.1M            | 122.9M         | 62.7M          | 998.5M          | 504.6M          | 233.1 M  | 449.9 M  |
am              | 245.2K         | 106.3K         | 7.1M            | 5.3M            | 157M           | 95.2M          | 869.9M          | 509M            | 345.5 M  | 539.4 M  |
or              | 139.6K         | 100.5K         | 139.6K          | 3.1M            | 66M            | 47.3M          | 437.2M          | 309.5M          | 160.3 M  | 228.1 M  |
fo              | 382.9K         | 97.8K          | 3.9M            | 1.8M            | 136.5M         | 48.9M          | 923.3M          | 314.9M          | 122.0 M  | 328.8 M  |
gd              | 206K           | 94.3K          | 3.7M            | 2.4M            | 127.6M         | 84.5M          | 812M            | 526M            | 173.4 M  | 276.6 M  |
ba              | 372.4K         | 90.3K          | 9.3M            | 2.6M            | 101M           | 42.1M          | 766.5M          | 320.7M          | 154.8 M  | 352.4 M  |
tk              | 180.2K         | 82.5K          | 180.2K          | 1.8M            | 65.4M          | 43.3M          | 575.2M          | 369M            | 131.3 M  | 221.6 M  |
mi              | 711.9K         | 79.5K          | 5.9M            | 1.9M            | 262.5M         | 73.5M          | 1.6B            | 371.9M          | 120.2 M  | 539.1 M  |
hmn             | 241.3K         | 75.2K          | 3.5M            | 1.9M            | 192.1M         | 80.2M          | 1.2B            | 408.8M          | 124.3 M  | 366.0 M  |
grc             | 364.8K         | 70.7K          | 13.7M           | 2.8M            | 298.6M         | 65.3M          | 2B              | 417.8M          | 217.7 M  | 1.0 G    |
jv              | 999.5K         | 69.5K          | 13M             | 2M              | 302.3M         | 52.1M          | 2.3B            | 376.1M          | 130.9 M  | 797.8 M  |
ceb             | 617.5K         | 66.2K          | 6.7M            | 1.6M            | 225M           | 58.2M          | 1.5B            | 357.7M          | 116.2 M  | 451.4 M  |
sd              | 115.6K         | 65.9K          | 115.6K          | 2.4M            | 112.6M         | 77.8M          | 561M            | 380.4M          | 182.3 M  | 267.1 M  |
yi              | 160.6K         | 64.9K          | 3.3M            | 1.9M            | 129.1M         | 53.9M          | 838.4M          | 352.6M          | 146.0 M  | 350.8 M  |
kaa_Latn        | 375.2K         | 61.2K          | 3.6M            | 1.3M            | 375.2K         | 61.2K          | 1.5M            | 209.5K          | 86.2 M   | 264.6 M  |
sn              | 3.1M           | 60.2K          | 3.1M            | 1.2M            | 1.3B           | 31.6M          | 10.6B           | 266M            | 92.5 M   | 3.2 G    |
co              | 546.7K         | 55.4K          | 6.1M            | 1.3M            | 172.6M         | 43.6M          | 1.1B            | 265.5M          | 98.8 M   | 386.8 M  |
su              | 336.6K         | 55K            | 336.6K          | 1.6M            | 154M           | 39.5M          | 967.2M          | 286.7M          | 100.7 M  | 308.5 M  |
pap             | 259.1K         | 54.5K          | 259.1K          | 1.4M            | 183.9M         | 41.1M          | 1.4B            | 229.9M          | 83.5 M   | 451.4 M  |
ig              | 130.4K         | 54.4K          | 2.1M            | 1.4M            | 129.2M         | 45.7M          | 846.1M          | 251.4M          | 93.0 M   | 178.9 M  |
zu              | 372.3K         | 53.8K          | 3.8M            | 1.2M            | 148.4M         | 27.2M          | 1.2B            | 257.4M          | 89.6 M   | 374.7 M  |
xh              | 310.9K         | 53.7K          | 2.9M            | 1.4M            | 81.6M          | 31.2M          | 749.5M          | 287.3M          | 100.0 M  | 319.1 M  |
sm              | 137.8K         | 52.6K          | 1.9M            | 1.3M            | 100.9M         | 53.7M          | 607.9M          | 276.3M          | 88.6 M   | 184.5 M  |
ny              | 181.6K         | 52.2K          | 181.6K          | 1.5M            | 80.6M          | 34.8M          | 611.2M          | 277.5M          | 91.8 M   | 209.8 M  |
yo              | 115K           | 52.1K          | 2M              | 1.2M            | 76.6M          | 46.3M          | 415.6M          | 239M            | 89.2 M   | 157.8 M  |
cv              | 599.4K         | 47.3K          | 12M             | 1.6M            | 169.6M         | 22.2M          | 1B              | 168.9M          | 82.1 M   | 413.6 M  |
el_Latn         | 497.3K         | 46.4K          | 11.3M           | 1.7M            | 497.3K         | 46.4K          | 2.3M            | 162.8K          | 196.8 M  | 571.1 M  |
kl              | 85.9K          | 46K            | 2.1M            | 1.5M            | 32.3M          | 22.3M          | 403.9M          | 279.1M          | 84.2 M   | 126.1 M  |
haw             | 310.4K         | 45.7K          | 7.1M            | 1M              | 141M           | 43.3M          | 892M            | 214.2M          | 69.9 M   | 271.2 M  |
gsw             | 7.6M           | 42.7K          | 64.5M           | 1M              | 5B             | 22.3M          | 42.3B           | 149.2M          | 53.8 M   | 13.5 G   |
tet             | 291K           | 40.4K          | 1.9M            | 475.7K          | 240.6M         | 22.8M          | 1.6B            | 152.3M          | 51.2 M   | 455.4 M  |
st              | 96.8K          | 40.4K          | 96.8K           | 1.1M            | 65M            | 39.8M          | 381.5M          | 226.9M          | 74.0 M   | 127.0 M  |
lus             | 91.5K          | 36.4K          | 1.4M            | 863.5K          | 53M            | 31.3M          | 298.3M          | 167.3M          | 60.1 M   | 107.0 M  |
oc              | 2.4M           | 36.4K          | 2.4M            | 1.6M            | 887.6M         | 26.7M          | 6.7B            | 177.6M          | 58.7 M   | 1.9 G    |
as              | 53.9K          | 33.8K          | 2.4M            | 1.7M            | 41.4M          | 27.9M          | 275.8M          | 182.1M          | 95.8 M   | 146.1 M  |
rm              | 238.1K         | 33.8K          | 238.1K          | 603.4K          | 59.2M          | 15.8M          | 391M            | 100.2M          | 34.6 M   | 133.1 M  |
br              | 705.4K         | 33.2K          | 7.8M            | 731.7K          | 646.8M         | 21M            | 3.7B            | 125.4M          | 46.2 M   | 1.2 G    |
sah             | 1.3M           | 29.2K          | 1.3M            | 1.2M            | 283.7M         | 17.6M          | 2.2B            | 148.2M          | 68.3 M   | 852.3 M  |
hi_Latn         | 1.2M           | 26.7K          | 22.6M           | 1.2M            | 1.2M           | 26.7K          | 5.3M            | 98.9K           | 53.5 M   | 1.7 G    |
se              | 54.3K          | 23.9K          | 879.5K          | 493.3K          | 17.7M          | 10M            | 148.4M          | 84.6M           | 31.1 M   | 56.6 M   |
cnh             | 44.4K          | 21.6K          | 688.6K          | 406.9K          | 21.6M          | 12.5M          | 110.8M          | 63M             | 22.1 M   | 39.6 M   |
om              | 846.1K         | 18.9K          | 846.1K          | 469.8K          | 238M           | 11.2M          | 1.9B            | 88.5M           | 30.4 M   | 881.5 M  |
ce              | 59.3K          | 15K            | 991.1K          | 460.1K          | 17.8M          | 9.6M           | 130.6M          | 67.8M           | 31.1 M   | 60.2 M   |
udm             | 67.1K          | 13.4K          | 942.7K          | 510.3K          | 14M            | 7.4M           | 106M            | 55.5M           | 26.3 M   | 49.2 M   |
lg              | 61.1K          | 13K            | 510.9K          | 166.1K          | 21.4M          | 6.1M           | 160.7M          | 48M             | 17.3 M   | 56.7 M   |
os              | 172.1K         | 12.6K          | 172.1K          | 359.3K          | 27.1M          | 6.9M           | 233.5M          | 50.1M           | 23.1 M   | 87.7 M   |
nv              | 17.1K          | 12.6K          | 17.1K           | 86.5K           | 3.1M           | 1.1M           | 24.8M           | 9.1M            | 2.0 M    | 7.9 M    |
kha             | 37.8K          | 12.1K          | 235.5K          | 75.2K           | 15.8M          | 6M             | 88.6M           | 30.2M           | 9.8 M    | 27.3 M   |
ilo             | 69.8K          | 11.8K          | 889.2K          | 365.1K          | 26.7M          | 9M             | 187.9M          | 59.4M           | 20.6 M   | 64.0 M   |
ctd_Latn        | 23.3K          | 11.6K          | 575.6K          | 382.2K          | 23.3K          | 11.6K          | 90.7K           | 41K             | 21.5 M   | 35.1 M   |
vec             | 1.1M           | 11.1K          | 10M             | 209.7K          | 284.7M         | 7.8M           | 1.8B            | 43.8M           | 17.7 M   | 625.0 M  |
hil             | 126.8K         | 10.6K          | 1.1M            | 379.7K          | 43.9M          | 9.2M           | 293.5M          | 57.2M           | 18.5 M   | 95.2 M   |
tyv             | 61.6K          | 9.1K           | 596.6K          | 268.3K          | 9.9M           | 4.7M           | 80.2M           | 38.5M           | 16.7 M   | 36.6 M   |
iba             | 34K            | 7.6K           | 326.9K          | 126.1K          | 37.8M          | 4.8M           | 251.4M          | 30.5M           | 10.0 M   | 61.3 M   |
ru_Latn         | 346.3K         | 7.5K           | 346.3K          | 239.1K          | 346.3K         | 7.5K           | 1.5M            | 27.7K           | 14.9 M   | 452.3 M  |
kbd             | 154.7K         | 7.5K           | 1.4M            | 257.2K          | 31.9M          | 4.4M           | 321.4M          | 36.8M           | 16.8 M   | 209.6 M  |
ti              | 20.8K          | 7.3K           | 20.8K           | 481.3K          | 18.2M          | 8.8M           | 95.4M           | 44.6M           | 30.9 M   | 63.6 M   |
sa              | 154.3K         | 7.1K           | 154.3K          | 1.1M            | 70M            | 9.9M           | 512.5M          | 88.8M           | 44.9 M   | 236.6 M  |
av              | 107.6K         | 6.3K           | 806.1K          | 190.1K          | 15.5M          | 3.4M           | 129M            | 30.2M           | 12.8 M   | 56.0 M   |
bo              | 6.2K           | 6.2K           | 1.1M            | 1.1M            | 3.4M           | 3.4M           | 88.7M           | 88.7M           | 40.7 M   | 40.7 M   |
zza             | 370.1K         | 6K             | 3.3M            | 229.2K          | 87.7M          | 3.9M           | 617.3M          | 26.3M           | 10.0 M   | 234.1 M  |
ber_Latn        | 480.5K         | 5.6K           | 10.5M           | 169.4K          | 480.5K         | 5.6K           | 2.1M            | 18.9K           | 11.0 M   | 945.3 M  |
otq             | 17.6K          | 5.6K           | 17.6K           | 114.8K          | 10.2M          | 3.8M           | 65M             | 23.4M           | 7.7 M    | 22.8 M   |
te_Latn         | 236.6K         | 5.3K           | 4.4M            | 269.1K          | 236.6K         | 5.3K           | 1M              | 19.3K           | 11.4 M   | 254.3 M  |
bua             | 9.8K           | 5.3K           | 252K            | 144.6K          | 4.7M           | 2.7M           | 38M             | 21.7M           | 10.0 M   | 17.9 M   |
ts              | 34.7K          | 5.2K           | 34.7K           | 248.6K          | 39.6M          | 6.5M           | 377.2M          | 38.8M           | 12.2 M   | 99.5 M   |
cfm             | 9.1K           | 4.9K           | 199.6K          | 128.6K          | 6.2M           | 4M             | 32.9M           | 21.5M           | 7.4 M    | 11.6 M   |
tn              | 138.2K         | 4.8K           | 138.2K          | 174.4K          | 46M            | 5.5M           | 302.3M          | 29.2M           | 9.4 M    | 99.0 M   |
krc             | 359.5K         | 4.8K           | 2.3M            | 153.9K          | 50.2M          | 2.6M           | 369.5M          | 20.7M           | 9.1 M    | 139.9 M  |
ak              | 19.5K          | 4.8K           | 341.7K          | 210.2K          | 12.3M          | 4.7M           | 74.5M           | 24.8M           | 9.1 M    | 24.7 M   |
meo             | 790.7K         | 4.7K           | 16.5M           | 39K             | 478M           | 1.2M           | 3B              | 7.5M            | 3.1 M    | 1.2 G    |
chm             | 81.5K          | 4.7K           | 929.1K          | 179.7K          | 17.2M          | 2.9M           | 132.2M          | 21.3M           | 9.8 M    | 53.5 M   |
to              | 14.3K          | 4.6K           | 14.3K           | 149K            | 10.3M          | 5.7M           | 58.2M           | 29.9M           | 9.6 M    | 19.0 M   |
ee              | 14.1K          | 4.5K           | 353.6K          | 246.7K          | 9.7M           | 6.2M           | 67.9M           | 32.8M           | 11.8 M   | 23.3 M   |
nso             | 376.2K         | 4.4K           | 376.2K          | 188.4K          | 419.2M         | 5.3M           | 2B              | 28.2M           | 9.1 M    | 502.7 M  |
ady             | 74.9K          | 4.2K           | 446.8K          | 96.9K           | 8M             | 1.6M           | 67.9M           | 14.8M           | 6.4 M    | 30.6 M   |
rom             | 22.9K          | 4.2K           | 22.9K           | 76.1K           | 8.9M           | 2.6M           | 59M             | 15.9M           | 5.8 M    | 21.0 M   |
bho             | 13.6K          | 4.1K           | 306.2K          | 118.5K          | 7.1M           | 2.7M           | 37.6M           | 13.4M           | 7.4 M    | 20.6 M   |
ltg             | 13.1K          | 4.1K           | 213.7K          | 87.3K           | 4M             | 1.9M           | 29.2M           | 13.9M           | 5.6 M    | 11.7 M   |
fj              | 17K            | 4K             | 410K            | 164.1K          | 11.6M          | 5.2M           | 67.7M           | 28M             | 8.6 M    | 22.5 M   |
yua             | 10.4K          | 4K             | 141.6K          | 77.6K           | 5.2M           | 2.5M           | 36.8M           | 17.2M           | 5.7 M    | 12.4 M   |
gn              | 87.1K          | 3.9K           | 770.9K          | 162.6K          | 19.2M          | 2.7M           | 140.7M          | 20.8M           | 7.8 M    | 52.1 M   |
az_RU           | 6.5K           | 3.8K           | 231.8K          | 177.3K          | 6.5K           | 3.8K           | 24K             | 12.9K           | 10.3 M   | 15.1 M   |
ln              | 94.7K          | 3.3K           | 718.7K          | 139K            | 42.4M          | 3.4M           | 291.8M          | 21.5M           | 6.8 M    | 85.3 M   |
ada             | 6.5K           | 3.1K           | 291.5K          | 199.2K          | 7.5M           | 4.9M           | 38.9M           | 24.2M           | 8.6 M    | 13.9 M   |
myv             | 164.8K         | 3.1K           | 164.8K          | 130K            | 16M            | 1.7M           | 120.3M          | 13.8M           | 6.2 M    | 49.5 M   |
bik             | 44.8K          | 3.1K           | 376.7K          | 77K             | 14.8M          | 2.5M           | 102.3M          | 15.7M           | 5.3 M    | 34.0 M   |
tlh             | 516.9K         | 3.1K           | 516.9K          | 46.9K           | 221.3M         | 1.1M           | 1.4B            | 7.8M            | 2.7 M    | 554.2 M  |
kbp             | 5.9K           | 3K             | 247.9K          | 128.3K          | 5.6M           | 2.6M           | 30.8M           | 14.6M           | 5.7 M    | 12.4 M   |
war             | 1M             | 2.9K           | 114M            | 96.2K           | 612.1M         | 2.4M           | 3.5B            | 16.1M           | 3.7 M    | 1.2 G    |
wa              | 70.6K          | 2.8K           | 1.5M            | 127.2K          | 35.2M          | 3.6M           | 198.8M          | 20.4M           | 7.2 M    | 67.8 M   |
bew             | 311.1K         | 2.7K           | 10.4M           | 58.4K           | 212.4M         | 1.3M           | 1.4B            | 8.5M            | 3.1 M    | 547.1 M  |
rcf             | 21.6K          | 2.6K           | 21.6K           | 50.5K           | 4.9M           | 1.2M           | 30.2M           | 5.7M            | 2.1 M    | 11.4 M   |
ta_Latn         | 260.7K         | 2.6K           | 3.4M            | 142.7K          | 260.7K         | 2.6K           | 1.2M            | 9.1K            | 5.0 M    | 215.4 M  |
kac             | 5.9K           | 2.6K           | 109.2K          | 77.4K           | 5M             | 2.8M           | 26.6M           | 13.6M           | 4.3 M    | 8.0 M    |
iu              | 5.4K           | 2.5K           | 92.6K           | 53.1K           | 1.9M           | 907.4K         | 17.5M           | 8.3M            | 4.8 M    | 9.9 M    |
ay              | 8.1K           | 2.5K           | 196.7K          | 83.8K           | 3.9M           | 1.4M           | 34.5M           | 13.1M           | 4.5 M    | 12.7 M   |
kum             | 4.2K           | 2.5K           | 132.2K          | 89.7K           | 2.3M           | 1.6M           | 18.2M           | 12.4M           | 5.3 M    | 8.0 M    |
qu              | 149.7K         | 2.4K           | 1M              | 87K             | 26.7M          | 1.3M           | 200.6M          | 12.2M           | 4.0 M    | 68.3 M   |
bgp             | 355.7K         | 2.4K           | 5.6M            | 43.3K           | 186.1M         | 1.8M           | 1.1B            | 9.8M            | 3.1 M    | 377.5 M  |
hif             | 702K           | 2.4K           | 7.9M            | 124.7K          | 1.2B           | 3.2M           | 9.1B            | 19.1M           | 5.9 M    | 3.5 G    |
kw              | 176.9K         | 2.3K           | 1M              | 51.6K           | 53.1M          | 1.3M           | 327.8M          | 7.7M            | 2.8 M    | 89.2 M   |
nan_Latn_TW     | 7.4K           | 2.3K           | 7.4K            | 72.7K           | 7.4K           | 2.3K           | 28.3K           | 7.7K            | 4.8 M    | 15.4 M   |
srn             | 16.7K          | 2.3K           | 16.7K           | 139.5K          | 8M             | 3.4M           | 49.1M           | 17M             | 5.1 M    | 15.6 M   |
tly_IR          | 406.3K         | 2.2K           | 406.3K          | 18.2K           | 406.3K         | 2.2K           | 1.6M            | 8.6K            | 580.4 K  | 283.0 M  |
sg              | 4.2K           | 2.1K           | 154K            | 117.9K          | 4.6M           | 3.3M           | 22.6M           | 15.5M           | 4.6 M    | 6.8 M    |
gom             | 4.6K           | 2.1K           | 178.3K          | 108K            | 2.7M           | 1.4M           | 19.8M           | 10M             | 5.0 M    | 10.5 M   |
ml_Latn         | 260.8K         | 2.1K           | 3.5M            | 77.3K           | 260.8K         | 2.1K           | 1.1M            | 7.2K            | 3.5 M    | 277.7 M  |
kj              | 112.2K         | 2.1K           | 881.8K          | 22.6K           | 46.9M          | 877.3K         | 339.6M          | 6M              | 2.1 M    | 104.9 M  |
ksd             | 14.9K          | 2K             | 533K            | 78.6K           | 11.5M          | 2.1M           | 62.4M           | 10M             | 2.9 M    | 20.0 M   |
dz              | 1.9K           | 1.9K           | 191.7K          | 191.7K          | 1.1M           | 1.1M           | 22.7M           | 22.7M           | 10.0 M   | 10.0 M   |
kv              | 59.1K          | 1.9K           | 584.3K          | 88.8K           | 9.5M           | 1.2M           | 91.4M           | 9M              | 4.4 M    | 41.0 M   |
msi             | 686.7K         | 1.9K           | 686.7K          | 22.6K           | 414.8M         | 440.4K         | 2.6B            | 2.7M            | 1.1 M    | 1.0 G    |
ve              | 3.8K           | 1.9K           | 97.8K           | 79.4K           | 3.2M           | 2.1M           | 19M             | 11.7M           | 3.8 M    | 6.2 M    |
zap             | 5.5K           | 1.8K           | 202.3K          | 93.5K           | 4.2M           | 1.8M           | 26.4M           | 11.4M           | 4.0 M    | 9.6 M    |
zxx_xx_dtynoise | 118.8K         | 1.8K           | 3.8M            | 49.3K           | 118.8K         | 1.8K           | 501K            | 6.6K            | 3.9 M    | 367.0 M  |
meu             | 5.9K           | 1.7K           | 232.1K          | 72.6K           | 4.2M           | 1.4M           | 27.2M           | 8.6M            | 2.6 M    | 9.1 M    |
iso             | 3.7K           | 1.7K           | 155.8K          | 111.5K          | 4.4M           | 2.7M           | 23M             | 13.7M           | 4.9 M    | 8.1 M    |
ium             | 100.3K         | 1.7K           | 6.2M            | 54.9K           | 48.4M          | 1.7M           | 314M            | 7.4M            | 2.6 M    | 124.0 M  |
nhe             | 3K             | 1.7K           | 3K              | 57.7K           | 1.9M           | 1.2M           | 15.6M           | 9.8M            | 2.7 M    | 4.8 M    |
tyz             | 8K             | 1.7K           | 454.8K          | 104.6K          | 7.5M           | 1.9M           | 46.3M           | 11.3M           | 3.8 M    | 16.0 M   |
hui             | 2K             | 1.7K           | 80.1K           | 74.7K           | 1.8M           | 1.7M           | 11.8M           | 10.9M           | 3.0 M    | 3.3 M    |
new             | 6.6K           | 1.6K           | 6.6K            | 85K             | 3.2M           | 1.4M           | 21.2M           | 8.8M            | 4.4 M    | 10.6 M   |
mdf             | 71K            | 1.6K           | 394.7K          | 45.1K           | 8.3M           | 670.1K         | 65.8M           | 5.5M            | 2.5 M    | 26.7 M   |
pag             | 49.6K          | 1.6K           | 49.6K           | 88.8K           | 13.8M          | 1.9M           | 92.9M           | 12M             | 3.9 M    | 29.2 M   |
gv              | 501.9K         | 1.6K           | 18.8M           | 26.9K           | 137.7M         | 996.2K         | 933.1M          | 6.2M            | 2.0 M    | 318.6 M  |
gag             | 33.9K          | 1.6K           | 491K            | 37K             | 10.2M          | 661K           | 84.9M           | 5.2M            | 2.1 M    | 32.6 M   |
ngu             | 3.8K           | 1.5K           | 3.8K            | 87.1K           | 2.7M           | 1.5M           | 21.4M           | 11.8M           | 3.6 M    | 6.7 M    |
quc             | 4.4K           | 1.5K           | 89.2K           | 41.2K           | 2.8M           | 1.1M           | 16.6M           | 6.4M            | 2.2 M    | 5.9 M    |
mam             | 23K            | 1.5K           | 446.3K          | 52.9K           | 9.8M           | 1.2M           | 70.4M           | 7.2M            | 2.6 M    | 30.7 M   |
min             | 28.2K          | 1.5K           | 500.9K          | 75.6K           | 10.2M          | 1.4M           | 70.5M           | 9.9M            | 2.6 M    | 21.1 M   |
ho              | 2K             | 1.5K           | 57K             | 47.8K           | 1.8M           | 1.3M           | 12.3M           | 7.8M            | 1.9 M    | 3.1 M    |
pon             | 5.7K           | 1.5K           | 167.8K          | 48.7K           | 3M             | 1.1M           | 18.3M           | 6.7M            | 2.1 M    | 6.1 M    |
mrj             | 97.1K          | 1.4K           | 97.1K           | 60.3K           | 14.5M          | 1.1M           | 100.6M          | 7.6M            | 3.6 M    | 40.8 M   |
lu              | 10.6K          | 1.4K           | 316K            | 112.1K          | 7.8M           | 2.3M           | 54.2M           | 15.4M           | 4.8 M    | 18.0 M   |
gom_Latn        | 231.1K         | 1.4K           | 4.1M            | 77.9K           | 231.1K         | 1.4K           | 1M              | 5.1K            | 3.6 M    | 240.6 M  |
alt             | 2.6K           | 1.4K           | 110.1K          | 65.9K           | 1.8M           | 1.1M           | 14.3M           | 8.7M            | 3.8 M    | 6.4 M    |
nzi             | 2.5K           | 1.4K           | 2.5K            | 71.8K           | 2.5M           | 1.7M           | 14.4M           | 9.4M            | 3.1 M    | 4.8 M    |
tzo             | 2.8K           | 1.4K           | 100.4K          | 75.7K           | 2.5M           | 1.7M           | 15.9M           | 10.6M           | 3.2 M    | 4.9 M    |
bci             | 7.4K           | 1.3K           | 124.8K          | 87.1K           | 5M             | 1.9M           | 32.8M           | 9M              | 3.1 M    | 9.4 M    |
dtp             | 4.6K           | 1.3K           | 51.2K           | 7.9K            | 1.9M           | 419.4K         | 12.7M           | 3M              | 1013.9 K | 4.5 M    |
abt             | 1.6K           | 1.3K           | 122.7K          | 110.3K          | 1.5M           | 1.3M           | 9.6M            | 8.2M            | 2.2 M    | 2.7 M    |
bbc             | 72.3K          | 1.3K           | 718.3K          | 73.2K           | 21.7M          | 1.7M           | 151.3M          | 10.6M           | 3.6 M    | 47.9 M   |
pck             | 8.9K           | 1.3K           | 8.9K            | 69.7K           | 6.8M           | 2.1M           | 39.8M           | 11.5M           | 4.2 M    | 14.2 M   |
mai             | 54.3K          | 1.2K           | 1M              | 60.2K           | 24.6M          | 1.2M           | 156M            | 6.8M            | 3.6 M    | 67.1 M   |
mps             | 2.7K           | 1.2K           | 132.8K          | 71.9K           | 2.8M           | 1.6M           | 16M             | 8.7M            | 2.3 M    | 4.8 M    |
emp             | 3.6K           | 1.2K           | 106.4K          | 75.4K           | 1.9M           | 999.1K         | 14.5M           | 7.4M            | 2.4 M    | 4.9 M    |
mgh             | 5.5K           | 1.2K           | 151.8K          | 61.2K           | 2.8M           | 1.1M           | 24.1M           | 8.2M            | 2.8 M    | 8.3 M    |
tab             | 7.8K           | 1.2K           | 226.4K          | 26.8K           | 4.3M           | 538.9K         | 33.7M           | 4.4M            | 1.9 M    | 15.7 M   |
crh             | 5.1K           | 1.2K           | 170.9K          | 61.8K           | 2.4M           | 943K           | 18.8M           | 7.5M            | 3.4 M    | 8.9 M    |
tbz             | 5.1K           | 1.1K           | 128.7K          | 37.5K           | 3.5M           | 893.4K         | 22M             | 4.8M            | 1.9 M    | 10.2 M   |
ss              | 8.1K           | 1.1K           | 8.1K            | 30.4K           | 2.7M           | 568.3K         | 23.7M           | 5.5M            | 1.8 M    | 7.4 M    |
chk             | 2.8K           | 1.1K           | 98.8K           | 44K             | 2M             | 1M             | 12M             | 5.8M            | 1.8 M    | 4.0 M    |
bru             | 3K             | 1.1K           | 89.7K           | 48.2K           | 2.4M           | 938.1K         | 12.9M           | 4.8M            | 1.5 M    | 4.5 M    |
nnb             | 4.9K           | 1.1K           | 4.9K            | 70.2K           | 3.2M           | 1.2M           | 27.7M           | 9.1M            | 3.3 M    | 10.0 M   |
fon             | 5.3K           | 1.1K           | 222.9K          | 67.3K           | 6.9M           | 1.8M           | 34M             | 8.3M            | 3.1 M    | 14.8 M   |
ppk             | 2.6K           | 1.1K           | 85.8K           | 34.9K           | 1.9M           | 801.8K         | 13.2M           | 5.5M            | 1.6 M    | 4.3 M    |
tiv             | 3.8K           | 1.1K           | 3.8K            | 80.7K           | 3.7M           | 2.1M           | 20.4M           | 10.2M           | 3.2 M    | 6.0 M    |
btx             | 3.1K           | 1K             | 81.7K           | 43.9K           | 2M             | 907.5K         | 13.1M           | 5.9M            | 2.0 M    | 4.6 M    |
bg_Latn         | 200.4K         | 991            | 2.8M            | 25.5K           | 200.4K         | 991            | 927.1K          | 3.7K            | 1.7 M    | 143.6 M  |
mbt             | 1.6K           | 969            | 86K             | 45.4K           | 2.4M           | 1.3M           | 14.6M           | 7.5M            | 2.2 M    | 5.1 M    |
ace             | 65.5K          | 966            | 632.5K          | 32.5K           | 19.9M          | 1.1M           | 146.1M          | 7.4M            | 2.2 M    | 42.3 M   |
tvl             | 2.3K           | 933            | 72.9K           | 53.6K           | 2.5M           | 1.7M           | 12.6M           | 8.1M            | 2.4 M    | 3.8 M    |
dov             | 3.5K           | 923            | 129.8K          | 56.7K           | 2.6M           | 967.5K         | 20.7M           | 8M              | 2.6 M    | 7.1 M    |
ach             | 2K             | 915            | 63K             | 40.1K           | 1.6M           | 890.9K         | 9M              | 4.7M            | 1.6 M    | 3.0 M    |
xal             | 71.8K          | 913            | 498.5K          | 30.8K           | 8.5M           | 449.8K         | 64.7M           | 3.2M            | 1.5 M    | 24.4 M   |
cuk             | 4.1K           | 899            | 76.5K           | 34.3K           | 2M             | 469.9K         | 24.7M           | 4.6M            | 1.5 M    | 6.1 M    |
kos             | 2.2K           | 881            | 44.6K           | 27.8K           | 1.1M           | 780.1K         | 6.5M            | 4.2M            | 1.4 M    | 2.2 M    |
crs             | 7.6K           | 873            | 282.4K          | 40.1K           | 7.3M           | 1.2M           | 40.1M           | 6.8M            | 2.2 M    | 13.2 M   |
wo              | 36.4K          | 871            | 303.4K          | 25.4K           | 30.7M          | 850.7K         | 213.4M          | 4.5M            | 1.7 M    | 59.9 M   |
bts             | 3.2K           | 869            | 109.1K          | 29.1K           | 3.1M           | 663.3K         | 20.8M           | 4.2M            | 1.4 M    | 6.2 M    |
ubu             | 2.2K           | 846            | 113.5K          | 47.5K           | 2.3M           | 996.4K         | 15.9M           | 6.7M            | 1.9 M    | 4.7 M    |
gym             | 1.5K           | 820            | 73.7K           | 49.6K           | 1.6M           | 1.1M           | 10.3M           | 6.9M            | 2.0 M    | 3.2 M    |
ibb             | 74.1K          | 818            | 516.5K          | 36.3K           | 26.4M          | 776.1K         | 190.9M          | 4.9M            | 1.5 M    | 56.0 M   |
ape             | 7K             | 814            | 147K            | 56.1K           | 12.4M          | 881.5K         | 71M             | 5.8M            | 1.6 M    | 18.8 M   |
stq             | 111.9K         | 809            | 111.9K          | 27.7K           | 34.4M          | 600.4K         | 243.1M          | 3.8M            | 1.5 M    | 82.5 M   |
ang             | 66.5K          | 803            | 1.8M            | 86.7K           | 28.5M          | 1.7M           | 193M            | 9.8M            | 3.4 M    | 67.1 M   |
enq             | 7.1K           | 793            | 241.9K          | 39.1K           | 11M            | 718.8K         | 68.5M           | 4.8M            | 1.3 M    | 18.8 M   |
tsg             | 353.8K         | 789            | 353.8K          | 17.9K           | 158M           | 588.9K         | 1.1B            | 3.8M            | 1.0 M    | 309.9 M  |
shn             | 889            | 788            | 46.4K           | 46.2K           | 383.8K         | 378.5K         | 5.7M            | 5.7M            | 2.6 M    | 2.6 M    |
kri             | 39.1K          | 786            | 271.2K          | 38.8K           | 12.6M          | 995.2K         | 86.4M           | 5M              | 1.6 M    | 20.9 M   |
kek             | 3.2K           | 782            | 70.4K           | 38.4K           | 1.8M           | 709K           | 13.6M           | 4.4M            | 1.4 M    | 4.7 M    |
rmc             | 2.4K           | 738            | 2.4K            | 25.8K           | 1.3M           | 545.4K         | 7.9M            | 3.2M            | 1.1 M    | 2.9 M    |
acf             | 4.9K           | 730            | 81.9K           | 24.6K           | 2.1M           | 602.2K         | 11.6M           | 3M              | 1.1 M    | 4.7 M    |
fip             | 3.7K           | 729            | 165.6K          | 49K             | 3.5M           | 916.8K         | 25.7M           | 6.6M            | 2.1 M    | 8.6 M    |
syr             | 3.5K           | 716            | 326.4K          | 197.1K          | 4.6M           | 1.9M           | 31.5M           | 14M             | 6.1 M    | 13.9 M   |
qub             | 972            | 705            | 61K             | 51.1K           | 589.2K         | 455.5K         | 5.9M            | 4.4M            | 1.4 M    | 1.8 M    |
bm              | 21.9K          | 702            | 172.3K          | 24.5K           | 7.1M           | 583.1K         | 48.4M           | 3M              | 1.1 M    | 14.4 M   |
tzh             | 1.7K           | 702            | 41.7K           | 33.9K           | 1.5M           | 929.6K         | 9.3M            | 5.6M            | 1.6 M    | 2.6 M    |
jiv             | 1.7K           | 696            | 80.9K           | 32K             | 1.1M           | 418.9K         | 9.6M            | 3.5M            | 1.1 M    | 3.3 M    |
kn_Latn         | 72.9K          | 688            | 765.9K          | 10.1K           | 72.9K          | 688            | 328.1K          | 2.5K            | 430.8 K  | 61.4 M   |
kjh             | 1.5K           | 672            | 42.8K           | 28.7K           | 566.1K         | 379.2K         | 4.5M            | 3.1M            | 1.3 M    | 2.0 M    |
yap             | 1.9K           | 638            | 37.6K           | 19.5K           | 1.3M           | 661.4K         | 6.9M            | 3.3M            | 1.0 M    | 2.2 M    |
ban             | 8K             | 637            | 150.9K          | 16.3K           | 5M             | 499.7K         | 35.4M           | 3.6M            | 1.1 M    | 12.0 M   |
tuc             | 3.5K           | 635            | 193.2K          | 50.3K           | 2.9M           | 703K           | 17.2M           | 4.1M            | 1.2 M    | 5.7 M    |
tcy             | 10.7K          | 632            | 338.7K          | 37.1K           | 5.5M           | 432.6K         | 41.6M           | 3.3M            | 1.7 M    | 20.9 M   |
cab             | 1.2K           | 629            | 50.4K           | 37.5K           | 1M             | 690.9K         | 7.5M            | 5.1M            | 1.6 M    | 2.4 M    |
cak             | 1.2K           | 617            | 70.4K           | 32.6K           | 1.3M           | 730.1K         | 7.6M            | 4.2M            | 1.3 M    | 2.4 M    |
din             | 128.4K         | 611            | 885.8K          | 23.6K           | 31.6M          | 541.7K         | 210M            | 2.9M            | 1.1 M    | 64.3 M   |
zh_Latn         | 739.4K         | 602            | 10.7M           | 45.1K           | 739.4K         | 602            | 3.4M            | 2.3K            | 2.0 M    | 969.9 M  |
arn             | 2.4K           | 593            | 64.5K           | 26.2K           | 1.5M           | 541.9K         | 10.2M           | 3.7M            | 1.2 M    | 3.7 M    |
lrc             | 42.4K          | 587            | 351.9K          | 9K              | 17.3M          | 248.9K         | 85.3M           | 1.4M            | 646.9 K  | 37.5 M   |
rwo             | 938            | 572            | 938             | 45.5K           | 734.8K         | 590.4K         | 5.1M            | 4.2M            | 1.1 M    | 1.4 M    |
hus             | 825            | 569            | 26.5K           | 23.7K           | 733.4K         | 542.1K         | 4.4M            | 3.1M            | 967.6 K  | 1.3 M    |
bum             | 4.7K           | 559            | 103.8K          | 36.5K           | 3M             | 805.5K         | 18.8M           | 4M              | 1.3 M    | 6.1 M    |
mak             | 1K             | 555            | 32.5K           | 20.4K           | 761K           | 457.4K         | 6.1M            | 3.7M            | 1.1 M    | 2.0 M    |
frp             | 148K           | 550            | 3.5M            | 8.2K            | 71.2M          | 230.2K         | 535.4M          | 1.4M            | 518.3 K  | 129.7 M  |
seh             | 5.6K           | 545            | 68.8K           | 37.2K           | 2M             | 650.6K         | 14.9M           | 4.9M            | 1.5 M    | 4.4 M    |
twu             | 2.5K           | 539            | 109.9K          | 24.4K           | 2.4M           | 571.2K         | 14.2M           | 3.2M            | 1.0 M    | 4.8 M    |
kmb             | 1.3K           | 538            | 60.4K           | 36.9K           | 1.4M           | 810.8K         | 8.4M            | 4.6M            | 1.4 M    | 2.6 M    |
ksw             | 560            | 536            | 16.1K           | 16K             | 219.9K         | 218.8K         | 2.9M            | 2.9M            | 1.4 M    | 1.4 M    |
sja             | 1.3K           | 527            | 67.7K           | 24.9K           | 982.5K         | 459.3K         | 7.7M            | 3.4M            | 1.1 M    | 2.6 M    |
amu             | 1.8K           | 511            | 72K             | 25.2K           | 1.5M           | 443.3K         | 9.6M            | 3.2M            | 1.0 M    | 3.4 M    |
mad             | 103.8K         | 509            | 500.6K          | 18.5K           | 16.2M          | 386.7K         | 111.8M          | 2.8M            | 960.3 K  | 34.2 M   |
quh             | 1K             | 501            | 42K             | 29.9K           | 624.4K         | 396.8K         | 5.8M            | 3.7M            | 1.2 M    | 1.8 M    |
dyu             | 1.2K           | 483            | 55.8K           | 19.7K           | 1.2M           | 421.8K         | 5.7M            | 2M              | 665.5 K  | 1.9 M    |
toj             | 736            | 452            | 736             | 26.1K           | 691.2K         | 540.2K         | 4.3M            | 3.3M            | 1.0 M    | 1.3 M    |
ch              | 12.9K          | 449            | 147.5K          | 16K             | 8.9M           | 393.9K         | 63.5M           | 2.5M            | 906.8 K  | 10.0 M   |
sus             | 664            | 437            | 664             | 15.2K           | 648K           | 402.8K         | 3.7M            | 2.1M            | 674.0 K  | 1.0 M    |
nog             | 970            | 419            | 970             | 11K             | 330.3K         | 200.4K         | 2.6M            | 1.6M            | 714.0 K  | 1.2 M    |
jam             | 12.7K          | 416            | 68.5K           | 15.8K           | 3.5M           | 378.4K         | 25.8M           | 1.7M            | 609.5 K  | 7.6 M    |
gui             | 1.1K           | 409            | 62.7K           | 24.8K           | 915K           | 314K           | 6.5M            | 2M              | 619.3 K  | 2.1 M    |
nia             | 2K             | 408            | 2K              | 25K             | 1.7M           | 476.5K         | 11.3M           | 3.1M            | 1.0 M    | 3.9 M    |
mas             | 15.2K          | 405            | 216.8K          | 17.6K           | 6.2M           | 390.1K         | 42.1M           | 3M              | 927.5 K  | 13.4 M   |
bzj             | 983            | 404            | 33.6K           | 26.4K           | 824.3K         | 565K           | 4.5M            | 2.9M            | 981.2 K  | 1.4 M    |
mkn             | 956            | 402            | 33.1K           | 25.4K           | 584.2K         | 456.9K         | 3.4M            | 2.6M            | 734.8 K  | 1.0 M    |
lhu             | 46K            | 377            | 975K            | 15.7K           | 29.1M          | 441.2K         | 208.6M          | 2.5M            | 623.0 K  | 38.8 M   |
ctu             | 690            | 366            | 35.5K           | 20.6K           | 646.7K         | 352.8K         | 3.6M            | 2M              | 614.9 K  | 1.2 M    |
kg              | 4.7K           | 365            | 85.5K           | 21.7K           | 2.5M           | 406.7K         | 16.6M           | 2.6M            | 905.4 K  | 5.7 M    |
inb             | 387            | 343            | 17.3K           | 17K             | 202.8K         | 197K           | 2M              | 1.9M            | 535.2 K  | 555.6 K  |
guh             | 1.9K           | 331            | 104.9K          | 28.4K           | 1.5M           | 328.4K         | 11.2M           | 3M              | 789.5 K  | 3.5 M    |
rn              | 8.2K           | 323            | 8.2K            | 11.1K           | 4.5M           | 179K           | 33.2M           | 1.3M            | 449.9 K  | 11.8 M   |
bus             | 467            | 322            | 21.4K           | 12.1K           | 418.4K         | 219.2K         | 2.1M            | 1.1M            | 428.8 K  | 830.9 K  |
mfe             | 7.5K           | 320            | 198.8K          | 18.2K           | 4.6M           | 374.8K         | 26.9M           | 2.1M            | 716.4 K  | 10.1 M   |
sda             | 1.6K           | 317            | 43.2K           | 6.2K            | 2.5M           | 218.3K         | 15.8M           | 1.6M            | 529.0 K  | 4.7 M    |
bi              | 71.9K          | 311            | 308.5K          | 13.6K           | 19.4M          | 359.4K         | 132.4M          | 1.9M            | 546.9 K  | 42.6 M   |
cr_Latn         | 19K            | 303            | 170K            | 8.9K            | 19K            | 303            | 81.8K           | 1K              | 590.4 K  | 15.0 M   |
gor             | 1.7K           | 303            | 53.3K           | 6.5K            | 1.4M           | 227.1K         | 9.4M            | 1.7M            | 494.0 K  | 3.1 M    |
jac             | 8.2K           | 303            | 61.6K           | 11.9K           | 1.8M           | 271K           | 15.7M           | 1.7M            | 530.3 K  | 7.3 M    |
chr             | 964            | 301            | 33.8K           | 7.5K            | 629.9K         | 172.3K         | 4.7M            | 1M              | 564.1 K  | 2.1 M    |
mh              | 4.6K           | 296            | 235.1K          | 13K             | 3.6M           | 393.5K         | 24.9M           | 2.2M            | 778.4 K  | 8.4 M    |
mni             | 1.2K           | 290            | 38.1K           | 13.2K           | 841.3K         | 245.5K         | 6.4M            | 1.8M            | 866.6 K  | 3.0 M    |
wal             | 2.6K           | 286            | 128K            | 14K             | 2M             | 203.4K         | 17M             | 1.7M            | 525.7 K  | 5.1 M    |
teo             | 2.8K           | 274            | 131.5K          | 13.7K           | 2.3M           | 221.4K         | 15.3M           | 1.6M            | 564.9 K  | 5.3 M    |
gub             | 31.7K          | 271            | 160.4K          | 25K             | 4.7M           | 286.2K         | 44.7M           | 1.6M            | 431.3 K  | 23.1 M   |
qvi             | 1.2K           | 266            | 48.4K           | 19.3K           | 720.4K         | 248.9K         | 6.5M            | 2.3M            | 641.2 K  | 1.9 M    |
tdx             | 1.7K           | 262            | 26.3K           | 13.2K           | 1M             | 238.5K         | 7M              | 1.6M            | 503.6 K  | 2.1 M    |
rki             | 331            | 251            | 331             | 7.8K            | 119.7K         | 113.7K         | 1.6M            | 1.5M            | 751.3 K  | 781.8 K  |
djk             | 560            | 246            | 30.9K           | 24.4K           | 669.5K         | 455.6K         | 3.7M            | 2.2M            | 644.3 K  | 1.0 M    |
nr              | 10.7K          | 246            | 10.7K           | 11.3K           | 5.3M           | 162.5K         | 49M             | 1.5M            | 519.7 K  | 17.8 M   |
zne             | 1.3K           | 239            | 61.9K           | 21.3K           | 1.4M           | 504.6K         | 8.2M            | 2.8M            | 882.3 K  | 2.8 M    |
izz             | 423            | 237            | 21.7K           | 14.5K           | 382.8K         | 194.5K         | 2.1M            | 1.1M            | 382.2 K  | 789.9 K  |
noa             | 902            | 234            | 902             | 11.5K           | 821.1K         | 243.9K         | 5.2M            | 1.6M            | 534.3 K  | 1.7 M    |
bqc             | 275            | 228            | 9.8K            | 8.2K            | 193K           | 151.7K         | 997K            | 788.4K          | 317.0 K  | 408.1 K  |
srm             | 847            | 227            | 847             | 17.3K           | 1.2M           | 445.3K         | 6.3M            | 2M              | 613.4 K  | 1.7 M    |
niq             | 26.7K          | 226            | 26.7K           | 4.2K            | 9.9M           | 103.4K         | 72.1M           | 716.2K          | 239.1 K  | 20.9 M   |
bas             | 4.2K           | 216            | 105.2K          | 14.9K           | 4.3M           | 362.8K         | 25.7M           | 1.7M            | 600.7 K  | 7.6 M    |
dwr             | 452            | 215            | 22.1K           | 11.1K           | 269.4K         | 139.5K         | 2.2M            | 1.2M            | 375.4 K  | 747.6 K  |
guc             | 537            | 214            | 22.9K           | 12.5K           | 422.4K         | 218.1K         | 3.4M            | 1.8M            | 540.1 K  | 1.1 M    |
jvn             | 1K             | 213            | 36.2K           | 7.8K            | 790.5K         | 185.6K         | 5.3M            | 1.2M            | 357.2 K  | 1.7 M    |
hvn             | 737            | 200            | 33.9K           | 7K              | 779.7K         | 239.4K         | 4.3M            | 1.2M            | 378.5 K  | 1.4 M    |
sxn             | 587            | 197            | 587             | 9.9K            | 494K           | 220.6K         | 3.4M            | 1.5M            | 507.1 K  | 1.2 M    |
koi             | 20.7K          | 196            | 153.9K          | 5K              | 2.2M           | 89.9K          | 17.1M           | 664.5K          | 323.0 K  | 7.1 M    |
alz             | 2.2K           | 195            | 59.3K           | 12.2K           | 1.3M           | 246.9K         | 7.9M            | 1.4M            | 488.1 K  | 2.9 M    |
nyu             | 1.2K           | 195            | 1.2K            | 11K             | 988.7K         | 210.5K         | 7.7M            | 1.6M            | 492.6 K  | 2.2 M    |
bn_Latn         | 98.7K          | 191            | 1.3M            | 12K             | 98.7K          | 191            | 458K            | 730             | 314.7 K  | 81.0 M   |
suz             | 226            | 186            | 226             | 11.3K           | 169.6K         | 140.5K         | 1M              | 855.2K          | 339.5 K  | 429.6 K  |
pau             | 1.7K           | 185            | 1.7K            | 13.1K           | 2M             | 394.6K         | 12.4M           | 2M              | 600.1 K  | 3.2 M    |
nij             | 1K             | 183            | 1K              | 9.2K            | 741.6K         | 186.1K         | 4.7M            | 1.2M            | 389.6 K  | 1.6 M    |
sat_Latn        | 39K            | 183            | 39K             | 5.5K            | 39K            | 183            | 183.8K          | 601             | 276.1 K  | 39.2 M   |
gu_Latn         | 58.2K          | 179            | 688.4K          | 5.4K            | 58.2K          | 179            | 260.8K          | 673             | 241.0 K  | 47.9 M   |
msm             | 520            | 177            | 520             | 8.6K            | 410.8K         | 190.5K         | 2.5M            | 1.1M            | 339.7 K  | 789.8 K  |
maz             | 585            | 170            | 21.3K           | 8.2K            | 452.9K         | 174K           | 2.9M            | 951.7K          | 304.7 K  | 971.4 K  |
qxr             | 2.6K           | 153            | 40.8K           | 6.4K            | 761.5K         | 75.4K          | 6.6M            | 724K            | 186.4 K  | 1.9 M    |
shp             | 874            | 150            | 22.4K           | 3.7K            | 534.1K         | 96.8K          | 3.8M            | 710.4K          | 216.9 K  | 1.2 M    |
hne             | 3K             | 146            | 118.4K          | 4.3K            | 2.3M           | 139.3K         | 12M             | 697K            | 379.3 K  | 6.5 M    |
ktu             | 3.3K           | 144            | 115.5K          | 7.8K            | 3.2M           | 196.9K         | 18.5M           | 1.1M            | 300.1 K  | 5.4 M    |
laj             | 6.5K           | 144            | 61K             | 6.4K            | 2.4M           | 140.1K         | 15.8M           | 730.5K          | 233.5 K  | 4.6 M    |
pis             | 1.1K           | 139            | 62K             | 7.2K            | 1.3M           | 136.8K         | 7.7M            | 764K            | 212.7 K  | 2.2 M    |
mag             | 631            | 138            | 62.6K           | 22.1K           | 2.1M           | 544.2K         | 10.7M           | 2.6M            | 1.4 M    | 5.4 M    |
gbm             | 2.5K           | 137            | 50.8K           | 3.8K            | 1.7M           | 99.7K          | 9.1M            | 499.6K          | 282.4 K  | 4.5 M    |
tzj             | 471            | 136            | 11.1K           | 7.3K            | 299.9K         | 150.8K         | 1.9M            | 884.2K          | 272.0 K  | 663.9 K  |
oj              | 2.5K           | 135            | 2.5K            | 1.6K            | 1.2M           | 35.9K          | 9.6M            | 337.1K          | 117.6 K  | 3.4 M    |
ndc_ZW          | 2.2K           | 132            | 2.2K            | 8.7K            | 2.2K           | 132            | 9.1K            | 523             | 343.1 K  | 2.2 M    |
tks             | 63.7K          | 127            | 63.7K           | 6.8K            | 17.1M          | 41.5K          | 88.9M           | 260.8K          | 39.5 K   | 33.0 M   |
awa             | 5.8K           | 126            | 100.1K          | 8.4K            | 2.2M           | 98.7K          | 11.1M           | 475K            | 226.6 K  | 5.8 M    |
gvl             | 37.9K          | 126            | 213K            | 6.9K            | 21.1M          | 161.1K         | 141M            | 789.2K          | 257.8 K  | 31.7 M   |
knj             | 229            | 126            | 10.1K           | 9.2K            | 202.6K         | 171.8K         | 1.1M            | 855K            | 253.1 K  | 345.4 K  |
spp             | 733            | 123            | 733             | 5.8K            | 902.7K         | 141.8K         | 4.4M            | 682.5K          | 217.8 K  | 1.4 M    |
mqy             | 69.3K          | 119            | 309K            | 2.5K            | 12.1M          | 88.6K          | 78.9M           | 506.5K          | 170.4 K  | 16.3 M   |
tca             | 410            | 117            | 20K             | 7.3K            | 283K           | 121.5K         | 2.3M            | 786K            | 226.2 K  | 781.2 K  |
cce             | 847            | 116            | 23.2K           | 11K             | 539.3K         | 227.2K         | 3.3M            | 1.3M            | 393.8 K  | 1.1 M    |
skr             | 3.8K           | 107            | 279.3K          | 17.1K           | 6.2M           | 324K           | 32.2M           | 1.7M            | 768.5 K  | 15.4 M   |
kmz_Latn        | 24K            | 106            | 361K            | 2.4K            | 24K            | 106            | 108.6K          | 401             | 231.8 K  | 16.7 M   |
dje             | 913            | 100            | 40.2K           | 3.7K            | 816.3K         | 97.5K          | 4.7M            | 480.7K          | 161.2 K  | 1.5 M    |
gof             | 2.8K           | 97             | 33.8K           | 5.5K            | 703K           | 68.8K          | 5.5M            | 506K            | 159.1 K  | 1.7 M    |
agr             | 465            | 93             | 16.1K           | 3.6K            | 295.4K         | 67.2K          | 2.3M            | 554.5K          | 177.0 K  | 760.1 K  |
qvz             | 534            | 88             | 6.8K            | 3.5K            | 145.5K         | 50.5K          | 1.2M            | 438.3K          | 124.2 K  | 382.7 K  |
adh             | 2.6K           | 87             | 107.2K          | 1K              | 2.4M           | 42.1K          | 14.5M           | 254.9K          | 84.6 K   | 5.0 M    |
quf             | 522            | 86             | 8.4K            | 5.2K            | 155.7K         | 61.8K          | 1.5M            | 609K            | 173.7 K  | 542.8 K  |
kjg             | 113            | 84             | 3K              | 2.9K            | 67.6K          | 67K            | 408.5K          | 399K            | 159.2 K  | 167.7 K  |
tsc             | 12.6K          | 82             | 12.6K           | 4K              | 3.5M           | 93.1K          | 23.4M           | 521.3K          | 161.9 K  | 7.0 M    |
ber             | 2.7K           | 79             | 12.6K           | 1.2K            | 1.1M           | 46.4K          | 6.4M            | 265.9K          | 141.5 K  | 3.0 M    |
ify             | 611            | 79             | 19.8K           | 2.8K            | 422.7K         | 56.2K          | 2.6M            | 334K            | 109.5 K  | 913.1 K  |
cbk             | 10.1K          | 78             | 43.8K           | 2K              | 1.7M           | 64.3K          | 10.3M           | 339.3K          | 93.4 K   | 3.4 M    |
quy             | 588            | 78             | 28.1K           | 2.7K            | 423.3K         | 37.3K          | 4.5M            | 368.2K          | 114.5 K  | 1.2 M    |
ahk             | 244            | 77             | 6.2K            | 4.1K            | 264K           | 124.8K         | 1.3M            | 715.5K          | 182.8 K  | 359.7 K  |
cac             | 212            | 77             | 3.4K            | 1.8K            | 125.7K         | 54.1K          | 978.7K          | 319.8K          | 95.8 K   | 280.3 K  |
akb             | 1K             | 71             | 21.3K           | 408             | 870.9K         | 54.5K          | 5.2M            | 337.8K          | 93.7 K   | 1.6 M    |
nut             | 29K            | 67             | 29K             | 1.5K            | 4.8M           | 39.8K          | 23.5M           | 184.1K          | 36.4 K   | 8.3 M    |
ffm             | 1.8K           | 65             | 30.1K           | 2K              | 745.6K         | 39.1K          | 4.6M            | 236.1K          | 83.8 K   | 1.8 M    |
taj             | 146            | 65             | 21.6K           | 14.3K           | 309.7K         | 203K           | 2.3M            | 1.4M            | 503.0 K  | 872.7 K  |
ms_Arab         | 698            | 63             | 698             | 320             | 698            | 63             | 2.9K            | 239             | 64.7 K   | 1016.0 K |
brx             | 322            | 62             | 5.3K            | 2.4K            | 144.2K         | 41K            | 1.1M            | 304.4K          | 146.6 K  | 515.7 K  |
ann             | 464            | 56             | 5K              | 1.6K            | 116.4K         | 35.9K          | 760.9K          | 215.1K          | 74.9 K   | 295.2 K  |
qup             | 169            | 53             | 4.3K            | 2.5K            | 77.5K          | 31.3K          | 763.8K          | 297.8K          | 74.7 K   | 207.3 K  |
ms_Arab_BN      | 2.6K           | 46             | 2.6K            | 374             | 2.6K           | 46             | 10.5K           | 171             | 50.0 K   | 5.1 M    |
miq             | 236            | 45             | 6.4K            | 3.5K            | 183.7K         | 80.2K          | 1.2M            | 485.6K          | 157.6 K  | 384.1 K  |
msb             | 811            | 41             | 811             | 1K              | 705.9K         | 28.8K          | 4.4M            | 167.5K          | 53.3 K   | 1.7 M    |
bim             | 410            | 40             | 31.1K           | 6.3K            | 669.8K         | 167.4K         | 3.2M            | 793.4K          | 252.7 K  | 1.1 M    |
raj             | 1.8K           | 40             | 1.8K            | 5.7K            | 1.3M           | 81.1K          | 7.1M            | 405K            | 226.2 K  | 3.9 M    |
kwi             | 382            | 37             | 16.9K           | 2.2K            | 253.8K         | 23.4K          | 1.8M            | 172.8K          | 47.6 K   | 536.2 K  |
tll             | 200            | 37             | 200             | 2.7K            | 304.2K         | 62.2K          | 2.2M            | 409.8K          | 132.3 K  | 664.5 K  |
trp             | 12.8K          | 36             | 12.8K           | 1.7K            | 4.1M           | 39K            | 29.9M           | 257.3K          | 87.5 K   | 10.2 M   |
smt             | 1.4K           | 34             | 1.4K            | 703             | 1M             | 36.5K          | 6.8M            | 245.4K          | 87.9 K   | 2.5 M    |
mrw             | 11.3K          | 29             | 11.3K           | 1K              | 4.2M           | 45.7K          | 27.8M           | 257.2K          | 81.3 K   | 8.8 M    |
dln             | 236            | 28             | 5.2K            | 969             | 150.8K         | 21.5K          | 860.5K          | 118.3K          | 36.8 K   | 280.3 K  |
qvc             | 3.4K           | 27             | 14.6K           | 2.2K            | 495.7K         | 25.7K          | 5M              | 233.7K          | 65.3 K   | 2.6 M    |
doi             | 1.7K           | 26             | 21.8K           | 975             | 568.7K         | 25.5K          | 3.2M            | 135.3K          | 66.7 K   | 1.6 M    |
ff              | 13.6K          | 26             | 150K            | 5K              | 3.4M           | 46.5K          | 22.8M           | 277.6K          | 78.8 K   | 8.5 M    |


## Citation Information

~~~
@misc{kudugunta2023madlad400,
      title={MADLAD-400: A Multilingual And Document-Level Large Audited Dataset}, 
      author={Sneha Kudugunta and Isaac Caswell and Biao Zhang and Xavier Garcia and Christopher A. Choquette-Choo and Katherine Lee and Derrick Xin and Aditya Kusupati and Romi Stella and Ankur Bapna and Orhan Firat},
      year={2023},
      eprint={2309.04662},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
~~~