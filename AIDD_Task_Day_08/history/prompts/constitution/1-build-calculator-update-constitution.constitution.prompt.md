---
id: 1
title: Build Calculator Update Constitution
stage: constitution
date: 2024-12-19
surface: agent
model: Auto
feature: none
branch: main
user: Kavita-LachmanDas
command: /sp.constitution
labels: ["calculator", "streamlit", "constitution", "python", "ui"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
  - calculator.py
  - requirements.txt
  - README.md
  - .specify/memory/constitution.md
tests:
  - No tests run (initial implementation)
---

## Prompt

/sp.constitution Build a **Calculator** using **Python** and **Streamlit**.
- Operations allowed: add, subtract, multiply, divide, and more.
- Keep an **animated and interactive UI**.
- Use **simple functions** to handle calculations.
- Allow **single input prompt** style OR buttons for operations.
- Validate input to prevent errors like division by zero.
- Show **results dynamically** in the interface.
- Keep the UI clean, responsive, and user-friendly.
- Optional: Add colors, emojis, or animations for better engagement.

--- Cursor Command: sp.constitution.md ---

## User Input

```text
Build a **Calculator** using **Python** and **Streamlit**.
```

You **MUST** consider the user input before proceeding (if not empty).

## Outline

You are updating the project constitution at `.specify/memory/constitution.md`. This file is a TEMPLATE containing placeholder tokens in square brackets (e.g. `[PROJECT_NAME]`, `[PRINCIPLE_1_NAME]`). Your job is to (a) collect/derive concrete values, (b) fill the template precisely, and (c) propagate any amendments across dependent artifacts.

Follow this execution flow:

1. Load the existing constitution template at `.specify/memory/constitution.md`.
   - Identify every placeholder token of the form `[ALL_CAPS_IDENTIFIER]`.
   **IMPORTANT**: The user might require less or more principles than the ones used in the template. If a number is specified, respect that - follow the general template. You will update the doc accordingly.

2. Collect/derive values for placeholders:
   - If user input (conversation) supplies a value, use it.
   - Otherwise infer from existing repo context (README, docs, prior constitution versions if embedded).
   - For governance dates: `RATIFICATION_DATE` is the original adoption date (if unknown ask or mark TODO), `LAST_AMENDED_DATE` is today if changes are made, otherwise keep previous.
   - `CONSTITUTION_VERSION` must increment according to semantic versioning rules:
     - MAJOR: Backward incompatible governance/principle removals or redefinitions.
     - MINOR: New principle/section added or materially expanded guidance.
     - PATCH: Clarifications, wording, typo fixes, non-semantic refinements.
   - If version bump type ambiguous, propose reasoning before finalizing.

3. Draft the updated constitution content:
   - Replace every placeholder with concrete text (no bracketed tokens left except intentionally retained template slots that the project has chosen not to define yet—explicitly justify any left).
   - Preserve heading hierarchy and comments can be removed once replaced unless they still add clarifying guidance.
   - Ensure each Principle section: succinct name line, paragraph (or bullet list) capturing non‑negotiable rules, explicit rationale if not obvious.
   - Ensure Governance section lists amendment procedure, versioning policy, and compliance review expectations.

4. Consistency propagation checklist (convert prior checklist into active validations):
   - Read `.specify/templates/plan-template.md` and ensure any "Constitution Check" or rules align with updated principles.
   - Read `.specify/templates/spec-template.md` for scope/requirements alignment—update if constitution adds/removes mandatory sections or constraints.
   - Read `.specify/templates/tasks-template.md` and ensure task categorization reflects new or removed principle-driven task types (e.g., observability, versioning, testing discipline).
   - Read each command file in `.specify/templates/commands/*.md` (including this one) to verify no outdated references (agent-specific names like CLAUDE only) remain when generic guidance is required.
   - Read any runtime guidance docs (e.g., `README.md`, `docs/quickstart.md`, or agent-specific guidance files if present). Update references to principles changed.

5. Produce a Sync Impact Report (prepend as an HTML comment at top of the constitution file after update):
   - Version change: old → new
   - List of modified principles (old title → new title if renamed)
   - Added sections
   - Removed sections
   - Templates requiring updates (✅ updated / ⚠ pending) with file paths
   - Follow-up TODOs if any placeholders intentionally deferred.

6. Validation before final output:
   - No remaining unexplained bracket tokens.
   - Version line matches report.
   - Dates ISO format YYYY-MM-DD.
   - Principles are declarative, testable, and free of vague language ("should" → replace with MUST/SHOULD rationale where appropriate).

7. Write the completed constitution back to `.specify/memory/constitution.md` (overwrite).

8. Output a final summary to the user with:
   - New version and bump rationale.
   - Any files flagged for manual follow-up.
   - Suggested commit message (e.g., `docs: amend constitution to vX.Y.Z (principle additions + governance update)`).

Formatting & Style Requirements:

- Use Markdown headings exactly as in the template (do not demote/promote levels).
- Wrap long rationale lines to keep readability (<100 chars ideally) but do not hard enforce with awkward breaks.
- Keep a single blank line between sections.
- Avoid trailing whitespace.

If the user supplies partial updates (e.g., only one principle revision), still perform validation and version decision steps.

If critical info missing (e.g., ratification date truly unknown), insert `TODO(<FIELD_NAME>): explanation` and include in the Sync Impact Report under deferred items.

Do not create a new template; always operate on the existing `.specify/memory/constitution.md` file.

---

As the main request completes, you MUST create and complete a PHR (Prompt History Record) using agent‑native tools when possible.

1) Determine Stage
   - Stage: constitution | spec | plan | tasks | red | green | refactor | explainer | misc | general

