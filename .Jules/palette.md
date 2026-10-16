## 2024-05-18 - Improve contact form accessibility
**Learning:** In a contact form relying entirely on placeholders, screen readers may not reliably announce the purpose of each field. This is a common pattern in minimalist designs that sacrifices accessibility for aesthetics.
**Action:** Always complement placeholder-only designs with `aria-label` attributes (or visually hidden `<label>` elements) to ensure screen readers can announce the field purpose. In addition, add `required` attributes to enforce and announce required fields.

## 2024-05-19 - Interactive div accessibility
**Learning:** Custom interactive `div` elements acting as buttons or interactive floating cards fail on accessibility because they lack inherent keyboard interactivity and context.
**Action:** Always add `role="button"`, `tabindex="0"`, dynamic `aria-expanded` attributes, and `keydown` event listeners for 'Enter' or 'Space' keys to ensure these custom elements are fully accessible and navigable via keyboards. Also make sure to provide visual `:focus-visible` styles.

## 2024-05-20 - Form semantics and native validation
**Learning:** Using generic `div` elements instead of `form` for data entry ignores native browser validation (like the `required` attribute) and breaks natural keyboard interaction (e.g., submitting via Enter key).
**Action:** Always wrap data input sections in a semantic `<form>` element and handle form submission via the `submit` event rather than a `click` event on the submit button. Ensure to reset the form state visually and programmatically using `form.reset()` after a successful submission.

## 2024-05-21 - Focus visibility and form submission feedback
**Learning:** Custom CSS resets or generic styles can inadvertently suppress native focus indicators for interactive elements like buttons, links, and inputs. Furthermore, users often lack confidence when a form lacks immediate visual feedback upon submission, leading to potential duplicate submissions and confusion.
**Action:** Always verify that interactive elements retain clear `:focus-visible` styles, especially when custom styles are heavily applied. Provide immediate visual feedback (such as a 'Sending...' state and disabling the submit button) upon form submission to improve user experience and prevent multiple submissions.
