## 2024-05-18 - Improve contact form accessibility
**Learning:** In a contact form relying entirely on placeholders, screen readers may not reliably announce the purpose of each field. This is a common pattern in minimalist designs that sacrifices accessibility for aesthetics.
**Action:** Always complement placeholder-only designs with `aria-label` attributes (or visually hidden `<label>` elements) to ensure screen readers can announce the field purpose. In addition, add `required` attributes to enforce and announce required fields.

## 2025-02-12 - Interactive custom divs require roles and keyboard handlers
**Learning:** When using generic `<div>` elements as interactive, clickable cards (e.g. expanding cards with `.fc` class), screen readers and keyboard users cannot interact with them. Mouse users can click, but the interaction is hidden from assistive technologies.
**Action:** For any `<div>` functioning as a button, add `role="button"`, `tabindex="0"`, and `aria-expanded="false"`. Crucially, update the JavaScript to toggle `aria-expanded` and add a `keydown` listener to allow activation via `Enter` or `Space` keys.
