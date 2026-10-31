---
license:
- cc-by-sa-4.0
- gfdl
language:
- ar
- de
- en
- es
- fr
- it
- ja
- ko
- pt
- ru
- zh
dataset_info:
- config_name: arwiki-20250901-v1.0.0
  features:
  - name: id
    dtype: string
  - name: lang
    dtype: string
  - name: page_id
    dtype: int64
  - name: revision_id
    dtype: int64
  - name: page_type
    dtype: string
  - name: title
    dtype: string
  - name: wikidata_qid
    dtype: string
  - name: paragraph_texts
    list: string
  - name: paragraph_sections
    list: string
  - name: paragraph_wikilinks
    list:
      list:
      - name: lang
        dtype: string
      - name: title
        dtype: string
      - name: text
        dtype: string
      - name: start
        dtype: int64
      - name: end
        dtype: int64
  - name: paragraph_html_tags
    list: string
  - name: linked_articles
    list: string
  - name: categories
    list: string
  - name: templates
    list: string
  - name: num_inlinks
    dtype: int64
  - name: redirects
    list: string
  splits:
  - name: train
    num_bytes: 7009191432
    num_examples: 2475043
  download_size: 2386458150
  dataset_size: 7009191432
- config_name: arwiki-20250901-v1.1.0
  features:
  - name: id
    dtype: string
  - name: lang
    dtype: string
  - name: page_id
    dtype: int64
  - name: revision_id
    dtype: int64
  - name: page_type
    dtype: string
  - name: title
    dtype: string
  - name: wikidata_qid
    dtype: string
  - name: paragraph_texts
    list: string
  - name: paragraph_sections
    list: string
  - name: paragraph_wikilinks
    list:
      list:
      - name: lang
        dtype: string
      - name: title
        dtype: string
      - name: text
        dtype: string
      - name: start
        dtype: int64
      - name: end
        dtype: int64
  - name: paragraph_html_tags
    list: string
  - name: linked_articles
    list: string
  - name: categories
    list: string
  - name: templates
    list: string
  - name: num_inlinks
    dtype: int64
  - name: redirects
    list: string
  splits:
  - name: train
    num_bytes: 7009192411
    num_examples: 2475043
  download_size: 2358430829
  dataset_size: 7009192411
- config_name: arwiki-20251202-v1.1.0
  features:
  - name: id
    dtype: string
  - name: lang
    dtype: string
  - name: page_id
    dtype: int64
  - name: revision_id
    dtype: int64
  - name: page_type
    dtype: string
  - name: title
    dtype: string
  - name: wikidata_qid
    dtype: string
  - name: paragraph_texts
    list: string
  - name: paragraph_sections
    list: string
  - name: paragraph_wikilinks
    list:
      list:
      - name: lang
        dtype: string
      - name: title
        dtype: string
      - name: text
        dtype: string
      - name: start
        dtype: int64
      - name: end
        dtype: int64
  - name: paragraph_html_tags
    list: string
  - name: linked_articles
    list: string
  - name: categories
    list: string
  - name: templates
    list: string
  - name: num_inlinks
    dtype: int64
  - name: redirects
    list: string
  splits:
  - name: train
    num_bytes: 7109622094
    num_examples: 2493414
  download_size: 2402263311
  dataset_size: 7109622094
- config_name: arwiki-20260301-v1.2.0
  features:
  - name: id
    dtype: string
  - name: lang
    dtype: string
  - name: page_id
    dtype: int64
  - name: revision_id
    dtype: int64
  - name: page_type
    dtype: string
  - name: title
    dtype: string
  - name: wikidata_qid
    dtype: string
  - name: paragraph_texts
    list: string
  - name: paragraph_sections
    list: string
  - name: paragraph_wikilinks
    list:
      list:
      - name: lang
        dtype: string
      - name: title
        dtype: string
      - name: text
        dtype: string
      - name: start
        dtype: int64
      - name: end
        dtype: int64
  - name: paragraph_html_tags
    list: string
  - name: linked_articles
    list: string
  - name: categories
    list: string
  - name: templates
    list: string
  - name: num_inlinks
    dtype: int64
  - name: redirects
    list: string
  splits:
  - name: train
    num_bytes: 7292545579
    num_examples: 2524290
  download_size: 7085155946
  dataset_size: 7292545579
- config_name: arwiki-20260607-v1.2.1
  features:
  - name: id
    dtype: string
  - name: lang
    dtype: string
  - name: page_id
    dtype: int64
  - name: revision_id
    dtype: int64
  - name: page_type
    dtype: string
  - name: title
    dtype: string
  - name: wikidata_qid
    dtype: string
  - name: paragraph_texts
    list: string
  - name: paragraph_sections
    list: string
  - name: paragraph_wikilinks
    list:
      list:
      - name: lang
        dtype: string
      - name: title
        dtype: string
      - name: text
        dtype: string
      - name: start
        dtype: int64
      - name: end
        dtype: int64
  - name: paragraph_html_tags
    list: string
  - name: linked_articles
    list: string
  - name: categories
    list: string
  - name: templates
    list: string
  - name: num_inlinks
    dtype: int64
  - name: redirects
    list: string
  splits:
  - name: train
    num_bytes: 7485930006
    num_examples: 2541558
  download_size: 7275306671
  dataset_size: 7485930006
- config_name: dewiki-20250901-v1.0.0
  features:
  - name: id
    dtype: string
  - name: lang
    dtype: string
  - name: page_id
    dtype: int64
  - name: revision_id
    dtype: int64
  - name: page_type
    dtype: string
  - name: title
    dtype: string
  - name: wikidata_qid
    dtype: string
  - name: paragraph_texts
    list: string
  - name: paragraph_sections
    list: string
  - name: paragraph_wikilinks
    list:
      list:
      - name: lang
        dtype: string
      - name: title
        dtype: string
      - name: text
        dtype: string
      - name: start
        dtype: int64
      - name: end
        dtype: int64
  - name: paragraph_html_tags
    list: string
  - name: linked_articles
    list: string
  - name: categories
    list: string
  - name: templates
    list: string
  - name: num_inlinks
    dtype: int64
  - name: redirects
    list: string
  splits:
  - name: train
    num_bytes: 19583128400
    num_examples: 3686436
  download_size: 10370922598
  dataset_size: 19583128400
- config_name: dewiki-20250901-v1.1.0
  features:
  - name: id
    dtype: string
  - name: lang
    dtype: string
  - name: page_id
    dtype: int64
  - name: revision_id
    dtype: int64
  - name: page_type
    dtype: string
  - name: title
    dtype: string
  - name: wikidata_qid
    dtype: string
  - name: paragraph_texts
    list: string
  - name: paragraph_sections
    list: string
  - name: paragraph_wikilinks
    list:
      list:
      - name: lang
        dtype: string
      - name: title
        dtype: string
      - name: text
        dtype: string
      - name: start
        dtype: int64
      - name: end
        dtype: int64
  - name: paragraph_html_tags
    list: string
  - name: linked_articles
    list: string
  - name: categories
    list: string
  - name: templates
    list: string
  - name: num_inlinks
    dtype: int64
  - name: redirects
    list: string
  splits:
  - name: train
    num_bytes: 19583139282
    num_examples: 3686436
  download_size: 10166903658
  dataset_size: 19583139282
- config_name: dewiki-20251202-v1.1.0
  features:
  - name: id
    dtype: string
  - name: lang
    dtype: string
  - name: page_id
    dtype: int64
  - name: revision_id
    dtype: int64
  - name: page_type
    dtype: string
  - name: title
    dtype: string
  - name: wikidata_qid
    dtype: string
  - name: paragraph_texts
    list: string
  - name: paragraph_sections
    list: string
  - name: paragraph_wikilinks
    list:
      list:
      - name: lang
        dtype: string
      - name: title
        dtype: string
      - name: text
        dtype: string
      - name: start
        dtype: int64
      - name: end
        dtype: int64
  - name: paragraph_html_tags
    list: string
  - name: linked_articles
    list: string
  - name: categories
    list: string
  - name: templates
    list: string
  - name: num_inlinks
    dtype: int64
  - name: redirects
    list: string
  splits:
  - name: train
    num_bytes: 19796061419
    num_examples: 3719543
  download_size: 10276422820
  dataset_size: 19796061419
- config_name: dewiki-20260301-v1.2.0
  features:
  - name: id
    dtype: string
  - name: lang
    dtype: string
  - name: page_id
    dtype: int64
  - name: revision_id
    dtype: int64
  - name: page_type
    dtype: string
  - name: title
    dtype: string
  - name: wikidata_qid
    dtype: string
  - name: paragraph_texts
    list: string
  - name: paragraph_sections
    list: string
  - name: paragraph_wikilinks
    list:
      list:
      - name: lang
        dtype: string
      - name: title
        dtype: string
      - name: text
        dtype: string
      - name: start
        dtype: int64
      - name: end
        dtype: int64
  - name: paragraph_html_tags
    list: string
  - name: linked_articles
    list: string
  - name: categories
    list: string
  - name: templates
    list: string
  - name: num_inlinks
    dtype: int64
  - name: redirects
    list: string
  splits:
  - name: train
    num_bytes: 19999477978
    num_examples: 3752756
  download_size: 19793164520
  dataset_size: 19999477978
