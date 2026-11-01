---
license: mit
task_categories:
- text-classification
- text-generation
- feature-extraction
language:
- en
- ja
- zh
- ko
tags:
- art
- anime
- not-for-all-audiences
size_categories:
- 100K<n<1M
annotations_creators:
- no-annotation
source_datasets:
- danbooru
---

# Danbooru Full Wiki Dataset

This is the full wiki dataset of [danbooru.donmai.us](https://danbooru.donmai.us/), containing the wiki pages/tags/tag aliases/tag implications. You can train something like LLMs on this dataset

# Information

## Wiki Pages

There are 189161 wiki items in total. Last updated at `2024-06-16 02:31:27 UTC`.

These are the information of recent 50 wiki items:

|     id | title                                    | other_names                                            |   text_length | is_locked   | is_deleted   |   created_at |   updated_at |
|-------:|:-----------------------------------------|:-------------------------------------------------------|--------------:|:------------|:-------------|-------------:|-------------:|
| 196503 | li_yuting_(female)                       | ["离雨婷", "头七女主"]                                        |             0 | False       | False        |  1.7185e+09  |  1.7185e+09  |
| 196502 | raindrop_cake                            | ["水信玄餅"]                                               |           139 | False       | False        |  1.7185e+09  |  1.7185e+09  |
| 196501 | kimaris_(megido72)                       | ["キマリス(メギド72)"]                                        |             0 | False       | False        |  1.7185e+09  |  1.7185e+09  |
| 196500 | ophelia_valentine                        | ["ValentinesBounty", "BootyButtbounty"]                |           238 | False       | False        |  1.7185e+09  |  1.7185e+09  |
| 196499 | senniursa                                | ["senniART"]                                           |           249 | False       | False        |  1.7185e+09  |  1.7185e+09  |
| 196498 | barakiel_(megido72)                      | ["バラキエル(メギド72)"]                                       |             0 | False       | False        |  1.7185e+09  |  1.7185e+09  |
| 196497 | iphone_xr                                | []                                                     |            89 | False       | False        |  1.7185e+09  |  1.7185e+09  |
| 196496 | mikan_daifuku                            | []                                                     |           106 | False       | False        |  1.7185e+09  |  1.7185e+09  |
| 196495 | sky_above_me_(vtuber)                    | ["artaboveme"]                                         |           201 | False       | False        |  1.7185e+09  |  1.7185e+09  |
| 196494 | eldritch_loreteller_(idolmaster)         | ["エルドリッチ・ロアテラー"]                                       |             0 | False       | False        |  1.7185e+09  |  1.7185e+09  |
| 196493 | sesame_ball                              | ["麻糰", "麻圆", "珍袋", "碌䭔", "ごま団子", "중국식", "참깨경단", "煎丸欸"] |           506 | False       | False        |  1.7185e+09  |  1.7185e+09  |
| 196492 | bury_pink_gril                           | ["bury_pink_gril", "bury_pink_girl"]                   |           430 | False       | False        |  1.71849e+09 |  1.71849e+09 |
| 196491 | socks_agency                             | []                                                     |           238 | False       | False        |  1.71849e+09 |  1.7185e+09  |
| 196490 | wealth_symbol                            | ["禄"]                                                  |            83 | False       | False        |  1.71849e+09 |  1.71849e+09 |
| 196489 | semi-transparent                         | []                                                     |           265 | False       | False        |  1.71849e+09 |  1.71849e+09 |
| 196488 | olivia_monroe                            | ["OliMart"]                                            |           160 | False       | False        |  1.71849e+09 |  1.71849e+09 |
| 196487 | abigail_dovely                           | ["abiart"]                                             |           161 | False       | False        |  1.71849e+09 |  1.71849e+09 |
| 196486 | princession_orchestra                    | ["プリンセッション・オーケストラ"]                                    |           525 | False       | False        |  1.71849e+09 |  1.71849e+09 |
| 196485 | bible_verse                              | []                                                     |            89 | False       | False        |  1.71849e+09 |  1.71849e+09 |
| 196484 | sargatanas_(megido72)                    | ["サルガタナス(メギド72)"]                                      |             0 | False       | False        |  1.71849e+09 |  1.71849e+09 |
| 196483 | symbol_freckles                          | []                                                     |           123 | False       | False        |  1.71849e+09 |  1.71849e+09 |
| 196482 | butterfly_facial_mark                    | []                                                     |           115 | False       | False        |  1.71849e+09 |  1.71849e+09 |
| 196481 | flower_facial_mark                       | []                                                     |           199 | False       | False        |  1.71849e+09 |  1.71849e+09 |
| 196480 | himeri_alice                             | ["姫莉アリス"]                                              |           104 | False       | False        |  1.71849e+09 |  1.71849e+09 |
| 196479 | lunacy_(limbus_company)                  | []                                                     |            89 | False       | False        |  1.71849e+09 |  1.71849e+09 |
| 196478 | clover_facial_mark                       | []                                                     |           154 | False       | False        |  1.71849e+09 |  1.71849e+09 |
| 196477 | table_turf                               | ["Tableturf", "ナワバトラー"]                                |           334 | False       | False        |  1.71849e+09 |  1.71849e+09 |
| 196476 | logos'_mother_(arknights)                | ["lamalien_(arknights)"]                               |             0 | False       | False        |  1.71849e+09 |  1.71849e+09 |
| 196475 | club_facial_mark                         | []                                                     |           126 | False       | False        |  1.71849e+09 |  1.71849e+09 |
| 196474 | ibuki_(senran_kagura)                    | ["伊吹(閃乱カグラ)"]                                          |             0 | False       | False        |  1.71849e+09 |  1.71849e+09 |
| 196473 | eyeshadow_under_eye                      | []                                                     |           185 | False       | False        |  1.71848e+09 |  1.71848e+09 |
| 196472 | mark_under_both_eyes                     | []                                                     |           435 | False       | False        |  1.71848e+09 |  1.71849e+09 |
| 196471 | circle_facial_mark                       | []                                                     |            37 | False       | False        |  1.71848e+09 |  1.71848e+09 |
| 196470 | melchom_(megido72)                       | ["メルコム(メギド72)"]                                        |             0 | False       | False        |  1.71848e+09 |  1.71848e+09 |
| 196469 | blanked_123                              | []                                                     |             0 | False       | True         |  1.71848e+09 |  1.71848e+09 |
| 196468 | diamond_facial_mark                      | []                                                     |           122 | False       | False        |  1.71848e+09 |  1.71848e+09 |
| 196467 | princess_sweetfloss_(catch!_teenieping)  | []                                                     |            93 | False       | False        |  1.71848e+09 |  1.71848e+09 |
| 196466 | romi_(catch!_teenieping)                 | []                                                     |           104 | False       | False        |  1.71848e+09 |  1.71848e+09 |
| 196465 | catch!_teenieping                        | []                                                     |           134 | False       | False        |  1.71848e+09 |  1.71848e+09 |
| 196464 | liu_qingcheng                            | ["刘箐橙", "刘青城"]                                         |             0 | False       | False        |  1.71848e+09 |  1.71848e+09 |
| 196463 | li_yuting_(male)                         | ["离宇亭", "头七男主"]                                        |             0 | False       | False        |  1.71848e+09 |  1.7185e+09  |
| 196462 | nai_he                                   | ["佴和"]                                                 |             0 | False       | False        |  1.71848e+09 |  1.71848e+09 |
| 196461 | mo_chengwei                              | ["莫承威"]                                                |             0 | False       | False        |  1.71848e+09 |  1.71848e+09 |
| 196460 | fu_shun_(touqi_guaitan)                  | ["符顺"]                                                 |             0 | False       | False        |  1.71848e+09 |  1.71848e+09 |
| 196459 | touqi_guaitan                            | ["头七怪谈", "头七"]                                         |             0 | False       | False        |  1.71848e+09 |  1.71848e+09 |
| 196458 | huai_yunqing                             | ["怀蕴清"]                                                |             0 | False       | False        |  1.71848e+09 |  1.71848e+09 |
| 196457 | kamijou_no_touma                         | []                                                     |           165 | False       | False        |  1.71848e+09 |  1.71848e+09 |
| 196456 | enyo_(summer)_(granblue_fantasy)         | []                                                     |            47 | False       | False        |  1.71848e+09 |  1.71848e+09 |
| 196455 | cucouroux_(halloween)_(granblue_fantasy) | []                                                     |            54 | False       | False        |  1.71848e+09 |  1.71848e+09 |
| 196454 | charlotta_(summer)_(granblue_fantasy)    | []                                                     |            52 | False       | False        |  1.71848e+09 |  1.71848e+09 |

# Tags

There are 1322381 tags in total.

These are the information of hottest 50 tags:

|      id | name               |   category |   post_count | is_deprecated   |   created_at |   updated_at |
|--------:|:-------------------|-----------:|-------------:|:----------------|-------------:|-------------:|
|  470575 | 1girl              |          0 |      5442850 | False           |  1.36202e+09 |  1.57741e+09 |
|    1566 | highres            |          5 |      4548085 | False           |  1.36202e+09 |  1.56713e+09 |
|  212816 | solo               |          0 |      4527019 | False           |  1.36207e+09 |  1.57741e+09 |
|   13197 | long_hair          |          0 |      3904080 | False           |  1.36203e+09 |  1.56687e+09 |
|    8601 | breasts            |          0 |      3088747 | False           |  1.36203e+09 |  1.56694e+09 |
|  542523 | commentary_request |          5 |      3042756 | False           |  1.36205e+09 |  1.56622e+09 |
|  469576 | looking_at_viewer  |          0 |      2930500 | False           |  1.36203e+09 |  1.56512e+09 |
|    3389 | blush              |          0 |      2663640 | False           |  1.36207e+09 |  1.57741e+09 |
|    1815 | smile              |          0 |      2550582 | False           |  1.36207e+09 |  1.56687e+09 |
|   11906 | open_mouth         |          0 |      2101732 | False           |  1.36202e+09 |  1.56673e+09 |
|   15080 | short_hair         |          0 |      2033770 | False           |  1.36207e+09 |  1.57741e+09 |
|   10959 | blue_eyes          |          0 |      1590978 | False           |  1.36207e+09 |  1.57741e+09 |
|  412368 | simple_background  |          0 |      1566256 | False           |  1.36204e+09 |  1.56563e+09 |
|   12590 | shirt              |          0 |      1540208 | False           |  1.36205e+09 |  1.56586e+09 |
|   11716 | absurdres          |          5 |      1498320 | False           |  1.36207e+09 |  1.56551e+09 |
|  403247 | large_breasts      |          0 |      1421609 | False           |  1.36207e+09 |  1.57741e+09 |
|     429 | skirt              |          0 |      1415895 | False           |  1.36207e+09 |  1.56679e+09 |
|   87788 | blonde_hair        |          0 |      1394192 | False           |  1.36207e+09 |  1.56679e+09 |
|  566835 | multiple_girls     |          0 |      1392012 | False           |  1.36203e+09 |  1.57741e+09 |
|   16867 | brown_hair         |          0 |      1347917 | False           |  1.36207e+09 |  1.56572e+09 |
|   13200 | black_hair         |          0 |      1325367 | False           |  1.36207e+09 |  1.56584e+09 |
|  383159 | long_sleeves       |          0 |      1321753 | False           |  1.36201e+09 |  1.56742e+09 |
|  515193 | white_background   |          0 |      1283945 | False           |  1.36209e+09 |  1.56611e+09 |
|  380350 | hair_ornament      |          0 |      1262621 | False           |  1.36203e+09 |  1.57741e+09 |
|  540830 | 1boy               |          0 |      1225534 | False           |  1.36207e+09 |  1.56696e+09 |
|    5735 | gloves             |          0 |      1202364 | False           |  1.36207e+09 |  1.56515e+09 |
|    8526 | red_eyes           |          0 |      1151650 | False           |  1.36207e+09 |  1.56568e+09 |
|  375387 | holding            |          0 |      1141633 | False           |  1.36202e+09 |  1.56623e+09 |
|    2241 | dress              |          0 |      1135921 | False           |  1.36208e+09 |  1.56607e+09 |
|  389885 | commentary         |          5 |      1122650 | False           |  1.36209e+09 |  1.56734e+09 |
|  527167 | bad_id             |          5 |      1114724 | False           |  1.36207e+09 |  1.56566e+09 |
|    2373 | hat                |          0 |      1096805 | False           |  1.36203e+09 |  1.56574e+09 |
|    1882 | thighhighs         |          0 |      1083459 | False           |  1.36202e+09 |  1.57741e+09 |
|      18 | original           |          3 |      1058766 | False           |  1.36207e+09 |  1.56655e+09 |
|    4563 | bow                |          0 |      1054980 | False           |  1.36208e+09 |  1.56545e+09 |
|    9294 | navel              |          0 |      1038169 | False           |  1.36207e+09 |  1.56572e+09 |
|    6126 | animal_ears        |          0 |      1032626 | False           |  1.36207e+09 |  1.57741e+09 |
|  658573 | hair_between_eyes  |          0 |      1008516 | False           |  1.36206e+09 |  1.56733e+09 |
|  464575 | ribbon             |          0 |       993079 | False           |  1.36207e+09 |  1.56579e+09 |
|  572080 | closed_mouth       |          0 |       981958 | False           |  1.36204e+09 |  1.56721e+09 |
|    1821 | 2girls             |          0 |       920488 | False           |  1.36207e+09 |  1.57741e+09 |
|   16613 | jewelry            |          0 |       904825 | False           |  1.36209e+09 |  1.57741e+09 |
|    4607 | cleavage           |          0 |       904460 | False           |  1.36203e+09 |  1.56593e+09 |
| 1400438 | bad_pixiv_id       |          5 |       878823 | False           |  1.48364e+09 |  1.56687e+09 |
|  376054 | bare_shoulders     |          0 |       874579 | False           |  1.36208e+09 |  1.56623e+09 |
|      29 | touhou             |          3 |       868163 | False           |  1.36202e+09 |  1.5669e+09  |
|  417660 | very_long_hair     |          0 |       843417 | False           |  1.36208e+09 |  1.56664e+09 |
|   12289 | sitting            |          0 |       839844 | False           |  1.36208e+09 |  1.57741e+09 |
|    1709 | twintails          |          0 |       821274 | False           |  1.36207e+09 |  1.57741e+09 |
|  667868 | medium_breasts     |          0 |       814948 | False           |  1.36184e+09 |  1.57741e+09 |

# Tag Aliases

There are 38454 tag aliases in total.

These are the information of recent 50 tag aliases:

|     id | antecedent_name          | consequent_name             | status   | reason   |   created_at |   updated_at |
|-------:|:-------------------------|:----------------------------|:---------|:---------|-------------:|-------------:|
| 121130 | ame_0611                 | hanaochi_raku               | active   |          |  1.71849e+09 |  1.71849e+09 |
| 121127 | komugikokonko            | komugirakko                 | active   |          |  1.71848e+09 |  1.71848e+09 |
| 121125 | rokuhashi_8              | moko_(gloriaaaaaa)          | active   |          |  1.71848e+09 |  1.71848e+09 |
| 121124 | ichinee924               | moko_(gloriaaaaaa)          | active   |          |  1.71848e+09 |  1.71848e+09 |
| 121118 | ghost_finches            | dead_finch                  | active   |          |  1.71848e+09 |  1.71848e+09 |
| 121115 | en_3_(pixiv103361645)    | ogye_01                     | active   |          |  1.71848e+09 |  1.71848e+09 |
| 121108 | dtasu18                  | drunktatsu                  | active   |          |  1.71845e+09 |  1.71845e+09 |
| 121106 | kou_(alt_kou)            | alterinku                   | active   |          |  1.71845e+09 |  1.71845e+09 |
| 121102 | valtaur_tw               | valtaur                     | active   |          |  1.71844e+09 |  1.71844e+09 |
| 121099 | atat250                  | ketsu_juuji_killer_(kejuki) | active   |          |  1.71844e+09 |  1.71844e+09 |
| 121096 | lyna_deathshaow          | lyna-zf                     | active   |          |  1.71844e+09 |  1.71844e+09 |
| 121093 | 5dogs                    | lyna-zf                     | active   |          |  1.71844e+09 |  1.71844e+09 |
| 121088 | xmz41107923              | mokkorisha                  | active   |          |  1.71843e+09 |  1.71843e+09 |
| 121083 | hvar127                  | sn_kaze                     | active   |          |  1.71843e+09 |  1.71843e+09 |
| 121077 | you_sou_(youtho1226)     | youtho                      | active   |          |  1.71841e+09 |  1.71841e+09 |
| 121076 | youtho_(cfztudv8qzpfhrz) | youtho                      | active   |          |  1.71841e+09 |  1.71841e+09 |
| 121071 | you_sou                  | youtho                      | active   |          |  1.71841e+09 |  1.71841e+09 |
| 121068 | karasumaru128k           | karasumaru_(128k)           | active   |          |  1.71841e+09 |  1.71841e+09 |
| 121065 | youtho                   | you_sou                     | deleted  |          |  1.71841e+09 |  1.71841e+09 |
| 121061 | user_vsvz2754            | orange_ardy1203             | active   |          |  1.7184e+09  |  1.7184e+09  |
| 121047 | ultraspank               | hentyler                    | active   |          |  1.7184e+09  |  1.7184e+09  |
| 121043 | taiyaki_(astre)          | yotsuba_haru                | active   |          |  1.71839e+09 |  1.71839e+09 |
| 121041 | gailil0                  | sumooo_(ga_ilil)            | active   |          |  1.71839e+09 |  1.71839e+09 |
| 121036 | anna_kurenotani          | beninoya_anna               | active   |          |  1.71839e+09 |  1.71839e+09 |
| 121035 | haruo_(msax2545)         | haruo_(haruooimo)           | active   |          |  1.71839e+09 |  1.71839e+09 |
| 121034 | yanfeikawaii             | haruo_(haruooimo)           | active   |          |  1.71839e+09 |  1.71839e+09 |
| 121033 | mio_desuwa               | mio_kurapin                 | active   |          |  1.71839e+09 |  1.71839e+09 |
| 121032 | siolink                  | amami_shiwo                 | active   |          |  1.71839e+09 |  1.71839e+09 |
| 121031 | g.tails                  | radical_bullet              | active   |          |  1.71839e+09 |  1.71839e+09 |
| 121030 | kenno9mp40               | kenno_(kenno9mp40)          | active   |          |  1.71839e+09 |  1.71839e+09 |
| 121029 | yanagui                  | yanagui_yugi                | active   |          |  1.71839e+09 |  1.71839e+09 |
| 121028 | user_ehgd8577            | xin_sanmu                   | active   |          |  1.71839e+09 |  1.71839e+09 |
| 121008 | zikau                    | zikaualpha                  | active   |          |  1.71839e+09 |  1.71839e+09 |
| 121005 | jii3                     | jiisuri_chan                | active   |          |  1.71838e+09 |  1.71838e+09 |
| 121003 | pi_g_r                   | pino_(pppnonon)             | active   |          |  1.71838e+09 |  1.71838e+09 |
| 121002 | t705gp                   | gomahichi                   | active   |          |  1.71838e+09 |  1.71838e+09 |
| 120999 | coffea80903              | coffea_(ancoffea)           | active   |          |  1.71838e+09 |  1.71838e+09 |
| 120993 | chariot.f                | oninaart                    | active   |          |  1.71838e+09 |  1.71838e+09 |
| 120990 | umulpagi                 | sunaringo                   | active   |          |  1.71837e+09 |  1.71837e+09 |
| 120985 | zmjjkk00                 | sambel_kacang1              | active   |          |  1.71836e+09 |  1.71836e+09 |
| 120982 | rokitokkii               | tomii_(gegofish)            | active   |          |  1.71836e+09 |  1.71836e+09 |
| 120974 | hijirisawa               | hijirin_dere                | active   |          |  1.71835e+09 |  1.71835e+09 |
| 120971 | fukefu                   | fu_kefu                     | retired  |          |  1.71835e+09 |  1.7185e+09  |
| 120964 | lunarlunatic             | lunarmimi                   | active   |          |  1.71834e+09 |  1.71834e+09 |
| 120962 | lewdefy                  | lewd_nessie                 | active   |          |  1.71834e+09 |  1.71834e+09 |
| 120956 | vexo-r                   | ourobot                     | active   |          |  1.71833e+09 |  1.71833e+09 |
| 120953 | akumekkio                | acmecchio                   | active   |          |  1.71833e+09 |  1.71833e+09 |
| 120940 | hua3928076               | zhrc                        | active   |          |  1.71832e+09 |  1.71832e+09 |
| 120936 | ning_re_huahe_erhao_ji   | ningre_huahe                | active   |          |  1.71831e+09 |  1.71831e+09 |
| 120931 | fei_qiu_da_ye            | lao_xi                      | active   |          |  1.7183e+09  |  1.7183e+09  |

# Tag Implications

There are 24569 tag implications in total.

These are the information of recent 50 tag implications:

|     id | antecedent_name                                       | consequent_name               | status   | reason   |   created_at |   updated_at |
|-------:|:------------------------------------------------------|:------------------------------|:---------|:---------|-------------:|-------------:|
| 101281 | lyoo_(gajyago)                                        | banned_artist                 | active   |          |  1.71827e+09 |  1.71827e+09 |
| 101280 | bear_position                                         | all_fours                     | active   |          |  1.71827e+09 |  1.71827e+09 |
| 101277 | musashi_(purest_wisteria)_(azur_lane)                 | musashi_(azur_lane)           | active   |          |  1.71827e+09 |  1.71827e+09 |
| 101276 | eldridge_(afternoon_worship_in_the_woods)_(azur_lane) | eldridge_(azur_lane)          | active   |          |  1.71827e+09 |  1.71827e+09 |
| 101275 | hai_tien_(luan-feng's_everlasting_duet)_(azur_lane)   | hai_tien_(azur_lane)          | active   |          |  1.71827e+09 |  1.71827e+09 |
| 101274 | lung_wu_(invitation_to_jade_seas)_(azur_lane)         | lung_wu_(azur_lane)           | active   |          |  1.71827e+09 |  1.71827e+09 |
| 101269 | elysia_(herrscher_of_human:_ego)_(honkai_impact)      | elysia_(honkai_impact)        | active   |          |  1.71827e+09 |  1.71827e+09 |
| 101268 | holding_tripod                                        | holding                       | active   |          |  1.71826e+09 |  1.71826e+09 |
| 101267 | holding_tripod                                        | tripod                        | active   |          |  1.71826e+09 |  1.71826e+09 |
| 101264 | soul_hackers_2                                        | devil_summoner_(series)       | active   |          |  1.71826e+09 |  1.71826e+09 |
| 101263 | devil_summoner_2:_raidou_kuzunoha_vs_king_abaddon     | devil_summoner_(series)       | active   |          |  1.71826e+09 |  1.71826e+09 |
| 101262 | devil_summoner:_raidou_kuzunoha_vs_the_soulless_army  | devil_summoner_(series)       | active   |          |  1.71826e+09 |  1.71826e+09 |
| 101261 | devil_summoner:_soul_hackers                          | devil_summoner_(series)       | active   |          |  1.71826e+09 |  1.71826e+09 |
| 101208 | gilgamesh_(immoral_biker_jacket)_(fate)               | gilgamesh_(fate)              | active   |          |  1.71823e+09 |  1.71823e+09 |
| 101206 | wadanohara_(red_sea)                                  | wadanohara                    | active   |          |  1.71823e+09 |  1.71823e+09 |
| 101205 | wadanohara_(blue_sea)                                 | wadanohara                    | active   |          |  1.71823e+09 |  1.71823e+09 |
| 101202 | spine_eren                                            | eren_yeager                   | active   |          |  1.71823e+09 |  1.71823e+09 |
| 101200 | devil_summoner_(game)                                 | devil_summoner_(series)       | active   |          |  1.71823e+09 |  1.71823e+09 |
| 101194 | airani_iofifteen_(6th_costume)                        | airani_iofifteen              | active   |          |  1.71823e+09 |  1.71823e+09 |
| 101192 | shining_nikki                                         | nikki_(series)                | active   |          |  1.71823e+09 |  1.71823e+09 |
| 101191 | miracle_nikki                                         | nikki_(series)                | active   |          |  1.71823e+09 |  1.71823e+09 |
| 101190 | nikki_up2u2:_world_traveller                          | nikki_(series)                | active   |          |  1.71823e+09 |  1.71823e+09 |
| 101186 | doom:_the_dark_ages                                   | doom_(series)                 | active   |          |  1.71823e+09 |  1.71823e+09 |
| 101175 | firefly_(ar-26710)_(honkai:_star_rail)                | firefly_(honkai:_star_rail)   | active   |          |  1.71821e+09 |  1.71821e+09 |
| 101173 | march_7th_(hunt)_(honkai:_star_rail)                  | march_7th_(honkai:_star_rail) | active   |          |  1.71821e+09 |  1.71821e+09 |
| 101172 | march_7th_(preservation)_(honkai:_star_rail)          | march_7th_(honkai:_star_rail) | active   |          |  1.71821e+09 |  1.71821e+09 |
| 101169 | yanqing_(star_rail_live_2024)_(honkai:_star_rail)     | yanqing_(honkai:_star_rail)   | active   |          |  1.71821e+09 |  1.71821e+09 |
| 101168 | argenti_(star_rail_live_2024)_(honkai:_star_rail)     | argenti_(honkai:_star_rail)   | active   |          |  1.71821e+09 |  1.71821e+09 |
| 101167 | kafka_(star_rail_live_2024)_(honkai:_star_rail)       | kafka_(honkai:_star_rail)     | active   |          |  1.71821e+09 |  1.71821e+09 |
| 101166 | jingliu_(star_rail_live_2024)_(honkai:_star_rail)     | jingliu_(honkai:_star_rail)   | active   |          |  1.71821e+09 |  1.71821e+09 |
| 101161 | holding_lead_pipe                                     | lead_pipe                     | active   |          |  1.71821e+09 |  1.71821e+09 |
| 101160 | holding_lead_pipe                                     | holding                       | active   |          |  1.71821e+09 |  1.71821e+09 |
| 101157 | shishiro_botan_(5th_costume)                          | shishiro_botan                | active   |          |  1.71821e+09 |  1.71821e+09 |
| 101156 | shiranui_flare_(5th_costume)                          | shiranui_flare                | active   |          |  1.71821e+09 |  1.71821e+09 |
| 101149 | meica_(vtuber)_(1st_costume)                          | meica_(vtuber)                | active   |          |  1.7182e+09  |  1.7182e+09  |
| 101148 | meica_(vtuber)_(old_design)                           | meica_(vtuber)                | active   |          |  1.7182e+09  |  1.7182e+09  |
| 101147 | yuzuki_choco_(7th_costume)                            | yuzuki_choco                  | active   |          |  1.7182e+09  |  1.7182e+09  |
| 101143 | takanashi_kiara_(7th_costume)                         | takanashi_kiara               | active   |          |  1.7182e+09  |  1.7182e+09  |
| 101141 | hoshimachi_suisei_(casual)                            | hoshimachi_suisei             | active   |          |  1.7182e+09  |  1.7182e+09  |
| 101140 | aizawa_ema_(3rd_costume)                              | aizawa_ema                    | active   |          |  1.7182e+09  |  1.7182e+09  |
| 101139 | aizawa_ema_(2nd_costume)                              | aizawa_ema                    | active   |          |  1.7182e+09  |  1.7182e+09  |
| 101138 | aizawa_ema_(1st_costume)                              | aizawa_ema                    | active   |          |  1.7182e+09  |  1.7182e+09  |
| 101137 | hanabusa_lisa_(4th_costume)                           | hanabusa_lisa                 | active   |          |  1.7182e+09  |  1.7182e+09  |
| 101136 | hanabusa_lisa_(3rd_costume)                           | hanabusa_lisa                 | active   |          |  1.7182e+09  |  1.7182e+09  |
| 101135 | hanabusa_lisa_(2nd_costume)                           | hanabusa_lisa                 | active   |          |  1.7182e+09  |  1.7182e+09  |
| 101134 | hanabusa_lisa_(1st_costume)                           | hanabusa_lisa                 | active   |          |  1.7182e+09  |  1.7182e+09  |
| 101133 | ichinose_uruha_(6th_costume)                          | ichinose_uruha                | active   |          |  1.7182e+09  |  1.7182e+09  |
| 101132 | ichinose_uruha_(5th_costume)                          | ichinose_uruha                | active   |          |  1.7182e+09  |  1.7182e+09  |
| 101131 | ichinose_uruha_(4th_costume)                          | ichinose_uruha                | active   |          |  1.7182e+09  |  1.7182e+09  |
| 101130 | ichinose_uruha_(3rd_costume)                          | ichinose_uruha                | active   |          |  1.7182e+09  |  1.7182e+09  |

