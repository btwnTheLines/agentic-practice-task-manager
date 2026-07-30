Repository Rules

- Read the repository before making changes.
- Never invent requirements.
- Prefer maintainability.
- One milestone at a time.
- Explain architectural changes.
- Wait for approval.

When executing commands:

- Commands MUST be valid PowerShell.
- Never use && or ||.
- Never assume Bash.
- Never assume CMD.
- If uncertain, ask instead of guessing.

When proposing tests:

- Prefer tests that validate behaviour over implementation.
- Prefer integration tests over configuration checks when both provide similar confidence.
- Avoid tests that merely verify framework defaults.
- Every test should reduce project risk.