- config_name: dewiki-20260607-v1.2.1
  features:
  - name: id
    dtype: string
  - name: lang
    dtype: string
  - name: page_id
    dtype: int64
  - name: revision_id
    dtype: int64
  - name: page_type
    dtype: string
  - name: title
    dtype: string
  - name: wikidata_qid
    dtype: string
  - name: paragraph_texts
    list: string
  - name: paragraph_sections
    list: string
  - name: paragraph_wikilinks
    list:
      list:
      - name: lang
        dtype: string
      - name: title
        dtype: string
      - name: text
        dtype: string
      - name: start
        dtype: int64
      - name: end
        dtype: int64
  - name: paragraph_html_tags
    list: string
  - name: linked_articles
    list: string
  - name: categories
    list: string
  - name: templates
    list: string
  - name: num_inlinks
    dtype: int64
  - name: redirects
    list: string
  splits:
  - name: train
    num_bytes: 20238302504
    num_examples: 3786915
  download_size: 20029390250
  dataset_size: 20238302504
- config_name: enwiki-20250901-v1.0.0
  features:
  - name: id
    dtype: string
  - name: lang
    dtype: string
  - name: page_id
    dtype: int64
  - name: revision_id
    dtype: int64
  - name: page_type
    dtype: string
  - name: title
    dtype: string
  - name: wikidata_qid
    dtype: string
  - name: paragraph_texts
    list: string
  - name: paragraph_sections
    list: string
  - name: paragraph_wikilinks
    list:
      list:
      - name: lang
        dtype: string
      - name: title
        dtype: string
      - name: text
        dtype: string
      - name: start
        dtype: int64
      - name: end
        dtype: int64
  - name: paragraph_html_tags
    list: string
  - name: linked_articles
    list: string
  - name: categories
    list: string
  - name: templates
    list: string
  - name: num_inlinks
    dtype: int64
  - name: redirects
    list: string
  splits:
  - name: train
    num_bytes: 46307168832
    num_examples: 10278170
  download_size: 23935468828
  dataset_size: 46307168832
- config_name: enwiki-20250901-v1.1.0
  features:
  - name: id
    dtype: string
  - name: lang
    dtype: string
  - name: page_id
    dtype: int64
  - name: revision_id
    dtype: int64
  - name: page_type
    dtype: string
  - name: title
    dtype: string
  - name: wikidata_qid
    dtype: string
  - name: paragraph_texts
    list: string
  - name: paragraph_sections
    list: string
  - name: paragraph_wikilinks
    list:
      list:
      - name: lang
        dtype: string
      - name: title
        dtype: string
      - name: text
        dtype: string
      - name: start
        dtype: int64
      - name: end
        dtype: int64
  - name: paragraph_html_tags
    list: string
  - name: linked_articles
    list: string
  - name: categories
    list: string
  - name: templates
    list: string
  - name: num_inlinks
    dtype: int64
  - name: redirects
    list: string
  splits:
  - name: train
    num_bytes: 46307295487
    num_examples: 10278170
  download_size: 23366994562
  dataset_size: 46307295487
- config_name: enwiki-20251202-v1.1.0
  features:
  - name: id
    dtype: string
  - name: lang
    dtype: string
  - name: page_id
    dtype: int64
  - name: revision_id
    dtype: int64
  - name: page_type
    dtype: string
  - name: title
    dtype: string
  - name: wikidata_qid
    dtype: string
  - name: paragraph_texts
    list: string
  - name: paragraph_sections
    list: string
  - name: paragraph_wikilinks
    list:
      list:
      - name: lang
        dtype: string
      - name: title
        dtype: string
      - name: text
        dtype: string
      - name: start
        dtype: int64
      - name: end
        dtype: int64
  - name: paragraph_html_tags
    list: string
  - name: linked_articles
    list: string
  - name: categories
    list: string
  - name: templates
    list: string
  - name: num_inlinks
    dtype: int64
  - name: redirects
    list: string
  splits:
  - name: train
    num_bytes: 46831421492
    num_examples: 10367020
  download_size: 23630081238
  dataset_size: 46831421492
- config_name: enwiki-20260301-v1.2.0
  features:
  - name: id
    dtype: string
  - name: lang
    dtype: string
  - name: page_id
    dtype: int64
  - name: revision_id
    dtype: int64
  - name: page_type
    dtype: string
  - name: title
    dtype: string
  - name: wikidata_qid
    dtype: string
  - name: paragraph_texts
    list: string
  - name: paragraph_sections
    list: string
  - name: paragraph_wikilinks
    list:
      list:
      - name: lang
        dtype: string
      - name: title
        dtype: string
      - name: text
        dtype: string
      - name: start
        dtype: int64
      - name: end
        dtype: int64
  - name: paragraph_html_tags
    list: string
  - name: linked_articles
    list: string
  - name: categories
    list: string
  - name: templates
    list: string
  - name: num_inlinks
    dtype: int64
  - name: redirects
    list: string
  splits:
  - name: train
    num_bytes: 47125618805
    num_examples: 10458608
  download_size: 46481749542
  dataset_size: 47125618805
- config_name: enwiki-20260607-v1.2.1
  features:
  - name: id
    dtype: string
  - name: lang
    dtype: string
  - name: page_id
    dtype: int64
  - name: revision_id
    dtype: int64
  - name: page_type
    dtype: string
  - name: title
    dtype: string
  - name: wikidata_qid
    dtype: string
  - name: paragraph_texts
    list: string
  - name: paragraph_sections
    list: string
  - name: paragraph_wikilinks
    list:
      list:
      - name: lang
        dtype: string
      - name: title
        dtype: string
      - name: text
        dtype: string
      - name: start
        dtype: int64
      - name: end
        dtype: int64
  - name: paragraph_html_tags
    list: string
  - name: linked_articles
    list: string
  - name: categories
    list: string
  - name: templates
    list: string
  - name: num_inlinks
    dtype: int64
  - name: redirects
    list: string
  splits:
  - name: train
    num_bytes: 47912386793
    num_examples: 10539509
  download_size: 47260574977
  dataset_size: 47912386793
- config_name: eswiki-20250901-v1.0.0
  features:
  - name: id
    dtype: string
  - name: lang
    dtype: string
  - name: page_id
    dtype: int64
  - name: revision_id
    dtype: int64
  - name: page_type
    dtype: string
  - name: title
    dtype: string
  - name: wikidata_qid
    dtype: string
  - name: paragraph_texts
    list: string
  - name: paragraph_sections
    list: string
  - name: paragraph_wikilinks
    list:
      list:
      - name: lang
        dtype: string
      - name: title
        dtype: string
      - name: text
        dtype: string
      - name: start
        dtype: int64
      - name: end
        dtype: int64
  - name: paragraph_html_tags
    list: string
  - name: linked_articles
    list: string
  - name: categories
    list: string
  - name: templates
    list: string
  - name: num_inlinks
    dtype: int64
  - name: redirects
    list: string
  splits:
  - name: train
    num_bytes: 12079137098
    num_examples: 2571062
  download_size: 6016367357
  dataset_size: 12079137098
- config_name: eswiki-20250901-v1.1.0
  features:
  - name: id
    dtype: string
  - name: lang
    dtype: string
  - name: page_id
    dtype: int64
  - name: revision_id
    dtype: int64
  - name: page_type
    dtype: string
  - name: title
    dtype: string
  - name: wikidata_qid
    dtype: string
  - name: paragraph_texts
    list: string
  - name: paragraph_sections
    list: string
  - name: paragraph_wikilinks
    list:
      list:
      - name: lang
        dtype: string
      - name: title
        dtype: string
      - name: text
        dtype: string
      - name: start
        dtype: int64
      - name: end
        dtype: int64
  - name: paragraph_html_tags
    list: string
  - name: linked_articles
    list: string
  - name: categories
    list: string
  - name: templates
    list: string
  - name: num_inlinks
    dtype: int64
  - name: redirects
    list: string
  splits:
  - name: train
    num_bytes: 12079143337
    num_examples: 2571062
  download_size: 5913128471
  dataset_size: 12079143337
- config_name: eswiki-20251202-v1.1.0
  features:
  - name: id
    dtype: string
  - name: lang
    dtype: string
  - name: page_id
    dtype: int64
  - name: revision_id
    dtype: int64
  - name: page_type
    dtype: string
  - name: title
    dtype: string
  - name: wikidata_qid
    dtype: string
  - name: paragraph_texts
    list: string
  - name: paragraph_sections
    list: string
  - name: paragraph_wikilinks
    list:
      list:
      - name: lang
        dtype: string
      - name: title
        dtype: string
      - name: text
        dtype: string
      - name: start
        dtype: int64
      - name: end
        dtype: int64
  - name: paragraph_html_tags
    list: string
  - name: linked_articles
    list: string
  - name: categories
    list: string
  - name: templates
    list: string
  - name: num_inlinks
    dtype: int64
  - name: redirects
    list: string
  splits:
  - name: train
    num_bytes: 12224957826
    num_examples: 2595993
  download_size: 5989184483
  dataset_size: 12224957826
