# Revision notes — 30 October 2026

## Overall assessment
The notebook covers the assignment: problem framing, dataset exploration and cleaning, feature preparation, multiple clustering algorithms, parameter choices, evaluation, visualisations, reflection and an accessible impact brief. The wider-k experiment and fixed-seed subset diagnostic are useful additions. Weak separation is a legitimate exploratory finding when its implications are reported honestly.

## Corrections made
1. Replaced assertions of seven validated harm mechanisms with provisional thematic interpretations. Military autonomy is an application area; the licence-plate group may be product-led, and Flock is outside the ten-name detector. No independent coherence audit has been completed.
2. Removed the untested time-saving claim and assertions about existing reviewers' workloads/workflows. The dataset averages around 630 reports per month; it does not measure what any team receives.
3. Clarified that ordinary K-means fits Euclidean distances, while evaluation and the other tested distance-based methods use cosine. Normalisation reduces vector-magnitude effects but does not guarantee absence of length or selection bias.
4. Corrected the length box plot: Tukey whiskers now end at observed values inside the 1.5-IQR fences, rather than at the fence coordinates. The aggregate histogram supplies the exact lengths without source text.
5. Prevented new snapshots from inheriting relevance and event flags by ID alone. Same IDs can contain revised content. New mode now resets all reviews and always suppresses the old analyst interpretations. Exact-mode label alignment compares complete recorded profiles rather than one keyword per cluster. This is a sanity check, not semantic validation.
6. Qualified the fixed-seed subset interpretation: the observed ARI ranges overlap, but these few runs do not isolate causal contributions of sampling and initialisation. Using the same seed on a changed subset does not guarantee identical starting centres.
7. Shortened the impact brief to about 820 words, retaining its two charts and action table. Clarified that hypotheses and cluster readings are exploratory, not confirmatory tests.
8. Removed the unverified claim of university-policy compliance and added a student confirmation note on the first-person reflection and AI-assistance disclosure.

## Before submission
- Confirm that first-person statements accurately describe your work, decisions and understanding. In particular, distinguish AI-assisted preliminary screening from your own or independent expert reading.
- Check the university's actual assistance-disclosure requirements.
- Ensure your assessor has an appropriate way to obtain the exact source snapshot for full recomputation. The ZIP runs without it only in explicitly labelled aggregate replay.
- Keep conclusions exploratory unless scope and source verification and an independent coherence audit are completed. Those are material limitations, not findings that the code tests can resolve.

No model result was improved or replaced to make the conclusions look stronger; all recorded numerical findings reproduced.

## Added mixed-cluster interpretation
Section 6.1a now distinguishes two evidenced candidate subthemes each within C2, C3 and C11; explains their shared vocabulary, different governance implications and proposed review routes; and states selection and verification limits. Six example IDs were checked against the saved partition. The impact brief no longer interprets ARI as a percentage of reports moving groups. Model fitting and numerical results are unchanged.
