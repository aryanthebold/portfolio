## 2024-05-18 - Improve contact form accessibility
**Learning:** In a contact form relying entirely on placeholders, screen readers may not reliably announce the purpose of each field. This is a common pattern in minimalist designs that sacrifices accessibility for aesthetics.
**Action:** Always complement placeholder-only designs with `aria-label` attributes (or visually hidden `<label>` elements) to ensure screen readers can announce the field purpose. In addition, add `required` attributes to enforce and announce required fields.

## 2026-10-03 - HTML5 Form Validation Requirements
**Learning:** The 'required' attributes, native validation UI, and 'Enter-to-submit' keyboard accessibility fail when inputs are wrapped in generic `<div>` elements instead of semantic `<form>` tags.
**Action:** Always wrap input fields meant for submission in a `<form>` tag and ensure the submission button can trigger it (either `<button type="submit">` inside, or through proper binding).
