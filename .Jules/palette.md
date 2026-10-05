## 2024-05-18 - Improve contact form accessibility
**Learning:** In a contact form relying entirely on placeholders, screen readers may not reliably announce the purpose of each field. This is a common pattern in minimalist designs that sacrifices accessibility for aesthetics.
**Action:** Always complement placeholder-only designs with `aria-label` attributes (or visually hidden `<label>` elements) to ensure screen readers can announce the field purpose. In addition, add `required` attributes to enforce and announce required fields.

## 2024-05-18 - HTML5 Form Validation and Keyboard Submission
**Learning:** Using `required` attributes on input elements only triggers native HTML5 validation if those inputs are wrapped within a semantic `<form>` element. Furthermore, a proper `<form>` wrapper automatically enables form submission via the `Enter` key, bridging both accessibility and native UX expectations that are often lost when developers use generic `<div>` wrappers and custom JavaScript click handlers.
**Action:** Always wrap form inputs and buttons in a semantic `<form>` tag and use `type="submit"` for the primary button to leverage native browser validation and keyboard submission flows.