- config_name: eswiki-20260301-v1.2.0
  features:
  - name: id
    dtype: string
  - name: lang
    dtype: string
  - name: page_id
    dtype: int64
  - name: revision_id
    dtype: int64
  - name: page_type
    dtype: string
  - name: title
    dtype: string
  - name: wikidata_qid
    dtype: string
  - name: paragraph_texts
    list: string
  - name: paragraph_sections
    list: string
  - name: paragraph_wikilinks
    list:
      list:
      - name: lang
        dtype: string
      - name: title
        dtype: string
      - name: text
        dtype: string
      - name: start
        dtype: int64
      - name: end
        dtype: int64
  - name: paragraph_html_tags
    list: string
  - name: linked_articles
    list: string
  - name: categories
    list: string
  - name: templates
    list: string
  - name: num_inlinks
    dtype: int64
  - name: redirects
    list: string
  splits:
  - name: train
    num_bytes: 12370482902
    num_examples: 2620690
  download_size: 12216544555
  dataset_size: 12370482902
- config_name: eswiki-20260607-v1.2.1
  features:
  - name: id
    dtype: string
  - name: lang
    dtype: string
  - name: page_id
    dtype: int64
  - name: revision_id
    dtype: int64
  - name: page_type
    dtype: string
  - name: title
    dtype: string
  - name: wikidata_qid
    dtype: string
  - name: paragraph_texts
    list: string
  - name: paragraph_sections
    list: string
  - name: paragraph_wikilinks
    list:
      list:
      - name: lang
        dtype: string
      - name: title
        dtype: string
      - name: text
        dtype: string
      - name: start
        dtype: int64
      - name: end
        dtype: int64
  - name: paragraph_html_tags
    list: string
  - name: linked_articles
    list: string
  - name: categories
    list: string
  - name: templates
    list: string
  - name: num_inlinks
    dtype: int64
  - name: redirects
    list: string
  splits:
  - name: train
    num_bytes: 12538454825
    num_examples: 2645446
  download_size: 12383065383
  dataset_size: 12538454825
- config_name: frwiki-20250901-v1.0.0
  features:
  - name: id
    dtype: string
  - name: lang
    dtype: string
  - name: page_id
    dtype: int64
  - name: revision_id
    dtype: int64
  - name: page_type
    dtype: string
  - name: title
    dtype: string
  - name: wikidata_qid
    dtype: string
  - name: paragraph_texts
    list: string
  - name: paragraph_sections
    list: string
  - name: paragraph_wikilinks
    list:
      list:
      - name: lang
        dtype: string
      - name: title
        dtype: string
      - name: text
        dtype: string
      - name: start
        dtype: int64
      - name: end
        dtype: int64
  - name: paragraph_html_tags
    list: string
  - name: linked_articles
    list: string
  - name: categories
    list: string
  - name: templates
    list: string
  - name: num_inlinks
    dtype: int64
  - name: redirects
    list: string
  splits:
  - name: train
    num_bytes: 19567554983
    num_examples: 3628349
  download_size: 9290798704
  dataset_size: 19567554983
- config_name: frwiki-20250901-v1.1.0
  features:
  - name: id
    dtype: string
  - name: lang
    dtype: string
  - name: page_id
    dtype: int64
  - name: revision_id
    dtype: int64
  - name: page_type
    dtype: string
  - name: title
    dtype: string
  - name: wikidata_qid
    dtype: string
  - name: paragraph_texts
    list: string
  - name: paragraph_sections
    list: string
  - name: paragraph_wikilinks
    list:
      list:
      - name: lang
        dtype: string
      - name: title
        dtype: string
      - name: text
        dtype: string
      - name: start
        dtype: int64
      - name: end
        dtype: int64
  - name: paragraph_html_tags
    list: string
  - name: linked_articles
    list: string
  - name: categories
    list: string
  - name: templates
    list: string
  - name: num_inlinks
    dtype: int64
  - name: redirects
    list: string
  splits:
  - name: train
    num_bytes: 19567607165
    num_examples: 3628349
  download_size: 9211450686
  dataset_size: 19567607165
- config_name: frwiki-20251202-v1.1.0
  features:
  - name: id
    dtype: string
  - name: lang
    dtype: string
  - name: page_id
    dtype: int64
  - name: revision_id
    dtype: int64
  - name: page_type
    dtype: string
  - name: title
    dtype: string
  - name: wikidata_qid
    dtype: string
  - name: paragraph_texts
    list: string
  - name: paragraph_sections
    list: string
  - name: paragraph_wikilinks
    list:
      list:
      - name: lang
        dtype: string
      - name: title
        dtype: string
      - name: text
        dtype: string
      - name: start
        dtype: int64
      - name: end
        dtype: int64
  - name: paragraph_html_tags
    list: string
  - name: linked_articles
    list: string
  - name: categories
    list: string
  - name: templates
    list: string
  - name: num_inlinks
    dtype: int64
  - name: redirects
    list: string
  splits:
  - name: train
    num_bytes: 19817258179
    num_examples: 3658379
  download_size: 9320727988
  dataset_size: 19817258179
- config_name: frwiki-20260301-v1.2.0
  features:
  - name: id
    dtype: string
  - name: lang
    dtype: string
  - name: page_id
    dtype: int64
  - name: revision_id
    dtype: int64
  - name: page_type
    dtype: string
  - name: title
    dtype: string
  - name: wikidata_qid
    dtype: string
  - name: paragraph_texts
    list: string
  - name: paragraph_sections
    list: string
  - name: paragraph_wikilinks
    list:
      list:
      - name: lang
        dtype: string
      - name: title
        dtype: string
      - name: text
        dtype: string
      - name: start
        dtype: int64
      - name: end
        dtype: int64
  - name: paragraph_html_tags
    list: string
  - name: linked_articles
    list: string
  - name: categories
    list: string
  - name: templates
    list: string
  - name: num_inlinks
    dtype: int64
  - name: redirects
    list: string
  splits:
  - name: train
    num_bytes: 20016499397
    num_examples: 3688096
  download_size: 19809187647
  dataset_size: 20016499397
- config_name: frwiki-20260607-v1.2.1
  features:
  - name: id
    dtype: string
  - name: lang
    dtype: string
  - name: page_id
    dtype: int64
  - name: revision_id
    dtype: int64
  - name: page_type
    dtype: string
  - name: title
    dtype: string
  - name: wikidata_qid
    dtype: string
  - name: paragraph_texts
    list: string
  - name: paragraph_sections
    list: string
  - name: paragraph_wikilinks
    list:
      list:
      - name: lang
        dtype: string
      - name: title
        dtype: string
      - name: text
        dtype: string
      - name: start
        dtype: int64
      - name: end
        dtype: int64
  - name: paragraph_html_tags
    list: string
  - name: linked_articles
    list: string
  - name: categories
    list: string
  - name: templates
    list: string
  - name: num_inlinks
    dtype: int64
  - name: redirects
    list: string
  splits:
  - name: train
    num_bytes: 20252965982
    num_examples: 3718670
  download_size: 20044076048
  dataset_size: 20252965982
- config_name: itwiki-20250901-v1.0.0
  features:
  - name: id
    dtype: string
  - name: lang
    dtype: string
  - name: page_id
    dtype: int64
  - name: revision_id
    dtype: int64
  - name: page_type
    dtype: string
  - name: title
    dtype: string
  - name: wikidata_qid
    dtype: string
  - name: paragraph_texts
    list: string
  - name: paragraph_sections
    list: string
  - name: paragraph_wikilinks
    list:
      list:
      - name: lang
        dtype: string
      - name: title
        dtype: string
      - name: text
        dtype: string
      - name: start
        dtype: int64
      - name: end
        dtype: int64
  - name: paragraph_html_tags
    list: string
  - name: linked_articles
    list: string
  - name: categories
    list: string
  - name: templates
    list: string
  - name: num_inlinks
    dtype: int64
  - name: redirects
    list: string
  splits:
  - name: train
    num_bytes: 11504818525
    num_examples: 2595445
  download_size: 5648140309
  dataset_size: 11504818525
- config_name: itwiki-20250901-v1.1.0
  features:
  - name: id
    dtype: string
  - name: lang
    dtype: string
  - name: page_id
    dtype: int64
  - name: revision_id
    dtype: int64
  - name: page_type
    dtype: string
  - name: title
    dtype: string
  - name: wikidata_qid
    dtype: string
  - name: paragraph_texts
    list: string
  - name: paragraph_sections
    list: string
  - name: paragraph_wikilinks
    list:
      list:
      - name: lang
        dtype: string
      - name: title
        dtype: string
      - name: text
        dtype: string
      - name: start
        dtype: int64
      - name: end
        dtype: int64
  - name: paragraph_html_tags
    list: string
  - name: linked_articles
    list: string
  - name: categories
    list: string
  - name: templates
    list: string
  - name: num_inlinks
    dtype: int64
  - name: redirects
    list: string
  splits:
  - name: train
    num_bytes: 11504846121
    num_examples: 2595445
  download_size: 5587730351
  dataset_size: 11504846121
