# 🎭 Beale Street Theater - Duda Theme Package

**A complete, production-ready design system for Duda website builder**

---

## 📦 What's Included

This package contains everything you need to recreate the BST design in Duda:

```
/duda-export/
├── bst-theme.css                 # Complete CSS design system
├── bst-scripts.js                # Vanilla JavaScript functionality
├── component-templates.html      # 15+ copy-paste HTML components
├── duda-implementation-guide.md  # Step-by-step setup instructions
└── README.md                     # This file
```

---

## 🚀 Quick Start (5 Minutes)

### 1. Add Google Fonts
In Duda, go to **Site Settings** → **Custom Code** → **Header**:

```html
<link href="https://fonts.googleapis.com/css2?family=League+Spartan:wght@700&family=Noto+Sans:wght@700&family=Roboto:wght@400;500&display=swap" rel="stylesheet">
```

### 2. Add CSS
Go to **Design** → **Custom CSS** and paste the entire contents of `bst-theme.css`

### 3. Add JavaScript
Go to **Site Settings** → **Custom Code** → **Footer** and paste the entire contents of `bst-scripts.js` wrapped in `<script>` tags

### 4. Start Building
Use the templates in `component-templates.html` to build your pages!

---

## 🎨 Design System Overview

### Colors
- **Stage Black**: `#111315` (Background)
- **Neon Teal**: `#14b8a6` (Accent)
- **Text Primary**: `#e8e8e8` (Headings)
- **Text Secondary**: `#8a8f98` (Body text)

### Typography
- **Headings**: League Spartan (Bold, uppercase, increased tracking)
- **Body**: Roboto (Regular, comfortable line-height)
- **Buttons**: Noto Sans (Bold, uppercase)

### BST Curve
The signature asymmetrical rounding:
- Left: 0px
- Right: 10px
- Applied to all cards, buttons, and components

### Shadows
- Right-side drop shadow with teal glow effect
- Creates the "neon marquee" aesthetic

---

## 📚 Component Library

All components are in `component-templates.html`:

- ✅ Navigation (desktop + mobile)
- ✅ Hero sections
- ✅ Show cards (with hover effects)
- ✅ Info cards (with icons)
- ✅ Section headers
- ✅ Buttons (3 variants, 3 sizes)
- ✅ CTA sections
- ✅ Stats/KPI cards
- ✅ Contact info cards
- ✅ Footer
- ✅ Testimonials
- ✅ Two-column layouts
- ✅ FAQ/Accordion structure
- ✅ Image gallery
- ✅ Breadcrumbs

---

## 🎯 Duda-Specific Features

### CSS Variables
All colors and fonts use CSS variables for easy customization:

```css
:root {
  --bst-stage-black: #111315;
  --bst-neon-teal: #14b8a6;
  /* Change these to customize globally */
}
```

### Responsive Grid
Built-in responsive grid system:

```html
<div class="bst-grid bst-grid-3">
  <!-- 3 columns on desktop, 2 on tablet, 1 on mobile -->
</div>
```

### Utility Classes
Quick styling with utility classes:

```html
<div class="bst-mb-lg bst-text-center">
  <!-- Margin-bottom large, centered text -->
</div>
```

---

## 🔧 Customization Guide

### Change Brand Colors

Edit in `bst-theme.css`:

```css
:root {
  --bst-neon-teal: #YOUR_COLOR; /* Change accent color */
}
```

### Change Fonts

1. Add your font link to Duda Header
2. Update CSS variables:

```css
:root {
  --font-heading: 'Your Font', sans-serif;
}
```

### Modify Button Styles

All button styles are in the `.bst-btn-*` classes:

```css
.bst-btn-primary {
  background-color: var(--bst-neon-teal);
  /* Customize here */
}
```

---

## 📱 Responsive Breakpoints

CSS automatically adapts at these breakpoints:

- **Desktop**: 992px and up
- **Tablet**: 640px - 991px
- **Mobile**: 639px and below

Test in Duda's responsive editor!

