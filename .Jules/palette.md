## 2024-05-18 - Improve contact form accessibility
**Learning:** In a contact form relying entirely on placeholders, screen readers may not reliably announce the purpose of each field. This is a common pattern in minimalist designs that sacrifices accessibility for aesthetics.
**Action:** Always complement placeholder-only designs with `aria-label` attributes (or visually hidden `<label>` elements) to ensure screen readers can announce the field purpose. In addition, add `required` attributes to enforce and announce required fields.

## 2024-05-19 - Interactive div accessibility
**Learning:** Custom interactive `div` elements acting as buttons or interactive floating cards fail on accessibility because they lack inherent keyboard interactivity and context.
**Action:** Always add `role="button"`, `tabindex="0"`, dynamic `aria-expanded` attributes, and `keydown` event listeners for 'Enter' or 'Space' keys to ensure these custom elements are fully accessible and navigable via keyboards. Also make sure to provide visual `:focus-visible` styles.

## 2024-05-20 - Form semantics and native validation
**Learning:** Using generic `div` elements instead of `form` for data entry ignores native browser validation (like the `required` attribute) and breaks natural keyboard interaction (e.g., submitting via Enter key).
**Action:** Always wrap data input sections in a semantic `<form>` element and handle form submission via the `submit` event rather than a `click` event on the submit button. Ensure to reset the form state visually and programmatically using `form.reset()` after a successful submission.

## 2024-05-21 - Essential Focus Visibility for Custom Cursors
**Learning:** Websites utilizing custom cursors that disable the native pointer (`cursor: none`) inadvertently degrade accessibility for keyboard users. The default browser focus outlines are often insufficient or invisible, especially on dark-themed interfaces with low-contrast native styling, rendering keyboard navigation extremely difficult or entirely disorienting since the user cannot visually track their tab position.
**Action:** Always implement robust, high-contrast `:focus-visible` styles across all interactive elements (`a`, `button`, `input`, `textarea`, custom widgets). This guarantees a reliable, predictable visual indicator for keyboard navigation, bridging the gap created by hiding the native cursor.