- config_name: itwiki-20251202-v1.1.0
  features:
  - name: id
    dtype: string
  - name: lang
    dtype: string
  - name: page_id
    dtype: int64
  - name: revision_id
    dtype: int64
  - name: page_type
    dtype: string
  - name: title
    dtype: string
  - name: wikidata_qid
    dtype: string
  - name: paragraph_texts
    list: string
  - name: paragraph_sections
    list: string
  - name: paragraph_wikilinks
    list:
      list:
      - name: lang
        dtype: string
      - name: title
        dtype: string
      - name: text
        dtype: string
      - name: start
        dtype: int64
      - name: end
        dtype: int64
  - name: paragraph_html_tags
    list: string
  - name: linked_articles
    list: string
  - name: categories
    list: string
  - name: templates
    list: string
  - name: num_inlinks
    dtype: int64
  - name: redirects
    list: string
  splits:
  - name: train
    num_bytes: 11636301693
    num_examples: 2613752
  download_size: 5652830823
  dataset_size: 11636301693
- config_name: itwiki-20260301-v1.2.0
  features:
  - name: id
    dtype: string
  - name: lang
    dtype: string
  - name: page_id
    dtype: int64
  - name: revision_id
    dtype: int64
  - name: page_type
    dtype: string
  - name: title
    dtype: string
  - name: wikidata_qid
    dtype: string
  - name: paragraph_texts
    list: string
  - name: paragraph_sections
    list: string
  - name: paragraph_wikilinks
    list:
      list:
      - name: lang
        dtype: string
      - name: title
        dtype: string
      - name: text
        dtype: string
      - name: start
        dtype: int64
      - name: end
        dtype: int64
  - name: paragraph_html_tags
    list: string
  - name: linked_articles
    list: string
  - name: categories
    list: string
  - name: templates
    list: string
  - name: num_inlinks
    dtype: int64
  - name: redirects
    list: string
  splits:
  - name: train
    num_bytes: 11739720858
    num_examples: 2628502
  download_size: 11579025632
  dataset_size: 11739720858
- config_name: itwiki-20260607-v1.2.1
  features:
  - name: id
    dtype: string
  - name: lang
    dtype: string
  - name: page_id
    dtype: int64
  - name: revision_id
    dtype: int64
  - name: page_type
    dtype: string
  - name: title
    dtype: string
  - name: wikidata_qid
    dtype: string
  - name: paragraph_texts
    list: string
  - name: paragraph_sections
    list: string
  - name: paragraph_wikilinks
    list:
      list:
      - name: lang
        dtype: string
      - name: title
        dtype: string
      - name: text
        dtype: string
      - name: start
        dtype: int64
      - name: end
        dtype: int64
  - name: paragraph_html_tags
    list: string
  - name: linked_articles
    list: string
  - name: categories
    list: string
  - name: templates
    list: string
  - name: num_inlinks
    dtype: int64
  - name: redirects
    list: string
  splits:
  - name: train
    num_bytes: 11902039974
    num_examples: 2647180
  download_size: 11739907383
  dataset_size: 11902039974
- config_name: jawiki-20250901-v1.0.0
  features:
  - name: id
    dtype: string
  - name: lang
    dtype: string
  - name: page_id
    dtype: int64
  - name: revision_id
    dtype: int64
  - name: page_type
    dtype: string
  - name: title
    dtype: string
  - name: wikidata_qid
    dtype: string
  - name: paragraph_texts
    list: string
  - name: paragraph_sections
    list: string
  - name: paragraph_wikilinks
    list:
      list:
      - name: lang
        dtype: string
      - name: title
        dtype: string
      - name: text
        dtype: string
      - name: start
        dtype: int64
      - name: end
        dtype: int64
  - name: paragraph_html_tags
    list: string
  - name: linked_articles
    list: string
  - name: categories
    list: string
  - name: templates
    list: string
  - name: num_inlinks
    dtype: int64
  - name: redirects
    list: string
  splits:
  - name: train
    num_bytes: 14900366555
    num_examples: 1889973
  download_size: 7150421473
  dataset_size: 14900366555
- config_name: jawiki-20250901-v1.1.0
  features:
  - name: id
    dtype: string
  - name: lang
    dtype: string
  - name: page_id
    dtype: int64
  - name: revision_id
    dtype: int64
  - name: page_type
    dtype: string
  - name: title
    dtype: string
  - name: wikidata_qid
    dtype: string
  - name: paragraph_texts
    list: string
  - name: paragraph_sections
    list: string
  - name: paragraph_wikilinks
    list:
      list:
      - name: lang
        dtype: string
      - name: title
        dtype: string
      - name: text
        dtype: string
      - name: start
        dtype: int64
      - name: end
        dtype: int64
  - name: paragraph_html_tags
    list: string
  - name: linked_articles
    list: string
  - name: categories
    list: string
  - name: templates
    list: string
  - name: num_inlinks
    dtype: int64
  - name: redirects
    list: string
  splits:
  - name: train
    num_bytes: 14901212737
    num_examples: 1889973
  download_size: 7173940753
  dataset_size: 14901212737
- config_name: jawiki-20251202-v1.1.0
  features:
  - name: id
    dtype: string
  - name: lang
    dtype: string
  - name: page_id
    dtype: int64
  - name: revision_id
    dtype: int64
  - name: page_type
    dtype: string
  - name: title
    dtype: string
  - name: wikidata_qid
    dtype: string
  - name: paragraph_texts
    list: string
  - name: paragraph_sections
    list: string
  - name: paragraph_wikilinks
    list:
      list:
      - name: lang
        dtype: string
      - name: title
        dtype: string
      - name: text
        dtype: string
      - name: start
        dtype: int64
      - name: end
        dtype: int64
  - name: paragraph_html_tags
    list: string
  - name: linked_articles
    list: string
  - name: categories
    list: string
  - name: templates
    list: string
  - name: num_inlinks
    dtype: int64
  - name: redirects
    list: string
  splits:
  - name: train
    num_bytes: 15048782188
    num_examples: 1902753
  download_size: 7245596267
  dataset_size: 15048782188
- config_name: jawiki-20260301-v1.2.0
  features:
  - name: id
    dtype: string
  - name: lang
    dtype: string
  - name: page_id
    dtype: int64
  - name: revision_id
    dtype: int64
  - name: page_type
    dtype: string
  - name: title
    dtype: string
  - name: wikidata_qid
    dtype: string
  - name: paragraph_texts
    list: string
  - name: paragraph_sections
    list: string
  - name: paragraph_wikilinks
    list:
      list:
      - name: lang
        dtype: string
      - name: title
        dtype: string
      - name: text
        dtype: string
      - name: start
        dtype: int64
      - name: end
        dtype: int64
  - name: paragraph_html_tags
    list: string
  - name: linked_articles
    list: string
  - name: categories
    list: string
  - name: templates
    list: string
  - name: num_inlinks
    dtype: int64
  - name: redirects
    list: string
  splits:
  - name: train
    num_bytes: 15183315338
    num_examples: 1915010
  download_size: 15070737994
  dataset_size: 15183315338
- config_name: jawiki-20260607-v1.2.1
  features:
  - name: id
    dtype: string
  - name: lang
    dtype: string
  - name: page_id
    dtype: int64
  - name: revision_id
    dtype: int64
  - name: page_type
    dtype: string
  - name: title
    dtype: string
  - name: wikidata_qid
    dtype: string
  - name: paragraph_texts
    list: string
  - name: paragraph_sections
    list: string
  - name: paragraph_wikilinks
    list:
      list:
      - name: lang
        dtype: string
      - name: title
        dtype: string
      - name: text
        dtype: string
      - name: start
        dtype: int64
      - name: end
        dtype: int64
  - name: paragraph_html_tags
    list: string
  - name: linked_articles
    list: string
  - name: categories
    list: string
  - name: templates
    list: string
  - name: num_inlinks
    dtype: int64
  - name: redirects
    list: string
  splits:
  - name: train
    num_bytes: 15382294721
    num_examples: 1929103
  download_size: 15268296712
  dataset_size: 15382294721
- config_name: kowiki-20250901-v1.0.0
  features:
  - name: id
    dtype: string
  - name: lang
    dtype: string
  - name: page_id
    dtype: int64
  - name: revision_id
    dtype: int64
  - name: page_type
    dtype: string
  - name: title
    dtype: string
  - name: wikidata_qid
    dtype: string
  - name: paragraph_texts
    list: string
  - name: paragraph_sections
    list: string
  - name: paragraph_wikilinks
    list:
      list:
      - name: lang
        dtype: string
      - name: title
        dtype: string
      - name: text
        dtype: string
      - name: start
        dtype: int64
      - name: end
        dtype: int64
  - name: paragraph_html_tags
    list: string
  - name: linked_articles
    list: string
  - name: categories
    list: string
  - name: templates
    list: string
  - name: num_inlinks
    dtype: int64
  - name: redirects
    list: string
  splits:
  - name: train
    num_bytes: 3347079151
    num_examples: 1201801
  download_size: 1543077548
  dataset_size: 3347079151
