# Software Quality Plan — KA12

Governed by SWEBOK v4 — KA 12 (Software Quality). This plan defines the metrics and verification procedures to ensure the Personal AI Core meets its QoS requirements.

## 1. Quality Metrics

| ID | Metric | Target | Verification Method |
|----|--------|--------|---------------------|
| M-001 | Latency per Token | ≤ 50ms | Performance profiling on local hardware. |
| M-002 | Hallucination Rate | < 1% | Evaluation against "Golden Set" of 500 prompts. |
| M-003 | Test Coverage | ≥ 80% | Automated coverage reports (pytest-cov). |
| M-004 | Security Score | 0 High Vulnerabilities | Static analysis (Bandit) + Dependency Audit. |

## 2. Quality Gates (Ref: swebok-quality-gates.md)
We enforce a 5-phase quality gate system:
1. **Pre-Flight:** Compliance with `no-vibe-coding`.
2. **Structural:** Linting and type checks (MyPy).
3. **Logic:** Unit and Integration tests.
4. **Behavioral:** Manual/Agentic walkthrough against SRS.
5. **Release:** Governance sign-off by `swebok-compliance-master`.

## 3. Continuous Improvement
Quality results from each sprint are analyzed to refine system prompts and tool interfaces, aiming for a "Diamond" quality standard.
