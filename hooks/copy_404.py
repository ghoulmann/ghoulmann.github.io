import shutil
from pathlib import Path


def on_post_build(config, **kwargs):
    """Copy docs/404.html to site_dir after build, overwriting Material theme's version."""
    src = Path(config['docs_dir']) / '404.html'
    dst = Path(config['site_dir']) / '404.html'
    if src.exists():
        shutil.copy(src, dst)
