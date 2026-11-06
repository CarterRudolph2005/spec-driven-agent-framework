# Law: Tests

Loaded whenever you write code. The test framework, file locations, and setup come from `project-context.md` → **Stack conventions → Testing**. If that doesn't exist yet (first feature with tests), use the stack's standard tools and describe the setup in the plan. The sidecar step records it.

1. **Every "Done when" item in the spec gets at least one test,** named after it: `test_done2_signup_rejected_when_shift_full`.
2. **Every endpoint gets** one happy-path test plus one test per error status it can return.
3. **Tests are isolated.** They use a separate, throwaway database (in-memory or temp file), never the dev database. Each test creates the data it needs and doesn't depend on other tests or seed data.
4. **Assert behavior, not just status codes.** After a create, check the response body or read it back.
5. **Frontend:** if a frontend test framework is already set up, test pure logic (formatters, validators, state helpers). If not, write manual check steps in the sidecar's "How to demo." Don't add a test framework unless the plan says to.
6. **Never delete, skip, or weaken a test to make checks pass.** If a test looks wrong, stop and ask.
7. **External services are faked in tests** (LLMs, payment, email). Tests must pass offline.
