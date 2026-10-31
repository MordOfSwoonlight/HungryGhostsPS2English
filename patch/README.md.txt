# Hungry Ghosts (PS2): English fan translation, v1.0

An unofficial, free fan translation of *Hungry Ghosts* (Japan, SCPS-15046) by Mord of
Swoonlight. This bundle holds patch files only, no game data. You need your own copy of the
game. Never share the patched disc image.

**Files in this bundle**

- `README.md.txt`: this file
- `HungryGhosts_English_v1.0_Standard.xdelta`: the patch, Standard edition
- `HungryGhosts_English_v1.0_ModernControls.xdelta`: the patch, Modern Controls edition
- `SCPS-15046_B3C0E286.pnach`: PCSX2 options for the Standard edition
- `SCPS-15046_798E3212.pnach`: PCSX2 options for the Modern Controls edition
- `SCPS-15046_91AA4B28.pnach`: the same options for the original Japanese disc
- `PCSX2_OPTIONS_README.md.txt`: how to install and use the PCSX2 options
- `HungryGhosts_PlayerGuide_spoilers.html`: the player's guide; open it in a web browser. **Contains spoilers** (the fifteen judgments and how to reach them)

## 1. What you need
- **Your own dump of the Japanese disc**, as a single `.iso` file of 4,389,568,512 bytes. It
  must match these hashes exactly:
  - SHA-1 `e765a2db962bea182f47e768c7ef67876947cbb6`
  - MD5 `251e818a9b8d8c3d9a32024446bf83dc`
  - CRC32 `9d898274`
- **Only if your copy isn't a plain `.iso`:**
  - Inside a `.7z` or `.zip` archive: unpack it first.
  - A `.chd` (a compressed image some emulator users keep; PCSX2 plays it directly):
    convert it back to an ISO with MAME's `chdman` tool:
    `chdman extractdvd -i "Hungry Ghosts (Japan).chd" -o "Hungry Ghosts (Japan).iso"`.
    After patching, you can compress the English ISO into a CHD again with
    `chdman createdvd` if you like.
- **An xdelta patcher** (free):
  - Windows, macOS or Linux: **Delta Patcher** (a small app with a window; get it from its
    GitHub page, `marco-calautti/DeltaPatcher`, under Releases);
  - Linux command line: **xdelta3** from your package manager (`sudo apt install xdelta3`,
    `sudo dnf install xdelta`, `sudo pacman -S xdelta3`).
- **PCSX2** (version 2.0 or later) to play.

## 2. Check your dump (recommended)
Compare your ISO's SHA-1 with the one above:
- **Windows** (PowerShell): `Get-FileHash -Algorithm SHA1 "Hungry Ghosts (Japan).iso"`
- **macOS** (Terminal): `shasum -a 1 "Hungry Ghosts (Japan).iso"`
- **Linux:** `sha1sum "Hungry Ghosts (Japan).iso"`

If it differs, the patch will refuse to apply. Get a clean dump of the disc.

## 3. Apply the patch
Pick one edition. Both play the same story. The difference is the controls:

- **Standard edition:** original controls; the Controls screen and help text describe them.
  - patch: `HungryGhosts_English_v1.0_Standard.xdelta`
  - patched SHA-1: `5992a8ad15050b16bd6268d35b3a6b36c9829d91`
  - PCSX2 code (CRC): `B3C0E286`
- **Modern Controls edition:** modern twin-stick controls (left stick moves and strafes, right stick looks, R1 attacks); the Controls screen and help text are re-lettered to match.
  - patch: `HungryGhosts_English_v1.0_ModernControls.xdelta`
  - patched SHA-1: `698241df995f137f4d813bb646d20970a38950ce`
  - PCSX2 code (CRC): `798E3212`

**Delta Patcher:**
1. **Work on a copy of your ISO.** Delta Patcher may write the result over the file you
   select, so keep your original safe.
2. Open Delta Patcher. Under **Original file**, choose your Japanese ISO (the copy).
3. Under **XDelta patch**, choose the `.xdelta` file for your edition.
4. Click **Apply patch** and wait about a minute.
5. Rename the result if you like, e.g. `Hungry Ghosts (English).iso`.

**xdelta3 (command line):**

```
xdelta3 -d -s "Hungry Ghosts (Japan).iso" "HungryGhosts_English_v1.0_Standard.xdelta" "Hungry Ghosts (English).iso"
```

This leaves your original ISO untouched.

**Check the result (recommended):** its SHA-1 must match the "patched SHA-1" for your
edition in the list above. Use the same commands as in step 2.

## 4. Play in PCSX2
1. Add the patched ISO to PCSX2's game list, or start it with **System → Start File**.
2. **Install the `.pnach` file** for widescreen and the other options. Instructions are in
   `PCSX2_OPTIONS_README.md.txt`. The file name must stay exactly as shipped,
   `SCPS-15046_<code>.pnach`. PCSX2 matches it to the patched game by that code, and each
   edition has its own code.
3. **Saves:** memory-card saves from the Japanese release keep working. The game finds them
   the same way. Only new saves get the English save titles.
4. **Savestates:** make new ones on this version. A savestate holds a copy of the game's code,
   so loading one made on another version (including the Japanese disc) brings that version
   back until you restart.

PCSX2 shows the game as "HUNGRY GHOSTS", region NTSC-J. That's expected: the patch keeps the
Japanese disc's serial, so your saves and PCSX2's settings for the game still apply.

## About
Unofficial English fan translation by Mord of Swoonlight. Free, not for sale, and not
affiliated with or endorsed by Sony Interactive Entertainment or Deep Space Inc.
*Hungry Ghosts* © 2003 Deep Space Inc. / Sony Computer Entertainment Inc. The game's own
copyright notices and staff credits are kept intact.

**Credits:**
- Widescreen 16:9 patch by Arapapa (included in the `.pnach` file, from PCSX2's patch
  collection).
- Typefaces drawn into the patch: Gentium Book Plus and Weathered SF (in-game text);
  DHPHSGothic-W5 (small labels); Oldania ADF Std (menus, headers); Linux Libertine O (rank
  titles); HG Mincho E (『』 brackets); Liberation Sans (title notice); Verdana (help-bar
  words); Domestic Manners (potato label).
