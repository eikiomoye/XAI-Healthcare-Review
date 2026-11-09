# Provenance and scope

## Authoritative source

Final published PDF supplied by the user: `1-s2.0-S2352914824001448-main.pdf`, 15 pages, DOI https://doi.org/10.1016/j.imu.2024.101587. Its SHA-256 and publication metadata are recorded in `source_metadata.json`. No changes were made to that PDF and it is not redistributed in this package.

The title page was checked visually. It credits seven authors in the order used in `CITATION.cff` and `paper.bib`. The author contribution statement on page 12 identifies Ikiomoye Douglas Emmanuel's contributions as writing the original draft, reviewing/editing and validation. The companion does not substitute a different authorship account.

## Reference extraction

The references occupy pages 12-15. Extraction used the right column of page 12, then the left and right columns of pages 13, 14 and 15 in reading order. On each page the crop excluded the running header and footer. The text was segmented at numbered bibliography markers `[1]` through `[131]`.

Whitespace was collapsed inside each citation. Typographic en/em dashes were normalised to ASCII hyphens for plain-text portability. Line-wrap hyphens and extraction imperfections may remain. The original reference numbers, source pages and source columns are retained so ambiguous text can be checked directly against the PDF.

All 131 expected numbers were found exactly once, with no missing number. This is a structural completeness check; it does not independently establish the correctness of all extracted names, DOI strings or titles. No DOI resolver links are generated from potentially imperfect reference text. Every row carries the status `extracted_from_survey_not_independently_verified`.

The bibliography includes methodological, contextual and non-healthcare sources. Its size must not be described as the number of included clinical studies or the output of a reconstructed systematic screening procedure.

## Structured summaries

`methods.csv`, `evaluation_dimensions.csv`, `application_areas.csv` and `research_directions.csv` are newly created companion summaries. Each row records the relevant survey section and page. Source summaries are paraphrased. Additional cautions or reading questions are placed in fields explicitly named `companion_note` or `companion_reading_question`.

The 12 method rows split decision trees and rule-based systems into separate entries and identify Grad-CAM within the CNN discussion. This count is a companion organisational choice, not a claim that the survey reports 12 independent experiments or a universally agreed taxonomy. SHAP is recorded under the survey's model-agnostic family, with a note that individual implementations can be model-specific.

Application mappings are at section level. No assertion is made that every reference in the source's application table has been checked against the original cited study. The reference inventory does not include newly invented dataset sizes, diagnostic performance values, screening decisions or risk-of-bias assessments.

## Validation and limits

Checks cover reference-number continuity, CSV/JSON agreement, expected catalogue counts, valid cross-references, citation author order, recorded source identity and command-line search behaviour. Validation details are recorded in `VALIDATION.json`.

The tool only searches citation metadata; no clinical data or model predictions are processed. No new literature search, model experiment, clinical validation or regulatory update has been carried out. The catalogue represents the supplied 2024 survey, not an exhaustive account of research available in 2026.

The new utility and the companion summaries should be distinguished from original materials used during the paper's preparation. Original screening/extraction files were not supplied. This package is a later research companion.
