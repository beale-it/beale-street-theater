# README-DEV: Phase 1 Component Implementations

## Implemented ARIA Roles & Accessibility Attributes

This document lists the ARIA attributes utilized within the Phase 1 components, specifically demonstrated in the **Adopt A Seat** widget:

**Widget Root (`.bst-adopt-seat-widget`):**
- `role="region"`: Categorizes the component as a major landmark of the page for screen readers.
- `aria-label="Adopt a Seat Support Page"`: Provides clear context of this widget's overarching purpose.

**Content & Focus Elements:**
- `aria-labelledby="hero-title"` applied to `.bst-hero-adopt` ties the semantic `<section>` block explicitly to its `<h1>` element.
- `tabindex="0"` on the `.hero-text-wrapper` ensures keyboard users can easily navigate to and focus on the primary narrative text before tabbing to the CTA.

**Trust Blocks (Impact Stats):**
- `role="list"` and `role="listitem"`: Explicitly declare the semantic grouping of the benefit bullet points since standard `<div>` or `<span>` elements lack semantic list parsing.
- `aria-hidden="true"`: Applied to the custom checkmark icons (`✓`) to instruct screen readers to ignore decorative visuals and narrate purely the substantive text.

**Interactive Elements:**
- `role="button"`: Affirms that despite functioning as an `<a>` anchor, the element serves visually and operationally as a conversion button.
- `aria-label="Donate 1000 dollars to adopt a seat"`: Spells out the transaction value and action for accessibility tools explicitly, upgrading the generic standard "Adopt A Seat" link text.

---

## Implemented JSON-LD Schema Types

The following schema markup was included within the `application/ld+json` script block to support organic crawling and structured data rendering:

**1. Primary Schema: `DonateAction`**
- Categorizes this specific component as an actionable fundraising event, matching Phase 1's goal of high-conversion support pages.
- Populated with `name` and `description` string keys using real values sourced directly from the `/collection-data/` repository.

**2. Nested Schema: `Organization`**
- Located within the `recipient` property.
- Explicitly informs search crawlers that **Beale Street Theater** is the financial beneficiary of the DonateAction.

**3. Nested Schema: `PriceSpecification`**
- Maps the fixed target cost of `$1,000`.
- Documents `1000` `USD` explicitly to support search queries pertaining to philanthropic giving pricing or specific Kingman local theater donation parameters.

---

## Additional Support Pages Implemented

The remaining Phase 1 Support pages were successfully built with similar semantic ARIA roles (`role="region"`, `role="list"`, `role="listitem"`, `role="button"`) and structural JSON-LD configurations.

**1. Pay It Forward** (`pages/pay-it-forward.html`)
- **Primary Schema:** `DonateAction`
- **Focus:** General monetary/ticket-value donation for underserved youth.

**2. Fund Our Equipment** (`pages/av-equipment-fund.html`)
- **Primary Schema:** `DonateAction`
- **Focus:** Capital funding mapped toward professional Audio/Visual equipment.

**3. Sponsor A Production** (`pages/sponsor-a-show.html`)
- **Primary Schema:** `DonateAction`
- **Focus:** Corporate and community operational sponsorships with broad benefits processing. 

**4. Volunteer Opportunities** (`pages/volunteer.html`)
- **Primary Schema:** `Organization`
- **Focus:** Establishes localized functional identity (`bealestreettheater.com`). Opts out of `DonateAction` specifically because time/commitment donation requires distinct non-monetary semantic strategies in JSON-LD.
