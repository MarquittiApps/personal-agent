# Product Guidelines (product-guidelines.md)

## 1. Prose Style
- **Tone:** Friendly and Engaging.
- **Goal:** Clear, easy to follow, and welcoming for the user.
- **Language:**
  - **PRD & Workflows:** Português (Brasil).
  - **Skills Andru.ia:** Español.
  - **Code & Low-level Docs:** English.

## 2. Branding & Visual Identity
- **Theme:** Modern & Glassmorphism.
- **Mode:** Automatic Dark/Light mode support.
- **Design System:** Unified using `shadcn/ui` or `Radix UI`.
- **Methodology:** Atomic Design (Atoms, Molecules, Organisms).

## 3. UX Principles
- **Human-in-the-Loop (HITL):** Confirm critical actions or when ambiguity exists (e.g., IoT sensor placement).
- **Performance-First:** Optimize for fast interactions, minimal clicks, and low latency dashboards.
- **Interactivity:** Use `react-konva` or `d3.js` for interactive canvas (zoom, pan, drag-and-drop).
- **Acessibilidade:** Compliance with WCAG 2.1 AA.

## 4. Naming Conventions
- **General:** Adhere to language-specific standards.
  - **TypeScript/React:** camelCase for variables/functions, PascalCase for components/classes.
  - **Python:** snake_case for functions/variables.
- **Commits:** Follow Conventional Commits (`<tipo>[escopo]: <descrição>`).
