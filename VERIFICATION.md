# Review verification — 30 October 2026

- The separately attached notebook and the notebook inside the supplied ZIP were byte-identical before revision.
- Every code cell of the revised analysis was executed sequentially in a fresh local IPython session using the exact source CSV (SHA-256 bcaf26d36fe5634c267188d39aece923e4b13f6f6464a5deea9208409d166da1).
- All 28 main configurations and the 8 wider-k configurations reproduced the uploaded results. The recorded summary differed only in the Python patch version. The selected model and substantive numerical findings were unchanged.
- All 24 code cells also ran without errors in a separate fresh session with the source CSV absent. That test explicitly replayed saved aggregates; the delivered notebook retains full-computation outputs.
- Targeted regression checks confirmed that new-snapshot mode resets all old review flags, including where the same ID has changed text, and disables old analyst labels even if the profiles happen to match.
- Notebook structure was validated with nbformat. All nine embedded figures were visually inspected, including the corrected Tukey whiskers derived from the aggregate length histogram.
- The impact brief contains approximately 820 words, two charts and one action table.
- The source CSV, original titles/summaries, original Excel exports and temporary replay notebooks are absent from the ZIP. No source-text redistribution right is asserted.

Execution used an in-process IPython interpreter; a separate socket-backed Jupyter kernel/front-end was not tested in this review. Full new-snapshot clustering was not rerun; its changed review-reset and label branches were tested directly.

These checks verify computation and packaging, not source accuracy, complete relevance screening, independent thematic coherence, usability benefits or university-policy compliance.

## Interpretation addition
The six illustrative IDs were checked against the saved full-run cluster assignments and the source CSV. This verifies membership and what the exported descriptions discuss, not their underlying claims. The addition is explanatory markdown, with no changes to fitting, metrics or plotting logic.
