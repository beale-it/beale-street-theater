# 🎨 BST Design System - Token Reference

A visual guide to all design tokens and component variants in the Beale Street Theater theme.

---

## 🎨 Color Palette

### Primary Colors
```
Stage Black (Background)
HEX: #111315
RGB: rgb(17, 19, 21)
USE: Main background color for all sections
```

```
Neon Teal (Accent)
HEX: #14b8a6
RGB: rgb(20, 184, 166)
USE: Buttons, borders, icons, links, highlights
```

### Text Colors
```
Text Primary (Headings)
HEX: #e8e8e8
RGB: rgb(232, 232, 232)
USE: All headings and emphasized text
```

```
Text Secondary (Body)
HEX: #8a8f98
RGB: rgb(138, 143, 152)
USE: Body copy, descriptions, captions
```

### Utility Colors
```
Border Teal Transparent
HEX: #14b8a633
RGBA: rgba(20, 184, 166, 0.2)
USE: Dividers, subtle borders
```

```
Card Background
HEX: #111315
RGB: rgb(17, 19, 21)
USE: Same as Stage Black (for consistency)
```

---

## 📐 Typography Scale

### Headings (League Spartan)

```
.bst-heading-xl
Font: League Spartan Bold
Size: clamp(2rem, 5vw, 3.5rem) [32px - 56px]
Weight: 700
Letter-spacing: 0.08em
Transform: uppercase
Line-height: 1.1
USE: Page titles, hero headings
```

```
.bst-heading-lg
Font: League Spartan Bold
Size: clamp(1.5rem, 4vw, 2.5rem) [24px - 40px]
Weight: 700
Letter-spacing: 0.08em
Transform: uppercase
Line-height: 1.2
USE: Section titles, major headings
```

```
.bst-heading-md
Font: League Spartan Bold
Size: 1.5rem [24px]
Weight: 700
Letter-spacing: 0.06em
Transform: uppercase
Line-height: 1.3
USE: Card titles, subsection headings
```

```
.bst-heading-sm
Font: League Spartan Bold
Size: 1.15rem [18.4px]
Weight: 700
Letter-spacing: 0.06em
Transform: uppercase
Line-height: 1.4
USE: Small headings, labels
```

### Labels (League Spartan)

```
.bst-label
Font: League Spartan Bold
Size: 0.7rem [11.2px]
Weight: 700
Letter-spacing: 0.15em
Transform: uppercase
Color: Neon Teal (#14b8a6)
USE: Category tags, eyebrows, micro-copy
```

### Body Text (Roboto)

```
.bst-body-lg
Font: Roboto Regular
Size: 1.05rem [16.8px]
Weight: 400
Line-height: 1.8
Color: Text Secondary (#8a8f98)
USE: Lead paragraphs, emphasis body
```

```
.bst-body
Font: Roboto Regular
Size: 1rem [16px]
Weight: 400
Line-height: 1.7
Color: Text Secondary (#8a8f98)
USE: Standard body copy
```

```
.bst-body-sm
Font: Roboto Regular
Size: 0.9rem [14.4px]
Weight: 400
Line-height: 1.6
Color: Text Secondary (#8a8f98)
USE: Small text, captions, metadata
```

---

## 🔘 Button System

### Variants

#### Primary Button (.bst-btn-primary)
```
Background: Neon Teal (#14b8a6)
Text: Stage Black (#111315)
Border: none
Border-radius: 0px 10px 10px 0px (BST Curve)
Hover: Opacity 0.9 + glow shadow
```
**USE: Primary actions (Buy Tickets, Submit, etc.)**

#### Secondary Button (.bst-btn-secondary)
```
Background: Transparent
Text: Neon Teal (#14b8a6)
Border: 2px solid Neon Teal (except left)
Border-radius: 0px 10px 10px 0px (BST Curve)
Hover: Background rgba(20, 184, 166, 0.1)
```
**USE: Secondary actions (Learn More, Cancel, etc.)**

