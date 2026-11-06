# Law: Comments

Loaded whenever you write code. Use the language's normal comment and docstring style.

1. **Every new file starts with a header comment** naming the feature and the file's purpose.
   e.g. `Feature 003-shift-signup: routes for signing volunteers up for shifts.`
2. **Every function, endpoint, and component gets a one-line description** of what it does. Add a second line only if *why* isn't obvious.
3. **Comment the why, not the what.** "409 instead of 400: the request is valid, the shift is just full" is useful. "return 409" is not.
4. **Business rules point at the spec:** `Spec 003, Done when #2: no signups past capacity.`
5. **TODOs carry the feature ID:** `TODO(003): handle waitlist`. Every TODO also goes in the sidecar's "Known gaps".
6. **No commented-out code.** Delete it. Git has the history.
7. **Keep comments true.** Change the code → fix the comment above it.
