# Hungry Ghosts (PS2): English fan translation

An unofficial, free English fan translation of *Hungry Ghosts* (ハングリィゴースト; Deep Space /
Sony Computer Entertainment, 2003, Japan only, SCPS-15046) by Mord of Swoonlight.
Current version: v1.0.

This repository holds patch files only, no game data. You need your own dump of the Japanese
disc as a plain `.iso`; the readme lists the hashes it must match. Never share a patched disc
image.

The main patch is also listed at [swordofmoonlight.com/translations/community](https://www.swordofmoonlight.com/translations/community/).

**Player's companion guide:** [read it in your browser](https://mordofswoonlight.github.io/HungryGhostsPS2English/guide/HungryGhosts_PlayerGuide_spoilers.html).
How the game works, its dangers, places and every item, plus the fifteen endings and how to
reach them. **Contains spoilers.**

## What's here

| folder | contents |
|---|---|
| `patch/` | the two `.xdelta` patches (Standard and Modern Controls editions) and `README.md.txt`, the step-by-step instructions: checking your dump, applying the patch, playing in PCSX2 |
| `pcsx2_options/` | optional PCSX2 `.pnach` files (wide aspect ratios with the HUD and menus kept in shape, a faster camera, and modern controls for the original Japanese disc too) and their readme |
| `alt_patcher/` | an alternative patcher written in Python, for dumps the `.xdelta` refuses (trimmed, padded or rebuilt images) |
| `guide/` | the player's companion guide, one HTML page to open in a browser. **Contains spoilers** (the fifteen judgments and how to reach them) |

To download everything at once, use **Code → Download ZIP**, or the zip attached to the latest
entry on the Releases page.

## PCSX2 options (`.pnach`)

One file per game executable: `SCPS-15046_91AA4B28.pnach` for the original Japanese disc,
`SCPS-15046_B3C0E286.pnach` for the Standard edition and `SCPS-15046_798E3212.pnach` for the
Modern Controls edition. Each option is its own checkbox in PCSX2 (right-click the game →
Properties → Patches):

- Modern controls (twin-stick, for the original disc and the Standard edition) and Classic
  controls (the original layout, for the Modern Controls edition)
- Widescreen 16:9 (Arapapa's patch, included unchanged)
- Faster camera, +25% or +50%
- Aspect ratio 16:10, 16:9, 21:9 (2560×1080 and 3440×1440) and 32:9, with the HUD and menus
  kept in their original shape

## Quick start

1. Read `patch/README.md.txt`.
2. Check your ISO's SHA-1 against the one in that readme.
3. Apply the `.xdelta` for the edition you want, on a copy of your ISO, with Delta Patcher
   (Windows, macOS, Linux) or `xdelta3`.
4. Copy the matching `.pnach` file from `pcsx2_options/` into PCSX2's `patches` folder; see
   `pcsx2_options/PCSX2_OPTIONS_README.md.txt`.

Both editions have the whole game in English. Standard keeps the original controls. Modern
Controls has twin-stick controls (left stick moves and strafes, right stick looks, R1 attacks)
with a matching Controls screen and help text.

Made and tested on PCSX2 2.0 or later; untested on a hardware PS2.


## Credits

- Translation, patching, menu graphics and the companion guide: Mord of Swoonlight's English
  fan translation project
- Original 16:9 widescreen patch: Arapapa (from PCSX2's patch collection)
- Thanks to Evil7, whose GameFAQs walkthrough of the Japanese release helped with route
  details in the guide

Unofficial fan translation. Free, not for sale, and not affiliated with or endorsed by Sony
Interactive Entertainment or Deep Space Inc. *Hungry Ghosts* © 2003 Deep Space Inc. / Sony
Computer Entertainment Inc. The game's own copyright notices and staff credits are kept intact.
