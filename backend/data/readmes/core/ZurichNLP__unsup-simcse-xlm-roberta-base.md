---
language:
  - multilingual
  - af
  - am
  - ar
  - as
  - az
  - be
  - bg
  - bn
  - br
  - bs
  - ca
  - cs
  - cy
  - da
  - de
  - el
  - en
  - eo
  - es
  - et
  - eu
  - fa
  - fi
  - fr
  - fy
  - ga
  - gd
  - gl
  - gu
  - ha
  - he
  - hi
  - hr
  - hu
  - hy
  - id
  - is
  - it
  - ja
  - jv
  - ka
  - kk
  - km
  - kn
  - ko
  - ku
  - ky
  - la
  - lo
  - lt
  - lv
  - mg
  - mk
  - ml
  - mn
  - mr
  - ms
  - my
  - ne
  - nl
  - 'no'
  - om
  - or
  - pa
  - pl
  - ps
  - pt
  - ro
  - ru
  - sa
  - sd
  - si
  - sk
  - sl
  - so
  - sq
  - sr
  - su
  - sv
  - sw
  - ta
  - te
  - th
  - tl
  - tr
  - ug
  - uk
  - ur
  - uz
  - vi
  - xh
  - yi
  - zh
license: mit
pipeline_tag: feature-extraction
---

[xlm-roberta-base](https://huggingface.co/xlm-roberta-base) fine-tuned for sentence embeddings with [SimCSE](http://dx.doi.org/10.18653/v1/2021.emnlp-main.552) (Gao et al., EMNLP 2021).

See a similar English model released by Gao et al.: https://huggingface.co/princeton-nlp/unsup-simcse-roberta-base.

Fine-tuning was done using the [reference implementation of unsupervised SimCSE](https://github.com/princeton-nlp/SimCSE) and the 1M sentences from English Wikipedia released by the authors.
As a sentence representation, we used the average of the last hidden states (`pooler_type=avg`), which is compatible with Sentence-BERT.

Fine-tuning command:
```bash
python train.py \
    --model_name_or_path xlm-roberta-base \
    --train_file data/wiki1m_for_simcse.txt \
    --output_dir unsup-simcse-xlm-roberta-base \
    --num_train_epochs 1 \
    --per_device_train_batch_size 32 \
    --gradient_accumulation_steps 16 \
    --learning_rate 1e-5 \
    --max_seq_length 128 \
    --pooler_type avg \
    --overwrite_output_dir \
    --temp 0.05 \
    --do_train \
    --fp16 \
    --seed 28852
```

## [Citation](https://arxiv.org/abs/2305.13303)
```bibtex
@inproceedings{vamvas-sennrich-2023-rsd,
      title={Towards Unsupervised Recognition of Token-level Semantic Differences in Related Documents},
      author={Jannis Vamvas and Rico Sennrich},
      month = dec,
      year = "2023",
      booktitle = "Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing",
      address = "Singapore",
      publisher = "Association for Computational Linguistics",
}
```
