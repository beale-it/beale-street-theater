# Beale Street Theater Component Library & Brand Assets

This repository serves as the central component library and brand asset hub for the Beale Street Theater website. It contains reusable HTML, CSS, and JavaScript components designed to be integrated directly into the Duda Widget Builder or custom page layouts.

## Project Philosophy

This project adheres strictly to **Duda Web Architecture** rules:
- **Vanilla Stack**: Built exclusively with vanilla HTML, CSS, and standard JavaScript. No front-end frameworks (React, Vue, Tailwind, etc.) are used.
- **Isolated CSS**: CSS is strictly encapsulated within unique root classes (e.g., `.custom-widget`) to prevent leaking into Duda's global scope.
- **Duda Syntax**: Components are prepared with Duda's double-curly-bracket syntax (e.g., `{{Variable_Name}}`) for seamless data-binding.
- **Ready to Copy**: All code is separated into clean HTML, CSS, and JS blocks for easy copy-pasting directly into the Duda platform.

## Repository Structure

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

## Getting Started

1. Navigate to the `snippets/` or `pages/` directory to find the component you need.
2. Open the file to view the separated HTML, CSS, and JS blocks.
3. Copy the corresponding blocks and paste them directly into their respective tabs in the Duda Widget Builder, or into a Duda Custom HTML element as instructed within each file.
