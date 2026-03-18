# 🚀 BST Duda Launch Night Guide

**Quick implementation guide for embedding pages tonight**

---

## ✅ **What's New (Since Last Week)**

I've created **4 new complete page templates** with clear placeholder breaks for your Duda widgets:

### **New Pages:**
1. **`get-tickets-page.html`** - Shows organized by category (Concert, Youth, Community, Special Events) + FAQ
2. **`youth-theater-page.html`** - Youth Productions + Auditions + Classes sections
3. **`support-page.html`** - All 4 support programs (Sponsor, Equipment, Adopt-a-Seat, Pay-It-Forward)
4. **`community-theater-page.html`** - Volunteer + Auditions + Classes sections

### **New Component:**
5. **`show-page-header.html`** - 3 header layouts for individual show detail pages

---

## 🎯 **Tonight's Implementation Plan (30 Minutes)**

### **Step 1: Setup (If not done yet) - 5 minutes**

1. Add Google Fonts to **Site Settings** → **Custom Code** → **Header**:
```html
<link href="https://fonts.googleapis.com/css2?family=League+Spartan:wght@700&family=Noto+Sans:wght@700&family=Roboto:wght@400;500&display=swap" rel="stylesheet">
```

2. Paste `bst-theme.css` into **Design** → **Custom CSS**

3. Paste `bst-scripts.js` into **Site Settings** → **Custom Code** → **Footer** (wrapped in `<script>` tags)

---

### **Step 2: Embed Your First Page - 5 minutes**

**Start with Home Page:**

1. Open `/duda-export/pages/home-page.html`
2. In Duda, add **HTML Widget** to your homepage
3. Copy/paste the entire home page code
4. Replace placeholder images with your actual images
5. Update ticket links
6. **Save and Preview**

---

### **Step 3: Add Other Pages - 15 minutes**

Use the same process for each page:

| Page | File | What to Customize |
|------|------|-------------------|
| **Get Tickets** | `get-tickets-page.html` | Replace show cards in each category section |
| **Youth Theater** | `youth-theater-page.html` | Add your youth productions, update audition notices |
| **Support** | `support-page.html` | Update sponsorship tiers, equipment needs |
| **Community Theater** | `community-theater-page.html` | Add your volunteer form, current auditions |

---

### **Step 4: Individual Show Pages - 5 minutes per show**

1. Open `/duda-export/snippets/show-page-header.html`
2. Choose **Option 1** (Hero-Style) - it's the most impressive
3. Copy the code
4. Create new Duda page for the show
5. Add HTML Widget at the top
6. Paste header code
7. **Customize:**
   - Replace `SHOW-POSTER-IMAGE-URL-HERE.jpg` with your show poster
   - Update show title
   - Update dates, times, venue
   - Update ticket link
   - Update category badge

---

## 📋 **Finding Placeholders for Your Widgets**

Each page template has clear markers:

```html
<!-- ▼▼▼ DUDA PLACEHOLDER: Insert your widget here ▼▼▼ -->

<!-- Your Duda widget goes between these markers -->

<!-- ▲▲▲ END DUDA PLACEHOLDER ▲▲▲ -->
```

**How to use:**
1. Find the placeholder marker
2. Delete the example content (if any)
3. Add your Duda widget (collection, form, calendar, etc.)
4. Keep the placeholder comments for future reference

---

## 🎨 **Quick Customizations**

### **Change Text**
Find any text in the HTML and edit directly:
```html
<h1 class="bst-heading-xl">YOUR NEW TEXT</h1>
```

### **Change Images**
Replace the `src` URL:
```html
<img src="YOUR-IMAGE-URL.jpg" alt="Description">
```

**Pro Tip:** Upload images to Duda Media Library, then right-click → "Copy Image URL"

### **Change Links**
Update the `href`:
```html
<a href="YOUR-LINK-HERE" class="bst-btn bst-btn-primary bst-btn-lg">Button Text</a>
```

### **Change Colors (Site-Wide)**
Edit in **Custom CSS** (at the top):
```css
:root {
  --bst-neon-teal: #14b8a6;  /* Change this to any color */
}
```

---

## 🔥 **Page Template Features**

### **Get Tickets Page**
- ✅ Category sections with glow borders (Concert, Youth, Community, Special Events)
- ✅ Placeholder breaks for show card grids
- ✅ FAQ section at bottom
- ✅ Responsive 3-column grid (stacks on mobile)

### **Youth Theater Page**
- ✅ Program overview with icons
- ✅ Featured audition notice card
- ✅ Audition prep tips
- ✅ Classes grid with enrollment buttons

