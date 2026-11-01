# RBD DMS Effect Prediction

RBD DMS validation results with ESM-2 and structure features

# RBD DMS Effect Prediction

This dataset contains summary tables from a computational biology project analyzing RBD deep mutational scanning (DMS) effect prediction.

The project evaluates whether mutation-level features, structure-derived annotations, reference ESM-2 residue embeddings, and mutant-sequence delta ESM features can reproduce experimentally measured receptor-binding and expression/folding scores.

The main purpose of this dataset is to compare different validation settings and distinguish easy interpolation from difficult extrapolation.

## Included validation settings

* Background-held-out validation
* Mutation-held-out validation
* Site-held-out validation
* Delta ESM validation
* Grouped feature-importance analysis
* Difficult-site analysis

## Main finding

The model performs well when predicting new substitutions at already represented residue positions. However, generalization to completely unseen residue positions remains difficult.

This means the model is useful for DMS effect reproduction and known-site interpolation, but it should not be interpreted as a fully general predictor of unseen residue effects.

## Included files

This dataset includes:

* background-held-out validation summary
* mutation-held-out validation summary
* delta ESM site-held-out summary
* delta ESM mutation-held-out summary
* grouped permutation feature-importance results
* difficult-site analysis results
* English and Korean project summaries

## Interpretation

The key result is not simply that some models achieved high performance. Rather, this project shows that biological effect prediction models can look accurate under easier validation settings while still failing under strict unseen-site validation.

Therefore, this dataset is intended to support analysis of interpolation versus extrapolation in protein mutation-effect prediction.

출처: Kaggle (binivin/rbd-dms-effect-prediction)
태그: biology, health, computer science
라이선스: Apache 2.0
수정일: 2026-06-04T18:13:32.520Z
