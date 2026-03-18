# 🚀 Duda Editor 2.0 Setup Guide

**Complete step-by-step instructions for implementing the BST theme in Duda**

---

## ⏱️ Quick Setup (10 Minutes)

### Step 1: Add Google Fonts (2 minutes)

1. In Duda, click **Site Settings** (gear icon)
2. Go to **Custom Code**
3. In the **Header** section, paste:

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=League+Spartan:wght@700&family=Noto+Sans:wght@700&family=Roboto:wght@400;500&display=swap" rel="stylesheet">
```

4. Click **Save**

---

### Step 2: Add BST CSS (3 minutes)

1. In Duda, click **Design** (paintbrush icon)
2. Scroll down and click **Custom CSS**
3. Open `/duda-export/bst-theme.css`
4. Copy **ALL** the CSS code
5. Paste into Duda's Custom CSS editor
6. Click **Save**

✅ **Your design system is now active!**

---

### Step 3: Add BST JavaScript (2 minutes)

1. Go back to **Site Settings** → **Custom Code**
2. In the **Footer** section (scroll down), paste:

```html
<script>
  // Paste the ENTIRE contents of bst-scripts.js here
</script>
```

3. Open `/duda-export/bst-scripts.js`
4. Copy **ALL** the JavaScript code
5. Paste it between the `<script>` tags in Duda
6. Click **Save**

✅ **Interactive features are now working!**

---

### Step 4: Create Your First Component (3 minutes)

1. In Duda Editor, click **Add Element** (+ button)
2. Choose **HTML Widget**
3. Drag it onto your page
4. Click **Edit HTML**
5. Open `/duda-export/pages/home-page.html`
6. Copy the **Hero Section** code (lines 1-20)
7. Paste into Duda's HTML widget
8. Click **Save**

✅ **You've created your first BST component!**

---

## 📂 File Organization

Your export package contains:

```
/duda-export/
│
├── bst-theme.css               ← Add to Custom CSS
├── bst-scripts.js              ← Add to Footer Custom Code
│
├── pages/
│   └── home-page.html          ← Complete page template
│
├── snippets/
│   ├── all-buttons.html        ← All button variants
│   ├── all-icons.html          ← Icon library
│   ├── all-section-headings.html ← Headers & titles
│   └── show-cards.html         ← Show card components
│
└── component-templates.html    ← Footer, stats, CTAs, etc.
```

---

## 🎨 Building Pages in Duda Editor 2.0

### Option A: Use Complete Page Templates

**Best for:** Creating full pages quickly

1. Open `/duda-export/pages/home-page.html`
2. Copy the ENTIRE file
3. In Duda, add a new **HTML Widget**
4. Paste the complete page code
5. Customize text, images, and links

**Available templates:**
- `home-page.html` - Complete homepage with hero, shows, stats, CTA

---

### Option B: Build with Individual Components

**Best for:** Custom layouts and flexibility

#### Example: Building a Custom Page

1. **Add Hero Section:**
   - Add HTML Widget
   - Copy hero code from `home-page.html` (lines 1-20)
   - Paste and customize

2. **Add Section Heading:**
   - Add HTML Widget below hero
   - Open `snippets/all-section-headings.html`
   - Copy "Standard Section Header"
   - Paste and customize

3. **Add Show Cards Grid:**
   - Add HTML Widget
   - Open `snippets/show-cards.html`
   - Copy "Show Card Grids (3-Column)"
   - Paste and customize

4. **Add CTA Section:**
   - Add HTML Widget
   - Open `component-templates.html`
   - Copy "CTA Section"
   - Paste and customize

---

## 🔧 Customizing Components

### Changing Text

Find the text in the HTML and edit directly:

```html
<h1 class="bst-heading-xl">
  YOUR NEW TEXT HERE
</h1>
```

### Changing Images

Replace the `src` URL:

```html
<!-- Before -->
<img src="https://images.unsplash.com/photo-..." alt="Show">

