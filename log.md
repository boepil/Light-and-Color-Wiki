# Ingest Log

## [2026-08-12] ingest | Toxicity reference page + page-structure fix
- **New page `Painting/Pigment Sources, Composition & Toxicity Reference.md`** (sequence 32) — built from the user's untracked `Painting/pigment_sources_toxicity.md` draft (family toxicity + binder tables preserved) deepened by NotebookLM session `2e6311cd` (1 direct query, 5 contributing sources) + handprint `pigmt6.md` toxicity section (lines 974–1038): family table (Cd/Co/Pb/Hg/As/Cr/Mn/Ni/Cu; cadmium vapor >700 °C, cobalt-violet arsenic, orpiment/realgar/iodine scarlet/verdigris/emerald-green); exposure routes (ingestion brush-licking + one-tube lethal dose, inhalation spray/sanding/pastel dust, skin Cu/Ni/Mn/Co sensitizers); labeling (ASTM D4236 "Conforms to", ACMI AP/CL, CS98-62, CI names on MSDS); binder/solvent risk table (benzene/carbon tet never, turpentine vs mineral spirits, TLV); historical replacements (Hansa/phthalo/cadmium red) + EU cadmium position; safe practice. Handprint Perspectives: warnings often overstate, "cadmium … overstated but do not ignore", CA never ruled a watercolor site polluted, watercolor safer than house paints. Contradiction flag: draft/notebook "High — carcinogen" rating vs insoluble-in-binder reality.
- **Renumber once more:** toxicity page inserted at sequence 32; tail ≥32 → +1 (Movements index 32→33, Pigments index 43→44, Farges 52→53, Reference 54–74→55–75, Intersections 75–83→76–84). Chain now 0 + 1–84 contiguous.
- **Page-structure fix:** `Supports & Materials.md` + `Brushes.md` — moved YAML frontmatter above the header-image prompt so the order is frontmatter → image prompt → Scope, matching `Painting/Composition.md` template (previously the prompt sat above the frontmatter, breaking the template).
- Updated `Painting/index.md` hub (toxicity section), root `index.md` (one-liner), `page-status.md` (new entry, counts 84 → 85), `log.md`.

