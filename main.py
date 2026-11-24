# THE WORLD LEDGER — Tuesday, 24 November 2026
#
# Entry for make.fun news-image-20261124: one image summing up the world's
# news of Tuesday 24 November 2026.
#
# The front page is composed in this repository as entry.png (1024x1024,
# 507,109 bytes): masthead "THE WORLD LEDGER", dated Tuesday, 24 November
# 2026, headlined "U.S. PUTS MADURO'S CARTEL ON TERROR LIST" over a
# purpose-built illustration of a U.S. carrier strike group in the Caribbean,
# carrying eight stories from around the world — the terror listing taking
# effect as a carrier group patrols, the Crimea Platform summit opening in
# Stockholm as Zelensky urges four-way peace talks, Trump ordering a wider
# federal death penalty, the UN chief calling for global AI safety rules
# within a year, and the search going on after the Cikande factory fire, plus
# the India–New Zealand Test draw and the Kanton Island evacuation. Every
# fact was checked against reporting of 24 November 2026; the illustration
# carries no text, and all type on the page is drawn crisp by the build
# script so it stays legible at 300 pixels across.
#
# This program copies that image to /output/entry.png. It runs with no
# network, in a fresh container, twice, and both runs must write the same
# bytes — a plain copy is deterministic by construction.
#
# Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

import os
import shutil
import sys

PNG_MAGIC = b"\x89PNG\r\n\x1a\n"
JPEG_MAGIC = b"\xff\xd8\xff"
MAX_BYTES = 1048576  # 1 MiB, the competition's cap


def main() -> int:
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    with open(src, "rb") as f:
        data = f.read()
    if not (data.startswith(PNG_MAGIC) or data.startswith(JPEG_MAGIC)):
        print("entry.png is neither PNG nor JPEG", file=sys.stderr)
        return 1
    if len(data) > MAX_BYTES:
        print(f"entry.png is {len(data)} bytes, over the 1 MiB cap",
              file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dest = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dest)
    os.chmod(dest, 0o644)
    print(f"wrote {dest} ({len(data)} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
