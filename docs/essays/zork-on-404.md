---
layout: post
title: Zork on a 404
date: 2025-06-03
tags:
- Zork
- interactive fiction
- MkDocs
- Z-machine
- MIT
categories:
- Technical Essays
---

## What?  A Zork 404 page?

A 404 page on this simple site...because [Microsoft open sourced Zork](https://opensource.microsoft.com/blog/2025/11/20/preserving-code-that-shaped-generations-zork-i-ii-and-iii-go-open-source/) and I've wanted to do this for many years.

Why?

The utterly bastard groovy feature at the homepage of [Sisters of Mercy](https://www.the-sisters-of-mercy.com/), the likely work of Eldrith and Bax Corp. and Dr. Jeep themselves: [The 404 page with a custom text adventure game](https://www.the-sisters-of-mercy.com/we-are-not-a-goth-band).

That's why.


## The License

Zork was proprietary. Infocom closed in 1989. For thirty-six years, the game was frozen: reference-only, archived, untouchable. In November 2025, Microsoft opened it. MIT License. The source code went to GitHub as `historicalsource/zork1` along with the compiled Z-machine binary, `COMPILED/zork1.z3`.

This changes everything.

## The Stack

Three pieces, all MIT-licensed, all fits together:

1. **The game:** `zork1.z3` (86 KB). The compiled Z-machine V3 bytecode from `historicalsource/zork1/COMPILED/`. Copy it to your assets.

2. **The interpreter:** `zvm.min.js` — ifvms.js, written by Dannii Willis. It's the Z-machine engine Parchment uses. Loads in the browser as `window.ZVM`. Export `zvm.min.js` from the ifvms npm package (or fetch it separately) to your assets.

3. **The Glk shim:** You write this. ZVM doesn't talk to the DOM directly. It uses Glk, the Virtual Machine interface standard. You implement Glk methods that write to a `<div>`, read from an `<input>`, and resume the VM when the player types. A minimal implementation is ~150 lines.

## The MkDocs Problem

Material for MkDocs declares `404.html` as a static template. During the build, it copies your custom `docs/404.html` into `_site/` first, then Material's theme template overwrites it. Your file is gone.

The solution: a `on_post_build` hook. Create `hooks/copy_404.py`:

```python
import shutil
from pathlib import Path

def on_post_build(config, **kwargs):
    """Copy docs/404.html to site_dir, overwriting Material's version."""
    src = Path(config['docs_dir']) / '404.html'
    dst = Path(config['site_dir']) / '404.html'
    if src.exists():
        shutil.copy(src, dst)
```

Add this to `mkdocs.yml`:

```yaml
hooks:
  - hooks/copy_404.py
```

MkDocs calls `on_post_build` after every build—including the incremental rebuilds during `mkdocs serve`. Your custom 404 stays in place.

## Wiring Glk

ZVM runs synchronously until it needs input. It calls `Glk.glk_select(eventStruct)` and pauses. Your code resumes it by calling `vmRef.resume(eventStruct)` with the player's input.

The minimal pattern:

```javascript
let pendingEvent, pendingBuf;

const Glk = {
  glk_put_jstring: function(text) {
    output.textContent += text;
  },
  glk_request_line_event_uni: function(win, buf) {
    pendingBuf = buf;
  },
  glk_select: function(event) {
    pendingEvent = event;
    input.disabled = false;
    input.focus();
  },
  // ... (other methods as no-ops or stubs)
};

function submitInput() {
  const text = input.value;
  input.disabled = true;
  
  // Fill the buffer the VM provided
  if (pendingBuf) {
    for (let i = 0; i < text.length && i < pendingBuf.length; i++) {
      pendingBuf[i] = text.charCodeAt(i);
    }
    pendingEvent._f = [3, null, text.length, 0]; // line event
  }
  
  vmRef.resume(pendingEvent);
}
```

The VM pauses at `glk_select()`. You enable the input field and attach a listener. On submit, fill the buffer, mark the event type, call `vmRef.resume()`. The VM wakes up, reads the player's command, and continues until the next `glk_select()`.

## The Bootstrap

```javascript
fetch('/assets/zork/zork1.z3')
  .then(r => r.arrayBuffer())
  .then(buf => {
    vmRef = new ZVM();
    vmRef.prepare(new Uint8Array(buf), { Glk: Glk });
    vmRef.start();
  });
```

Load the game file. Create a ZVM instance. Call `prepare()` with the bytecode and your Glk object. Call `start()`. The VM runs, encounters `glk_select()` on the first turn, and waits for input.

## What Doesn't Work

Save and restore: `glk_fileref_create_by_prompt()` returns null. The VM treats it as cancelled. You can't save the game state in the browser. Acceptable for a 404 page.

Status bar window: The upper window is declared but output goes nowhere. It's where Zork prints "Score: 34 Moves: 12". You can implement it; most players won't miss it.

## Deploy

1. Copy `zork1.z3` to `docs/assets/zork/`
2. Copy `zvm.min.js` to `docs/assets/lib/`
3. Place your custom `docs/404.html` in the repo root
4. Add the `copy_404.py` hook and the `hooks:` entry to `mkdocs.yml`
5. Run `mkdocs build`. Material's 404 is overwritten. Zork lives on yours.
6. Test locally: `mkdocs serve` and visit `/nonexistent`.

You now have a 404 page where lost users can replay a classic game. The page tells them nothing else — no nav, no way back. They can quit. They can try to solve the puzzle. They can wander in the dark. That's the point.

---

**Sources:** [historicalsource/zork1](https://github.com/historicalsource/zork1), [ifvms.js](https://github.com/curiousdannii/parchment), [MkDocs hooks documentation](https://www.mkdocs.org/user-guide/plugins/#hooks)