## [2026-08-12] ingest | Appendix hub + Painting physical-stage pages (Supports & Materials, Brushes)
- **Appendix placement fix:** root cause — `Appendix/` had no `index.md`, so the quartz Explorer `sortFn` (`a.data?.sequence ?? Number.MAX_SAFE_INTEGER`) put the folder last in the sidebar while its pages (sequence 2–5) came first in PageNavigation. Created `Appendix/index.md` (sequence 2, hub format per Colors: Scope + `### [[Subpage|path]]` sections + Cross-References); removed the `# Title` H1 headers from `Bibliography.md` and `History & Key Figures.md` (no-H1 convention).
- **Renumbered whole chain 0 + 1–83 contiguous** (`Temp\opencode\renumber_appendix.py`): Appendix 2–5 → 3–6; old 6–28 → +1 (Colors 6→7 … Composition 28→29); old ≥29 → +3 (Movements index 29→32, Pigments index 40→43, Farges 49→52, Reference sheets 51–71→54–74, Intersections 72–80→75–83); new Painting pages at 30–31.
- **New page `Painting/Supports & Materials.md`** (sequence 30) — NotebookLM session `2e6311cd` (3 direct queries, no timeouts): watercolor paper (72/90/140 lb min, 250–400 lb board = no stretching, HP/CP/rough, cotton fiber, sizing, pH, blocks, "paper is the palette"); oil (linen vs cotton duck, animal-glue size prevents binder rot, white-lead oil ground vs gesso crackle, stretcher keys + cold-room warning, copper/aluminum panels); acrylic (flexible non-absorbent polymer primer); pastel tooth/tinted; gouache opaque; tempera rigid absorbent gesso; scratchboard; Mylar; white ground as "internal light" + imprimatura. Handprint Perspectives: intstud paper attributes define the gamut + staining-vs-finish (CP-of-one-brand-may-be-R-of-another), litetest Arches-on-plywood method. Contradiction flag: gesso luminosity vs crackle (resolution: rigid panel vs canvas).
- **New page `Painting/Brushes.md`** (sequence 31) — same session: anatomy (hair/ferrule vulcanized rubber/handle — short watercolor vs long oil), hair types (kolinsky sable ~$1,500/lb + snap, squirrel, hog flags, nylon, ox, camel-hair trade name), shapes (round, flat 2×, bright 1.5×, filbert, fan, liner/rigger, mop, badger blender), medium rules (watercolor soft reservoir + pointed tip + 1"-flat bead + half-charge squeeze + damp-brush lifting; oil bristle scrub-in + sable glazes + kerosene/mineral-spirits rinse; acrylic nylon + submerged while painting; gouache stiffer synthetic; tempera red sable hatching; pastel trimmed bristle), sizes No. 0–30 + fractional-inch flats, care (rinse, Murphy's Oil Soap, naphthalene, never rest on hair). Handprint: pigmt5 #6 sable pan cleaning, pigmt3 1" flat as calibrated water measure, pigmt9 lift-scrub + rinse discipline, pigmt7 gouache/watercolor brush split, pigmt6 never point brushes with lips.
- Hubs updated: `Painting/index.md` (two new `### [[…]]` sections, scope line), root `index.md` (Appendix hub line + 2 new Painting one-liners), `page-status.md` (2 new entries + Appendix hub + counts 81 → 84 + renumber note), `log.md`.
- Verified: sequence chain 0 + 1–83, no dups, no gaps (`seq_check2.py`); link audit **854 wiki links / 192 files — NO BROKEN LINKS** (`link_audit.py`).


## [2026-08-11] restructure | Pigments promoted to root section + 16 pigment data sheets
- **Restructure:** `git mv` moved `Painting/Pigments/*` → root `Pigments/` (hub `Pigments.md` → `Pigments/index.md`), the 5 essays (Chemistry, Natural vs. Synthetic, High-Chroma Synthetics, Particle Size-Tinting-Polymorphism, Sourcing Real Spectral Data) unchanged, and absorbed the experimental `Painting/Pigment Reference/PB29 - Ultramarine Blue.md` sample into `Pigments/Reference/`. All in-repo links updated (`index.md` — new `## Pigments` section with a Reference sub-list; `Painting/index.md`; Light/Wave Nature, Light/Natural Daylight, Vermeer, Turner pages).
- **Reference data sheets (16 pages, NotebookLM queries, one per pigment family, session `22b5c02b`, direct MCP tool — no timeouts):**
  - Whites/blacks: PW6 (rutile/anatase TiO₂, 1791 discovery → 1919/1923/1939/1957 grades, RI 2.55/2.71, Titanox A/B, whiteout; handprint litetest), PBk6 (amorphous carbon pure/impure, Lascaux, atramentum, 1864 furnace black, granulating weak traditional vs intense modern; handprint PBk6+PB29 neutrals).
  - Yellows: PY35 (CdS + CdS·xZnS, Stromeyer 1817–18, 1846 England, calcination, Cu/Pb incompatibility warnings — dark CuS + black PbS), PY97 (monoarylide azo, 1962 Paint Standard, non-poisonous gamboge replacement, +phthalo ≈ emerald), PY43 (goethite earth, Roussillon, granulating).
  - Reds: PR108 (CdS·xCdSe, ~1910/1919, 700–800 °C calcination, toxic-dust warning, viridian blacks), PR101 (synthetic α-Fe₂O₃, hue range to Mars violet, bricks/rouge), PBr7 burnt sienna (goethite→hematite roasting, Roman, classic glaze, rapid drier), violet oxides PV101 (protocrystalline hematite on clay, hydration-ladder table).
  - Umbers: PBr7 raw (goethite + MnO₂, Cyprus, manganese siccative rapid drier + underpainting crack caution, umber+ultramarine warm blacks), PBr7 burnt (roasted, deep warm red-brown).
  - Greens: PG18 viridian (Pannetier/Binet 1838 → Guignet 1859 → England 1862, masstone blackish, replaced verdigris), PG7 phthalo (Scottish Dyes 1927–28, ~1938, let-downs, alizarin chromatic black, black-admixture deadening + gouache drying-shift warnings).
  - Blues: PB29 ultramarine (lazurite/Badakhshan, Cennini wax-kneading, currency-grade, Mary's robe + Vermeer, Guimet 1824–1828 + 6000-franc prize + Gmelin, 3000→20–40 francs, S₃ charge transfer, scumbling), PB28 cobalt (Thénard 1802, smalt replacement, Renoir/Monet/Turner), PB35 cerulean (CoO·nSnO₂, Rowney ~1860, Impressionist sky).
  - Modern transparent: PR83 alizarin (Graebe/Liebermann + Perkin 1868, first duplicated natural dye, FUGITIVE warning, Cézanne), PV23 dioxazine (1928/~1950s, extreme staining, PV23+PG7+PB29 darks).
- Every sheet: swatch div + swatch disclaimer linking Sourcing Real Spectral Data, Scope, Identity/History/Production/Color Data sections, Munsell-not-available note, warning callouts (PbS/CuS, toxicity, fugitive, drying shift), Handprint Perspectives, Subtopics, Cross-References, Sources last.
- Updated `page-status.md` (new `## Pigments` section: 5 essays + 16 Reference sheets → done; counts 81), `index.md` (new `## Pigments` + Reference one-liners), `log.md`.

## [2026-08-11] ingest | Reflection vs. Emission deep — wiki 100% complete
- NotebookLM query (session `22b5c02b`, direct MCP tool): radiant/self-luminous sources, specular (i=r, viewer-dependent highlights revealing source shape) vs diffuse reflection, RGB additive vs CMY subtractive media (display gamut larger/more vivid, emissive black R=G=B=0 vs ambient screen limit; pigment black only dull gray + paper substrate caps), object mode (lightness) vs illuminant mode (brightness), lightness constancy, moon apparent self-luminance, 45/0 reflectance geometry vs radiometric display measurement, artists' highlights + vibrational color.
- Rewrote `Light/Reflection vs. Emission.md` in no-H1 format (kept the existing blackbody/Wien + absorption/refraction/fluorescence material, added the new sections and citations); Handprint Perspectives preserved with the additive-linear vs multiplicative-overlap contradiction flag (color18b).
- Also restored the `Light/Spectral Locus & Excitation Purity.md` tracker line after an edit accident. Updated `page-status.md` (→ done — last remaining content page), `log.md`.

## [2026-08-11] ingest | Pigments cluster complete — final wiki section (6 pages)
- NotebookLM queries (session `22b5c02b`, direct MCP tool — one per page): (1) Chemistry — pigment vs dye (insoluble, crystal-retaining particulate), inorganic ligand-field/charge-transfer (Prussian blue) vs organic chromophore/conjugated π→π\* mechanisms, narrow-band reflectance ⇒ chroma (green "window" easier than red "spike"), fading chemistry (photo-oxidation, photoreduction, CdS+Pb→PbS black, zinc soaps); (2) Natural vs Synthetic — earths (Fe/Mn oxide clays, cave 10,500 BC, France/Italy), madder/indigo/kermes-cochineal/Indian yellow (banned 1908), 1828 Guimet–Gmelin ultramarine, chromium 1797/cadmium 1817, Perkin's mauve 1856, alizarin crimson 1868, chrome-yellow darkening, modern subtle-granular vs narrow-band trade-off; (3) High-Chroma Synthetics — PB15/PG7(Cl)/PG36(Cl+Br) tetrabenzotetraazaporphin, PR122/PV19 trans-linear quinacridones, PV23 carbazole violet, chroma at dark values, CMY primaries, geranium reds formerly reproduction-only, 50–75% "let down" with inert bases; (4) Particle Size-Tinting-Polymorphism — CdS fine=yellow/coarse=orange, overgrinding chrome orange→yellow, refractive-index Δ (TiO₂ 2.5–2.7 vs oil 1.5; ultramarine ≈1.5 transparent), granulation, rub-out/volumetric/NBS Y standards, PB15 α/β polymorphism, vermilion→metacinnabar; (5) Sourcing — 380–780 nm reflectance fingerprints, drying shift (binder index ≈ pigment index ⇒ darker drier), RIT MCSL real.dat/1929.dat/ColorChecker/CERAM, Munsell Renotation 1943 limits, smalt-vs-cobalt dating, cadmium red c.1910 forgery, Pointer Gamut; (6) Pigments hub — four families (earths/synthetic inorganics/lakes/modern organics), color tree, restoration metamerism, 1704 Prussian blue → forensic dating → non-toxic frontiers.
- Rewrote all 6 `Painting/Pigments/*.md` pages in no-H1 format: header image prompt blockquotes, Scope, cited sections, Handprint Perspectives (pigmt1/pigmt3/pigmt6/pigmt8), Subtopics, Cross-References, Sources last; preserved Particle Size contradiction flag, added "natural-as-label" contradiction flag to Natural vs. Synthetic.
- Updated `page-status.md` (all 6 → done — wiki 100% complete), `log.md`.

## [2026-08-11] ingest | Movements & Painters completion (8 pages)
- NotebookLM (direct MCP): session `b40983ca` served Turner + Fauvism, then large multi-part questions repeatedly timed out (-32001, even 240 s). Diagnosed wedged session (message_count reset), switched to fresh session `22b5c02b`; oversized questions still hung, so research was split into compact single questions (43 s probe confirmed health); Bauhaus answer pasted by the user after 4 timeouts (AGENTS.md fallback).
- **Turner:** psychico-expressive color, atmospheric veil (cooler/lighter with distance; *Burning of the Houses of Lords and Commons* fire painted cool), controverted "doctrine of the balance of colors" (single point of rich brownish crimson), Newton–Goethe engagement, sun paintings/"first abstractionist". Handprint: color11 value wheel (Turner RA lectures, via Kemp), pigmt6 Winsor quip + Turner Bequest + Russell–Abney 1888.
- **Fauvism:** 1905 Salon d'Automne "fauves" label, anti-local-color, green line (*Madame Matisse*), violet-eyebrow complement vibration, "Plus c'est plat…", Gauguin/cloisonnism → Cubism. Handprint: color18b emancipation cycles, color16 complement discipline.
- **Bauhaus** (user-pasted): Vorkurs "in a vacuum", Itten's seven contrasts/12-hue circle/Runge sphere/subjective color, Kandinsky color-form coordinates + pseudo-synaesthete, Klee's middle-point-gray keystone, Albers "color deceives continually" + color-aid papers. Handprint: color18a "color crank Itten" hue-only shorthand, color18b Bauhaus surveys (no consistent effects), Kandinsky red = Russian icon corner, color13 "crackpot nonsense".
- **Post-Impressionism:** Van Gogh complements "ray of light" + Goethe shadows; Cézanne warm-cool modulations/passages; Gauguin flat symbolic color; Seurat impressioniste-luministe; flatness → abstraction. Handprint: color16 warm-focal preference, color18a late-Van Gogh pure pigments, tech13 Gauguin warm-yellow-light palette map (250 px, 9 paints).
- **Neo-Impressionism:** divisionism, touching dots, lustre, chromatic grays, dotted frames, critiques (machine-like, Rood appalled, gray-sum). Handprint: color18b rules 39–40 + broken colors; tech13 <1 octave luminous span.
- **Color Field:** vanishing boundaries, durational experience/fluting, Newman zip + wall scale, Rothko luminous film color + tragic + chapel, Reinhardt nine-square grid. Handprint: color18b universal-psychology debunk + chromatic Esperanto.
- **Op Art:** vibrating boundaries, moiré/saccades, Kitaoka snakes, Ouchi, Riley *Current* Benham effect. Handprint: color18a spatial effects ignored by traditional theory.
- **Newton's Influence:** Opticks 1704 circle, ROYGBIV unequal spacing, diatonic analogy, Newton's Rings complementarity, Le Blon/Moses Harris 1766, Goethe "fairy tale" rejection, George Field → Pre-Raphaelites. Handprint: tech13 diatonic division in wavenumber spacing + grating caveat.
- Updated `page-status.md` (all → done), `log.md`.

## [2026-08-11] ingest | Light & Appendix backfill (Illuminants, Natural Daylight, Data & Methodology, Project Notes, Composition, Movements & Painters hub, Vermeer)
- Backfilled pending log entries for pages deepened earlier today (queries were direct-MCP session `b40983ca`; details in the pages): `Light/Illuminants & Correlated Color Temperature.md` (CIE A/B/C/D50/D65/D75/F2, blackbody/Planck/Wien 2897/T, CCT table 1900–12000+ K, CRI/von-Kries limits; handprint color12 blackbody locus + CRI 100); `Light/Natural Daylight Variation & Hyperspectral Scene Data.md` (diurnal CCT phases, Rayleigh 1/λ⁴, sky 10000+ K, hyperspectral reflectance + CIE integration; handprint color12 dominant wavelength 530 nm pale-green sun); `Appendix/Data & Methodology.md` (instruments + protocols 1–20 nm/380–780 + geometries + observers, CIE pipeline X = kΣP·x̄·R·Δλ, datasets Munsell 1943/Pointer 1980/MacAdam 1942/RIT 1 nm; color13/tech13 spectral fingerprint); `Appendix/Project Notes.md` (CIELAB spindle, Munsell tree, MacAdam spindle, Pointer hull, display prisms, L\* formula, constant-L\* slices; intstud/color18a/tech13); `Painting/Composition.md` (harmony as analogy of opposites, proportional frameworks + Itten 3:6:8, seven contrasts, warm/cool, critique of Albers/Munsell/Brewster/Gage); `Painting/Movements & Painters/Movements & Painters.md` (4-stage arc, theory pipeline Goethe→Chevreul→Rood→Munsell→Albers 1963, signature ideas, rejections); `Painting/Movements & Painters/Vermeer-Dutch Golden Age.md` (lapis economics, Huygens/Hooke blue-yellow "shimmering prismatic hypotheses", diffraction edges, grey wall anchoring, Goethe/Maxwell anticipations; color18b master of materials; contradiction flag).
- Also on this date: MCP session moved `b40983ca` → `22b5c02b` (wedged session diagnosed and replaced per AGENTS.md).

## [2026-08-09] ingest | Visible Spectrum deep
- NotebookLM query (session `b40983ca`, direct MCP tool): Newton 1666 prism (heterogeneous differently-refrangible rays, term "spectrum" coined, components-not-modifications, continuous hues), hue wavelength ranges (violet 380-440 / blue 440-490 / green 490-575 / yellow 575-585 / orange 585-610 / red 610-760 + alternate convention 450-500/500-560/560-590/590-610/610-750), fuzzy boundaries (observer/adaptation; cornea+lens UV absorption, post-surgery near-UV; IR photons <1.8 eV), nonspectral purple/magenta → perceptual color circle, wavelength-dependent glass speed dispersion (blue slowed more).
- Rewrote `Light/The Visible Spectrum.md` in no-H1 format: header image prompt blockquote (prism dispersion plate + magenta dashed connector), Scope, 6 synthesized sections incl. hue-range table + NOTE on conventional boundaries, Handprint Perspectives (color18a six-hue taxonomy red/orange/yellow/green/blue + extraspectral violet; color11 unequal spectral luminosity — green brighter than equal blue), Subtopics, Cross-References, Sources.
- Updated `page-status.md` (→ done + next-up = Reflection vs. Emission), `index.md`, `log.md`.

## [2026-08-09] ingest | Wave Nature deep
- NotebookLM query (session `b40983ca`, direct MCP tool): EM wave definition + parameters (λ, f, amplitude, c, c = f·λ, phase), frequency↔color vs amplitude↔intensity + visible 4.28→7.50×10^14 Hz, E = hf + E(eV) = 1240/λ(nm) + worked 700 nm → 1.77 eV / 400 nm → 3.10 eV, dual nature in interactions (single-photon rhodopsin absorption, photoelectric effect, Snell refraction, prism dispersion, polarization), SPD definition.
- Rewrote `Light/Wave Nature.md` in no-H1 format: header image prompt blockquote (EM wave E/B field plate + spectral inset), Scope, 5 synthesized sections, Handprint Perspectives (color18a three photon-surface outcomes — surface scattering/whiteness, chromatic reflectance/hue, infrared/heat — + single-wavelength never-pure-cone-response < ~570 nm; intstud "colors exist in the mind ... shaped by the physical behavior of light"), Subtopics, Cross-References (incl. Chemistry link, fixed a dead `[[How Light Interacts with Pigments]]` link during write), Sources last.
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

## [2026-08-11] chore | Frontmatter sequence pass (1–71)
- Added `sequence` frontmatter to all 71 content pages (section hubs + every page, incl. the 18 Pigment Reference sheets) for deterministic Quartz sidebar ordering.
- Re-applied frontmatter lost in a workspace revert on 19 pages (Home, Appendix×4, Colors×8, Eye×6).
- Added the missing `index.md` one-liner for `Intersections/The Neuroscience Behind Why Colours Rewire Your Brain`.

## [2026-08-11] feat | New page: Media, Vehicles & Solvents (Pigments)
- Added `Pigments/Media, Vehicles & Solvents.md` (NotebookLM session `8f1b391e`, sources requested) — gum arabic/honey/glycerin/ox gall watercolor, chalk-filled gouache, oxidizing linseed oils, acrylic emulsion, shellac/dye/pigment inks, egg tempera/casein/pastel, and the refractive-index physics (air 1.00 vs pigment 2.0–2.7 vs oil 1.48) behind per-medium chroma; header image prompt; handprint perspectives (color18a transparent-vehicle law, intstud vehicle dilution, pigmt7 gouache, pigmt5 vehicle history).
- Renumbered for insertion: Reference index 46→47, sheets 47–64→48–65, Intersections hub 65→66, Intersections pages 66–73→67–74; chain contiguous 1–74.
- Synced `index.md` one-liner, `Pigments/index.md` cross-reference, `page-status.md` (74 pages), `log.md`.

## [2026-08-11] fix | Continuous navigation + Intersections hub
- Created `Intersections/index.md` hub (NotebookLM query session `28d4c19d`, sources requested) — Scope + 8 linked subsections + Sources + header image prompt; `sequence: 65`.
- Created `Pigments/Reference/index.md` (18 data sheets grouped by color family, `sequence: 46`).
- Renamed `Colors/Gamuts/Gamuts.md` → `Colors/Gamuts/index.md` and `Painting/Movements & Painters/Movements & Painters.md` → `Painting/Movements & Painters/index.md` so every folder is a real sequenced page (no Quartz auto-folder dead ends).
- Renumbered Reference sheets 46–63 → 47–64 and Intersections pages 64–71 → 66–73; final contiguous `sequence` 1–73.
- Fixed links: `index.md` (2 paths + Intersections/Reference hub one-liners), `Colors/index.md`, `Painting/index.md`, `Impressionism.md`, `page-status.md`.
- Website build (`website/`, per user request): `contentIndex.tsx` emits `sequence` into `ContentDetails`; `quartz.layout.ts` Explorer `sortFn` now orders by `sequence` (sidebar = prev/next order); `ignorePatterns` += `page-status.md`, `AGENTS.md`, `.agents` (hidden from sidebar/search).

## [2026-08-11] feat | Transparency/codes page + artist's color wheel + 3 new pigment sheets
- Added `Pigments/Transparency, Opacity & Pigment Codes.md` (NotebookLM session `8f1b391e`, sources requested) — Δn hiding-power physics (ultramarine n≈1.50 vs oil 1.48 transparent; TiO₂ 2.71 opaque), particle-size scattering ~500 nm, transparent/semi/opaque classes + glazing/scumbling, masstone/undertone/tinting strength (rub-out 0.1 g/2.0 g ZnO; 50:1 for phthalos), label anatomy (CI generic PR108, constitution 77196, series, ASTM I–IV, Blue Wool 1–8, ACMI/D4236), CI structure P+hue-letter+number (77000–77999 inorganics; PB15:3 vs PB15:6), trust hierarchy (ASTM > manufacturer; handprint litetest skepticism); handprint pigmt8 one-line summaries + Sharpie opacity test + ASTM-D5067 demand. `sequence: 47`.
- Filled `Pigments/The artist's color wheel.md` (renamed from `color wheel pigment.md` by user; Obsidian) — the artistColorWheel.pdf (image-only scan, Photoshop CS2 Mac 2009): CIECAM hue angle/chroma placements, complements opposite, neutral center (titanium white/carbon black/sepia), italics convenience mixes, bold common pigments, numbered sectors 1–6 with degree marks; Munsell placements from notebook query (8.0Y 9.2/9.0 cadmium yellow, 0.8YR 6.4/13.4 pyrrole red, 3.5PB 4.6/14.0 phthalo blue, 5.0PB 6.3/10.0 ultramarine, 1.5Y 8.7/5.0 yellow ochre, 1.0Y 7.6/4.5 raw sienna, 1.5Y 6.9/2.0 raw umber, 7.5BG 7.3/4.5 viridian), chroma ceilings (green 34 vs red 20; V(λ) 555 nm), pigment vs light wheel, darkness-kills-chroma; handprint color14 wheel-as-landscape + asymmetry-follows-luminosity. `sequence: 48`.
- Added 3 sheets: `PB15 - Phthalo Blue` (66 — Cu phthalocyanine, Scottish Dyes 1927–28, marketed 1936, α/β forms, 50–75% let-down, replaced Prussian blue, CMY cyan), `PR122 - Quinacridone Magenta` (68 — dimethyl trans-linear quinacridone, lab 1930s Germany → du Pont 1950s, replaced aniline magentas, lightfast over PR83), `PR254 - Pyrrole Red` (69 — diketopyrrolo-pyrrole, non-toxic cadmium substitute, formulable opacity; handprint pigmt8 "very lightfast, semiopaque, highly staining, dark valued").
- Renumbered for insertion: Reference index 47→49, sheets 48–65→50–67 + PR83 64→67 + PV23 65→70, Intersections hub 66→71, Intersections pages 67–74→72–79; chain contiguous 1–79 (21 sheets + 2 new essays).
- Synced `index.md` one-liners, `Pigments/index.md`, `Reference/index.md` (21 sheets grouped by family), `page-status.md` (80 pages), `log.md`.

## [2026-08-11] fix | Mojibake pass 2 (CP1255 double-decode) + BOM strip
- Root cause: text written as UTF-8 then byte-decoded as the Hebrew code page CP1255 — each correct character became a Hebrew-letter + Latin artifact sequence (e.g. `—` → `ג€”`, `–` → `ג€“`, `→` → `ג†'`, `₂` → `ג‚‚`, `₃` → `ג‚ƒ`, `₄` → `ג‚„`, `α` → `־±`, `Σ` → `־£`, `λ` → `־»`, `Δ` → `־”`, `λ̄`-macron → `ּ„`, `ȳ` → `ָ³`, `é` → `׳©`, `°` → `ג°`, `·` → `ג·`, `′` → `ג€²`, `≡` → `ג‰¡`, `≈` → `ג‰ˆ`, `−` → `גˆ'`, `…` → `ג€¦`, `≠` → `ג‰ `).
- Pass 1 had fixed 28 files' em-dashes; pass 2 replaced all remaining variant sequences via literal-code-point table in 25+10 wiki files (Reference sheets, Intersections pages, hub pages), pass 3 caught `é`-prefix variant U+05B3. Verified by re-scan: zero Hebrew/CP1255 artifacts remain; remaining U+2013/U+00B7/U+2019 hits are legitimate typography.
- Stripped UTF-8 BOMs from 27 files (Intersections pages + Reference index + 18 sheets).

## [2026-08-11] ingest | Florent Farges' Color Theory for Artists page
- Enriched `Florent Farges' Color Theory for Artists.md` (root, `sequence: 80`) — NotebookLM query (session `8c0e3067`) returned **no corpus material on Farges**, so the page is transcribed from the embedded image-only PDF via Windows OCR (System.Runtime.WindowsRuntime OcrEngine; pypdf text layer = links only): three chroma-tier wheels (HIGH/MEDIUM/LOW) sharing one fixed 0–360° hue scaffold, six main hues R Y G C B M (RGB+CMY scaffold, not RYB), degree marks + sector labels (R-O ~20°, O-Y ~50°, G-Y ~110°, G-C ~150°, B-C ~210°, R-M ~340°), pigments placed by hue angle per tier (high: PR108, PR254, PR177 "Alizarin Crimson (perm.)", quinacridone magenta (code unclear), PO20, PY35, PY154, Hansa, PG36, PG7, PB36, PG50, PB35, PG19, PB29 ×2, PB28, PB27, PV15/14/16; medium: PR101, PR102, PY42/43, PY42 Mars, PY43, PBr7 Raw Sienna, PG17, Paynes Grey (m); low: Van Dyck Brown, PBr7 Raw/Burnt Umber, Olive Green (m), PG23, Ivory Black), whites PW1/PW4/PW6 footnote, "PICK COLOR STRINGS IN THE WHEELS, MIX AND ADJUST ON YOUR PALETTE" workflow, complements opposite/mixing across circle neutralizes, legend HUE/CHROMA (peak chroma)/VALUE, ©2020 free SD version + 87-page PDF + 9-hour "Art and Practice of Color" course upsell, printed disclaimer (hue angles = rough average across brands/media).
- Page carries a provenance note (OCR transcription, uncertain codes flagged), Handprint Perspectives (color16/color14 measured-hue convergence), and a contradiction flag: fixed even six-hue scaffold vs handprint's measured-geometry critique of equally spaced wheels (color13 "the wheel is not a color theory" + Castel 1740).
- Synced `index.md` (new ## For Painters section), `page-status.md` (81 pages), `log.md`.



