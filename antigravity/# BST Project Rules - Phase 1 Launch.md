# BST Project Rules - Phase 1 Launch (Duda 2.0)

## 1. Typography & Readability (CRITICAL)
- **Base Body Size:** 1.15rem (approx 18.4px). This is mandatory for readability on Stage Black.
- **Line Height:** 1.7 for body text; 1.1 for headings.
- **Headings:** Use `.bst-heading-xl`. Font: 'League Spartan', Uppercase, Letter-spacing: 0.08em.

## 2. Layout & Flexbox Logic
- **Hero Alignment:** Always use `flex-direction: row-reverse` on `.bst-hero-content`.
- **Visual Order:** Image must sit on the LEFT, Text must sit on the RIGHT.
- **Desktop Spacing:** Use `gap: 3rem` (48px) between columns.
- **Mobile Behavior:** At 768px, force `flex-direction: column` and `text-align: center`.

## 3. High-Converting Landing Pages (Support Section)
- **Focus:** Treat "Volunteer", "Fund Our Equipment", "Sponsor A Show", "Pay It Forward", and "Adopt A Seat" as P1 sales pages.
- **Elements:** Use `bst-btn-lg` for primary actions. Include "Impact Stats" and "Trust Blocks" in the HTML scaffolding.

## 4. Technical Standards & Data
- **Schema:** Every HTML file MUST start with a `<script type="application/ld+json">` block.
- **Source of Truth:** Never hallucinate data. Pull all show names, dates, and prices from `/collection-data/`.
- **BST Curve:** Strictly apply `border-radius: 0px 10px 10px 0px;` to all buttons and cards.
- **Duda Compatibility:** No <html> or <body> tags. Output only the content intended for the HTML Widget.

## 5. Data Handling & Sources of Truth
- **Zero-Hallucination Policy:** Never use placeholder show titles or dates. Always pull from the files located in `/collection-data/`.
- **Mapping:** - Use `{{field_name}}` syntax when preparing code specifically for the Duda Dynamic Template editor.
    - Use the actual values from `/collection-data/` when generating static landing pages or demo components for approval.
- **Syncing:** If a value in the HTML does not match the corresponding entry in the collection data, the collection data file is the final authority.

## Data Sources & Sources of Truth
- **Location:** `/collection-data/`
- **Format:** CSV or JSON exports from Duda Collections.
- **Usage:** Antigravity must reference these files to populate:
    1. HTML Content (Titles, Descriptions, Images).
    2. Schema.org JSON-LD blocks (Dates, Prices, Locations).
    3. Custom attribute tags for filtering logic.

   
   
# BST Project Rules - Phase 1 Launch (Duda 2.0)

## 1. Typography & Readability (CRITICAL)
- **Base Body Size:** 1.15rem (approx 18.4px). Mandatory for readability on Stage Black.
- **Line Height:** 1.7 for body text; 1.1 for headings.
- **Headings:** Use `.bst-heading-xl`. Font: 'League Spartan', Uppercase, Letter-spacing: 0.08em.

## 2. Layout & Flexbox Logic
- **Hero Alignment:** Always use `flex-direction: row-reverse` on `.bst-hero-content`.
- **Visual Order:** Image must sit on the LEFT, Text must sit on the RIGHT.
- **Desktop Spacing:** Use `gap: 3rem` (48px) between columns.
- **Mobile Behavior:** At 768px, force `flex-direction: column` and `text-align: center`.

## 3. High-Converting Landing Pages (Support Section)
- **Priority:** Treat "Volunteer", "Fund Our Equipment", "Sponsor A Show", "Pay It Forward", and "Adopt A Seat" as P1 sales pages.
- **Design:** Use clear, singular CTAs (`bst-btn-lg`). Include "Impact Stats" or "Testimonial" blocks in the HTML.
- **BST Curve:** Strictly apply `border-radius: 0px 10px 10px 0px;` to all buttons and cards.

## 4. Technical Standards & SEO
- **Schema:** Every HTML file MUST start with a `<script type="application/ld+json">` block (Event, DonateAction, or Organization).
- **Duda Compatibility:** Prohibit <html> or <body> tags. Output only the content for the Duda HTML Widget.
- **Connected Data:** Use `{{field_name}}` syntax for dynamic collection binding.
- **CSS Variables:** Use `--bst-neon-teal` and `--bst-stage-black`. No hardcoded hex codes.

## 5. Data Handling (Source of Truth)
- **Zero-Hallucination:** Pull all show names, dates, and prices from `/collection-data/`.
- **Syncing:** The collection files are the final authority for all content values.