- config_name: kowiki-20250901-v1.1.0
  features:
  - name: id
    dtype: string
  - name: lang
    dtype: string
  - name: page_id
    dtype: int64
  - name: revision_id
    dtype: int64
  - name: page_type
    dtype: string
  - name: title
    dtype: string
  - name: wikidata_qid
    dtype: string
  - name: paragraph_texts
    list: string
  - name: paragraph_sections
    list: string
  - name: paragraph_wikilinks
    list:
      list:
      - name: lang
        dtype: string
      - name: title
        dtype: string
      - name: text
        dtype: string
      - name: start
        dtype: int64
      - name: end
        dtype: int64
  - name: paragraph_html_tags
    list: string
  - name: linked_articles
    list: string
  - name: categories
    list: string
  - name: templates
    list: string
  - name: num_inlinks
    dtype: int64
  - name: redirects
    list: string
  splits:
  - name: train
    num_bytes: 3347446850
    num_examples: 1201801
  download_size: 1504312356
  dataset_size: 3347446850
- config_name: kowiki-20251202-v1.1.0
  features:
  - name: id
    dtype: string
  - name: lang
    dtype: string
  - name: page_id
    dtype: int64
  - name: revision_id
    dtype: int64
  - name: page_type
    dtype: string
  - name: title
    dtype: string
  - name: wikidata_qid
    dtype: string
  - name: paragraph_texts
    list: string
  - name: paragraph_sections
    list: string
  - name: paragraph_wikilinks
    list:
      list:
      - name: lang
        dtype: string
      - name: title
        dtype: string
      - name: text
        dtype: string
      - name: start
        dtype: int64
      - name: end
        dtype: int64
  - name: paragraph_html_tags
    list: string
  - name: linked_articles
    list: string
  - name: categories
    list: string
  - name: templates
    list: string
  - name: num_inlinks
    dtype: int64
  - name: redirects
    list: string
  splits:
  - name: train
    num_bytes: 3483028642
    num_examples: 1217803
  download_size: 1571549293
  dataset_size: 3483028642
- config_name: kowiki-20260301-v1.2.0
  features:
  - name: id
    dtype: string
  - name: lang
    dtype: string
  - name: page_id
    dtype: int64
  - name: revision_id
    dtype: int64
  - name: page_type
    dtype: string
  - name: title
    dtype: string
  - name: wikidata_qid
    dtype: string
  - name: paragraph_texts
    list: string
  - name: paragraph_sections
    list: string
  - name: paragraph_wikilinks
    list:
      list:
      - name: lang
        dtype: string
      - name: title
        dtype: string
      - name: text
        dtype: string
      - name: start
        dtype: int64
      - name: end
        dtype: int64
  - name: paragraph_html_tags
    list: string
  - name: linked_articles
    list: string
  - name: categories
    list: string
  - name: templates
    list: string
  - name: num_inlinks
    dtype: int64
  - name: redirects
    list: string
  splits:
  - name: train
    num_bytes: 3586798869
    num_examples: 1231248
  download_size: 3497991050
  dataset_size: 3586798869
- config_name: kowiki-20260607-v1.2.1
  features:
  - name: id
    dtype: string
  - name: lang
    dtype: string
  - name: page_id
    dtype: int64
  - name: revision_id
    dtype: int64
  - name: page_type
    dtype: string
  - name: title
    dtype: string
  - name: wikidata_qid
    dtype: string
  - name: paragraph_texts
    list: string
  - name: paragraph_sections
    list: string
  - name: paragraph_wikilinks
    list:
      list:
      - name: lang
        dtype: string
      - name: title
        dtype: string
      - name: text
        dtype: string
      - name: start
        dtype: int64
      - name: end
        dtype: int64
  - name: paragraph_html_tags
    list: string
  - name: linked_articles
    list: string
  - name: categories
    list: string
  - name: templates
    list: string
  - name: num_inlinks
    dtype: int64
  - name: redirects
    list: string
  splits:
  - name: train
    num_bytes: 3686140950
    num_examples: 1247301
  download_size: 3596463661
  dataset_size: 3686140950
- config_name: ptwiki-20250901-v1.0.0
  features:
  - name: id
    dtype: string
  - name: lang
    dtype: string
  - name: page_id
    dtype: int64
  - name: revision_id
    dtype: int64
  - name: page_type
    dtype: string
  - name: title
    dtype: string
  - name: wikidata_qid
    dtype: string
  - name: paragraph_texts
    list: string
  - name: paragraph_sections
    list: string
  - name: paragraph_wikilinks
    list:
      list:
      - name: lang
        dtype: string
      - name: title
        dtype: string
      - name: text
        dtype: string
      - name: start
        dtype: int64
      - name: end
        dtype: int64
  - name: paragraph_html_tags
    list: string
  - name: linked_articles
    list: string
  - name: categories
    list: string
  - name: templates
    list: string
  - name: num_inlinks
    dtype: int64
  - name: redirects
    list: string
  splits:
  - name: train
    num_bytes: 5892980284
    num_examples: 1646107
  download_size: 2854696510
  dataset_size: 5892980284
- config_name: ptwiki-20250901-v1.1.0
  features:
  - name: id
    dtype: string
  - name: lang
    dtype: string
  - name: page_id
    dtype: int64
  - name: revision_id
    dtype: int64
  - name: page_type
    dtype: string
  - name: title
    dtype: string
  - name: wikidata_qid
    dtype: string
  - name: paragraph_texts
    list: string
  - name: paragraph_sections
    list: string
  - name: paragraph_wikilinks
    list:
      list:
      - name: lang
        dtype: string
      - name: title
        dtype: string
      - name: text
        dtype: string
      - name: start
        dtype: int64
      - name: end
        dtype: int64
  - name: paragraph_html_tags
    list: string
  - name: linked_articles
    list: string
  - name: categories
    list: string
  - name: templates
    list: string
  - name: num_inlinks
    dtype: int64
  - name: redirects
    list: string
  splits:
  - name: train
    num_bytes: 5892986474
    num_examples: 1646107
  download_size: 2787337899
  dataset_size: 5892986474
- config_name: ptwiki-20251202-v1.1.0
  features:
  - name: id
    dtype: string
  - name: lang
    dtype: string
  - name: page_id
    dtype: int64
  - name: revision_id
    dtype: int64
  - name: page_type
    dtype: string
  - name: title
    dtype: string
  - name: wikidata_qid
    dtype: string
  - name: paragraph_texts
    list: string
  - name: paragraph_sections
    list: string
  - name: paragraph_wikilinks
    list:
      list:
      - name: lang
        dtype: string
      - name: title
        dtype: string
      - name: text
        dtype: string
      - name: start
        dtype: int64
      - name: end
        dtype: int64
  - name: paragraph_html_tags
    list: string
  - name: linked_articles
    list: string
  - name: categories
    list: string
  - name: templates
    list: string
  - name: num_inlinks
    dtype: int64
  - name: redirects
    list: string
  splits:
  - name: train
    num_bytes: 5993104856
    num_examples: 1657254
  download_size: 2839704441
  dataset_size: 5993104856
- config_name: ptwiki-20260301-v1.2.0
  features:
  - name: id
    dtype: string
  - name: lang
    dtype: string
  - name: page_id
    dtype: int64
  - name: revision_id
    dtype: int64
  - name: page_type
    dtype: string
  - name: title
    dtype: string
  - name: wikidata_qid
    dtype: string
  - name: paragraph_texts
    list: string
  - name: paragraph_sections
    list: string
  - name: paragraph_wikilinks
    list:
      list:
      - name: lang
        dtype: string
      - name: title
        dtype: string
      - name: text
        dtype: string
      - name: start
        dtype: int64
      - name: end
        dtype: int64
  - name: paragraph_html_tags
    list: string
  - name: linked_articles
    list: string
  - name: categories
    list: string
  - name: templates
    list: string
  - name: num_inlinks
    dtype: int64
  - name: redirects
    list: string
  splits:
  - name: train
    num_bytes: 6080601217
    num_examples: 1665888
  download_size: 5978570302
  dataset_size: 6080601217
- config_name: ptwiki-20260607-v1.2.1
  features:
  - name: id
    dtype: string
  - name: lang
    dtype: string
  - name: page_id
    dtype: int64
  - name: revision_id
    dtype: int64
  - name: page_type
    dtype: string
  - name: title
    dtype: string
  - name: wikidata_qid
    dtype: string
  - name: paragraph_texts
    list: string
  - name: paragraph_sections
    list: string
  - name: paragraph_wikilinks
    list:
      list:
      - name: lang
        dtype: string
      - name: title
        dtype: string
      - name: text
        dtype: string
      - name: start
        dtype: int64
      - name: end
        dtype: int64
  - name: paragraph_html_tags
    list: string
  - name: linked_articles
    list: string
  - name: categories
    list: string
  - name: templates
    list: string
  - name: num_inlinks
    dtype: int64
  - name: redirects
    list: string
  splits:
  - name: train
    num_bytes: 6223948527
    num_examples: 1682776
  download_size: 6120957948
  dataset_size: 6223948527
