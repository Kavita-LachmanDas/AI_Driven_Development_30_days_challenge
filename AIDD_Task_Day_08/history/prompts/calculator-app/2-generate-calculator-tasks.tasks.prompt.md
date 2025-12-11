---
id: 2
title: Generate Calculator Tasks
stage: tasks
date: 2024-12-19
surface: agent
model: Auto
feature: calculator-app
branch: 1-calculator-app
user: Kavita-LachmanDas
command: /sp.tasks
labels: ["calculator", "tasks", "implementation", "streamlit", "python"]
links:
  spec: specs/1-calculator-app/spec.md
  ticket: null
  adr: null
  pr: null
files:
  - specs/1-calculator-app/tasks.md
tests:
  - No test tasks included (not explicitly requested in specification)
---

## Prompt

/sp.tasks 
Build a **Calculator App** using **Python** and **Streamlit**. Follow these tasks:

1. **Create the UI**:
   - Title and description for the calculator.
   - Input fields for numbers or a single input prompt for expressions.
   - Buttons or dropdown to select operation (add, subtract, multiply, divide).

2. **Define calculation functions**:
   - Function for addition.
   - Function for subtraction.
   - Function for multiplication.
   - Function for division with division-by-zero handling.

3. **Handle user input**:
   - Validate the input to prevent errors.
   - Convert input strings to numbers if needed.

4. **Display results**:
   - Show result dynamically after calculation.
   - Use colors, emojis, or animations for better UX.

5. **Enhance UI** (Optional):
   - Add responsive design.
   - Add subtle animations for input/output interactions.
   - Make it visually appealing and interactive.


--- Cursor Command: sp.tasks.md ---

## User Input

```text
$ARGUMENTS
```

You **MUST** consider the user input before proceeding (if not empty).

## Outline

1. **Setup**: Run `.specify/scripts/powershell/check-prerequisites.ps1 -Json` from repo root and parse FEATURE_DIR and AVAILABLE_DOCS list. All paths must be absolute. For single quotes in args like "I'm Groot", use escape syntax: e.g 'I'\''m Groot' (or double-quote if possible: "I'm Groot").

2. **Load design documents**: Read from FEATURE_DIR:
   - **Required**: plan.md (tech stack, libraries, structure), spec.md (user stories with priorities)
   - **Optional**: data-model.md (entities), contracts/ (API endpoints), research.md (decisions), quickstart.md (test scenarios)
   - Note: Not all projects have all documents. Generate tasks based on what's available.

3. **Execute task generation workflow**:
   - Load plan.md and extract tech stack, libraries, project structure
   - Load spec.md and extract user stories with their priorities (P1, P2, P3, etc.)
   - If data-model.md exists: Extract entities and map to user stories
   - If contracts/ exists: Map endpoints to user stories
   - If research.md exists: Extract decisions for setup tasks
   - Generate tasks organized by user story (see Task Generation Rules below)
   - Generate dependency graph showing user story completion order
   - Create parallel execution examples per user story
   - Validate task completeness (each user story has all needed tasks, independently testable)

4. **Generate tasks.md**: Use `.specify.specify/templates/tasks-template.md` as structure, fill with:
   - Correct feature name from plan.md
   - Phase 1: Setup tasks (project initialization)
   - Phase 2: Foundational tasks (blocking prerequisites for all user stories)
   - Phase 3+: One phase per user story (in priority order from spec.md)
   - Each phase includes: story goal, independent test criteria, tests (if requested), implementation tasks
   - Final Phase: Polish & cross-cutting concerns
   - All tasks must follow the strict checklist format (see Task Generation Rules below)
   - Clear file paths for each task
   - Dependencies section showing story completion order
   - Parallel execution examples per story
   - Implementation strategy section (MVP first, incremental delivery)

5. **Report**: Output path to generated tasks.md and summary:
   - Total task count
   - Task count per user story
   - Parallel opportunities identified
   - Independent test criteria for each story
   - Suggested MVP scope (typically just User Story 1)
   - Format validation: Confirm ALL tasks follow the checklist format (checkbox, ID, labels, file paths)

Context for task generation: $ARGUMENTS

The tasks.md should be immediately executable - each task must be specific enough that an LLM can complete it without additional context.

## Task Generation Rules

**CRITICAL**: Tasks MUST be organized by user story to enable independent implementation and testing.

**Tests are OPTIONAL**: Only generate test tasks if explicitly requested in the feature specification or if user requests TDD approach.

### Checklist Format (REQUIRED)

Every task MUST strictly follow this format:

```text
- [ ] [TaskID] [P?] [Story?] Description with file path
```

**Format Components**:

