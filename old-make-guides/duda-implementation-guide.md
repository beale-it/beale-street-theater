# Beale Street Theater - Duda Implementation Guide

## 📋 Quick Start Checklist

- [ ] Add Google Fonts to Duda
- [ ] Upload `bst-theme.css` to Custom CSS
- [ ] Upload `bst-scripts.js` to Custom JavaScript
- [ ] Create HTML widgets using component templates below
- [ ] Test responsive design on mobile/tablet/desktop

---

## 🎨 Step 1: Add Google Fonts

### Option A: Duda Site Settings (Recommended)
1. Go to **Site Settings** → **Custom Code**
2. Add this to the **Header** section:

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=League+Spartan:wght@700&family=Noto+Sans:wght@700&family=Roboto:wght@400;500&display=swap" rel="stylesheet">
```

### Option B: Manual Font Upload
1. Download fonts from Google Fonts
2. Upload to Duda **Design** → **Fonts** → **Upload Custom Font**

---

## 🎯 Step 2: Add BST Theme CSS

1. Go to **Design** → **Custom CSS**
2. Copy the entire contents of `bst-theme.css`
3. Paste into the Custom CSS editor
4. Click **Save**

**Pro Tip:** The CSS uses CSS variables, so you can customize colors globally by changing the `:root` values at the top.

---

## ⚙️ Step 3: Add BST Scripts

1. Go to **Site Settings** → **Custom Code**
2. Add this to the **Footer** section (before `</body>`):

```html
<script src="/path-to-your-scripts/bst-scripts.js"></script>
```

Or paste the entire `bst-scripts.js` content directly:

```html
<script>
  // Paste bst-scripts.js content here
</script>
```

---

## 🧩 Step 4: HTML Component Templates

### Navigation (Navbar)

**Where to use:** Add as a **Global Element** or in your **Header**

```html
<nav class="bst-navbar">
  <div class="bst-navbar-container">
    <!-- Logo -->
    <a href="/">
      <img src="/images/bst-logo.png" alt="Beale Street Theater" class="bst-logo">
    </a>
    
    <!-- Desktop Navigation -->
    <ul class="bst-nav-links">
      <li><a href="/" class="bst-nav-link">Home</a></li>
      <li><a href="/get-tickets" class="bst-nav-link">Get Tickets</a></li>
      <li><a href="/youth-theater" class="bst-nav-link">Youth Theater</a></li>
      <li><a href="/community-theater" class="bst-nav-link">Community Theater</a></li>
      <li><a href="/about" class="bst-nav-link">About</a></li>
      <li><a href="/support" class="bst-nav-link">Support</a></li>
      <li><a href="/blog" class="bst-nav-link">Blog</a></li>
      <li><a href="/contact" class="bst-nav-link">Contact</a></li>
    </ul>
    
    <!-- CTA Button -->
    <a href="/get-tickets" class="bst-btn bst-btn-primary bst-btn-md">Buy Tickets</a>
    
    <!-- Mobile Toggle -->
    <button class="bst-mobile-toggle">
      <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
        <line x1="3" y1="12" x2="21" y2="12"></line>
        <line x1="3" y1="6" x2="21" y2="6"></line>
        <line x1="3" y1="18" x2="21" y2="18"></line>
      </svg>
    </button>
  </div>
  
  <!-- Mobile Menu -->
  <div class="bst-mobile-menu">
    <a href="/" class="bst-nav-link">Home</a>
    <a href="/get-tickets" class="bst-nav-link">Get Tickets</a>
    <a href="/youth-theater" class="bst-nav-link">Youth Theater</a>
    <a href="/community-theater" class="bst-nav-link">Community Theater</a>
    <a href="/about" class="bst-nav-link">About</a>
    <a href="/support" class="bst-nav-link">Support</a>
    <a href="/blog" class="bst-nav-link">Blog</a>
    <a href="/contact" class="bst-nav-link">Contact</a>
    <a href="/get-tickets" class="bst-btn bst-btn-primary bst-btn-md">Buy Tickets</a>
  </div>
