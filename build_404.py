#!/usr/bin/env python3
"""Post-build script: copy custom 404.html to _site root without MkDocs processing."""
import shutil
from pathlib import Path

src = Path("docs/404.html")
dst = Path("_site/404.html")

if src.exists():
    shutil.copy(src, dst)
    print(f"✓ Copied {src} → {dst}")
else:
    print(f"✗ {src} not found")
