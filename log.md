# Ingest Log

## [2026-07-29] ingest | NotebookLM Light Notes
- Successfully extracted "Light" notes from NotebookLM.
- Note on citations: The NotebookLM tool generated inline bracketed citation numbers (e.g. `[16]`) but completely failed to provide the corresponding mapping to the actual source document names due to a server-side bug.
- Updated `Light/Wave Nature.md` with synthesized notes.
- *Ingest halted due to NotebookLM server unresponsiveness for remaining queries (Eye, Colors, Painting).*

## [2026-07-29] ingest | NotebookLM All Notes
- Re-ran ingestion for Light (now with proper citations).
- User manually supplied notes for Eye, Colors, and Painting due to NotebookLM automation issues.
- Programmatically parsed and synthesized the notes into the 44 remaining wiki stubs.
- No major contradictions flagged. Citations preserved correctly.


## [2026-07-30] ingest | Handprint Color Theory & Pigments
- Scraped 24 key pages from Handprint (both color theory and watercolor pigments).
- Saved raw markdown to `raw_sources/handprint/`.
- Programmatically appended Handprint Perspectives to the bottom of 16 wiki stubs to preserve the unique voice.


## [2026-07-30] ingest | Handprint Redo
- Completely replaced previous Handprint copy-paste ingestion with high-quality, paraphrased LLM synthesis across all 17 target pages.
- Verified compliance with verbatim quote limit and correctly utilized internal wiki cross-references.


## [2026-07-30] ingest | Contradiction Consolidation
- Merged the categorical vs continuous rule fallacy (primary colors/geometric harmony) into Intersections/Optical vs. Physical Mixture.md.
- Sharpened the CIE Systems contradiction regarding perceptual uniformity vs mixture predictability.
- Refined scattered mentions into short cross-referential pointers.

## [2026-07-30] chore | Full Lint & Structural Fixes
- Fixed 11 broken links caused by punctuation/spacing mismatches.
- Created the 4 missing top-level section pages (Light, Eye, Colors, Painting) to provide structural hierarchy.
- Updated index.md to include dynamic 1-line summaries for all pages.
- Embedded newly flagged Handprint contradictions into Eye/Anatomy.md and Painting/Pigments/Particle Size-Tinting-Polymorphism.md.