- config_name: ruwiki-20250901-v1.0.0
  features:
  - name: id
    dtype: string
  - name: lang
    dtype: string
  - name: page_id
    dtype: int64
  - name: revision_id
    dtype: int64
  - name: page_type
    dtype: string
  - name: title
    dtype: string
  - name: wikidata_qid
    dtype: string
  - name: paragraph_texts
    list: string
  - name: paragraph_sections
    list: string
  - name: paragraph_wikilinks
    list:
      list:
      - name: lang
        dtype: string
      - name: title
        dtype: string
      - name: text
        dtype: string
      - name: start
        dtype: int64
      - name: end
        dtype: int64
  - name: paragraph_html_tags
    list: string
  - name: linked_articles
    list: string
  - name: categories
    list: string
  - name: templates
    list: string
  - name: num_inlinks
    dtype: int64
  - name: redirects
    list: string
  splits:
  - name: train
    num_bytes: 19742734128
    num_examples: 2949645
  download_size: 8299981380
  dataset_size: 19742734128
- config_name: ruwiki-20250901-v1.1.0
  features:
  - name: id
    dtype: string
  - name: lang
    dtype: string
  - name: page_id
    dtype: int64
  - name: revision_id
    dtype: int64
  - name: page_type
    dtype: string
  - name: title
    dtype: string
  - name: wikidata_qid
    dtype: string
  - name: paragraph_texts
    list: string
  - name: paragraph_sections
    list: string
  - name: paragraph_wikilinks
    list:
      list:
      - name: lang
        dtype: string
      - name: title
        dtype: string
      - name: text
        dtype: string
      - name: start
        dtype: int64
      - name: end
        dtype: int64
  - name: paragraph_html_tags
    list: string
  - name: linked_articles
    list: string
  - name: categories
    list: string
  - name: templates
    list: string
  - name: num_inlinks
    dtype: int64
  - name: redirects
    list: string
  splits:
  - name: train
    num_bytes: 19742737853
    num_examples: 2949645
  download_size: 8325604567
  dataset_size: 19742737853
- config_name: ruwiki-20251202-v1.1.0
  features:
  - name: id
    dtype: string
  - name: lang
    dtype: string
  - name: page_id
    dtype: int64
  - name: revision_id
    dtype: int64
  - name: page_type
    dtype: string
  - name: title
    dtype: string
  - name: wikidata_qid
    dtype: string
  - name: paragraph_texts
    list: string
  - name: paragraph_sections
    list: string
  - name: paragraph_wikilinks
    list:
      list:
      - name: lang
        dtype: string
      - name: title
        dtype: string
      - name: text
        dtype: string
      - name: start
        dtype: int64
      - name: end
        dtype: int64
  - name: paragraph_html_tags
    list: string
  - name: linked_articles
    list: string
  - name: categories
    list: string
  - name: templates
    list: string
  - name: num_inlinks
    dtype: int64
  - name: redirects
    list: string
  splits:
  - name: train
    num_bytes: 19919388669
    num_examples: 2971293
  download_size: 8404515599
  dataset_size: 19919388669
- config_name: ruwiki-20260301-v1.2.0
  features:
  - name: id
    dtype: string
  - name: lang
    dtype: string
  - name: page_id
    dtype: int64
  - name: revision_id
    dtype: int64
  - name: page_type
    dtype: string
  - name: title
    dtype: string
  - name: wikidata_qid
    dtype: string
  - name: paragraph_texts
    list: string
  - name: paragraph_sections
    list: string
  - name: paragraph_wikilinks
    list:
      list:
      - name: lang
        dtype: string
      - name: title
        dtype: string
      - name: text
        dtype: string
      - name: start
        dtype: int64
      - name: end
        dtype: int64
  - name: paragraph_html_tags
    list: string
  - name: linked_articles
    list: string
  - name: categories
    list: string
  - name: templates
    list: string
  - name: num_inlinks
    dtype: int64
  - name: redirects
    list: string
  splits:
  - name: train
    num_bytes: 20115307321
    num_examples: 3011804
  download_size: 19898491197
  dataset_size: 20115307321
- config_name: ruwiki-20260607-v1.2.1
  features:
  - name: id
    dtype: string
  - name: lang
    dtype: string
  - name: page_id
    dtype: int64
  - name: revision_id
    dtype: int64
  - name: page_type
    dtype: string
  - name: title
    dtype: string
  - name: wikidata_qid
    dtype: string
  - name: paragraph_texts
    list: string
  - name: paragraph_sections
    list: string
  - name: paragraph_wikilinks
    list:
      list:
      - name: lang
        dtype: string
      - name: title
        dtype: string
      - name: text
        dtype: string
      - name: start
        dtype: int64
      - name: end
        dtype: int64
  - name: paragraph_html_tags
    list: string
  - name: linked_articles
    list: string
  - name: categories
    list: string
  - name: templates
    list: string
  - name: num_inlinks
    dtype: int64
  - name: redirects
    list: string
  splits:
  - name: train
    num_bytes: 20348743705
    num_examples: 3036516
  download_size: 20130554248
  dataset_size: 20348743705
- config_name: zhwiki-20250901-v1.0.0
  features:
  - name: id
    dtype: string
  - name: lang
    dtype: string
  - name: page_id
    dtype: int64
  - name: revision_id
    dtype: int64
  - name: page_type
    dtype: string
  - name: title
    dtype: string
  - name: wikidata_qid
    dtype: string
  - name: paragraph_texts
    list: string
  - name: paragraph_sections
    list: string
  - name: paragraph_wikilinks
    list:
      list:
      - name: lang
        dtype: string
      - name: title
        dtype: string
      - name: text
        dtype: string
      - name: start
        dtype: int64
      - name: end
        dtype: int64
  - name: paragraph_html_tags
    list: string
  - name: linked_articles
    list: string
  - name: categories
    list: string
  - name: templates
    list: string
  - name: num_inlinks
    dtype: int64
  - name: redirects
    list: string
  splits:
  - name: train
    num_bytes: 6279278271
    num_examples: 3066778
  download_size: 3183007013
  dataset_size: 6279278271
- config_name: zhwiki-20250901-v1.1.0
  features:
  - name: id
    dtype: string
  - name: lang
    dtype: string
  - name: page_id
    dtype: int64
  - name: revision_id
    dtype: int64
  - name: page_type
    dtype: string
  - name: title
    dtype: string
  - name: wikidata_qid
    dtype: string
  - name: paragraph_texts
    list: string
  - name: paragraph_sections
    list: string
  - name: paragraph_wikilinks
    list:
      list:
      - name: lang
        dtype: string
      - name: title
        dtype: string
      - name: text
        dtype: string
      - name: start
        dtype: int64
      - name: end
        dtype: int64
  - name: paragraph_html_tags
    list: string
  - name: linked_articles
    list: string
  - name: categories
    list: string
  - name: templates
    list: string
  - name: num_inlinks
    dtype: int64
  - name: redirects
    list: string
  splits:
  - name: train
    num_bytes: 6279368223
    num_examples: 3066778
  download_size: 3098911229
  dataset_size: 6279368223
- config_name: zhwiki-20251202-v1.1.0
  features:
  - name: id
    dtype: string
  - name: lang
    dtype: string
  - name: page_id
    dtype: int64
  - name: revision_id
    dtype: int64
  - name: page_type
    dtype: string
  - name: title
    dtype: string
  - name: wikidata_qid
    dtype: string
  - name: paragraph_texts
    list: string
  - name: paragraph_sections
    list: string
  - name: paragraph_wikilinks
    list:
      list:
      - name: lang
        dtype: string
      - name: title
        dtype: string
      - name: text
        dtype: string
      - name: start
        dtype: int64
      - name: end
        dtype: int64
  - name: paragraph_html_tags
    list: string
  - name: linked_articles
    list: string
  - name: categories
    list: string
  - name: templates
    list: string
  - name: num_inlinks
    dtype: int64
  - name: redirects
    list: string
  splits:
  - name: train
    num_bytes: 6363624753
    num_examples: 3094104
  download_size: 3146862079
  dataset_size: 6363624753
