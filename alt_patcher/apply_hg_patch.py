#!/usr/bin/env python3
"""Hungry Ghosts (PS2) English fan translation by Mord of Swoonlight: file-level patch helper.

Unofficial English fan translation of Hungry Ghosts by Mord of Swoonlight.
Free, not for sale, and not affiliated with or endorsed by Sony Interactive
Entertainment or Deep Space Inc.  Hungry Ghosts (c) 2003 Deep Space Inc. /
Sony Computer Entertainment Inc.

Applies a Hungry Ghosts patch file (.hgpatch) to your own copy of Hungry
Ghosts (Japan, SCPS-15046).  Unlike an image patch (.xdelta), it works on
the two game files inside the disc image (DATA/PACK.DAT and SCPS_150.46), so
it also accepts images whose layout differs from the standard dump (trimmed,
padded or rebuilt), as long as those two files are intact.

Needs only Python 3.8 or later (python.org); nothing else to install.  Keep
this script and the .hgpatch file in the same folder; the same script works
for every later version of the patch.

Usage:
  python3 apply_hg_patch.py "Hungry Ghosts (Japan).iso" "Hungry Ghosts (English).iso" --edition modern
  python3 apply_hg_patch.py "Hungry Ghosts (Japan).iso" "Hungry Ghosts (English).iso" --edition standard

  --edition standard   original controls
  --edition modern     modern twin-stick controls (Controls screen re-lettered)
  --patch FILE         the .hgpatch file to use (default: the one next to this
                       script, or in the current folder)
  --in-place           patch the input image itself instead of writing a copy
                       (only on a copy you can afford to lose)

On Windows, use "py" instead of "python3".  What it does:
  1. finds the two files in your image and checks them against the original
     game (SHA-1); anything else is refused, nothing is written;
  2. copies your image to the output name and writes the changes into the copy;
  3. checks the patched files (SHA-1) and tells you the PCSX2 code (CRC) of
     the patched game, i.e. which SCPS-15046_<code>.pnach file belongs to it.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import lzma
import os
import shutil
import struct
import sys

HELPER_VERSION = 1
MAGIC = b"HGPATCH1"   # then the SHA-1 of the rest (20 bytes), then an xz stream
SECTOR = 2048


def iso_files(f) -> dict:
    """{'/PATH': (lba, size)} of every file in an ISO9660 image."""
    f.seek(16 * SECTOR)
    pvd = f.read(SECTOR)
    if pvd[1:6] != b"CD001":
        raise SystemExit("This is not a plain ISO image (no ISO9660 volume found). If your copy is "
                         "a .chd, .7z or .zip, convert or unpack it to an .iso first.")
    out = {}

    def walk(lba, size, path):
        f.seek(lba * SECTOR)
        d = f.read(-(-size // SECTOR) * SECTOR)
        i = 0
        while i < len(d):
            n = d[i]
            if n == 0:                                   # records never span sectors
                i = (i // SECTOR + 1) * SECTOR
                continue
            e_lba, e_size = struct.unpack_from("<I", d, i + 2)[0], struct.unpack_from("<I", d, i + 10)[0]
            flags, nlen = d[i + 25], d[i + 32]
            name = d[i + 33:i + 33 + nlen]
            if name not in (b"\0", b"\1"):
                name = name.decode("ascii", "replace").split(";")[0]
                if flags & 2:
                    walk(e_lba, e_size, path + name + "/")
                else:
                    out[path + name] = (e_lba, e_size)
            i += n
    root = pvd[156:190]
    walk(struct.unpack_from("<I", root, 2)[0], struct.unpack_from("<I", root, 10)[0], "/")
    return out


def file_sha1(f, lba: int, size: int) -> str:
    h = hashlib.sha1()
    f.seek(lba * SECTOR)
    left = size
    while left:
        b = f.read(min(left, 1 << 24))
        if not b:
            raise SystemExit("The image ends in the middle of a game file: it is incomplete.")
        h.update(b)
        left -= len(b)
    return h.hexdigest()


def exe_crc(f, lba: int, size: int) -> str:
    f.seek(lba * SECTOR)
    data = f.read(size)
    crc = 0
    for (w,) in struct.iter_unpack("<I", data[:len(data) // 4 * 4]):
        crc ^= w
    return f"{crc:08X}"


def find_patch(path=None) -> str:
    if path:
        return path
    here = os.path.dirname(os.path.abspath(__file__))
    for d in dict.fromkeys([here, os.getcwd()]):
        found = sorted(x for x in os.listdir(d) if x.lower().endswith(".hgpatch"))
        if len(found) == 1:
            return os.path.join(d, found[0])
        if len(found) > 1:
            raise SystemExit("Several .hgpatch files here: choose one with --patch FILE.")
    raise SystemExit("No .hgpatch file found: put it next to this script, or use --patch FILE.")


def load_data(path=None):
    path = find_patch(path)
    raw = open(path, "rb").read()
    if raw[:8] != MAGIC or hashlib.sha1(raw[28:]).digest() != raw[8:28]:
        raise SystemExit(f"{os.path.basename(path)} is not a Hungry Ghosts patch file, or it is "
                         f"damaged; download it again.")
    blob = lzma.decompress(raw[28:])
    n, = struct.unpack_from("<I", blob, 0)
    return json.loads(blob[4:4 + n].decode("utf-8")), memoryview(blob)[4 + n:]


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0],
                                 formatter_class=argparse.RawDescriptionHelpFormatter,
                                 epilog=__doc__.split("\n\n", 1)[1])
    ap.add_argument("input", help="your Japanese image (.iso)")
    ap.add_argument("output", nargs="?", help="the English image to write (.iso)")
    ap.add_argument("--edition", required=True, choices=["standard", "modern"])
    ap.add_argument("--in-place", action="store_true", help="patch the input image itself")
    ap.add_argument("--force", action="store_true", help="overwrite an existing output file")
    ap.add_argument("--patch", help="the .hgpatch file (default: the one next to this script)")
    a = ap.parse_args(argv)
    head, data = load_data(a.patch)
    if head.get("helper", 1) > HELPER_VERSION:
        raise SystemExit("This patch file needs a newer apply_hg_patch.py; download it again.")
    ed = head["editions"][a.edition]
    print(f"Hungry Ghosts English patch {head['version']}, {ed['title']} edition")
    print(head.get("credit", "Unofficial English fan translation by Mord of Swoonlight"))
    if a.in_place == bool(a.output):
        raise SystemExit("Give an output file name (or --in-place to patch the input itself).")
    if a.output:
        if os.path.abspath(a.output) == os.path.abspath(a.input):
            raise SystemExit("The output must be a different file from the input.")
        if os.path.exists(a.output) and not a.force:
            raise SystemExit(f"{a.output} already exists (use --force to overwrite it).")

    print("Checking your image ...")
    with open(a.input, "rb") as f:
        files = iso_files(f)
        for name, want in head["files"].items():
            if name not in files:
                raise SystemExit(f"{name} is missing: this is not Hungry Ghosts (Japan, SCPS-15046).")
            lba, size = files[name]
            if size != want["size"]:
                raise SystemExit(f"{name} has the wrong size: not the original Japanese game.")
            got = file_sha1(f, lba, size)
            if got != want["sha1"]:
                for other in head["editions"].values():
                    if other["files"][name]["sha1"] == got:
                        raise SystemExit(f"This image is already patched ({other['title']} edition). "
                                         f"Start from your original Japanese image.")
                raise SystemExit(f"{name} doesn't match the original game (SHA-1 {got}). The image "
                                 f"is modified or a bad dump; nothing was written.")
            print(f"  {name}: original, OK")

    target = a.input if a.in_place else a.output
    if not a.in_place:
        print(f"Copying to {target} ...")
        shutil.copyfile(a.input, target)
    print("Patching ...")
    ok = False
    try:
        with open(target, "r+b") as f:
            n_runs = 0
            for name, fe in ed["files"].items():
                lba, _ = files[name]
                for off, length, at in fe["runs"]:
                    f.seek(lba * SECTOR + off)
                    f.write(data[at:at + length])
                    n_runs += 1
            f.flush()
            print(f"  {n_runs} changes written. Checking the result ...")
            for name, fe in ed["files"].items():
                lba, size = files[name]
                if file_sha1(f, lba, size) != fe["sha1"]:
                    raise SystemExit(f"{name} did not come out as expected. The output is not usable.")
                print(f"  {name}: patched, OK")
            crc = exe_crc(f, *files["/SCPS_150.46"])
            f.seek(0, 2)
            same_size = f.tell() == ed["image_size"]
        ok = True
    finally:
        if not ok and not a.in_place and os.path.exists(target):
            os.remove(target)
    print(f"Done: {target}")
    print(f"PCSX2 code (CRC) of the patched game: {crc}. Its options file is SCPS-15046_{crc}.pnach.")
    if same_size:
        with open(target, "rb") as f:
            same = file_sha1(f, 0, ed["image_size"]) == ed["image_sha1"]
        print("The whole image is identical to the release image." if same else
              "The game files are patched; other parts of your image differ from the standard "
              "dump, which is fine.")
    else:
        print("Your image's layout differs from the standard dump; the game files are patched, "
              "which is all that matters.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
