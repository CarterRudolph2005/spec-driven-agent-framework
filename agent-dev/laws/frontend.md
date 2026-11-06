# Law: Frontend

Load if the plan touches client code (web or mobile). Framework-specific patterns come from `project-context.md` → **Stack conventions → Frontend**.

1. **All network calls go through one API module** with a named function per call (`signUp(shiftId, volunteerId)`). Screens and components never build URLs or call the HTTP client directly.
2. **Every data fetch handles three states:** loading, error, and empty.
3. **Screens/pages are separate from reusable components.** One component per file, named like the file.
4. **Forms:** every input has a visible label, submit is disabled while saving, and the API's error message is shown to the user.
5. **Follow the framework's state rules.** Don't mutate state the framework expects to be replaced. Derive values instead of storing duplicates.
6. **List items use stable IDs as keys,** never their position.
7. **Accessibility:** labeled inputs, real buttons for actions, alt text on images, errors announced (e.g. `role="alert"` on web), readable contrast.
8. **No hardcoded API URLs or secrets.** The base URL comes from config/env. Secret keys never ship to the client.
9. **Match the existing styling approach.** Don't introduce a second one.
10. **No new packages** unless the plan lists them.
