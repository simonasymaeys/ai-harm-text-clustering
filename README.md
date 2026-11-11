# Discovering AI Harm Themes Through Text Clustering

An exploratory machine-learning project examining whether reports about AI incidents and potential harms can be organised into meaningful themes for AI governance. The analysis compares text representations and clustering methods, then investigates whether the groups reflect shared harms, company names or news coverage.

**[Read the illustrated research report (PDF)](AI_Harm_Clustering_Report_Simona_Barbuceanu%20%282%29.pdf)** · **[Explore the full notebook](notebooks/clustering_capstone%20%283%29.ipynb)**

## Research question

> To what extent can text clustering reveal recurring AI harm themes in OECD AIM reports, rather than simply grouping reports about the same company or news story?

The intended use is an initial reading aid for governance reviewers. The study investigates whether related descriptions can be brought together to support human examination. It does not establish a validated harm taxonomy or demonstrate improved review performance.

## Why this matters

Reports about AI can describe similar concerns using different language. Equally, descriptions of different harms can share the same company names, products or legal vocabulary.

Understanding that distinction matters for:

- governance teams organising reports for review;
- policy teams identifying questions for consultation and scenario planning;
- researchers examining patterns and biases in reported AI harms; and
- reviewers considering concerns that receive less media attention.

A large cluster does not necessarily represent a common or severe harm. Repeated reporting and prominent news stories can also influence its size.

## Dataset