- config_name: zhwiki-20260301-v1.2.0
  features:
  - name: id
    dtype: string
  - name: lang
    dtype: string
  - name: page_id
    dtype: int64
  - name: revision_id
    dtype: int64
  - name: page_type
    dtype: string
  - name: title
    dtype: string
  - name: wikidata_qid
    dtype: string
  - name: paragraph_texts
    list: string
  - name: paragraph_sections
    list: string
  - name: paragraph_wikilinks
    list:
      list:
      - name: lang
        dtype: string
      - name: title
        dtype: string
      - name: text
        dtype: string
      - name: start
        dtype: int64
      - name: end
        dtype: int64
  - name: paragraph_html_tags
    list: string
  - name: linked_articles
    list: string
  - name: categories
    list: string
  - name: templates
    list: string
  - name: num_inlinks
    dtype: int64
  - name: redirects
    list: string
  splits:
  - name: train
    num_bytes: 6428168188
    num_examples: 3121028
  download_size: 6187744850
  dataset_size: 6428168188
- config_name: zhwiki-20260607-v1.2.1
  features:
  - name: id
    dtype: string
  - name: lang
    dtype: string
  - name: page_id
    dtype: int64
  - name: revision_id
    dtype: int64
  - name: page_type
    dtype: string
  - name: title
    dtype: string
  - name: wikidata_qid
    dtype: string
  - name: paragraph_texts
    list: string
  - name: paragraph_sections
    list: string
  - name: paragraph_wikilinks
    list:
      list:
      - name: lang
        dtype: string
      - name: title
        dtype: string
      - name: text
        dtype: string
      - name: start
        dtype: int64
      - name: end
        dtype: int64
  - name: paragraph_html_tags
    list: string
  - name: linked_articles
    list: string
  - name: categories
    list: string
  - name: templates
    list: string
  - name: num_inlinks
    dtype: int64
  - name: redirects
    list: string
  splits:
  - name: train
    num_bytes: 6534408603
    num_examples: 3146592
  download_size: 6292360298
  dataset_size: 6534408603
configs:
- config_name: arwiki-20250901-v1.0.0
  data_files:
  - split: train
    path: arwiki-20250901-v1.0.0/train-*
- config_name: arwiki-20250901-v1.1.0
  data_files:
  - split: train
    path: arwiki-20250901-v1.1.0/train-*
- config_name: arwiki-20251202-v1.1.0
  data_files:
  - split: train
    path: arwiki-20251202-v1.1.0/train-*
- config_name: arwiki-20260301-v1.2.0
  data_files:
  - split: train
    path: arwiki-20260301-v1.2.0/train-*
- config_name: arwiki-20260607-v1.2.1
  data_files:
  - split: train
    path: arwiki-20260607-v1.2.1/train-*
- config_name: dewiki-20250901-v1.0.0
  data_files:
  - split: train
    path: dewiki-20250901-v1.0.0/train-*
- config_name: dewiki-20250901-v1.1.0
  data_files:
  - split: train
    path: dewiki-20250901-v1.1.0/train-*
- config_name: dewiki-20251202-v1.1.0
  data_files:
  - split: train
    path: dewiki-20251202-v1.1.0/train-*
- config_name: dewiki-20260301-v1.2.0
  data_files:
  - split: train
    path: dewiki-20260301-v1.2.0/train-*
- config_name: dewiki-20260607-v1.2.1
  data_files:
  - split: train
    path: dewiki-20260607-v1.2.1/train-*
- config_name: enwiki-20250901-v1.0.0
  data_files:
  - split: train
    path: enwiki-20250901-v1.0.0/train-*
- config_name: enwiki-20250901-v1.1.0
  data_files:
  - split: train
    path: enwiki-20250901-v1.1.0/train-*
- config_name: enwiki-20251202-v1.1.0
  data_files:
  - split: train
    path: enwiki-20251202-v1.1.0/train-*
- config_name: enwiki-20260301-v1.2.0
  data_files:
  - split: train
    path: enwiki-20260301-v1.2.0/train-*
- config_name: enwiki-20260607-v1.2.1
  default: true
  data_files:
  - split: train
    path: enwiki-20260607-v1.2.1/train-*
- config_name: eswiki-20250901-v1.0.0
  data_files:
  - split: train
    path: eswiki-20250901-v1.0.0/train-*
- config_name: eswiki-20250901-v1.1.0
  data_files:
  - split: train
    path: eswiki-20250901-v1.1.0/train-*
- config_name: eswiki-20251202-v1.1.0
  data_files:
  - split: train
    path: eswiki-20251202-v1.1.0/train-*
- config_name: eswiki-20260301-v1.2.0
  data_files:
  - split: train
    path: eswiki-20260301-v1.2.0/train-*
- config_name: eswiki-20260607-v1.2.1
  data_files:
  - split: train
    path: eswiki-20260607-v1.2.1/train-*
- config_name: frwiki-20250901-v1.0.0
  data_files:
  - split: train
    path: frwiki-20250901-v1.0.0/train-*
- config_name: frwiki-20250901-v1.1.0
  data_files:
  - split: train
    path: frwiki-20250901-v1.1.0/train-*
- config_name: frwiki-20251202-v1.1.0
  data_files:
  - split: train
    path: frwiki-20251202-v1.1.0/train-*
- config_name: frwiki-20260301-v1.2.0
  data_files:
  - split: train
    path: frwiki-20260301-v1.2.0/train-*
- config_name: frwiki-20260607-v1.2.1
  data_files:
  - split: train
    path: frwiki-20260607-v1.2.1/train-*
- config_name: itwiki-20250901-v1.0.0
  data_files:
  - split: train
    path: itwiki-20250901-v1.0.0/train-*
- config_name: itwiki-20250901-v1.1.0
  data_files:
  - split: train
    path: itwiki-20250901-v1.1.0/train-*
- config_name: itwiki-20251202-v1.1.0
  data_files:
  - split: train
    path: itwiki-20251202-v1.1.0/train-*
- config_name: itwiki-20260301-v1.2.0
  data_files:
  - split: train
    path: itwiki-20260301-v1.2.0/train-*
- config_name: itwiki-20260607-v1.2.1
  data_files:
  - split: train
    path: itwiki-20260607-v1.2.1/train-*
- config_name: jawiki-20250901-v1.0.0
  data_files:
  - split: train
    path: jawiki-20250901-v1.0.0/train-*
- config_name: jawiki-20250901-v1.1.0
  data_files:
  - split: train
    path: jawiki-20250901-v1.1.0/train-*
- config_name: jawiki-20251202-v1.1.0
  data_files:
  - split: train
    path: jawiki-20251202-v1.1.0/train-*
- config_name: jawiki-20260301-v1.2.0
  data_files:
  - split: train
    path: jawiki-20260301-v1.2.0/train-*
- config_name: jawiki-20260607-v1.2.1
  data_files:
  - split: train
    path: jawiki-20260607-v1.2.1/train-*
- config_name: kowiki-20250901-v1.0.0
  data_files:
  - split: train
    path: kowiki-20250901-v1.0.0/train-*
- config_name: kowiki-20250901-v1.1.0
  data_files:
  - split: train
    path: kowiki-20250901-v1.1.0/train-*
- config_name: kowiki-20251202-v1.1.0
  data_files:
  - split: train
    path: kowiki-20251202-v1.1.0/train-*
- config_name: kowiki-20260301-v1.2.0
  data_files:
  - split: train
    path: kowiki-20260301-v1.2.0/train-*
- config_name: kowiki-20260607-v1.2.1
  data_files:
  - split: train
    path: kowiki-20260607-v1.2.1/train-*
- config_name: ptwiki-20250901-v1.0.0
  data_files:
  - split: train
    path: ptwiki-20250901-v1.0.0/train-*
- config_name: ptwiki-20250901-v1.1.0
  data_files:
  - split: train
    path: ptwiki-20250901-v1.1.0/train-*
- config_name: ptwiki-20251202-v1.1.0
  data_files:
  - split: train
    path: ptwiki-20251202-v1.1.0/train-*
- config_name: ptwiki-20260301-v1.2.0
  data_files:
  - split: train
    path: ptwiki-20260301-v1.2.0/train-*
- config_name: ptwiki-20260607-v1.2.1
  data_files:
  - split: train
    path: ptwiki-20260607-v1.2.1/train-*
- config_name: ruwiki-20250901-v1.0.0
  data_files:
  - split: train
    path: ruwiki-20250901-v1.0.0/train-*
- config_name: ruwiki-20250901-v1.1.0
  data_files:
  - split: train
    path: ruwiki-20250901-v1.1.0/train-*
- config_name: ruwiki-20251202-v1.1.0
  data_files:
  - split: train
    path: ruwiki-20251202-v1.1.0/train-*
- config_name: ruwiki-20260301-v1.2.0
  data_files:
  - split: train
    path: ruwiki-20260301-v1.2.0/train-*
- config_name: ruwiki-20260607-v1.2.1
  data_files:
  - split: train
    path: ruwiki-20260607-v1.2.1/train-*
- config_name: zhwiki-20250901-v1.0.0
  data_files:
  - split: train
    path: zhwiki-20250901-v1.0.0/train-*
- config_name: zhwiki-20250901-v1.1.0
  data_files:
  - split: train
    path: zhwiki-20250901-v1.1.0/train-*
- config_name: zhwiki-20251202-v1.1.0
  data_files:
  - split: train
    path: zhwiki-20251202-v1.1.0/train-*