---

## ⚡ Performance Tips

### Images
- Use Duda's **Media Library** for automatic optimization
- Upload high-quality images (Duda compresses them)
- Enable lazy loading for below-the-fold images

### Fonts
- Using Google Fonts CDN for fast loading
- Only loading necessary font weights (400, 500, 700)

### JavaScript
- All scripts are vanilla JS (no dependencies)
- Minimal file size for fast page loads

---

## 🧪 Testing Checklist

Before launching:

- [ ] Test on mobile (iOS + Android)
- [ ] Test on tablet
- [ ] Test on desktop (1920px wide)
- [ ] Verify all buttons work
- [ ] Check mobile menu opens/closes
- [ ] Validate form submissions
- [ ] Test page load speed
- [ ] Check browser compatibility (Chrome, Safari, Firefox)
- [ ] Verify accessibility (keyboard navigation, contrast)
- [ ] Run Duda's SEO checker

---

## 🎬 Example Implementations

### Full Home Page Structure

```html
<!-- Navigation -->
[Copy navbar from component-templates.html]

<!-- Hero Section -->
[Copy hero from component-templates.html]

<!-- Featured Shows -->
<section class="bst-section">
  [Copy show cards grid from component-templates.html]
</section>

<!-- Stats -->
<section class="bst-section">
  [Copy stats/KPI from component-templates.html]
</section>

<!-- CTA -->
[Copy CTA section from component-templates.html]

<!-- Footer -->
[Copy footer from component-templates.html]
```

### Simple About Page

```html
<!-- Navigation -->
[Use global navbar element]

<!-- Hero -->
[Copy hero with text + logo image]

<!-- Mission Cards -->
<section class="bst-section">
  [Copy info cards with icons]
</section>

<!-- Two-Column Story -->
[Copy text + image layout]

<!-- CTA -->
[Copy CTA section]

<!-- Footer -->
[Use global footer element]
```

---

## 🆘 Common Issues & Solutions

### "Fonts not displaying correctly"
- Check Google Fonts link is in **Header** (not Footer)
- Clear Duda cache: Settings → Advanced → Clear Cache

### "Mobile menu not working"
- Ensure JavaScript is in **Footer** section
- Verify `.bst-mobile-toggle` class is on button
- Check browser console for errors (F12)

### "Cards not hovering"
- JavaScript must be loaded for hover effects
- Check class name is exactly `.bst-card` (case-sensitive)

### "Colors look different"
- Verify CSS variables in `:root` are correct
- Check for conflicting Duda default styles
- Use browser inspector to debug

### "Buttons too small on mobile"
- Use `.bst-btn-lg` for important CTAs
- Duda will automatically optimize button sizes

---

## 🔗 Useful Duda Resources

- **Duda University**: Training videos and tutorials
- **Duda Support**: Live chat support for technical issues
- **Duda Community**: Forums for tips and best practices

---

## 🎨 Design Philosophy

This theme follows BST's core design principles:

1. **Stage Black Background**: Creates dramatic contrast
2. **Neon Teal Accents**: Evokes vintage marquee signage
3. **BST Curve**: Unique asymmetrical element for brand recognition
4. **Right-Side Shadows**: Directional lighting effect
5. **Bold Typography**: High contrast for readability and impact

---

## 📞 Need Help?

If you need additional components, custom functionality, or have questions:

**Share with me:**
1. Your Duda plan type (Flex/Classic)
2. Specific component you need
3. Screenshots of any issues

**I can create:**
- Additional page templates
- Custom Duda collection integration
- Advanced JavaScript features
- Specific layout requests

---

## ✨ Next Steps

1. **Set up the base** (fonts, CSS, JS)
2. **Create global elements** (navbar, footer)
3. **Build your first page** using templates
4. **Customize colors/fonts** to your brand
5. **Add content** (images, text, shows)
6. **Test thoroughly** on all devices
7. **Launch!** 🚀

---

**Built for Beale Street Theater with ❤️**

*Version 1.0 - March 2026*
