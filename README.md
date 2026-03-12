# Beale Street Theater Component Library & Brand Assets

This repository serves as the central component library and brand asset hub for the Beale Street Theater website. It contains reusable HTML, CSS, and JavaScript components designed to be integrated directly into the Duda Widget Builder or custom page layouts.

## Project Philosophy

This project adheres strictly to **Duda Web Architecture** rules:
- **Vanilla Stack**: Built exclusively with vanilla HTML, CSS, and standard JavaScript. No front-end frameworks (React, Vue, Tailwind, etc.) are used.
- **Isolated CSS**: CSS is strictly encapsulated within unique root classes (e.g., `.custom-widget`) to prevent leaking into Duda's global scope.
- **Duda Syntax**: Components are prepared with Duda's double-curly-bracket syntax (e.g., `{{Variable_Name}}`) for seamless data-binding.
- **Ready to Copy**: All code is separated into clean HTML, CSS, and JS blocks for easy copy-pasting directly into the Duda platform.

## Staff Portal & Brand Hub

The root `index.html` serves as a live Brand Hub and Staff Portal, allowing you to preview all components, download assets, and optimize images for the web.

### Building the Portal

If you modify any components in the `snippets/` or `pages/` directories, you must rebuild the main portal:

```bash
python3 build_portal.py
```

### Local Development

To view the Brand Hub locally:

```bash
python3 -m http.server 3000
```
Then visit `http://localhost:3000`.

## Repository Structure

- `index.html`: The generated Staff Portal & Brand Hub.
- `build_portal.py`: Clean build script for the portal.
- `bst-theme.css`: Core design system styling, variables, and typography.
- `bst-scripts.js`: Global functional scripts.
- `DESIGN-TOKENS.md`: Brand tokens and design guidelines.
- `antigravity-instructions.md`: Detailed AI assistant operating instructions for maintaining and patching this site.
- `component-templates.html`: Template definitions for custom widgets.
- `pages/`: Full page layout structures.
- `snippets/`: Modular component bits including:
  - Buttons (`all-buttons.html`)
  - Icons (`all-icons.html`)
  - Show Cards (`show-cards.html`)
  - Hero Sections (`hero-sections.html`)
  - Section Headings (`all-section-headings.html`)
  - Asset Optimizer (`asset-optimizer.html`)
