# BST Project Context: Phase 1 Scaffolding

## The Goal
Build high-performance, SEO-optimized HTML/CSS components for the Beale Street Theater website (Duda Editor 2.0).

## Repository Setup
- **Root:** Headless component library.
- **Data Source:** `/collection-data/` contains CSV/JSON exports from Duda Collections.
- **Output:** Clean code snippets ready for copy-pasting into Duda HTML Widgets.

## Final Sitemap (Source: Digital Allies Editor)
1. **Home:** Main landing page with revised "Left-Image" Hero.
2. **Get Tickets:** Conversion-focused season calendar.
3. **Youth Theater:** Sub-pages: Youth Productions, Youth Auditions.
4. **Community Theater:** Sub-pages: Auditions, Classes, Workshops.
5. **Support (High-Conversion Fundraisers):**
    - Volunteer
    - Fund Our Equipment
    - Sponsor A Show
    - Pay It Forward
    - Adopt A Seat
6. **About:** History, Mission, and Staff.
7. **Get In Touch:** - Plan Your Visit (Parking/Accessibility)
    - Blog


## SEO & Accessibility Strategy
- **Layering:** Meta tags are native in Duda. Schema (JSON-LD) and ARIA attributes must be in the custom widgets.
- **Semantic HTML:** Use <section>, <article>, and <nav> so crawlers see code as native content.

## Maintenance Note
The `index.html` at the root of this repo is a Staff Portal for internal previewing. It is NOT the live site.