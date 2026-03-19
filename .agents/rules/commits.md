# Rule: Atomic Commits and Conventional Commits

## Objective

Ensure that all the version history (Git) of the project follows the structured standard of [Conventional Commits (v1.0.0)](https://www.conventionalcommits.org/en/v1.0.0/) and that each commit is strictly **atomic**. Each commit must represent only one logical unit of change, avoiding the mixture of refactorings, new features, and isolated fixes in a single commit.

## Triggers (When to Activate)

- Constantly when staging files (`git add`) or creating a commit (`git commit`).
- When structuring a commit message at the user's request.
- When evaluating, analyzing, or rewriting the commit history of a branch or Pull Request.
- When acting as a code review agent suggesting integrations.

## Essential Rules

1. **Mandatory Structure:** All commits must follow the syntax `<type>[optional scope]: <description>`
   - *Most common types:* `feat`, `fix`, `docs`, `style`, `refactor`, `perf`, `test`, `build`, `ci`, `chore`, `revert`.
2. **Perfect Atomicity:** A commit must do only ONE thing. If you created a feature in module A and fixed a typo in module B, 2 separate commits must be made.
3. **Description Formatting:** Use the verb in the imperative and present tense (e.g., "add" instead of "added" or "adds"; "fix" instead of "fixed"). Do not use a period at the end of the short description.
4. **Optional Break (Body/Footer):** If the change needs additional context, insert a line break after the description and add a body explaining the "why" or the detailed "how".

## Examples

### ❌ Incorrect (Don'ts)

- **Not Atomic (doing many things together):** `feat: adds payment module and also fixes the navbar bug`
- **Non-Standard (without prefix):** `updating user tests`
- **Inadequate Grammar (verb in the past):** `fix: fixed null pointer exception on login`

### ✅ Correct (Do's)

- **Atomic (Feature Only):** `feat(payment): add Stripe integration checkout`
- **Atomic (Separate Fix Only):** `fix(ui): resolve navbar overlapping on mobile view`
- **Documentation Only:** `docs: update setup instructions in README`
- **Refactoring without logical scope change:** `refactor(auth): extract jwt validation to separate middleware`
