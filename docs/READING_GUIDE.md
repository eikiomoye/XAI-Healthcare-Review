# Reading guide

This is a new guide to the published survey. Section and page references below locate the source material; they are not a reconstruction of the authors' original review workflow.

## 1. Establish the concepts

Start with Section 3 (page 3): transparency, trustworthiness and accountability. Read these as related design concerns rather than proof that a particular explanation establishes all three. A model can be easy to inspect yet still be inaccurate or biased.

For wider background, the survey cites its reference [21] on XAI concepts and taxonomies, [23] on XAI research directions, and [24] on black-box explanation. Use `python tools/search_catalogue.py --reference 21` to locate the extracted citation.

## 2. Compare explanation approaches

Use Section 4 (pages 3-7) alongside `catalogue/methods.csv`. Distinguish explanations arising from a model's structure from approximations or analyses applied after fitting. The survey groups attention and CNN-related explanations under model-specific approaches and discusses SHAP, LIME, PDP, ICE, surrogates, counterfactuals and permutation importance under model-agnostic methods.

The companion notes qualify that broad taxonomy: some SHAP implementations exploit specific model structures, attention weights alone do not demonstrate faithful explanation, and an explanatory counterfactual is not automatically a causal or clinically feasible intervention. Those are reading cautions, not claims of new empirical evaluation in this repository.

Useful cited starting points include [51] for Grad-CAM, [61] for LIME, [64] for ICE, [68]-[69] for counterfactual explanations, [70] for dependence-related limitations of unrestricted permutation, and [95] for SHAP. Each number refers to the survey's bibliography; individual sources should be consulted before attributing detailed findings to them.

## 3. Examine evaluation

Section 5 (pages 7-8) covers fidelity, interpretability, stability, completeness and sparsity. `catalogue/evaluation_dimensions.csv` separates each source description from a newly written practical reading question. These are dimensions with method- and task-dependent operational definitions, not a single universal validation score.

Relevant survey citations include [72]-[73] on fidelity, [74] on stability, [75] on completeness and [76] on explanation evaluation. Do not rank a system's clinical suitability solely by a feature-attribution plot or a single explanation metric.

## 4. Connect methods with healthcare contexts

Section 7 (pages 9-10) has four application areas: diagnostic tools and clinical decision support, personalised medicine, medical imaging, and remote diagnostics/telemedicine. `catalogue/application_areas.csv` indexes those areas at section level. It does not independently certify that every individual citation supports every application claim in the survey's narrative or Table 2.

The complete reference inventory includes background work outside healthcare. A catalogue search hit is not an inclusion decision or an assessment of clinical evidence quality.

## 5. Develop a research question

Read Sections 8-9 (pages 10-12) for workflow integration, fairness, explanation usability, regulatory context and longer-term evaluation. The six rows in `catalogue/research_directions.csv` summarise the future-work themes explicitly presented in Section 9.

Potential follow-on projects include a clearly labelled new comparison of explanation stability, a study of clinician-facing explanation design, or a reproducible benchmark of interpretable and post-hoc models. Such work would need its own protocol, data provenance and evaluation. It should not be presented as an experiment conducted in the 2024 survey.