#### BST Curve Button (.bst-btn-curve)
```
Background: Stage Black (#111315)
Text: Neon Teal (#14b8a6)
Border: 2px solid Neon Teal (except left)
Border-radius: 0px 10px 10px 0px (BST Curve)
Shadow: 12px 0 20px -8px rgba(20, 184, 166, 0.4)
Hover: Glow shadow
```
**USE: Special CTAs, highlighted actions**

### Sizes

```
.bst-btn-lg (Large)
Padding: 1rem 2rem [16px 32px]
Font-size: 0.85rem [13.6px]
USE: Hero CTAs, important actions
```

```
.bst-btn-md (Medium)
Padding: 0.75rem 1.5rem [12px 24px]
Font-size: 0.8rem [12.8px]
USE: Standard buttons throughout site
```

```
.bst-btn-sm (Small)
Padding: 0.5rem 1rem [8px 16px]
Font-size: 0.75rem [12px]
USE: Inline actions, newsletter subscribe
```

---

## 🎴 Card System

### Standard Card (.bst-card)
```
Background: #111315
Border: 2px solid #14b8a6 (top, right, bottom)
Border-left: none
Border-radius: 0px 10px 10px 0px
Padding: 1.5rem [24px]
Shadow: 12px 0 20px -8px rgba(20, 184, 166, 0.4)
Hover: translateX(4px) + glow shadow
```

### Card Elements

```
.bst-card-image
Width: 100%
Height: 240px
Object-fit: cover
Border-radius: 0px 10px 10px 0px
Margin-bottom: 1rem
```

```
.bst-card-category
Font: League Spartan Bold
Size: 0.7rem [11.2px]
Letter-spacing: 0.1em
Transform: uppercase
Color: Neon Teal (#14b8a6)
Display: inline-block
```

```
.bst-card-title
Font: League Spartan Bold
Size: 1.15rem [18.4px]
Letter-spacing: 0.04em
Transform: uppercase
Color: Text Primary (#e8e8e8)
```

```
.bst-card-meta
Font: Roboto Regular
Size: 0.85rem [13.6px]
Color: Text Secondary (#8a8f98)
```

---

## 📏 Spacing Scale

```css
--spacing-xs: 0.5rem   [8px]
--spacing-sm: 1rem     [16px]
--spacing-md: 1.5rem   [24px]
--spacing-lg: 2rem     [32px]
--spacing-xl: 3rem     [48px]
```

### Utility Classes
```
.bst-mb-xs  → margin-bottom: 8px
.bst-mb-sm  → margin-bottom: 16px
.bst-mb-md  → margin-bottom: 24px
.bst-mb-lg  → margin-bottom: 32px
.bst-mb-xl  → margin-bottom: 48px

.bst-mt-xs  → margin-top: 8px
.bst-mt-sm  → margin-top: 16px
.bst-mt-md  → margin-top: 24px
.bst-mt-lg  → margin-top: 32px
.bst-mt-xl  → margin-top: 48px
```

---

## 🌟 Shadow System

### Right-Side Shadow (Default)
```css
box-shadow: 12px 0 20px -8px rgba(20, 184, 166, 0.4);
```
**USE: All cards in default state**

### Glow Shadow (Hover/Active)
```css
box-shadow: 0 0 20px rgba(20, 184, 166, 0.3);
```
**USE: Hover states, active elements**

---

## 🔲 Border Radius (BST Curve)

### Standard BST Curve
```css
border-radius: 0px 10px 10px 0px;
```
**Breakdown:**
- Top-left: 0px (sharp corner)
- Top-right: 10px (rounded)
- Bottom-right: 10px (rounded)
- Bottom-left: 0px (sharp corner)

**Applied to:**
- All buttons
- All cards
- All card images
- Form inputs (optional)

---

## 📱 Grid System

### Classes
```html
.bst-grid       → Base grid container (gap: 2rem)
.bst-grid-1     → 1 column
.bst-grid-2     → 2 columns
.bst-grid-3     → 3 columns
.bst-grid-4     → 4 columns
```

### Responsive Behavior