### **Support Page**
- ✅ 4-card overview of support programs
- ✅ Detailed sections for each program
- ✅ Sponsorship tier cards
- ✅ Equipment needs list
- ✅ Adopt-a-Seat details with placeholder for seat map
- ✅ Pay-It-Forward impact stats

### **Community Theater Page**
- ✅ Volunteer roles grid (3 categories)
- ✅ Featured audition notice
- ✅ Audition tips (before & day-of)
- ✅ Classes grid

### **Show Page Header**
- ✅ 3 layout options (Hero, Compact, Full-Width Banner)
- ✅ Show meta info with icons (dates, times, venue, price)
- ✅ CTA buttons for tickets
- ✅ Responsive design

---

## 🚨 **Common Issues & Quick Fixes**

### **"Fonts look weird"**
✅ Make sure Google Fonts link is in **Header** (not Footer)

### **"Buttons not working"**
✅ Check that `href="#"` is updated to your actual link

### **"Layout broken on mobile"**
✅ Preview in Duda's mobile view
✅ Remove any fixed widths

### **"Images not loading"**
✅ Verify image URLs are correct
✅ Make sure images are uploaded to Duda Media Library

### **"Widgets not showing"**
✅ Make sure you're pasting widgets BETWEEN the placeholder markers
✅ Check that widget is set to "visible"

---

## 📂 **File Locations**

All new files are in `/duda-export/pages/`:

```
/duda-export/
├── pages/
│   ├── home-page.html              ← Already had this
│   ├── get-tickets-page.html       ← NEW
│   ├── youth-theater-page.html     ← NEW
│   ├── support-page.html           ← NEW
│   └── community-theater-page.html ← NEW
│
└── snippets/
    └── show-page-header.html       ← NEW (3 layout options)
```

---

## ⚡ **Speed Tips**

### **Copy-Paste Workflow:**
1. Open page template file
2. Ctrl+A (Select All)
3. Ctrl+C (Copy)
4. In Duda, add HTML Widget
5. Ctrl+V (Paste)
6. Find-and-replace placeholder text
7. Save!

### **Batch Image Updates:**
1. Upload all images to Duda Media Library first
2. Copy each image URL
3. Use Find & Replace in code editor to swap URLs

### **Duplicate Pages:**
- Once you've customized one show page header, duplicate it in Duda
- Change only the show-specific details
- Saves time!

---

## 🎯 **Priority Order for Tonight**

If you're short on time, implement in this order:

1. **Home Page** (most important)
2. **Get Tickets Page** (drives revenue)
3. **Individual Show Pages** (pick your top 3 shows)
4. **Youth Theater** (if you have youth programs launching soon)
5. **Support** (can wait until after launch)
6. **Community Theater** (can wait)

---

## 📞 **Need Help?**

### **Check These First:**
- `DUDA-SETUP-GUIDE.md` - Step-by-step setup
- `INDEX.md` - File navigation
- `DESIGN-TOKENS.md` - Design specifications

### **Common Customization Questions:**

**Q: How do I change the section header glow?**
A: It's built into the CSS. Just use this HTML:
```html
<div style="display: inline-block; border: 4px solid #14b8a6; padding: 1.5rem 3rem; margin-bottom: 3rem; box-shadow: 0 0 20px rgba(20, 184, 166, 0.4);">
  <h2 class="bst-heading-lg" style="margin: 0;">YOUR TITLE</h2>
</div>
```

**Q: How do I add more show cards?**
A: Copy an existing show card, paste it inside the `.bst-grid` div, update the details.

**Q: Can I change the grid from 3 columns to 4?**
A: Yes! Change `bst-grid-3` to `bst-grid-4` in the class name.

---

## ✅ **Launch Checklist**

Before you publish:

- [ ] All page templates embedded
- [ ] Placeholder images replaced
- [ ] Placeholder text updated
- [ ] Ticket links working (test them!)
- [ ] Forms connected (if using)
- [ ] Test on mobile view
- [ ] Test on tablet view
- [ ] Test all buttons and links
- [ ] Check spelling/grammar
- [ ] Preview in different browsers

---

## 🎉 **You're Ready to Launch!**

All templates are designed to work together with consistent styling. Just:

1. Paste the page template
2. Replace placeholders with your content
3. Add your Duda widgets where marked
4. Save and preview

**Good luck with your launch tonight! 🎭✨**

---

**Questions during implementation?** Each file has detailed comments in the code explaining what each section does.

**Last Updated:** March 2026 (Launch Night Edition)
