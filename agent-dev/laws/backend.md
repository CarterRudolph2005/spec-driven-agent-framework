# Law: Backend

Load if the plan touches server code. Framework-specific patterns come from `project-context.md` → **Stack conventions → Backend**.

1. **Three layers, kept separate:**
   - **Handlers / routes:** HTTP only. Read params, validate input, call logic, pick the status code.
   - **Logic / services:** business rules. Knows nothing about HTTP.
   - **Data access / repository:** every database call. No queries in handlers.
   Small rules may live in the handler; move them to a service once they pass ~15 lines.
2. **One module per resource** (shifts, volunteers...), registered in the app's entry point.
3. **Validate at the edge.** Every request body and query param goes through a schema or validator before the logic sees it. Separate input shapes (create, update) from the stored record.
4. **Explicit responses.** Declare the response shape. Return 201 on create and 204 on delete.
5. **Status codes:**
   | Case | Code |
   |---|---|
   | Not found | 404 |
   | Valid request that conflicts with current state (full, duplicate) | 409 |
   | Malformed or invalid input | 400 / 422 (per the framework's default) |
   | Not logged in / not allowed | 401 / 403 |
   | Unexpected failure | 500, with no stack trace or secrets in the body |
   Error messages should make sense to the person using the app.
6. **Load-or-404 is written once** (a helper, dependency, or middleware) and reused, not copied into every route.
7. **Config comes from the environment** with sensible defaults. Never hardcode keys, URLs, or ports. List new variables in the plan (the sidecar step adds them to `project-context.md`).
8. **External calls (LLMs, third-party APIs) live in their own module,** with a timeout and a readable error if they fail.
9. **Don't change app wiring** (CORS, middleware, startup, auth) unless the plan says so.
