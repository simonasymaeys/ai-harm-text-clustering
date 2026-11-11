# Source-data access and loading

The same steps appear in Section 2.4 of the notebook.


The source text is deliberately omitted while OECD reuse clarification is pending. This package does not resolve processing or redistribution rights. It includes aggregate analytical outputs and our ID-keyed review annotations. Do not interpret those flags as verified source claims.

## Exact reproduction using the already collected sample

The separately held `oecd-aim-jul-sep-2026-reviewed-sample.zip` contains the original seven-column file `oecd-aim-2026-07-01-to-2026-09-30.csv`. Extract that CSV and place a byte-for-byte copy here as `oecd_aim_q3_2026.csv`. Do not re-save it in Excel. Its SHA-256 is:

`bcaf26d36fe5634c267188d39aece923e4b13f6f6464a5deea9208409d166da1`

The notebook validates this exact snapshot before computing. That earlier sample package contains source text; it is not included in this submission ZIP and should not be publicly redistributed without resolving the terms. If an assessor needs full recomputation, arrange appropriate source access or seek confirmation of permitted private academic sharing.

## Obtain a new snapshot from the external source

1. Visit https://oecd.ai/en/incidents and select the report-date period 1 July–30 September 2026. Confirm exported dates rather than relying only on displayed URL filters.
2. Use the official download function. In the studied collection, a download returned at most 100 rows. Start with the latest date and work backwards; include each preceding batch's oldest day in the next batch to avoid losing reports on partial boundary days. If a single day exceeds the cap, obtain an official complete export rather than claiming completeness.
3. Preserve each export and record selected ranges, file dates and counts. Combine by ID, retaining the seven source fields, and trim dates inclusively. Reconcile unique counts with the site's quarter count at your collection time; inspect boundary coverage and conflicting duplicate IDs.
4. The helper `load_exports.py` can combine local official Excel exports and create a candidate CSV; it does not automate the website or assert access permissions.
5. The site can revise historical data. A new snapshot may not match the study checksum or IDs. Keep it as a separately versioned dataset and run the notebook in new-snapshot mode: save the file as `data/oecd_aim_new_snapshot.csv` and start Jupyter with `CAPSTONE_SNAPSHOT_MODE=new jupyter lab`. That mode relaxes only the exact-snapshot checks, marks every report `unreviewed_new_snapshot` without carrying forward ID-keyed judgements, writes to `results_new_snapshot/` and replaces theme labels with top terms. Re-review annotations before interpreting themes; unchanged IDs do not guarantee unchanged report text. Do not disable the checksum and call it an exact reproduction.

## Bundled files

- `review_annotations.csv`: IDs and researcher flags only; full relevance adjudication remains incomplete.
- `collection_manifest.json`: collection counts and overlapping batch dates recorded in the earlier collection.
- `load_exports.py`: optional local loading logic for independently obtained exports.

Without source text, running the notebook reproduces saved figures from aggregates and explicitly reports AGGREGATE REPLAY. It does not silently rerun text clustering. No source-text API endpoint or automatic complete-download route has been established.
