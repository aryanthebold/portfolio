## 2024-05-18 - Improve contact form accessibility
**Learning:** In a contact form relying entirely on placeholders, screen readers may not reliably announce the purpose of each field. This is a common pattern in minimalist designs that sacrifices accessibility for aesthetics.
**Action:** Always complement placeholder-only designs with `aria-label` attributes (or visually hidden `<label>` elements) to ensure screen readers can announce the field purpose. In addition, add `required` attributes to enforce and announce required fields.

## 2024-05-18 - HTML5 Form Validation and Keyboard Submission
**Learning:** Using `required` attributes on input elements only triggers native HTML5 validation if those inputs are wrapped within a semantic `<form>` element. Furthermore, a proper `<form>` wrapper automatically enables form submission via the `Enter` key, bridging both accessibility and native UX expectations that are often lost when developers use generic `<div>` wrappers and custom JavaScript click handlers.
**Action:** Always wrap form inputs and buttons in a semantic `<form>` tag and use `type="submit"` for the primary button to leverage native browser validation and keyboard submission flows.

## 2024-05-19 - Interactive div accessibility
**Learning:** Custom interactive `div` elements acting as buttons or interactive floating cards fail on accessibility because they lack inherent keyboard interactivity and context.
**Action:** Always add `role="button"`, `tabindex="0"`, dynamic `aria-expanded` attributes, and `keydown` event listeners for 'Enter' or 'Space' keys to ensure these custom elements are fully accessible and navigable via keyboards. Also make sure to provide visual `:focus-visible` styles.
