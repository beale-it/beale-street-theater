# BST Safe-Scope Patch — Applied 2026-03-11

> **Status: ✅ ALL PATCHES APPLIED**
> Both `bst-theme.css` and `bst-scripts.js` have been updated per the instructions below.

---

## 1) CSS (`bst-theme.css` → Developer Mode → site.css)

### 1.1 ✅ Global reset removed
Deleted:
```css
* { margin: 0; padding: 0; box-sizing: border-box; }
```

### 1.2 ✅ Body limited to background only
```css
body { background-color: var(--bst-stage-black); }
```
No global font, color, or margins/padding.

### 1.3 ✅ `.bst-scope` base styles added (after `:root`)
```css
.bst-scope {
  color: var(--bst-text-primary);
  font-family: var(--font-body);
  line-height: 1.6;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

.bst-scope,
.bst-scope * { box-sizing: border-box; }
```

### 1.4 ✅ Background helper classes added
```css
.bst-bg-stage { background-color: var(--bst-stage-black); }
.bst-bg-card  { background-color: var(--bst-bg-card); }
```

---

## 2) JavaScript (`bst-scripts.js` → Site Settings → Custom Code → Body End/Footer)

### 2.1 ✅ All initializers accept `root`
Every `init*()` function now receives a `root` parameter and queries within it.

### 2.2 ✅ `root` sourced from `.bst-scope`
```js
var root = document.querySelector('.bst-scope');
if (!root) return; // no .bst-scope on this page – do nothing
```

### 2.3 ✅ `initCardHoverEffects()` removed
Function deleted; all references removed from `runInitializers()` and `window.BST`.
CSS `:hover` rule on `.bst-card` already handles the effect.

### 2.4 ✅ `initShowCardClicks` no longer hijacks inner links/buttons
```js
card.addEventListener('click', function(e) {
  if (e.target.closest('a') || e.target.closest('button')) return;
  // ...
});
```

---

## 3) Hardline Rules (unchanged)

| Rule | Detail |
|------|--------|
| BST components | Must be wrapped in `<div class="bst-scope">…</div>` |
| Ludus embeds | Must **NOT** be inside `.bst-scope` |
| Ludus embed code | Do not modify |

---

## Day-to-Day Building Rules

### BST widgets
Wrap every BST-designed HTML widget like this:
```html
<div class="bst-scope bst-bg-stage">
  <!-- BST component HTML -->
</div>
```
Swap to `.bst-bg-card` or use container/column backgrounds for different sections.

### Ludus embeds (Get Tickets + dynamic show page)
Keep the Ludus embed in its own HTML widget — **not** wrapped in `.bst-scope`.
The dynamic `showID` / collection-driven mapping approach works fine with this setup.

---

## One-Time Setup Checklist

| Step | Location | Action |
|------|----------|--------|
| Fonts | Site Settings → Custom Code → Head/Header | Paste Google Fonts `<link>` (with preconnect + `display=swap`) |
| BST CSS | Developer Mode → site.css | Paste patched `bst-theme.css` |
| BST JS | Site Settings → Custom Code → Body End/Footer | Paste patched `bst-scripts.js` |
| Republish | — | Republish after any code changes |

---

## Future Theme Changes

- **Global vibe change:** Update `--bst-stage-black` in `:root` (or change `body { background-color }`)
- **Per-section tweaks:** Use container/column backgrounds or `.bst-bg-*` helpers — no need to rewrite everything