The analysis uses a fixed collection from the [OECD AI Incidents and Hazards Monitor](https://oecd.ai/en/incidents).

| Characteristic | Study sample |
|---|---:|
| Reporting period | 1 July-30 September 2026 |
| Reports collected | 1,889 |
| Reports provisionally retained | 1,845 |
| Proposed exclusions | 6 |
| Cases held for further scope/source checks | 38 |

Title and summary text are used for clustering. Existing concept tags and other metadata are excluded from the feature matrix.

The records are media-based descriptions of incidents and hazards, rather than independently verified events. Targeted preliminary screening covered 181 summaries; the retained corpus remains provisional.

Original exported titles and summaries are not included in this repository while redistribution conditions are being clarified. Data-access and loading instructions are provided in [data/README.md](data/README.md).

## Workflow

The notebook documents the complete exploratory process:

1. Problem framing, intended beneficiaries and working hypotheses
2. Dataset selection, provenance and collection checks
3. Profiling, missing values, relevance screening and possible event overlap
4. Text cleaning and word/phrase TF-IDF features
5. Comparison with 100-component latent semantic analysis (LSA)
6. K-means, average-linkage hierarchical clustering and DBSCAN experiments
7. Evaluation of separation, coverage and cluster sizes
8. Random-start, subset and input-sensitivity checks
9. Cluster interpretation and examination of mixed groups
10. Reflection and a non-technical impact brief

## Method comparison and selection

The main grid contains **28 configurations**, comparing:

- **K-means:** 4, 6, 8, 10 and 12 clusters on TF-IDF and normalised LSA features;
- **Hierarchical clustering:** the same cluster-count grid, using average linkage and cosine distances on both representations; and
- **DBSCAN:** four cosine-distance radii and two minimum-sample settings on LSA features.

For a reading queue covering the whole corpus, the exploratory selection rule required full coverage, 4-12 groups, at least 20 reports per group and no group containing more than 45% of reports. The highest original-space cosine silhouette among eligible configurations determined the selected candidate.

These are analyst-defined constraints, not externally validated workflow requirements. A further **eight K-means configurations** examine 14-20 clusters without changing the main selection rule.

## Main results

The selected candidate is **K-means on normalised LSA-100 features, with 12 clusters**.

| Measure | Result |
|---|---:|
| Reports assigned | 1,845 (100% of the main subset) |
| Smallest / largest cluster | 45 / 370 reports |
| Cosine silhouette in original TF-IDF space | 0.027 |
| Cosine silhouette in fitted LSA space | 0.120 |
| Reports with negative original-space silhouette | 21.1% |
| Agreement across additional random starts (ARI) | 0.573-0.671 |
| Agreement after masking ten company/product names (ARI) | 0.647 |

The groups overlap substantially and membership changes under alternative inputs and random starts. ARI measures agreement between partitions; it is not the percentage of reports remaining in their original groups. Scores in different feature spaces should not be treated as directly equivalent evidence of quality.

The wider experiment reaches an original-space silhouette of 0.033 at 20 clusters. Twelve groups therefore represent the study's operational ceiling, not a demonstrated natural number of AI harm categories.

## What the clusters suggest

Recognisable candidate themes include fraud and impersonation, privacy and surveillance, synthetic media, sexual-image abuse, automated-driving safety and data-centre resource concerns.

The mixed groups reveal why interpretation requires care:

| Candidate group | Different concerns brought together | Governance implication |
|---|---|---|
| Platform content, rights and litigation | Child protection and creative rights | Safeguarding and licensing require different review questions, even when reports share platform or litigation vocabulary. |
| Chatbot, product and social concerns | Employment impacts and reliance on unreliable outputs | Workforce transition and output validation should not be treated as one mechanism. |
| General warnings and regulation | Broad future-risk debate and financial-system vulnerabilities | Record the evidence, harm pathway and time horizon; distinguish actual events from potential harms and commentary. |

These are provisional interpretations of keywords and selected descriptions, not independently validated categories or newly fitted subclusters.

## Implications for AI governance

The findings support testing clustering as a supervised reading aid:

- use candidate groups to organise reading and suggest questions;
- retain uncertainty and permit multiple themes per report;
- verify sources and separate repeated coverage from different events;
- consider smaller groups alongside the most-covered topics; and
- evaluate practical usefulness with reviewers before operational use.

Cluster membership alone should not determine severity, compliance, responsibility or policy priorities. No time saving or improvement in decisions has been demonstrated by this study.

## Project files

| File or folder | Purpose |
|---|---|
| [Research report](AI_Harm_Clustering_Report_Simona_Barbuceanu%20%282%29.pdf) | Illustrated overview of the methods, findings and governance implications |
| [Analysis notebook](notebooks/clustering_capstone%20%283%29.ipynb) | Executed analysis, reflection and impact brief |
| `data/` | Collection information, preliminary review annotations and data-loading instructions |
| `results/` | Saved aggregate metrics and arrays used to reproduce figures |
| `requirements.txt` | Analytical dependencies and Jupyter requirements |

## How to run

Use **Python 3.12**. Download or clone the repository, then install the dependencies and launch JupyterLab:

```bash
python -m pip install -r requirements.txt
jupyter lab
```

Open `notebooks/clustering_capstone (3).ipynb` and run the cells in order.

Three modes are documented in notebook Section 2.4:

- **Aggregate replay:** available with the repository files alone. Saved figures and tables are rebuilt; clustering is not recomputed.
- **Exact recomputation:** requires the separately held source CSV at `data/oecd_aim_q3_2026.csv`. A checksum verifies the studied snapshot before the analysis runs.
- **New snapshot:** uses a separately collected CSV and `CAPSTONE_SNAPSHOT_MODE=new`. Results are written separately, old review judgements are reset and recorded theme interpretations are disabled.

The analysis processes text locally and does not send it to an external AI service.

## Limitations and future work

Media attention is selective; summaries can contain errors; several reports may concern the same event. Relevance screening is incomplete, and neither independent thematic coherence nor workflow benefits have been established. Rare-term filtering may also suppress unusual but important concerns.

The next steps are to complete scope and event checks, conduct an independent reviewer audit, compare sentence embeddings, repeat the analysis on another quarter and evaluate assisted reading against an ordinary review workflow.

## Source and attribution

Source collection: OECD.AI, *AI Incidents and Hazards Monitor*, reports dated 1 July-30 September 2026, retrieved 23 October 2026. See the [monitor](https://oecd.ai/en/incidents) and its [methodology and disclosures](https://oecd.ai/en/incidents-methodology).

Interpretations and recommendations are project findings and should not be read as OECD-endorsed conclusions. No open licence for the exported source text is asserted.

## Author

**Simona Barbuceanu**  
BSc Artificial Intelligence & Sustainable Technologies, Tomorrow University  
Clustering capstone exploring applications to AI governance
