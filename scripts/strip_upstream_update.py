#!/usr/bin/env python3
"""Remove only the upstream Zotero AI Butler update URL from an XPI.

Usage:
    python3 scripts/strip_upstream_update.py input.xpi output.xpi

The transformed file must be re-tested in Zotero. No network requests are made.
"""
from __future__ import annotations
import json
import sys
import zipfile
from pathlib import Path

UPSTREAM_URL = (
    "https://github.com/steven-jianhao-li/"
    "zotero-AI-Butler/releases/download/release/update.json"
)

def transform(source: Path, output: Path) -> None:
    if source.resolve() == output.resolve():
        raise ValueError("Input and output paths must differ.")
    with zipfile.ZipFile(source, "r") as zi, zipfile.ZipFile(output, "w") as zo:
        names = zi.namelist()
        if "manifest.json" not in names:
            raise ValueError("XPI does not contain root manifest.json")
        manifest = json.loads(zi.read("manifest.json"))
        zotero = manifest["applications"]["zotero"]
        if zotero.get("update_url") != UPSTREAM_URL:
            raise ValueError("Upstream update URL mismatch; refusing to change XPI")
        zotero.pop("update_url")
        for info in zi.infolist():
            data = zi.read(info.filename)
            if info.filename == "manifest.json":
                data = (json.dumps(manifest, ensure_ascii=False, indent=2) + "\n").encode("utf-8")
            zo.writestr(info, data)
    with zipfile.ZipFile(output) as z:
        if z.testzip() is not None:
            raise ValueError("Output ZIP failed integrity test")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        raise SystemExit("Usage: strip_upstream_update.py input.xpi output.xpi")
    transform(Path(sys.argv[1]), Path(sys.argv[2]))
    print("Created:", sys.argv[2])