</nav>
```

---

### Hero Section

```html
<section class="bst-hero">
  <div class="bst-hero-content">
    <div>
      <span class="bst-label">2026 Season Now On Sale</span>
      <h1 class="bst-heading-xl">
        WHERE EVERY SEAT<br>IS CENTER STAGE
      </h1>
      <p class="bst-body bst-mb-lg">
        Beale Street Theater brings Kingman's boldest stories to life on Route 66. 
        From soul-stirring drama to electrifying live music, experience performances 
        that move you — in a venue built for intimacy.
      </p>
      <div style="display: flex; gap: 1rem; flex-wrap: wrap;">
        <a href="/get-tickets" class="bst-btn bst-btn-primary bst-btn-lg">View Season</a>
        <a href="/about" class="bst-btn bst-btn-secondary bst-btn-lg">Our Story</a>
      </div>
    </div>
    <div>
      <img src="/images/bst-logo.png" alt="BST Logo" style="max-width: 400px; width: 100%;">
    </div>
  </div>
</section>
```

---

### Section Header

```html
<div class="bst-section-header">
  <h2 class="bst-section-title">Upcoming Shows</h2>
  <p class="bst-section-subtitle">2026 Season</p>
</div>
```

---

### Show Card

```html
<div class="bst-card bst-show-card" data-ticket-url="https://bst.ludus.com/200484012">
  <img src="/images/show-phantom-tollbooth.jpg" alt="The Phantom Tollbooth" class="bst-card-image">
  <span class="bst-card-category">Community Theater</span>
  <h3 class="bst-card-title">The Phantom Tollbooth</h3>
  <p class="bst-card-meta">Feb 28, 2026 - 7:00 PM</p>
</div>
```

---

### Show Cards Grid (3-column)

```html
<section class="bst-section">
  <div class="bst-section-header">
    <h2 class="bst-section-title">Upcoming Shows</h2>
    <p class="bst-section-subtitle">2026 Season</p>
  </div>
  
  <div class="bst-grid bst-grid-3">
    <!-- Show Card 1 -->
    <div class="bst-card bst-show-card" data-ticket-url="https://bst.ludus.com/200484012">
      <img src="/images/show1.jpg" alt="The Phantom Tollbooth" class="bst-card-image">
      <span class="bst-card-category">Community Theater</span>
      <h3 class="bst-card-title">The Phantom Tollbooth</h3>
      <p class="bst-card-meta">Feb 28, 2026 - 7:00 PM</p>
    </div>
    
    <!-- Show Card 2 -->
    <div class="bst-card bst-show-card" data-ticket-url="https://bst.ludus.com/200519317">
      <img src="/images/show2.jpg" alt="Improv Group" class="bst-card-image">
      <span class="bst-card-category">Special Event</span>
      <h3 class="bst-card-title">Improv Group: "TBD"</h3>
      <p class="bst-card-meta">Mar 6, 2026 - 7:00 PM</p>
    </div>
    
    <!-- Show Card 3 -->
    <div class="bst-card bst-show-card" data-ticket-url="https://bst.ludus.com/200512719">
      <img src="/images/show3.jpg" alt="Baritone Robert Sims" class="bst-card-image">
      <span class="bst-card-category">Concert Series</span>
      <h3 class="bst-card-title">Baritone Robert Sims</h3>
      <p class="bst-card-meta">Mar 7, 2026 - 7:00 PM</p>
    </div>
  </div>
</section>
```

---

### Info Card (with Icon)

```html
<div class="bst-card">
  <div class="bst-icon-box bst-mb-md">
    <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
      <!-- Heart icon -->
      <path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"></path>
    </svg>
    <h3 class="bst-heading-sm">Community First</h3>
  </div>
  <p class="bst-body-sm">
    We create opportunities for local artists and provide accessible arts education 
    to youth throughout Mohave County.
  </p>