**Desktop (992px+)**
```
.bst-grid-4 → 4 columns
.bst-grid-3 → 3 columns
.bst-grid-2 → 2 columns
.bst-grid-1 → 1 column
```

**Tablet (640px - 991px)**
```
.bst-grid-4 → 2 columns
.bst-grid-3 → 2 columns
.bst-grid-2 → 2 columns
.bst-grid-1 → 1 column
```

**Mobile (< 640px)**
```
All grids → 1 column
```

---

## 🎯 Section Structure

### Standard Section
```html
<section class="bst-section">
  <!-- Content with automatic padding and max-width -->
</section>
```

**Styles:**
- Padding: 4rem 1.5rem [64px 24px]
- Max-width: 1400px
- Margin: 0 auto (centered)

### Section Header
```html
<div class="bst-section-header">
  <h2 class="bst-section-title">Title Here</h2>
  <p class="bst-section-subtitle">Subtitle Here</p>
</div>
```

**Title styles:**
- Centered text
- Teal underline (80px wide, 4px tall)
- Glowing effect on underline
- Margin-bottom: 3rem

---

## 🎨 Usage Guidelines

### DO:
✅ Use Stage Black background consistently
✅ Apply BST Curve to all cards and buttons
✅ Use League Spartan for ALL headings
✅ Use Roboto for ALL body text
✅ Maintain uppercase transformation on headings
✅ Use right-side shadows exclusively
✅ Keep letter-spacing consistent

### DON'T:
❌ Mix different border radius styles
❌ Use gradients (prohibited in design system)
❌ Add left-side borders to cards
❌ Use font sizes outside the scale
❌ Override uppercase transformation
❌ Use colors outside the palette
❌ Add shadows to multiple sides

---

## 🔧 Customization Variables

All customizable tokens are in `:root`:

```css
:root {
  /* Colors */
  --bst-stage-black: #111315;
  --bst-neon-teal: #14b8a6;
  --bst-text-primary: #e8e8e8;
  --bst-text-secondary: #8a8f98;
  
  /* Typography */
  --font-heading: 'League Spartan', sans-serif;
  --font-body: 'Roboto', sans-serif;
  --font-button: 'Noto Sans', sans-serif;
  
  /* BST Curve */
  --bst-curve: 0px 10px 10px 0px;
  
  /* Shadows */
  --bst-shadow-right: 12px 0 20px -8px rgba(20, 184, 166, 0.4);
  --bst-shadow-glow: 0 0 20px rgba(20, 184, 166, 0.3);
  
  /* Spacing */
  --spacing-xs: 0.5rem;
  --spacing-sm: 1rem;
  --spacing-md: 1.5rem;
  --spacing-lg: 2rem;
  --spacing-xl: 3rem;
}
```

---

## 📐 Component Anatomy

### Show Card Breakdown
```
┌─────────────────────────────────┐
│  [Image - 240px tall]           │ (.bst-card-image)
│  Border-radius: BST Curve       │
├─────────────────────────────────┤
│  CATEGORY TAG                   │ (.bst-card-category)
│                                 │ Color: Neon Teal
├─────────────────────────────────┤
│  SHOW TITLE                     │ (.bst-card-title)
│                                 │ League Spartan Bold
├─────────────────────────────────┤
│  Feb 28, 2026 - 7:00 PM        │ (.bst-card-meta)
│                                 │ Roboto Regular
└─────────────────────────────────┘
Border: 2px Teal (top/right/bottom)
Border-left: none
Shadow: Right-side glow
Hover: Shift 4px right + brighter glow
```

### Button Breakdown
```
┌──────────────────────┐
│   BUY TICKETS        │ Text: All caps, letter-spaced
└──────────────────────┘
  0px    10px    10px   0px
  ↑      ↑       ↑      ↑
  TL     TR      BR     BL
  
Padding: 1rem 2rem (Large)
Font: Noto Sans Bold
Letter-spacing: 0.08em
Transform: uppercase
```

---

**This token system ensures visual consistency across all BST pages and components.**
