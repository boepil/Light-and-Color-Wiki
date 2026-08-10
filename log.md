# Ingest Log

## [2026-08-09] ingest | Visible Spectrum deep
- NotebookLM query (session `b40983ca`, direct MCP tool): Newton 1666 prism (heterogeneous differently-refrangible rays, term "spectrum" coined, components-not-modifications, continuous hues), hue wavelength ranges (violet 380-440 / blue 440-490 / green 490-575 / yellow 575-585 / orange 585-610 / red 610-760 + alternate convention 450-500/500-560/560-590/590-610/610-750), fuzzy boundaries (observer/adaptation; cornea+lens UV absorption, post-surgery near-UV; IR photons <1.8 eV), nonspectral purple/magenta → perceptual color circle, wavelength-dependent glass speed dispersion (blue slowed more).
- Rewrote `Light/The Visible Spectrum.md` in no-H1 format: header image prompt blockquote (prism dispersion plate + magenta dashed connector), Scope, 6 synthesized sections incl. hue-range table + NOTE on conventional boundaries, Handprint Perspectives (color18a six-hue taxonomy red/orange/yellow/green/blue + extraspectral violet; color11 unequal spectral luminosity — green brighter than equal blue), Subtopics, Cross-References, Sources.
- Updated `page-status.md` (→ done + next-up = Reflection vs. Emission), `index.md`, `log.md`.

## [2026-08-09] ingest | Wave Nature deep
- NotebookLM query (session `b40983ca`, direct MCP tool): EM wave definition + parameters (λ, f, amplitude, c, c = f·λ, phase), frequency↔color vs amplitude↔intensity + visible 4.28→7.50×10^14 Hz, E = hf + E(eV) = 1240/λ(nm) + worked 700 nm → 1.77 eV / 400 nm → 3.10 eV, dual nature in interactions (single-photon rhodopsin absorption, photoelectric effect, Snell refraction, prism dispersion, polarization), SPD definition.
- Rewrote `Light/Wave Nature.md` in no-H1 format: header image prompt blockquote (EM wave E/B field plate + spectral inset), Scope, 5 synthesized sections, Handprint Perspectives (color18a three photon-surface outcomes — surface scattering/whiteness, chromatic reflectance/hue, infrared/heat — + single-wavelength never-pure-cone-response < ~570 nm; intstud "colors exist in the mind ... shaped by the physical behavior of light"), Subtopics, Cross-References (incl. Chemistry link, fixed a dead [[How Light Interacts with Pigments]] link during write), Sources last.
- Updated `page-status.md` (→ done + next-up = The Visible Spectrum), `index.md`, `log.md`.

