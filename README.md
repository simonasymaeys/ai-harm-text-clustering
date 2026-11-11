# Clustering capstone - Simona Barbuceanu
## 📓 [Open the full notebook](notebooks/clustering_capstone(3).ipynb)

Explore the analysis, visualisations, findings and impact brief.

Open `notebooks/clustering_capstone.ipynb`. It contains the complete study, results, reflection and non-technical impact brief. It is an exploratory study with provisional relevance screening, not a verified taxonomy of AI harms.

## Run

Use Python 3.12 (pandas 2.2.3 does not run on Python 3.14). Install the pinned packages (`python -m pip install -r requirements.txt`), start JupyterLab from this folder (`jupyter lab`) and open the notebook.

- **Without the source CSV (default):** every cell runs in clearly labelled aggregate-replay mode. Figures and tables are rebuilt from `results/`; clustering is not recomputed.
- **With `data/oecd_aim_q3_2026.csv`:** checksum-verified exact recomputation of exploration, all 28 experiments, stability, sensitivity and the Section 5.3 extension.
- **With a newly collected snapshot:** set `CAPSTONE_SNAPSHOT_MODE=new` and place the file at `data/oecd_aim_new_snapshot.csv`; results go to `results_new_snapshot/` and are labelled as a different dataset.

Section 2.4 of the notebook gives the full data-access steps; `data/README.md` repeats them. The analysis uses local libraries only and sends no text to external services. Original titles and summaries are omitted while reuse clarification with OECD is pending, so the folder uses the assignment's loading-logic option.

## Contents

- `notebooks/clustering_capstone.ipynb`: the single, self-contained analysis notebook.
- `data/`: data-access instructions, collection manifest, ID-keyed review flags and the export-combining helper.
- `results/`: aggregate experiment metrics, profiles, exploration aggregates and plotting arrays; no titles or summaries.
- `requirements.txt`: tested package versions.