</div>
```

---

### CTA Section

```html
<section class="bst-section">
  <div class="bst-card bst-text-center" style="padding: 3rem;">
    <span class="bst-label bst-mb-sm">Join Our Community</span>
    <h2 class="bst-heading-lg bst-mb-md">BECOME A PART OF BST</h2>
    <p class="bst-body bst-mb-lg" style="max-width: 600px; margin-left: auto; margin-right: auto;">
      Whether you want to volunteer, audition, or support our mission, there are 
      many ways to get involved with Beale Street Theater.
    </p>
    <div style="display: flex; gap: 1rem; justify-content: center; flex-wrap: wrap;">
      <a href="/volunteer" class="bst-btn bst-btn-primary bst-btn-lg">Volunteer</a>
      <a href="/support" class="bst-btn bst-btn-secondary bst-btn-lg">Support BST</a>
    </div>
  </div>
</section>
```

---

### Button Examples

```html
<!-- Primary Button -->
<a href="#" class="bst-btn bst-btn-primary bst-btn-lg">Primary Action</a>

<!-- Secondary Button -->
<a href="#" class="bst-btn bst-btn-secondary bst-btn-md">Secondary Action</a>

<!-- BST Curve Button -->
<a href="#" class="bst-btn bst-btn-curve bst-btn-sm">BST Curve CTA</a>
```

---

## 📱 Duda-Specific Tips

### 1. **Using Duda Widgets**
- Create a **Custom HTML Widget** for each component
- Name them clearly: "BST - Hero Section", "BST - Show Cards", etc.
- Save to your **Widget Library** for reuse

### 2. **Global Elements**
- Make the navbar a **Global Element** so it appears on all pages
- Edit once, updates everywhere

### 3. **Page Templates**
- Create page templates for common layouts (Home, Show Pages, etc.)
- Save templates to reuse for new pages

### 4. **Responsive Design**
- Duda's built-in responsive editor works with this CSS
- Test on **Desktop**, **Tablet**, and **Mobile** views
- Use Duda's breakpoint editor to adjust spacing if needed

### 5. **Image Optimization**
- Upload images to Duda's **Media Library**
- Duda automatically optimizes and serves WebP format
- Use lazy loading for better performance

### 6. **Dynamic Content**
- For show listings, use Duda's **Collection** feature
- Connect BST cards to a "Shows" collection
- Auto-generate pages from your data

---

## 🎨 Customization

### Change Colors
Edit the CSS variables in `:root`:

```css
:root {
  --bst-stage-black: #111315;  /* Background */
  --bst-neon-teal: #14b8a6;    /* Accent color */
  --bst-text-primary: #e8e8e8; /* Headings */
  --bst-text-secondary: #8a8f98; /* Body text */
}
```

### Change Fonts
Replace Google Fonts link with your preferred fonts, then update:

```css
:root {
  --font-heading: 'Your Heading Font', sans-serif;
  --font-body: 'Your Body Font', sans-serif;
}
```

---

## 🐛 Troubleshooting

### Fonts not loading?
- Check that Google Fonts link is in **Site Settings** → **Header**
- Clear Duda cache: **Settings** → **Advanced** → **Clear Cache**

### JavaScript not working?
- Ensure script is in **Footer** (not Header)
- Check browser console for errors (F12)
- Verify class names match exactly (case-sensitive)

### Cards not hovering?
- JavaScript must be loaded for hover effects
- Check that `.bst-card` class is applied correctly

### Mobile menu not opening?
- Ensure `.bst-mobile-toggle` and `.bst-mobile-menu` classes are present
- Check that JavaScript is loaded

---

## 📞 Need More Help?

Let me know:
1. **Which Duda plan you're on** (Flex vs Classic)
2. **Specific components you need** (I can create more templates)
3. **Any custom functionality** you want to add

I can provide:
- More component templates
- Custom Duda collection integration
- Advanced JavaScript features
- Specific page layouts

---

## ✅ Final Checklist

Before going live:

- [ ] Test on all devices (mobile, tablet, desktop)
- [ ] Check all links work correctly
- [ ] Verify images are optimized and loading
- [ ] Test forms (contact, newsletter)
- [ ] Ensure navbar is sticky and functional
- [ ] Validate mobile menu opens/closes
- [ ] Check page load speed
- [ ] Test in multiple browsers (Chrome, Safari, Firefox)
- [ ] Verify accessibility (contrast, keyboard navigation)
- [ ] Run Duda's built-in SEO checker

---

**You're ready to launch BST on Duda! 🎭✨**
