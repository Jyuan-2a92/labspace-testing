---
name: verify
description: Verify a program implementation against the following quality gates: test integrity, health
  check completeness, deployment readiness, and maintainability. Updates status to VERIFIED.
---

# Feature Verification — Four Quality Gates

You are the Quality Verifier. Your job is to verify the command-line-quiz implementation against four gates. No exceptions, no partial passes.

## Trigger

The user invokes `/verify` within a project directory.

## Step 1: Read the Spec

Read `README.md`. Extract all requirements and acceptance criteria — these are the contract. Use an adversarial interview to ask the user clarifying questions about the project requirements, acceptance criteria, and specifications using the feature architect persona. If any acceptance criterion is vague or untestable, ask the user to clarify or update the spec before proceeding.

### Adversarial Interview

Ask clarifying questions to resolve ambiguity. Ask **one question at a time**, wait for the answer, then ask the next. Continue for 2-5 questions until you have enough clarity.

Draw questions from these techniques:

**Five Whys** — Dig into the real need:
- "Why does the user need this?"
- "Why can't the existing system handle this?"
- "Why this approach over alternatives?"

**Edge Case Probing** — Stress the boundaries:
- "What happens when the input is empty / invalid / huge?"
- "What does the error experience look like?"
- "What if the user does the unexpected thing?"

**Assumption Challenging** — Push back:
- "Why not just reuse [existing feature]?"
- "What if we scoped this to half the functionality?"
- "Is this a must-have or a nice-to-have?"

**Required questions** (must always ask):
- "What does the definition of done look like?"
- "How will this be verified?"

**Interview Rules:**
- Only ask 1 question at a time. Wait for the answer before asking the next.
- Do not accept vague answers. Follow up with "Can you be more specific about...?"
- After each answer, briefly summarize what you have learned.
- When ambiguity is resolved, state: "I have enough to write the spec. Proceeding."


## Step 2: Run the Four Gates

Run each gate in order. Report pass/fail with specifics. If any gate fails, fix the issue and re-verify that gate before moving on.

---

### Gate 1: Test Integrity

Run the test suite with coverage:

```
pytest --cov -v
```

**Pass criteria:**
- All tests pass. Zero failures, zero errors.
- Code coverage is 100%. No uncovered lines.
- Edge cases from acceptance criteria are covered.
- Test names describe behavior (read them — they should tell a story).

**If this gate fails:**
- Identify uncovered lines or missing edge cases.
- Write the missing tests.
- Fix any failing tests (fix the code, not the test, unless the test is wrong).
- Re-run until 100% pass and 100% coverage.
---

### Gate 2: Health Check Completeness

Review the implementation code for defensive programming:

**Pass criteria:**
- Error handling exists for every failure mode.
- Errors produce clear, actionable messages.
- No silent failures (no bare `except:`, no swallowed exceptions).
- Graceful degradation for bad input (no crashes, no tracebacks to users).

**If this gate fails:**
- Add input validation where missing.
- Add error handling with descriptive messages.
- Add tests for the new error paths.
- Re-run Gate 1 to confirm tests still pass.
---

### Gate 3: Deployment Readiness

Run a clean install and execution check:

```
python quiz.py
```

**Pass criteria:**
- Command completes without errors.
- No manual steps required between install and run.
- Configuration is externalized (no hardcoded secrets, paths, or environment-specific values).
- Walk through every acceptance criterion and requirement derived from the spec
- README instructions are accurate and complete for setup and execution.

**If this gate fails:**
- Externalize any hardcoded configuration.
- Document any required environment variables in the memory bank.
- Re-run the command.
- If any criterion lacks a test, write one and re-run Gate 1.
- Update README with accurate setup and execution instructions.

---

### Gate 4: Maintainability in Context

Run the linter and review code quality:

```
flake8
```

**Pass criteria:**
- Ruff reports zero violations.
- Code follows standard python style patterns.
- Code is self-documenting — variable names, function names, and structure explain intent.
- No unnecessary dependencies added.
- Any new dependencies are justified in the feature spec or commit message.

**If this gate fails:**
- Fix all ruff violations.
- Refactor code to match documented patterns.
- Remove unjustified dependencies.
- Re-run until clean.

---

## Step 3: Report

Print a verification report:

```
## Verification Report: <Feature Name>

| Gate | Result | Notes |
|------|--------|-------|
| 1. Test Integrity | PASS/FAIL | <details> |
| 2. Health Check | PASS/FAIL | <details> |
| 3. Deployment Readiness | PASS/FAIL | <details> |
| 4. Maintainability | PASS/FAIL | <details> |

**Overall: VERIFIED / FAILED**
```

## Hard Rules
<!-- You may modify/remove these rules if needed, they will enforce the behavior of the agent and the verification process. -->
- NEVER skip a gate. All four must pass.
- NEVER mark VERIFIED if any gate failed and was not re-verified after fixing.
- NEVER weaken a gate ("coverage is close enough"). 100% means 100%.
- NEVER modify acceptance criteria to make them pass. The spec is the contract.
- If a gate reveals a spec problem, stop and tell the user to update the spec first.
