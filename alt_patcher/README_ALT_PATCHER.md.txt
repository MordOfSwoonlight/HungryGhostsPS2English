# Hungry Ghosts English patch v1.0: the alternative patcher

Unofficial English fan translation of *Hungry Ghosts* by Mord of Swoonlight. Free, not for
sale, and not affiliated with or endorsed by Sony Interactive Entertainment or Deep Space
Inc. *Hungry Ghosts* (c) 2003 Deep Space Inc. / Sony Computer Entertainment Inc.

Use this only if the .xdelta patch refuses your image (step 3 of README.md.txt). It patches
the two game files inside your image directly, so it also works when your dump's layout
differs from the standard one (trimmed, padded or rebuilt), as long as the game files are
intact.

**You need** Python 3.8 or later (free from python.org; on Linux and macOS it is usually
installed already). Keep these two files in the same folder:
- `apply_hg_patch.py`: the helper (the same for every version of the patch);
- `HungryGhosts_English_v1.0.hgpatch`: the patch itself (both editions).

**Run** (in a terminal, in that folder; on Windows type `py` instead of `python3`):

```
python3 apply_hg_patch.py "Hungry Ghosts (Japan).iso" "Hungry Ghosts (English).iso" --edition modern
```

Use `--edition standard` for the original controls. The helper checks your image first and
writes nothing if it isn't the original game (it also tells you if the image is already
patched). It writes the English image as a new file and leaves yours untouched. At the end
it prints the game's PCSX2 code; the matching options file from the main bundle is:
- Standard edition: `SCPS-15046_B3C0E286.pnach`
- Modern Controls edition: `SCPS-15046_798E3212.pnach`

Your patched game is the same as everyone else's, so everything else in README.md.txt
(PCSX2 setup, saves, savestates) applies as written.
