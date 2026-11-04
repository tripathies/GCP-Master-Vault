#!/usr/bin/env python3
"""Render the canonical GCP mind-map SVG to its repository PNG asset."""
from pathlib import Path
import struct
import cairosvg

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "assets" / "GCP-CLOUD-MINDMAP.svg"
TARGET = ROOT / "assets" / "GCP-CLOUD-MINDMAP.png"

def main() -> None:
    if not SOURCE.is_file():
        raise FileNotFoundError(f"Mind-map SVG not found: {SOURCE}")
    TARGET.parent.mkdir(parents=True, exist_ok=True)
    cairosvg.svg2png(url=str(SOURCE), write_to=str(TARGET), output_width=2650, output_height=2560)
    with TARGET.open("rb") as stream:
        header = stream.read(24)
    if header[:8] != b"\x89PNG\r\n\x1a\n":
        raise RuntimeError("Renderer did not produce a valid PNG file")
    width, height = struct.unpack(">II", header[16:24])
    if (width, height) != (2650, 2560):
        raise RuntimeError(f"Unexpected PNG dimensions: {width}x{height}")
    print(f"Rendered {TARGET.relative_to(ROOT)} ({width}x{height})")

if __name__ == "__main__":
    main()