1. **Checkbox**: ALWAYS start with `- [ ]` (markdown checkbox)
2. **Task ID**: Sequential number (T001, T002, T003...) in execution order
3. **[P] marker**: Include ONLY if task is parallelizable (different files, no dependencies on incomplete tasks)
4. **[Story] label**: REQUIRED for user story phase tasks only
   - Format: [US1], [US2], [US3], etc. (maps to user stories from spec.md)
   - Setup phase: NO story label
   - Foundational phase: NO story label  
   - User Story phases: MUST have story label
   - Polish phase: NO story label
5. **Description**: Clear action with exact file path

**Examples**:

- ✅ CORRECT: `- [ ] T001 Create project structure per implementation plan`
- ✅ CORRECT: `- [ ] T005 [P] Implement authentication middleware in src/middleware/auth.py`
- ✅ CORRECT: `- [ ] T012 [P] [US1] Create User model in src/models/user.py`
- ✅ CORRECT: `- [ ] T014 [US1] Implement UserService in src/services/user_service.py`
- ❌ WRONG: `- [ ] Create User model` (missing ID and Story label)
- ❌ WRONG: `T001 [US1] Create model` (missing checkbox)
- ❌ WRONG: `- [ ] [US1] Create User model` (missing Task ID)
- ❌ WRONG: `- [ ] T001 [US1] Create model` (missing file path)

### Task Organization

1. **From User Stories (spec.md)** - PRIMARY ORGANIZATION:
   - Each user story (P1, P2, P3...) gets its own phase
   - Map all related components to their story:
     - Models needed for that story
     - Services needed for that story
     - Endpoints/UI needed for that story
     - If tests requested: Tests specific to that story
   - Mark story dependencies (most stories should be independent)

2. **From Contracts**:
   - Map each contract/endpoint → to the user story it serves
   - If tests requested: Each contract → contract test task [P] before implementation in that story's phase

3. **From Data Model**:
   - Map each entity to the user story(ies) that need it
   - If entity serves multiple stories: Put in earliest story or Setup phase
   - Relationships → service layer tasks in appropriate story phase

4. **From Setup/Infrastructure**:
   - Shared infrastructure → Setup phase (Phase 1)
   - Foundational/blocking tasks → Foundational phase (Phase 2)
   - Story-specific setup → within that story's phase

### Phase Structure

- **Phase 1**: Setup (project initialization)
- **Phase 2**: Foundational (blocking prerequisites - MUST complete before user stories)
- **Phase 3+**: User Stories in priority order (P1, P2, P3...)
  - Within each story: Tests (if requested) → Models → Services → Endpoints → Integration
  - Each phase should be a complete, independently testable increment
- **Final Phase**: Polish & Cross-Cutting Concerns

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

Generated comprehensive task list for Calculator Application organized by user story:

**Tasks Created:**
- Total tasks: 42 tasks across 7 phases
- File: `specs/1-calculator-app/tasks.md`

**Task Organization:**
- Phase 1: Setup (3 tasks) - Project initialization
- Phase 2: Foundational (2 tasks) - Core infrastructure
- Phase 3: User Story 1 - Basic Arithmetic (10 tasks) - MVP
- Phase 4: User Story 2 - Error Handling (6 tasks)
- Phase 5: User Story 3 - Animated UI (7 tasks)
- Phase 6: User Story 4 - Dynamic Updates (6 tasks)
- Phase 7: Polish & Cross-Cutting (8 tasks)

**Key Features:**
- All tasks follow strict checklist format with IDs, story labels, and file paths
- Tasks organized by user story for independent implementation
- Parallel execution opportunities identified
- MVP scope defined (User Story 1 only)
- Implementation strategies provided (MVP first, incremental, parallel team)

**Task Breakdown:**
- User Story 1: 10 tasks (core arithmetic operations)
- User Story 2: 6 tasks (error handling and validation)
- User Story 3: 7 tasks (UI animations and responsiveness)
- User Story 4: 6 tasks (dynamic result updates)
- Polish: 8 tasks (edge cases, optimization, documentation)

## Outcome

- ✅ Impact: Complete task breakdown created with 42 executable tasks organized by user story. Each task includes exact file paths and can be completed independently. Ready for implementation.
- 🧪 Tests: No test tasks included (not explicitly requested in specification)
- 📁 Files: Created specs/1-calculator-app/tasks.md with comprehensive task list
- 🔁 Next prompts: Ready for implementation. Can start with Phase 1 (Setup) and proceed through phases sequentially or in parallel where marked.
- 🧠 Reflection: Successfully generated tasks that map directly to user stories from spec.md. All tasks follow the required format with checkboxes, IDs, story labels, and file paths. Tasks are organized to enable independent implementation and testing of each user story.

## Evaluation notes (flywheel)

- Failure modes observed: None - all tasks generated successfully
- Graders run and results (PASS/FAIL): Task format validation - PASS (all tasks follow required format)
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): Begin implementation starting with Phase 1 (Setup) tasks

