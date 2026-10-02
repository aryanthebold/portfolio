## 2024-05-18 - Improve contact form accessibility
**Learning:** In a contact form relying entirely on placeholders, screen readers may not reliably announce the purpose of each field. This is a common pattern in minimalist designs that sacrifices accessibility for aesthetics.
**Action:** Always complement placeholder-only designs with `aria-label` attributes (or visually hidden `<label>` elements) to ensure screen readers can announce the field purpose. In addition, add `required` attributes to enforce and announce required fields.

## 2024-05-19 - Form Validation
**Learning:** HTML5 validation attributes (like `required`) do not enforce validation if the input elements are not wrapped in a `<form>` tag and triggered by a submit event.
**Action:** Always wrap form inputs in a `<form>` element and handle the `submit` event instead of listening to `click` events on the submit button, ensuring native browser validation is applied correctly and accessible error messages are presented to the user.
