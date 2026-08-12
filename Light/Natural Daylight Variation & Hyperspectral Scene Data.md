---
title: Natural Daylight Variation & Hyperspectral Scene Data
sequence: 27
---
![[Pasted image 20260811113914.png]]

**Scope:** Daylight as a continuously varying spectral environment and the high-resolution hyperspectral measurements that capture it.

### Daylight Through the Day

Daylight changes constantly because the sun's altitude sets the **atmospheric path length** light must traverse (*A Comprehensive Overview of Color Vision Mechanisms, Color Spaces, and the Munsell System*).

- At **noon**, sunlight passes the atmosphere vertically — the shortest possible route; at **sunrise/sunset** the oblique angle forces light through "a significantly longer 'veil' of air," which "results in the scattering away of blue and even green wavelengths, leaving only the long-wavelength red to reach the eye" (*A Comprehensive Overview..., Contemporary Color*).
- CCT mapping of the phases: **sunrise/sunset ≈ 2,000 K** (low/red); **direct noon sun ≈ 4,800–5,500 K**; **average daylight (D65) = 6,500 K**; **clear blue sky > 12,000 K** (*Contemporary Color, The Science of Paintings, Illusions of Seeing*).

### Rayleigh Scattering — Blue Sky, Red Sun, White Clouds

Lord Rayleigh (1899) showed that **air molecules scatter light with an intensity inversely proportional to the fourth power of the wavelength (1/λ⁴)** (*Illusions of Seeing*).

- **Blue sky:** blue light is scattered much more strongly than red — "about 10 times more" — and this scattered, indirect light is the blue of the sky (*Illusions of Seeing*, *A Comprehensive Overview...*).
- **Red sun:** at the horizon, the extreme path length filters out "almost all the shorter blue and green components, leaving only the 'surviving' red rays" (*Contemporary Color*).
- **White clouds:** water droplets are far larger than gas molecules and scatter by the wavelength-blind **Mie scattering** process — "scatters all colors equally, resulting in a cloudy white appearance" (*A Comprehensive Overview..., The Science of Paintings*).

### Sunlight, Skylight, and Overcast Light

- **Sunlight** is the direct radiation of the sun's disk — physically "white" rather than yellow, "though it appears yellowed at noon as blue is scattered away" (*A Comprehensive Overview...*); see also [[Illuminants & Correlated Color Temperature]].
- **Skylight** is the huge secondary source from the entire blue sky vault — cooler (bluer) light that "influences shadow colors" (*A Comprehensive Overview..., Contemporary Color*).
- **Overcast sky:** clouds act as **ground glass**, diffusing sunlight "into a silver-white mass"; because the diffused light is scattered so thoroughly, "an overcast sky often has a much higher color temperature than a clear sun, frequently exceeding 10,000 K" (*Contemporary Color*, *A Comprehensive Overview...*).

### Hyperspectral Datasets and Colorimetric Computation

Physical light data is captured as **spectral reflectance curves** — the percentage of light reflected at each wavelength, typically sampled "at 1 nm or 5 nm intervals across the visible spectrum from 380 to 780 nm" (*Munsell Color Science Lab*, RIT; *A Comprehensive Overview...*).

- **Instruments:** **spectrophotometers** measure object reflectance or transmittance; **spectroradiometers** measure self-luminous sources and light SPDs (*The Measurement of Colour*, *Munsell Color Science Lab*).
- **CIE integration:** to compute tristimulus values, "researchers multiply the measurement at each wavelength by the spectral power distribution (SPD) of the illuminant and the color matching functions of the standard observer, then sum the results" (*A Comprehensive Overview...*, *Munsell Color Science Lab*).

### Spectral Fingerprints — Why Three RGB Numbers Are Not Enough

- Every substance has "a unique pattern of wavelength reflectance and intensity that acts as a characteristic 'fingerprint', allowing for precise identification of pigments or materials" (*A Comprehensive Overview...* — see [[Pigments/Sourcing Real Spectral Data]]).
- Full SPD information is required because **RGB values are device-dependent summaries** that cannot predict **metamerism** — two surfaces can match under one light but differ under another because their underlying reflectance curves are different (*A Comprehensive Overview..., Contemporary Color*; see [[Natural Light Gamut vs. Pigment Gamut - Metamerism]]).

## Handprint Perspectives

MacEvoy compresses several painter-relevant daylight facts: the **dominant wavelength of sunlight is about 530 nm** — "sunlight is not yellow, it is a very pale green!" — the perceived yellowness of sunlit scenes being an adaptation artifact rather than a physical property. The color of the clear sky "varies substantially by geographic latitude, altitude, season, humidity, distance from the zenith, time of day and concentration of atmospheric ice, dust or smoke," with chromaticities roughly parallel to the blackbody locus and "usually above a CCT of 10,000°K, corresponding to a dominant wavelength of about 470 to 475 nm." The warm/cool contrast of painters, he argues, is rooted in the visual system's adaptation to these "different phases of daylight," which changes both relative color sensitivity and judgments of surface colors to keep appearances stable *(Source: [[raw_sources/handprint/color12.md|color12.html]])*.

## Subtopics
- Diurnal daylight physics: path length, scattering losses, CCT phases (2,000 K → 12,000 K+)
- Rayleigh (1/λ⁴) vs. Mie scattering: blue sky, red sun, white clouds
- Sunlight vs. skylight vs. overcast silver-white (10,000 K+)
- Hyperspectral reflectance curves at 1–5 nm sampling, spectrophotometers/spectroradiometers, CIE integration
- Spectral fingerprints vs. device-dependent RGB; metamerism prediction

## Cross-References
- [[Illuminants & Correlated Color Temperature]] — D65, the daylight locus, and CCT
- [[Wave Nature]] — SPDs as the dataset's raw material
- [[The Visible Spectrum]] — the 380–780 nm measurement band
- [[Pigments/Sourcing Real Spectral Data]] — grand spectral data for pigments
- [[Natural Light Gamut vs. Pigment Gamut - Metamerism]] — metamerism from full-SPD data
- [[CIE Systems]] — tristimulus integration of hyperspectral data

## Sources
* "A Comprehensive Overview of Color Vision Mechanisms, Color Spaces, and the Munsell System"
* "Contemporary Color: Theory and Use" — Steven Bleicher
* "Illusions of Seeing" — Thomas Ditzinger
* "The Science of Paintings" — W. Stanley Taft Jr. and James W. Mayer
* "The Measurement of Colour" — R.W.G. Hunt
* "Munsell Color Science Lab Educational Resources" — Rochester Institute of Technology