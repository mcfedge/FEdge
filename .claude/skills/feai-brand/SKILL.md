---
name: feai-brand
description: Apply Forward Edge-AI corporate brand styling to presentations, documents, and spreadsheets. Use when the user invokes "feai-brand" or requests Forward Edge-AI/FEAI branded materials. Automatically applies corporate colors (#8275b1, #574b7c, #999999, #676767), Roboto font, proper font sizing, gradient specifications, and company logos to any created files.
---

# Forward Edge-AI Brand Application

This skill applies Forward Edge-AI's corporate brand identity to presentations, documents, and spreadsheets.

## Overview

When triggered, apply the Forward Edge-AI brand guidelines to ensure consistent, professional output across all document types. The brand guidelines are detailed in `references/brand_guidelines.md` and should be referenced for specific color codes, font specifications, and gradient patterns.

## Core Brand Elements

### Colors
- Purple Primary Light: `#8275b1`
- Purple Primary Dark: `#574b7c`
- Gray Light: `#999999`
- Gray Dark: `#676767`

### Typography
- **Font**: Roboto (all text)
- **Sizes**: H1: 28pt | H2: 18pt | Date: 14pt | Body: 16pt | Footer: 12pt

### Logos
Three logo files are available in `assets/`:
- `fe_logo_dark.png` - Use on light backgrounds
- `fe_logo_white.png` - Use on dark/colored backgrounds
- `isidore_logo_dark.png` - Product/division branding

## Application by Document Type

### PowerPoint Presentations (.pptx)

**Title Slide:**
- Background: Purple gradient (#574b7c to #8275b1, 0° angle, linear)
- Logo: `fe_logo_white.png` (top left or center)
- Title text: White, Roboto 28pt
- Subtitle/date: White, Roboto 14pt

**Content Slides:**
- Background: White or light gray
- Headers: Purple Primary colors (#8275b1 or #574b7c), Roboto 18pt
- Body text: Gray Dark (#676767), Roboto 16pt
- Bullets/accents: Purple Primary colors
- Footer: Gray Light (#999999), Roboto 12pt

**Reference**: See `references/brand_guidelines.md` for gradient specifications and logo usage

### Word Documents (.docx)

**Header:**
- Insert `fe_logo_dark.png` (top left or right)
- Title: Purple Primary Light (#8275b1), Roboto 28pt
- Subtitle: Purple Primary Dark (#574b7c), Roboto 18pt

**Body:**
- Font: Roboto 16pt
- Color: Gray Dark (#676767)
- Section headers: Purple Primary colors, Roboto 18pt

**Footer:**
- Text: Gray Light (#999999), Roboto 12pt
- Optional: Company name or page numbers

### Excel Spreadsheets (.xlsx)

**Header Row:**
- Background: Purple Primary Dark (#574b7c)
- Text: White, Roboto, Bold
- Font size: 16pt

**Data Cells:**
- Font: Roboto 16pt
- Text color: Gray Dark (#676767)
- Alternating row backgrounds: White and light gray (#999999 at 20% opacity)

**Charts:**
- Use purple primary colors as main chart colors
- Gridlines: Gray Light (#999999)
- Titles: Purple Primary Dark (#574b7c)

## Workflow

1. **Read brand guidelines**: Load `references/brand_guidelines.md` for complete specifications
2. **Select appropriate logos**: Choose from `assets/` based on background color
3. **Apply color palette**: Use exact hex values specified
4. **Set typography**: Apply Roboto font with correct sizes for each element type
5. **Implement gradients** (presentations): Follow 0° linear gradient specifications
6. **Verify consistency**: Ensure all elements follow brand guidelines

## Important Notes

- **Exact colors**: Always use the specified hex codes exactly as provided
- **Gradients**: Only linear gradients at 0° angle, never radial
- **Logo clearspace**: Maintain adequate spacing around logos
- **Font consistency**: Use Roboto exclusively for all text
- **Reference file**: Consult `references/brand_guidelines.md` for detailed specifications and examples

## Triggering

This skill activates when:
- User types "feai-brand" in their request
- User explicitly requests Forward Edge-AI or FEAI branded materials
- User mentions applying company branding to presentations, documents, or spreadsheets