<!-- After -->
<img src="/path-to-your-image.jpg" alt="Your Show Title">
```

**Tip:** Upload images to Duda's Media Library, then right-click and "Copy Image URL"

### Changing Links

Update the `href` attribute:

```html
<!-- Before -->
<a href="/get-tickets" class="bst-btn bst-btn-primary bst-btn-lg">Buy Tickets</a>

<!-- After -->
<a href="https://bst.ludus.com/YOUR-SHOW-ID" class="bst-btn bst-btn-primary bst-btn-lg">Buy Tickets</a>
```

### Changing Colors (Global)

Edit the CSS variables in **Custom CSS**:

```css
:root {
  --bst-neon-teal: #YOUR_COLOR;  /* Change accent color */
}
```

---

## 📱 Responsive Design

**All components are automatically responsive!**

### Testing Responsiveness in Duda:

1. Click the **device icons** at the top (Desktop/Tablet/Mobile)
2. Switch between views to see how components adapt
3. Adjust spacing if needed using Duda's spacing controls

### Responsive Breakpoints:

- **Desktop:** 992px and up → 3-4 columns
- **Tablet:** 640px - 991px → 2 columns
- **Mobile:** < 640px → 1 column (stacked)

---

## 🎯 Component Quick Reference

### Buttons

**File:** `snippets/all-buttons.html`

**Variants:**
```html
<!-- Primary (Solid Teal) -->
<a href="#" class="bst-btn bst-btn-primary bst-btn-lg">Primary Button</a>

<!-- Secondary (Outlined) -->
<a href="#" class="bst-btn bst-btn-secondary bst-btn-md">Secondary Button</a>

<!-- BST Curve (Special) -->
<a href="#" class="bst-btn bst-btn-curve bst-btn-sm">Curve Button</a>
```

**Sizes:** `.bst-btn-lg` | `.bst-btn-md` | `.bst-btn-sm`

---

### Section Headers

**File:** `snippets/all-section-headings.html`

**Standard Header:**
```html
<div class="bst-section-header">
  <h2 class="bst-section-title">Section Title</h2>
  <p class="bst-section-subtitle">Subtitle Text</p>
</div>
```

**Features:**
- Automatically centered
- Includes teal underline glow
- Proper spacing

---

### Show Cards

**File:** `snippets/show-cards.html`

**Standard Card:**
```html
<div class="bst-card bst-show-card">
  <img src="..." alt="Show Title" class="bst-card-image">
  <span class="bst-card-category">Category</span>
  <h3 class="bst-card-title">Show Title</h3>
  <p class="bst-card-meta">Date & Time</p>
  <p class="bst-body-sm bst-mb-md">Description...</p>
  <a href="#" class="bst-btn bst-btn-curve bst-btn-md">Get Tickets</a>
</div>
```

**3-Column Grid:**
```html
<div class="bst-grid bst-grid-3">
  <!-- Paste 3 show cards here -->
</div>
```

---

### Icons

**File:** `snippets/all-icons.html`

**Example:**
```html
<svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="#14b8a6" stroke-width="2">
  <!-- Icon path here -->
