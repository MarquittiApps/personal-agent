---
description: Interactive workflow to understand user requirements, refine issue definitions, and autonomously create or refine GitHub issues using project-standard templates.
---

# Workflow: `/create-issue`

This workflow helps you transform a thought or a problem into a high-quality GitHub issue, optimized for both humans and AI agents (like Jules).

---

## When to Use

- `/create-issue` — start a new issue definition.
- `/refine-issue` — refine an existing issue (requires issue # or URL).
- When the user mentions: "create a bug report", "new feature idea", "open an issue", "fix this on github".

---

## Pre-conditions

Before starting, if refining an existing issue, ensure you have access to the repository and the issue content using `github-mcp-server`.

---

## Step 1 — Intent Discovery (Role: Product Manager)

**Objective:** Understand if this is a new task or a refinement of something existing.

### Interaction:
Ask the user (in their preferred language):
- "What do you want to document today? Is it a **New Issue** or do you want to **Refine an Existing One**?"
- If Refine: "Please provide the issue number or URL."

---

## Step 2 — Requirement Gathering (Role: Product Owner)

**Objective:** Collect enough details to make the issue "Ready for Development".

### Case A: New Bug Report
Ask these questions one by one:
1. "What is failing? (Short summary)"
2. "What are the steps to reproduce this behavior?"
3. "What did you expect to happen versus what actually happened?"
4. "Any logs, error messages, or screenshots you can provide?"

### Case B: New Feature / Improvement
Ask these questions one by one:
1. "What is the goal of this feature? What problem does it solve?"
2. "Who are the users that benefit from this? (Build a User Story: 'As a [persona], I want [action] so that [benefit]')"
3. "What are the core Acceptance Criteria? (List at least 3)"
4. "Are there any technical constraints or design requirements to consider?"

### Case C: Refine Existing Issue
1. Fetch the issue content using `github_issue_read`.
2. Ask the user: "What specific parts of this issue need refinement? (e.g., more technical detail, clearer acceptance criteria, updated context)"

---

## Step 3 — Draft Generation (Role: Tech Lead)

**Objective:** Synthesize the collected information into the project's standard issue format.

### Rules for Drafting:
- Use the **GitHub Issue Creator** skill template for common issues.
- Use the **Jules Issue Architect** skill rules for technical tasks aimed at AI execution.
- Ensure the title is descriptive and prefixed with `[Jules]` if it's meant for the agent.
- Include a `# Context` and `# Acceptance Criteria` section.

### Output to User:
Present the completed Markdown text to the user.

---

## Step 4 — Review & Approval (Role: Scrum Master)

**Objective:** Finalize the text and decide on the action.

### Interaction:
Ask the user:
1. "How does this look? Does anything need to be changed?"
2. If changes are needed: Update the draft and repeat Step 3.
3. If approved: "**Would you like me to create this issue on GitHub for you now?**"

---

## Step 5 — Action (Role: DevOps)

**Objective:** Create or update the issue in the remote repository.

### Execution:
- If approved for creation, use `github_issue_write` (method: `create`) with the approved title and body.
- If approved for update, use `github_issue_write` (method: `update`) with the issue number.
- Provide the generated Issue URL to the user.

---

## Golden Rules

1. **One question at a time** — Do not overwhelm the user with a long list of questions.
2. **Language Awareness** — Interact in the user's language (e.g., Portuguese) while keeping technical documentation and metadata in English as per project rules.
3. **Optimized for Jules** — Structure issues so an AI agent can pick them up and work autonomously.
4. **No Hallucinations** — If details are missing, ask. Do not invent reproduction steps or technical requirements.
