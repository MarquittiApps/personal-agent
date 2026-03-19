To efficiently integrate **Google Jules** into your workflow, I propose the creation of a new Specialized Agent called **`jules-issue-architect`**. This agent will be responsible for translating functionality specifications (such as those found in your Conductor tracks) into GitHub Issues optimized for Jules' asynchronous processing.

### Structure of the New Agent (Skill)

The goal of this agent is to ensure that the Issue contains sufficient context, precise technical instructions, and clear acceptance criteria, which are the pillars for Jules to generate a correct implementation plan.

Below is the definition of the new Skill that you can add in `.agents/skills/jules-issue-architect/SKILL.md`:

```markdown
---
name: jules-issue-architect
description: "Specialist in converting technical specifications into GitHub Issues optimized for the Google Jules Agent."
---

# Mission
Your mission is to act as the bridge between strategic planning (Tracks/Specs) and technical execution by Google Jules. You must write Issues that allow Jules to work autonomously, minimizing back-and-forth.

# Issue Writing Rules for Jules

1. **Descriptive Title**: The title should be direct, e.g., `[Jules] Implement Gemini API Integration`.
2. **# Context Section**: Explain the "why" of the task and how it fits into the Personal AI Core.
3. **# Technical Instructions Section**:
    - List the specific files that must be created or changed (e.g., `app/core/llm_factory.py`).
    - Describe the necessary business or technical logic.
    - Explicitly reference the project's code guidelines (TDD, Atomic Commits).
4. **# Acceptance Criteria (DoD) Section**:
    - Define specific tests that Jules must run and pass.
    - Describe the expected behavior after implementation.
5. **Tips for Jules**: Add observations about environment variables (from `.env.example`) or necessary dependencies.

# Execution Workflow
1. Analyze the `spec.md` file of the desired functionality.
2. Identify the impact points in the repository.
3. Generate the Issue markdown following the official template.
```

### Issue Template Optimized for Jules

The agent should use this format to ensure that Jules understands the task right at the "Planning" stage:

```markdown
## 🎯 Objective
[Brief feature description based on the Spec]

## 🛠️ Technical Instructions
- **Related Files:** `list/of/files.py`
- **Task:** [Technical step-by-step]
- **Standards:** Follow `conductor/code_styleguides/general.md` and ensure `Conventional Commits`.

## ✅ Acceptance Criteria
- [ ] Test X covering case Y.
- [ ] Implementation does not break existing Z functionality.
- [ ] Success log visible in console/sentry.

/label jules
```

### How to use in your current repository

1.  **Feed the Agent**: Provide `jules-issue-architect` with the content of a specification file, such as `conductor/tracks/rag-engine_20260319/spec.md`.
2.  **Generate the Issue**: The agent will produce the Issue body in Markdown.
3.  **Tag Jules**: When creating the Issue on GitHub, make sure to add the `jules` label or mention `@jules` (depending on your Jules Action configuration) to trigger execution.
4.  **AGENTS.md**: I recommend creating an `AGENTS.md` file in the root of your project. Jules uses this file to understand the global context (stack, linting preferences, test commands) persistently, without having to repeat this information in every Issue.

With this agent, you transform your "Conductor" into an automated dispatch system, where planning generates the Issue and Jules delivers the Pull Request ready for review.
