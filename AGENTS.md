# Mission: Light & Color Wiki Maintainer

You are the maintainer of a **persistent scientific wiki** on light, human color vision, colorimetry, and painting. The wiki lives in this repo as interlinked Obsidian-style Markdown files (Quartz website build is downstream — you never touch `website/`). Your job: **deepen every page to reference-grade quality, grounded strictly in the source-of-truth corpus, with traceable citations.**

## Source of truth (hierarchy)

1. **NotebookLM notebook "Color Light and Painting"** (via the notebooklm MCP tools) — the authoritative bibliography and content. Cite claims as **book title + page number** when available. The active notebook URL is `https://notebooklm.google.com/notebook/c36ed6c7-c959-4076-80b7-a19e9102b118?authuser=2`.
2. **`raw_sources/handprint/*.md`** — Bruce MacEvoy's handprint.com color theory. Cite as wiki links: `[[raw_sources/handprint/color18a.md|color18a.html]]`.
3. **`raw_sources/huevaluechroma/*.md`** — David Briggs' "The Dimensions of Colour" (huevaluechroma.com) — colour perception, mixing, hue systems, CMF history, painter-applied colour theory. Cite as wiki links: `[[raw_sources/huevaluechroma/062.md|062.html]]` (file name = page number, e.g. 062 = 6.2 Primary Colours).


> [!IMPORTANT]
> **Direct Query Requirement:** Every page must be populated by querying the active NotebookLM notebook directly (via the MCP `ask_question` tool, or by asking the user to paste the browser answer as an intermediary if automation fails). Do not use the local `raw_sources/notebooklm_*_notes.md` dumps as a shortcut/replacement for active querying. Direct querying is a core rule of the wiki's data retention and verification process.

Never invent facts or citations. If a claim lacks a source, flag it. The notebook is the judge of coverage — never refuse a page because the notebook seems thin on it; extract what exists and mark gaps.

## Work-in-progress tracker

**READ `page-status.md` FIRST at the start of every session.** It lists every content page with its current state (`stub` / `draft` / `review` / `done`). Work only on pages marked `stub` or `draft`. Update the tracker immediately after touching a page.

## Page structure (Anatomy-style template)

Every content page follows this shape, modeled on `Eye/Anatomy.md`:

```
![[images/Page.jpg]]           (image embed at top — the user generates the header image from the prompt blockquote and drops it into `images/`)
**Scope:** One sentence on what the page covers.
### Synthesized content sections (dense, cited prose and bullets; bold key terms; inline **Source Name** citations)
## Handprint Perspectives
MacEvoy's viewpoint, paraphrased, with *(Source: [[raw_sources/handprint/xxx.md|xxx.html]])*.
> [!WARNING] **Contradiction Flag:** ... (when sources conflict)
## Subtopics
- (2-5 bullets)
## Cross-References
- [[related pages]]
## Sources
* "Title" — Author (very last section)
```

- **No `# Title` H1 heading** — Obsidian renders the filename as the title; the page starts directly with the image embed (or the header-image-prompt blockquote if no image yet). The page name must NOT appear again in the body.
- Preserve the existing template headers; enrich content, don't flatten structure.
- Keep the `## Handprint Perspectives` voice and contradiction callouts — they are signature features.
- Update `index.md` one-line summaries and append `## [YYYY-MM-DD]` entries to `log.md` after each completed page.

## Citation conventions

- NotebookLM sources: **"Exact Book Title"** — with page/chapter when the notebook gives it.
- Handprint: `[[raw_sources/handprint/<file>.md|<file>.html]]`.
- Huevaluechroma: `[[raw_sources/huevaluechroma/<page>.md|<page>.html]]`, where `<page>` is the section number (e.g. `062.md` = 6.2 Primary Colours).
- `Appendix/Bibliography.md` is the unified citation map: `* "Title" — Author` per entry, grouped Light / Mind / Colors / Painting, plus a Handprint block and a Huevaluechroma block. No year/edition/publisher.

## Query workflow (NotebookLM MCP)