- config_name: zhwiki-20260301-v1.2.0
  data_files:
  - split: train
    path: zhwiki-20260301-v1.2.0/train-*
- config_name: zhwiki-20260607-v1.2.1
  data_files:
  - split: train
    path: zhwiki-20260607-v1.2.1/train-*
---

# wikipedia-paragraphs

`wikipedia-paragraphs` is a dataset generated from Wikipedia, designed for natural language processing (NLP) research.

Each entry contains cleaned paragraph text and Wikilink information extracted from a Wikipedia page, along with useful metadata such as categories, templates, and the associated Wikidata QID.

## Dataset structure

### Configurations

The dataset is organized into multiple configurations, such as `enwiki-20260607-v1.2.1`.
Each configuration corresponds to a specific Wikipedia dump from which the data was sourced.
The version number denotes the version of the scripts used to process the data.

### Data instances

Each instance in the dataset represents a single Wikipedia page, which can be an **article**, **category**, or **template**.

The following example from the `enwiki-20260607-v1.2.1` configuration shows the data generated from the English Wikipedia article on [Éclair](https://en.wikipedia.org/w/index.php?title=%C3%89clair&oldid=1318785666).

```json
{
  "id": "en-1980219-1351522064",
  "lang": "en",
  "page_id": 1980219,
  "revision_id": 1351522064,
  "page_type": "article",
  "title": "Éclair",
  "wikidata_qid": "Q273426",
  "paragraph_texts": [
    "An éclair (English: /ɪˈklɛər/ ⓘ ih-KLAIR or /eɪˈklɛər/ ay-KLAIR, French: [eklɛːʁ] ⓘ; lit.\u2009'lightning') is a pastry made with choux dough filled with a cream and topped with a flavored icing. The dough, which is the same as that used for profiteroles, is typically piped into an oblong shape with a pastry bag and baked until it is crisp and hollow inside. Once cool, the pastry is filled with custard (crème pâtissière), whipped cream or chiboust cream, then iced with fondant icing. Other fillings include pistachio- and rum-flavored custard, fruit-flavored fillings or chestnut purée. When the icing is caramel, the dessert may be called a bâton de Jacob (lit.\u2009'Jacob's staff'). A similar pastry in a round rather than oblong shape is called a religieuse.",
    "The word comes from the French éclair, meaning 'flash of lightning', so named because it is eaten quickly (in a flash); however some believe that the name is due to the glistening of the frosting resembling lightning.",
    "The éclair originated during the 19th century in Lyon, France where it was called pain à la Duchesse ('Duchess-style bread') or petite duchesse ('little duchess') until 1850. The word is first attested both in English and in French in the 1860s.",
    ...
  ],
  "paragraph_sections": [
    "__LEAD__",
    "Etymology",
    "History",
    ...
  ],
  "paragraph_wikilinks": [                                                                                                                             [229/346]
    [
      {
        "lang": "en",
        "title": "Pastry",
        "text": "pastry",
        "start": 108,
        "end": 114
      },
      {
        "lang": "en",
        "title": "Choux pastry",
        "text": "choux",
        "start": 125,
        "end": 130
      },
      {
        "lang": "en",
        "title": "Profiterole",
        "text": "profiteroles",
        "start": 237,
        "end": 249
      },
      ...
    ],
    [
      {
        "lang": "en",
        "title": "Lightning",
        "text": "lightning",
        "start": 57,
        "end": 66
      }
    ],
    [
      {
        "lang": "en",
        "title": "Lyon",
        "text": "Lyon",
        "start": 49,
        "end": 53
      }
    ],
    ...
  ],
  "paragraph_html_tags": [
    "p",
    "p",
    "p",
    ...
  ],
  "linked_articles": [
    "France",
    "French cuisine",
    "Pastry",
    ...
  ],
  "categories": [
    "Albanian cuisine",
    "Belgian desserts",
    "Custard desserts",
    ...
  ],
  "templates": [
    "Short description",
    "Use American English",
    "Use mdy dates",
    ...
  ],
  "num_inlinks": 70,
  "redirects": [
    "Éclair",
    "Chocolate eclair",
    "Eclairs",
    ...
  ]
}
```

### Data Fields

- **id** (*string*): A unique ID for the instance, composed of `lang`, `page_id` and `revision_id`
- **lang** (*string*): The [Wikipedia edition code](https://en.wikipedia.org/wiki/List_of_Wikipedias#Wikipedia_edition_codes) of the page.
- **page_id** (*int64*): The [page ID](https://www.mediawiki.org/wiki/Manual:Page_table#page_id) of the page.
- **revision_id** (*int64*): The [revision ID](https://en.wikipedia.org/wiki/Wikipedia:Revision_ID) of the page.
- **page_type** (*string*): The page type, one of: [`"article"`](https://en.wikipedia.org/wiki/Wikipedia:What_is_an_article%3F), [`"category"`](https://en.wikipedia.org/wiki/Help:Category), or [`"template"`](https://en.wikipedia.org/wiki/Help:Template).
- **title** (*string*): The page title.
- **wikidata_qid** (*string, optional*): The corresponding [Wikidata](https://en.wikipedia.org/wiki/Wikipedia:Wikidata) QID, if available.
- **paragraph_texts** (*list of string*): A list of cleaned paragraph texts extracted from the page's HTML.
- **paragraph_sections** (*list of string*): A list of section titles corresponding to each paragraph. `__LEAD__` denotes the page's lead section.
- **paragraph_wikilinks** (*list of list*): A nested list where each inner list contains the wikilinks for the corresponding paragraph. Each wikilink object has the following fields:
<!-- - **paragraph_wikilinks** (*list of list*): A nested list where each inner list contains the wikilinks for the corresponding paragraph. If present, the first bolded text in the first paragraph is also included as a pseudo-wikilink for the page's own title. Each wikilink object has the following fields: -->
    - **lang** (*string*): The Wikipedia edition code of the target page.
    - **title** (*string*): The title of the target page.
    - **text** (*string*): The anchor text of the wikilink.
    - **start** (*int64*): The starting character index of the anchor text in the paragraph.
    - **end** (*int64*): The ending character index of the anchor text in the paragraph.
- **paragraph_html_tags** (*list of string*): The HTML tag from which each paragraph was extracted, one of: `"p"`, `"li"` `"dt"`, `"dd"`, or `"blockquote"`
- **linked_articles** (*list of string*): A list of article titles linked from the page.
- **categories** (*list of string*): A list of categories assigned to the page.
- **templates** (*list of string*): A list of templates used on the page.
- **num_inlinks** (*int64*): The number of pages linking to this page. The meaning depends on the page type:
    - For articles, it's the number of pages with wikilinks pointing to this page.
    - For categories, it's the number of pages assigned to this category.
    - For templates, it's the number of pages where this template is used.
- **redirects** (*list of string*): A list of page titles that redirect to this page.

## Example usage

The following example shows how to use the dataset to build a corpus of lead paragraphs from articles.

```python
from datasets import load_dataset

# Load the dataset in streaming mode to avoid downloading it all at once
dataset = load_dataset("singletongue/wikipedia-paragraphs", name="enwiki-20260607-v1.2.1", split="train", streaming=True)

# Define a function to filter for relevant article pages
def filter_example(example):
    # Keep only article pages
    if example["page_type"] != "article":
        return False
    
    # Exclude articles that are just lists
    if example["title"].startswith("List of"):
        return False
    
    # Exclude disambiguation pages
    if "Disambiguation" in example["templates"]:
        return False
    
    return True

dataset = dataset.filter(filter_example)

# Define a function to extract and combine all paragraphs from the lead section
def get_lead_paragraph_text(example):
    lead_paragraphs = []
    for text, section in zip(example["paragraph_texts"], example["paragraph_sections"]):
        if section == "__LEAD__":
            lead_paragraphs.append(text)
    
    # Join the paragraphs into a single string, replacing newlines with spaces
    return {"lead_paragraph_text": " ".join(lead_paragraphs).replace("\n", " ")}

dataset = dataset.map(get_lead_paragraph_text)

# Take the first 100 articles and save their lead paragraphs to a file
with open("corpus.txt", "w") as fo:
    for example in dataset.take(100):
        print(example["lead_paragraph_text"], file=fo)
```

## Dataset creation process

This dataset is created from the [Wikipedia CirrusSearch dumps](https://dumps.wikimedia.org/other/cirrussearch/) and [Wikimedia Enterprise HTML dumps](https://dumps.wikimedia.org/other/enterprise_html/).
We also utilized the [Wikimedia REST API](https://www.mediawiki.org/wiki/Wikimedia_REST_API) to fetch HTML content that was missing from the dumps.

The code used for creating this dataset is available in the [GitHub repository](https://github.com/singletongue/wikipedia-paragraphs).

## License

This dataset is available under the [CC-BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) and [GFDL](https://www.gnu.org/copyleft/fdl.html) licenses.

## Limitation

This dataset is created from specific snapshots of Wikipedia.
It may contain outdated information or content that is no longer available on Wikipedia, as well as material that may be considered inappropriate.
