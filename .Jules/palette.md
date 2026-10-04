## 2024-05-18 - Improve contact form accessibility
**Learning:** In a contact form relying entirely on placeholders, screen readers may not reliably announce the purpose of each field. This is a common pattern in minimalist designs that sacrifices accessibility for aesthetics.
**Action:** Always complement placeholder-only designs with `aria-label` attributes (or visually hidden `<label>` elements) to ensure screen readers can announce the field purpose. In addition, add `required` attributes to enforce and announce required fields.

## 2024-05-18 - Interactive Custom Elements Accessibility
**Learning:** Custom interactive elements (like floating cards) built with `<div>` often lack built-in keyboard support and semantic meaning, rendering them inaccessible to users who rely on keyboard navigation or screen readers.
**Action:** Always ensure that non-button interactive elements are equipped with `role="button"`, `tabindex="0"`, a visual `:focus-visible` state, and appropriate keyboard event listeners (`keydown` for 'Enter' and 'Space') to mirror pointer interactions. Update `aria-expanded` attributes dynamically for expandable content.
