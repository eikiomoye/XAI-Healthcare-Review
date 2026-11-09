# Explainable AI in Healthcare: Survey Companion

Reference catalogue and structured reading materials for:

**Mienye, I. D., Obaido, G., Jere, N., Mienye, E., Aruleba, K., Emmanuel, I. D., and Ogbuokiri, B. (2024). A survey of explainable artificial intelligence in healthcare: Concepts, applications, and challenges.** *Informatics in Medicine Unlocked*, 51, 101587.

**Read the paper:** https://doi.org/10.1016/j.imu.2024.101587

## About this repository

Prepared from the final published PDF supplied by co-author Ikiomoye Douglas Emmanuel. This companion organises the survey's reference list, explainability approaches, evaluation dimensions and application themes into readable documentation and machine-readable files.

The paper is a survey, not a newly executed clinical prediction benchmark. No patient dataset, trained diagnostic model or original experiment code was supplied or is claimed here. All catalogue files and the search utility were created for this companion on 9 November 2026. They are not the original authors' search logs, screening decisions or data-extraction sheets.

## Contents

| Resource | Contents |
| --- | --- |
| `catalogue/references.csv` | All 131 numbered references extracted from the survey, with source pages |
| `catalogue/references.json` | The same reference inventory in JSON |
| `catalogue/methods.csv` | 12 explainability approaches, linked to survey sections |
| `catalogue/evaluation_dimensions.csv` | Fidelity, interpretability, stability, completeness and sparsity |
| `catalogue/application_areas.csv` | Four application areas from Section 7 |
| `catalogue/research_directions.csv` | Six future-work themes from Section 9 |
| `docs/READING_GUIDE.md` | A route through the survey and its supporting literature |
| `docs/PROVENANCE.md` | Extraction process, limitations and authorship attribution |
| `tools/search_catalogue.py` | New, standard-library-only reference search tool |
| `CITATION.cff` and `paper.bib` | Citation metadata for the seven-author paper |

## Research themes

The survey considers transparent model structures and post-hoc explanation methods, including decision trees, rule-based systems, attention, Grad-CAM, Bayesian networks, SHAP, LIME, PDP, ICE, surrogate models, counterfactuals and permutation importance. It discusses evaluation, responsible AI and applications in clinical decision support, personalised medicine, imaging and telemedicine.

Method summaries follow the paper's organisation. The `companion_note` fields add explicitly identified methodological cautions and reading questions. For example, model reliance should not be treated as causality, and an explanation should be assessed for its intended audience and task. These notes are not new clinical validation findings.

## Search the reference catalogue

Requires Python 3.10 or later. No third-party packages are needed for searching.

```bash
python tools/search_catalogue.py --query "explainable" --limit 10
python tools/search_catalogue.py --query "Lundberg" --json
python tools/search_catalogue.py --reference 104
```

The tool searches extracted citation text. It does not search article full texts or verify the cited studies. Without filters, it shows the first ten records. CSV and JSON files can also be opened directly in a spreadsheet editor or analysis tool.

## How to interpret the catalogue

**131 references means 131 numbered bibliography entries.** It does not mean 131 included clinical studies, 131 independently reviewed papers or a PRISMA screening result. The bibliography also contains methodological and background literature from other domains. Bibliographic metadata and claims about individual cited studies have not all been independently checked against their original publications.

Text extraction can retain line-wrap hyphens or imperfect glyphs. Citation text is therefore labelled `extracted_from_survey_not_independently_verified`; consult the cited source before reusing a reference. No DOI or paper title has been guessed for missing metadata. Use the final PDF as the source of truth for ambiguous typography.

This companion reflects the 2024 survey. It is not an updated literature search, a current regulatory review or a validated decision tool for clinical care.

## Authorship and attribution

All seven paper authors are credited in their published order. The published CRediT statement lists Ikiomoye Douglas Emmanuel's roles as **Writing - review and editing; Writing - original draft; Validation**. The companion does not infer exclusive authorship or leadership beyond that statement.

The source paper is available under CC BY 4.0. See [LICENSE.md](LICENSE.md) for attribution and the terms applying to article-derived companion material and the new search utility.

## Citation

Please cite the research paper using `CITATION.cff` or `paper.bib`. If discussing the extracted catalogue, also identify it as a companion derived from the published survey on 9 November 2026. The software utility did not exist as part of the reported survey and should not be cited as original experimental code.