</svg>
```

**50+ icons available** for:
- Theater & Performance
- Location & Contact
- Community & People
- Navigation & UI
- Social Media

---

## 🌟 Advanced Tips

### Creating Reusable Widgets

1. Build a component in an HTML Widget
2. Click **Save as Widget** in Duda
3. Name it (e.g., "BST Show Card")
4. Reuse across multiple pages

### Using Duda's Widget Library

1. Save frequently-used BST components as widgets
2. Access from **Widgets** panel (left sidebar)
3. Drag and drop onto any page

### Global Elements (Navbar/Footer)

1. Create navbar using `component-templates.html` footer code
2. Right-click → **Make Global**
3. Edit once, updates everywhere

---

## 🐛 Troubleshooting

### "Fonts not showing correctly"

✅ **Solution:**
- Verify Google Fonts link is in **Header** (not Footer)
- Clear Duda cache: **Site Settings** → **Advanced** → **Clear Cache**
- Hard refresh browser: Ctrl+Shift+R (PC) or Cmd+Shift+R (Mac)

### "Buttons not clickable"

✅ **Solution:**
- Check that `href` attribute is present
- Ensure button is not inside another clickable element
- Verify no overlapping elements (check z-index)

### "Cards not hovering"

✅ **Solution:**
- Ensure JavaScript is loaded (check Footer Custom Code)
- Verify `.bst-card` class name is correct (case-sensitive)
- Check browser console for errors (F12)

### "Mobile menu not opening"

✅ **Solution:**
- Verify JavaScript is in **Footer** (not Header)
- Check that `.bst-mobile-toggle` class is on button
- Ensure `.bst-mobile-menu` exists below navbar

### "Layout broken on mobile"

✅ **Solution:**
- Test in Duda's mobile preview
- Check for fixed widths (use percentages instead)
- Verify grid classes: `.bst-grid-3` automatically stacks on mobile

---

## ✅ Pre-Launch Checklist

Before publishing your Duda site:

- [ ] Test on **Desktop** view (1920px)
- [ ] Test on **Tablet** view (768px)
- [ ] Test on **Mobile** view (375px)
- [ ] Click all buttons and links
- [ ] Verify mobile menu opens/closes
- [ ] Check all images load correctly
- [ ] Test ticket links (open in new tab?)
- [ ] Verify forms work (if applicable)
- [ ] Run Duda's **SEO checker**
- [ ] Check page load speed
- [ ] Test in Chrome, Safari, and Firefox
- [ ] Verify accessibility (contrast, keyboard navigation)

---

## 🎬 Common Page Structures

### Home Page
```
1. Hero Section (from home-page.html)
2. Section Header "Upcoming Shows"
3. Show Cards Grid (3 cards)
4. Section Header "Why BST?"
5. Info Cards (3 features)
6. Stats Section
7. CTA Section
8. Footer (from component-templates.html)
```

### Get Tickets Page
```
1. Page Title Header
2. Calendar Filter Buttons
3. Show Cards Grid (all shows)
4. CTA Section
5. Footer
```

### About Page
```
1. Hero with Mission Statement
2. Two-Column Text + Image
3. Stats Section
4. Team Cards Grid
5. CTA Section
6. Footer
```

---

## 📞 Need More Help?

### Available Resources:

**Included Files:**
- `README.md` - Project overview
- `DESIGN-TOKENS.md` - Complete design system reference
- `duda-implementation-guide.md` - Additional tips

**Component Libraries:**
- `/snippets/` - Individual component files
- `/pages/` - Complete page templates
- `component-templates.html` - Additional components

**Duda Resources:**
- **Duda University:** https://university.duda.co
- **Duda Support:** Live chat in editor (bottom right)
- **Duda Community:** https://community.duda.co

---

## 🎨 Design System At a Glance

**Colors:**
- Background: `#111315` (Stage Black)
- Accent: `#14b8a6` (Neon Teal)
- Text: `#e8e8e8` (Primary), `#8a8f98` (Secondary)

**Fonts:**
- Headings: League Spartan (Bold, Uppercase)
- Body: Roboto (Regular)
- Buttons: Noto Sans (Bold, Uppercase)

**BST Curve:**
- Border-radius: `0px 10px 10px 0px`
- Applied to: All cards, buttons, images

**Shadows:**
- Default: Right-side shadow
- Hover: Teal glow effect

---

**You're all set! Start building your BST Duda site! 🎭✨**

---

## 🔄 Quick Updates

### Changing the Accent Color Site-Wide

Edit in **Custom CSS**:

```css
:root {
  --bst-neon-teal: #FF6B6B;  /* Example: Coral Red */
}
```

All buttons, borders, and accents update instantly!

### Adding a New Page

1. Create new page in Duda
2. Add HTML widgets for each section
3. Copy/paste from template files
4. Customize content
5. Add to navigation menu

---

**Last Updated: March 2026**