## [2026-08-09] ingest | Spectral Locus & Excitation Purity deep
- Repaired notebooklm-mcp first (GitHub issue #88 patches applied to global install `C:\Users\Boaz\AppData\Roaming\npm\node_modules\notebooklm-mcp`: auth host check accepts notebook.google.com ×5, chat.js sanitizeAnswer strips Thoughts/expand_more/expand_less, selectors.js `[role="dialog"]` → `.mat-mdc-dialog-container` ×4; `opencode.jsonc` now runs the patched copy via node with 180 s timeout — auth, query, and answers verified working).
- NotebookLM query (session `b40983ca`, direct MCP tool): locus geometry + endpoints 380–400/700–780 nm + bowed-middle rationale, line of purples extraspectral colors, dominant-wavelength construction + complements ~480+580 nm + 540c suffix, excitation purity 100a/(a+w) lever ratio + worked examples (0.20,0.45)→510 nm/30 % + (0.33,0.15)→540c/70 %, D65/E anchoring, purity ≠ perceived saturation (xy non-uniformity).
- Rewrote `Light/Spectral Locus & Excitation Purity.md` in no-H1 format: header image prompt blockquote, Scope, 5 synthesized sections, Handprint Perspectives (color18a hue-purity synonym set incl. Sättigung/excitation purity, hue↔single-wavelength match, notation 575, brown ~610 nm; color12 warm colors keep max chroma along locus), NOTE callout on purity-vs-saturation, Subtopics, Cross-References, Sources last.
- Updated `page-status.md` (→ done + next-up = Wave Nature), `index.md`, `Light/index.md`, `log.md`.

## [2026-08-09] ingest | Color Psychology & Symbolism (new Intersections page)
- New page `Intersections/Color Psychology & Symbolism.md` (Painting × Eye cross-cutting node) — per user suggestion, since the topic is neither pure biology nor pure technique.
- NotebookLM queries (6, user-pasted browser answers due to auth failure/`setup_auth` timeout at session start): (1) evidence quality behind color-emotion claims (controlled vs tradition vs anecdote), (2) cultural variation in symbolism (white/red/blue/yellow inversions), (3) Kandinsky's synesthetic doctrine + "pseudo-synesthete", (4) warm/cool physics vs learned vs convention, (5) hue vs value vs chroma separation in research, (6) appetite/retail/branding evidence base.
- Page content: evidence pyramid (red-light replication failure, pink-cell 15-min dose window, mink/red-car anecdotes), cultural symbolism (China/Japan/Africa mourning-white, imperial yellow → machinery safety), Kandinsky sound/form maps + Bauhaus dissent, warm/cool 5–7° rooms + Carlson fire/ice + ~200-year convention, dockworkers' value story, Reinhardt close-valued fields, Gage "circular arguments of opinion polls".
- Handprint Perspectives: color12 (warm/cool depth-mood effects = lightness/chroma, Ruskin 1862 quote, violet-light reversal) + color18b (universal color psychology tested ~1890–present, "consistent physiological effects don't exist", SAD white-light exception, light+chroma dominant vs hue weak, Gage no consistent color meanings in world art).
- Contradiction flag: Notebook corpus's hue-leaning color-mood claims vs Handprint's lightness/chroma attribution; both partially agree (Query 1's own red-light finding failed to replicate).
- Note: `setup_auth` failed to recover session; per AGENTS.md fallback, user pasted all 6 browser answers (no per-claim source chips preserved — attribution follows answer text + Bibliography titles). Created header-image prompt blockquote (user generates `images/` file).
- Updated `page-status.md` (→ done), `index.md`, `log.md`; backfilled Cross-References from Bauhaus + Romanticism-Turner.

## [2026-08-08] ingest | Section hub pages (Eye/Light/Colors/Painting)
- User defined final hub format in `Eye_Test.md`: no-H1, `**Scope:**`, one linked `### [[Subpage|path]]` content section per subpage, `## Related Intersections`, `## Sources` last — no Handprint, no header image, no Subpages list.
- Replicated to `Eye.md` (added missing rods/visual acuity sections per user), wrote `Light.md`, `Colors.md`, `Painting.md` from the corresponding `raw_sources/notebooklm_*_notes.md` dumps, all facts grounded in the dumps + existing deep pages, Sources canonical per Bibliography.
- Updated `page-status.md` (hubs → done), `index.md`, `log.md`.

## [2026-08-08] ingest | Impressionism deep
- NotebookLM query (5 parts: plein air + atmospheric effects + collapsible tubes c. 1860s; broken color + optical mixture + lustre/flicker; local color abandonment + cold-warm contrast; Goethe 1810 colored shadows + Chevreul 1839 simultaneous/successive contrast; serial studies Monet series + 10-20 canvases + diurnal illuminants) — user pasted browser answer.
- Verified existing `Painting/Movements & Painters/Impressionism.md` draft against notebook data; grounded Handprint citations in color12 (diurnal changes best seen from darkened-room window, Monet Rouen Cathedral series) and color11 (limited value range not flat — Monet/Whistler); added Goethe + Chevreul to Sources (canonical titles per Bibliography).
- Updated `page-status.md` (→ done), `index.md`.

## [2026-08-08] ingest | Home landing deep
- NotebookLM query ("main connections in light, the eye, color, pigment, and perception"; user pasted browser answers — extraction flaky, citation query ran separately).
- Rewrote `Home.md` in no-H1 format: header image prompt blockquote, Scope, 5-stage chain (light → pigment → eye → neural processing → V1–V4 cortex) with notebook citations + page refs, suggested reading order, Handprint Perspectives from color18a (retinal trichromatic primaries as bridging vs opponent axes of appearance; peak-chroma lightness varies around hue circle, tracking photopic sensitivity with violet exception).
- Updated `page-status.md` (→ done), `index.md`, `log.md`.

## [2026-08-08] ingest | Causal Chain from Pigments to Perception
- Processed NotebookLM query tracing the causal chain between surface pigments, human luminosity sensitivity V(λ), Pointer's Gamut, and perceived color asymmetry.
- Created new intersection page `Intersections/Causal Chain - Pigments to Perception.md` in no-H1 format with detailed citations (optimal colors step function, V(λ) 555 nm peak, Pointer's Gamut, opponent processes).
- Integrated Handprint Perspective from color12 (MacEvoy's "warm cliff" reflectance curve, warm surface colors chroma preservation).
- Updated `page-status.md` (→ done), `index.md`, `log.md`.

## [2026-08-06] ingest | Simultaneous Contrast / Constancy / Afterimages deep
- NotebookLM query (6 parts: simultaneous contrast + Chevreul 1839 + opponent/lateral inhibition; constancy + discounting + sodium lamp failure + infant 2-4 mo; afterimages fatigue 30-60 s + complements + saccades; RGB vs CMY + optical mixture; agent vs effect + twilight + gray ground; 40 s afterimage demo + Johns Flag + gray carpet) — user pasted browser answer.
- Rewrote `Intersections/Simultaneous Contrast, Color Constancy, Afterimages, Subtractive vs. Additive Mixing.md` in no-H1 format with notebook citations + header image prompt blockquote; Handprint Perspectives (color18b afterimage asymmetry + positive afterimages) + preserved Color Wheel Fallacy contradiction flag (color14).
- Updated `page-status.md` (→ done), `log.md`.

## [2026-08-06] ingest | Optical vs. Physical Mixture deep
- NotebookLM query (6 parts: definitions + pointillism/halftone/pixels; Grassmann additive laws + RGB 613/542/457 nm + CMY; RYB fallacy + red+blue≠violet + red+green surprises; Seurat/pointillism + Chevreul simultaneous contrast + vibrancy; spatial averaging vs spectral absorption; gamut hierarchy + stochastic halftone + display ~1/3) — user pasted browser answer.
- Rewrote `Intersections/Optical vs. Physical Mixture.md` in no-H1 format with notebook citations + header image prompt blockquote; preserved handprint categorical-vs-continuous contradiction callout (color14/color16/tech13) with PG7 example.
- Updated `page-status.md` (→ done), `log.md`.

## [2026-08-06] ingest | Natural Light vs Pigment Gamut + Metamerism deep
- NotebookLM query (6 parts: natural SPD state space + hierarchy; pigment reflectance 0-100%/<90% + lightness-chroma bind + subtractive loss; metamerism receptor reduction + 580 nm = R+G; illuminant metamerism + metameric pairs + color constancy; 150 hues/7M levels + Pointer 4,000 + 85,879 spectra + 8-bit; CIE built-in metamerism + spectral vs colorimetric + observer metamerism) — user pasted browser answer.
- Rewrote `Intersections/Natural Light Gamut vs. Pigment Gamut - Metamerism.md` in no-H1 format with notebook citations + header image prompt blockquote; Handprint Perspectives (color18a yellow+orange filter thought experiment + mixing rule 42; tech13 grays/dull metamerism).
- Updated `page-status.md` (→ done), `log.md`.

## [2026-08-06] ingest | Perceptual Uniformity (Lab/Munsell) deep
- NotebookLM query (6 parts: xy non-uniformity + MacAdam/Munsell 1.0 vs 3.86 evidence; JND + tolerances + ΔE; Lab cube-root L* + opponent a*b* + Euclidean ΔE; Munsell 1905 visual scaling + 1943 3M obs/41 observers; sqrt vs cube-root scaling + cylindrical vs rectangular; blue-region 1.57x residual + CMC(l:c)/CIE94 + CIECAM) — user pasted browser answer.
- Rewrote `Intersections/Why Lab-Munsell Were Built for Perceptual Uniformity.md` in no-H1 format with notebook citations + header image prompt blockquote; Handprint Perspectives (color18a ~50 perceptible lightness levels, Gelb staircase anchoring).
- Updated `page-status.md` (→ done), `log.md`.

## [2026-08-06] ingest | Color Matching Functions deep
- NotebookLM query (6 parts: RGB matching experiments + negatives; x̄/ȳ/z̄ peaks 595-600/555/445-450 nm; V(λ) ≡ ȳ + flicker photometry + 555 nm solar tuning; 1924 blue deficiency + Judd-Vos 1988 V_M(λ); tristimulus integration X = kΣP·x̄·R + xy diagram + CIELAB; V′(λ) 507 nm + Purkinje shift + 4° crossover) — user pasted browser answer.
- Rewrote `Intersections/Color Matching Functions and the Photopic Luminosity Function.md` in no-H1 format with notebook citations + header image prompt blockquote; Handprint Perspectives (color18a peak-chroma lightness vs photopic sensitivity; color12 555→510 nm night shift).
- Updated `page-status.md` (→ done), `log.md`.

## [2026-08-06] ingest | Optimal Color Solid deep
- NotebookLM query (6 parts: 0-1 step optimal colors; Schrödinger 1919-20 ≤2 transitions + MacAdam 1935 Yxy limits; lopsided spindle shape + V(λ) 555 nm protrusion + red/blue constraints; band-pass/band-stop + convex set extremes; Pointer subset + 1943 Munsell realizability + device gaps; spectral imaging, phthalocyanines, evolutionary insight) — user pasted browser answer.
- Rewrote `Colors/Gamuts/Optimal Color Solid-MacAdam Limits.md` in no-H1 format with notebook citations + header image prompt blockquote; Handprint Perspectives (tech13 three chromaticity spaces: spectral/optimal/media).
- Updated `page-status.md` (→ done), `log.md`.

## [2026-08-06] ingest | Pointer's Gamut deep
- NotebookLM query (6 parts: 1980 study method + 4,000+ samples; definition + Illuminant C; shape/lopsidedness h_ab 150°/20° + V(λ) 555 nm; vs MacAdam limits/spectral locus/devices; industry 98% benchmarks + gamut mapping; fluorescence/gloss/ISO Reference Colour Gamut 85,879 spectra caveats) — user pasted browser answer.
- Rewrote `Colors/Gamuts/Pointer's Gamut.md` in no-H1 format with notebook citations + header image prompt blockquote; Handprint Perspectives (tech13 real surfaces duller than optimal colors; color18a optimal color definition).
- Updated `page-status.md` (→ done), `log.md`.

## [2026-08-06] ingest | Device Gamuts deep
- NotebookLM query (6 parts: primaries define gamut + display/print physics; sRGB/AdobeRGB/ProPhoto + BT.709 coordinates + coverage %; additive vs paper whitepoint/additivity failure; capture vs display vs print; ICC profiles + rendering intents + clipping; human vision 150 hues + MacAdam limits + Pointer + 10-bit) — user pasted browser answer.
- Rewrote `Colors/Gamuts/Device Gamuts.md` in no-H1 format with notebook citations + header image prompt blockquote; Handprint Perspectives (color18a color addresses, color13 CMYK vs RGB gamut).
- Updated `page-status.md` (→ done), `log.md`.

## [2026-08-06] ingest | Gamuts parent deep
- NotebookLM query (6 parts: gamut definition + representation; hierarchy eye ~7M levels → MacAdam limits → Pointer → sRGB/AdobeRGB; additive vs subtractive V(λ) limits + unwanted absorptions; spectral locus/line of purples/broadband limit; gamut mapping, clipping, ICC profiles; 1.4M distinguishable colors + triangle vs irregular geometry) — user pasted browser answer.
- Rewrote `Colors/Gamuts/Gamuts.md` in no-H1 format with notebook citations + header image prompt blockquote; Handprint Perspectives (color13 CIELAB gamut comparison, monitor vs CMYK, 3D context-sensitive gamuts).
- Updated `page-status.md` (→ done), `log.md`.

## [2026-08-06] ingest | MacAdam Ellipses deep
- NotebookLM query (6 parts: 1942 JND matching procedure; size/orientation variability incl. 10:1 + green largest/blue smallest + rotation; JND steps 150-300 + quantization, 8-bit banding, 10-bit/1024 levels, 1.4M distinguishable colors; motivation for CIELAB/CIELUV + 1960 UCS uv + ΔE 1.0; Munsell 3.86x distortion + 1943 Renotation; best discrimination 495/590 nm + industry ellipsoids) — user pasted browser answer.
- Rewrote `Colors/MacAdam Ellipses.md` in no-H1 format with notebook citations + header image prompt blockquote; Handprint Perspectives (color18a spectral hue spacing: yellow/cyan discrimination, green insensitivity, violet tinting).
- Updated `page-status.md` (→ done), `log.md`.

## [2026-08-06] ingest | Munsell Notation deep
- NotebookLM query (6 parts: 3 dimensions + scales; H V/C notation + vs RGB/CMYK/CIE; Color Tree irregularity + luminosity insight; Munsell biography/pedagogy; 1943 Renotation ~3M observations + CIE anchoring; value scaling 5/ ≈ 18-20% reflectance + practical uses) — user pasted browser answer.
- Rewrote `Colors/Munsell Notation.md` in no-H1 format with notebook citations + header image prompt blockquote; Handprint Perspectives (L* = 10× Munsell value, color strength = value × chroma, tech13/color18a).
- Updated `page-status.md` (→ done), `log.md`.

## [2026-08-06] ingest | CIE Systems deep
- NotebookLM query (6 parts: 1931 founding + matching experiments; XYZ imaginary primaries + Y=V(λ); 2° vs 10° observers; xy diagram + spectral locus 380-780 nm + purples + D65; CIELAB 1976 L*a*b*/ΔE 1.0/white point adaptation; gamuts/MacAdam/1943 Munsell Renotation/CIELUV/CIECAM97) — user pasted browser answer.
- Rewrote `Colors/CIE Systems.md` in no-H1 format with notebook citations + header image prompt blockquote; Handprint Perspectives (conceptual vs material primaries, color18a) + kept perceptual-uniformity vs mixture-predictability contradiction flag.
- Updated `page-status.md` (→ done), `log.md`.

## [2026-08-06] chore | Eye format conversion
- Removed `# Title` H1 headings from all `Eye/` pages (Obsidian renders the filename as the page title): Wavelength Perception, Opponent-Process Color Coding; normalized Anatomy's `## **Scope:**` → `**Scope:**`. Visual Acuity and Rods vs. Cones were already in the new format.
- Wavelength Perception header prompt blockquote replaced by user-generated image embed.
- AGENTS.md page-structure template updated to the new no-H1 format (image embed top → Scope → content sections → Handprint Perspectives → Subtopics → Cross-References → Sources last).

## [2026-08-06] ingest | Rods vs. Cones deep + format change
- User established new page format (per Obsidian reference): no `# Title` H1 (Obsidian renders filename), image embed at top, Scope, content, Handprint Perspectives, Subtopics, Cross-References, Sources last. Visual Acuity page converted by user (prompt → real generated image).
- NotebookLM query (6 parts: scotopic/photopic + dark adaptation; counts & species variation; distribution & crossover; rod-free avascular zone; convergence; S-cone asymmetries) — user pasted browser answer.
- Rewrote `Eye/Rods vs. Cones - Density & Distribution.md` in the new no-H1 format with notebook citations; Handprint Perspectives from tech13 (mesopic vision, dusk transitions).
- Updated `page-status.md` (→ done), `log.md`.

## [2026-08-06] ingest | Visual Acuity & Receptor Spacing deep
- NotebookLM query (6 parts: sampling limit/inter-receptor spacing; foveal numbers — 350,000 cones, 2° rod-free zone, 1 arcmin, 1.67 cm, Snellen E; eccentricity fall-off 4° rods predominate, 18-20° rod peak 150k/mm²; scotopic fixation blindness, 1,000:1 rod convergence; diffraction vs spacing; microsaccades/stabilized images, Landolt C, vernier 3.6 arcsec). User pasted browser answer (MCP extraction flaky).
- Rewrote `Eye/Visual Acuity & Receptor Spacing.md` to reference-grade: header image prompt blockquote, Scope, 6 cited sections, Handprint Perspectives (spatial frequency, visual fusion ~20 cpd from color18b), end-of-page Subtopics/Cross-References/Sources per Anatomy template.
- Updated `page-status.md` (→ done), `index.md`, `log.md`.
- Note: notebook auth expired mid-session; ran Chrome kill → cleanup_data(preserve_library) → setup_auth; login window opened for user.

## [2026-08-06] ingest | Wavelength Perception deep
- NotebookLM query (6 parts: trichromatic theory; S/M/L peak wavelengths & ranges; univariance; photopigments & phototransduction; activation-ratio color coding; rod/cone counts). Extraction flaky — user pasted the browser answer per AGENTS.md fallback.
- Rewrote `Eye/Wavelength Perception.md` to reference-grade with notebook citations (cones 440-448/518-540/560-617 nm, ~580 nm → yellow, 10:1 L:M → orange-red, rods ~120M / cones 5-8M, S-cones 5-10% of cones, iodopsin/rhodopsin), added header image prompt blockquote, Handprint Perspectives, and end-of-page Subtopics/Cross-References/Sources per Anatomy template.
- Updated `page-status.md` (→ done), `index.md`, `log.md`.

## [2026-08-06] ingest | Opponent-Process Color Coding deep
- Queried NotebookLM (Color Light and Painting) for opponent-process depth: three axes & cone computations, anatomy (bipolar/ganglion, LGN parvocellular, V1 double-opponent blobs), afterimages, dual-process reconciliation, and concrete data (cone ratios 10:5:1, peak sensitivities, V(λ) 555 nm, neutral points, receptive field sizes).
- Rewrote `Eye/Opponent-Process Color Coding.md` to reference-grade with notebook citations.
- Established `AGENTS.md` mission prompt + `page-status.md` work-in-progress tracker. Appendix Bibliography (54 sources) and History & Key Figures completed earlier.

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

