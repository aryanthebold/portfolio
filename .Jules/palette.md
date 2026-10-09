## 2024-05-18 - Improve contact form accessibility
**Learning:** In a contact form relying entirely on placeholders, screen readers may not reliably announce the purpose of each field. This is a common pattern in minimalist designs that sacrifices accessibility for aesthetics.
**Action:** Always complement placeholder-only designs with `aria-label` attributes (or visually hidden `<label>` elements) to ensure screen readers can announce the field purpose. In addition, add `required` attributes to enforce and announce required fields.

## 2024-05-19 - Interactive div accessibility
**Learning:** Custom interactive `div` elements acting as buttons or interactive floating cards fail on accessibility because they lack inherent keyboard interactivity and context.
**Action:** Always add `role="button"`, `tabindex="0"`, dynamic `aria-expanded` attributes, and `keydown` event listeners for 'Enter' or 'Space' keys to ensure these custom elements are fully accessible and navigable via keyboards. Also make sure to provide visual `:focus-visible` styles.

## 2024-05-20 - Form semantics and native validation
**Learning:** Using generic `div` elements instead of `form` for data entry ignores native browser validation (like the `required` attribute) and breaks natural keyboard interaction (e.g., submitting via Enter key).
**Action:** Always wrap data input sections in a semantic `<form>` element and handle form submission via the `submit` event rather than a `click` event on the submit button. Ensure to reset the form state visually and programmatically using `form.reset()` after a successful submission.

## 2024-05-21 - Visible focus for all interactive elements
**Learning:** Only adding `:focus-visible` styles to custom interactive elements (like custom floating cards) creates an inconsistent experience for keyboard users, where standard interactive elements (like links, buttons, and inputs) have no visible focus indicator because a CSS reset or styling approach has hidden the default outline.
**Action:** Always verify that a global focus state exists. Add a generic `:focus-visible` CSS rule for `a`, `button`, `input`, and `textarea` to ensure every interactive element provides clear visual feedback when navigated via keyboard.