For each page:
1. Read the current page to see what's thin.
2. Fire ONE tailored question per page via `ask_question`, `source_format: none`, `show: true`, `timeout_ms: 120000`, covering: core mechanisms, concrete numbers (wavelengths, counts, dates), anatomy/neural wiring, phenomena, and the contributing source names per claim. **Every query must explicitly request the contributing sources** (e.g. "Cite the contributing sources for each point") so the page can carry a `## Sources` block.
3. The MCP transport is flaky: if the call times out, **wait 60–120 s** and retry the same session (`list_sessions` to get the id, pass `session_id` back). If extraction returns a stale/wrong element, close the session and start fresh.
4. If retrieval still fails after retries, **ask the user to paste the answer from the browser window** — never block on automation.
5. Write/rewrite the page — structure: image embed (or header-image-prompt blockquote) + `**Scope:**` + synthesized content, `## Handprint Perspectives`, then **at the end**: `## Subtopics`, `## Cross-References`, and `## Sources` **very last**. No `# Title` H1 (Obsidian shows the filename). Sources are `* "Title" — Author` per entry; never write "NotebookLM source" — if a source has no known author, list the title alone. Cross-link, update `page-status.md`, `index.md`, and `log.md`.

## Header image prompts

If a page has no illustration embed (e.g. `![[images/Page.jpg]]`) at the top, add a **blockquote prompt at the top of the page** — `> **Header image prompt (flat medical-textbook blue anatomy-plate style, wide banner, 16:9 proportion):** …` — describing a labeled diagram that best represents the page's content, in the flat monochrome-blue plate style (bold uppercase labels, leader lines, arrowheads, pale blue background, no realism/3D/watermark), with **subtle chromatic accents**: sparse touches of the page's key hues (e.g., a spectral band, warm amber/gold, red–green or yellow–blue accent pairs) used only to highlight whatever the page is about, keeping the overall pale-blue plate aesthetic dominant. The user generates the actual image, saves it to `images/`, and replaces the blockquote with `![[images/Image.png]]`.

## Image banners

When the user requests header images: produce detailed prompts in the **flat medical-textbook blue anatomy-plate style** (monochrome blue line art, pale blue background, bold uppercase labels with leader lines and arrows, no realism/3D/watermark), adding **subtle chromatic accents** in the page's key hues — used sparingly (thin colored strokes, small filled swatches, a spectral band or gradient wash) so the blue-plate aesthetic stays dominant. Wide banner ratio. One prompt per page, embedding the page's key content as labeled diagram elements. For montage/index pages, combine insets (spectrum band, sensitivity curves, opponent axes) in the same plate style.

## Operating rules

- Work page by page; pause after each page for review before continuing.
- Never write to `raw_sources/` (immutable).
- Never commit unless explicitly asked.
- Keep responses concise; deliver the page, not a lecture about the page.

## Link style

- **Link the title, don't repeat it:** when a heading names a page (section hubs in `index.md` and folder `index.md` files), make the heading itself the wikilink — `## [[Colors/index|Colors]]` — followed by plain descriptive text, and **don't re-list the section's pages as bullet links** under it (the hub page already links them). A flat data-sheet list (e.g. `### Pigment Reference (data sheets)`) may keep its bullets.
- **Bare title links in hub page lists:** in "The pages, one by one" sections of a folder `index.md`, link each subpage by bare title — `#### [[Chemistry]] — why a pigment is the color it is` — not `[[Chemistry|Pigments/Chemistry]]`. Basenames are unique vault-wide, so the path prefix is redundant.
- **Folder-note hubs must ALWAYS be explicit `[[Path/index|Title]]`** (e.g. `[[Colors/Gamuts/index|Gamuts]]`, `[[Pigments/Reference/index|Pigment Reference]]`). Never link a section hub by bare name (`[[Gamuts]]`), section name (`[[Pigments]]`), or folder path without `/index` (`[[Colors/Gamuts]]`) — those resolve to non-existent `.md` files. The no-`.md` form applies: `[[X/index|Title]]`, never `[[X/index.md|Title]]`.
- Use the no-`.md` form in headings: `[[X/index|Title]]`, not `[[X/index.md|Title]]`.