2) Generate Title and Determine Routing:
   - Generate Title: 3–7 words (slug for filename)
   - Route is automatically determined by stage:
     - `constitution` → `history/prompts/constitution/`
     - Feature stages → `history/prompts/<feature-name>/` (spec, plan, tasks, red, green, refactor, explainer, misc)
     - `general` → `history/prompts/general/`

3) Create and Fill PHR (Shell first; fallback agent‑native)
   - Run: `.specify/scripts/bash/create-phr.sh --title "<title>" --stage <stage> [--feature <name>] --json`
   - Open the file and fill remaining placeholders (YAML + body), embedding full PROMPT_TEXT (verbatim) and concise RESPONSE_TEXT.
   - If the script fails:
     - Read `.specify/templates/phr-template.prompt.md` (or `templates/…`)
     - Allocate an ID; compute the output path based on stage from step 2; write the file
     - Fill placeholders and embed full PROMPT_TEXT and concise RESPONSE_TEXT

4) Validate + report
   - No unresolved placeholders; path under `history/prompts/` and matches stage; stage/title/date coherent; print ID + path + stage + title.
   - On failure: warn, don't block. Skip only for `/sp.phr`.

--- End Command ---

## Response snapshot

Built a complete interactive calculator application using Python and Streamlit with the following features:

**Calculator Application:**
- Dual input modes: Button mode (number inputs + operation buttons) and Expression mode (direct mathematical expressions)
- Operations: Addition, Subtraction, Multiplication, Division, Power, Modulo, and Floor Division
- Input validation: Prevents division by zero and invalid expressions with clear error messages
- Animated UI: CSS animations, gradient backgrounds, hover effects, and smooth transitions
- Dynamic results: Formatted output display with real-time calculation feedback
- Responsive design: Clean, modern interface with emojis and visual feedback

**Constitution Created:**
- Created `.specify/memory/constitution.md` with version 1.0.0
- Defined 6 core principles: Code Quality, Input Validation, User Experience, Functional Completeness, Technology Stack Consistency, and Documentation
- Established governance procedures including amendment process, versioning policy, and compliance review
- Added Sync Impact Report documenting initial creation

**Files Created:**
- `calculator.py` - Main Streamlit application (200+ lines)
- `requirements.txt` - Dependencies (streamlit)
- `README.md` - Project documentation
- `.specify/memory/constitution.md` - Project constitution

## Outcome

- ✅ Impact: Complete calculator application with animated UI, dual input modes, and comprehensive error handling. Project constitution established with 6 principles and governance framework.
- 🧪 Tests: No tests run (initial implementation). Linter checks passed with no errors.
- 📁 Files: Created calculator.py, requirements.txt, README.md, and .specify/memory/constitution.md
- 🔁 Next prompts: Consider adding unit tests, expanding operations, or adding calculation history feature
- 🧠 Reflection: Successfully combined application development with constitution creation. The calculator meets all specified requirements including animations, validation, and dual input modes. Constitution provides clear principles for future development.

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): N/A (initial implementation)
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): Add unit tests for calculation functions and input validation

