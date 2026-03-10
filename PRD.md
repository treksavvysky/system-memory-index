# PRD: System Memory Index Generator

## Product Summary

The product is a generator that creates a compliant `System_Memory_Index` subsystem inside a `Command_Environment` workspace.

The goal is to make SMI creation reproducible. Instead of manually assembling the same directory tree and core documents each time, the user should be able to run a defined command or script and receive the canonical subsystem structure.

The generator must preserve the current SMI internal design. It changes how the SMI is instantiated, not what the SMI is.

The reference implementation for the initial release is Python.

---

## Problem

The current documentation has been converging on a canonical SMI structure, but a documented structure alone is not enough. If each SMI instance is created manually:

- setup becomes inconsistent
- structural drift becomes likely
- validation becomes harder
- portability is weakened
- bootstrapping a new Command Environment becomes slower

What is needed is a reproducible creation mechanism that can generate the SMI subsystem anywhere, anytime, with the same canonical outcome.

---

## Product Goal

Provide a repeatable way to generate:

```text
Command_Environment/System_Memory_Index
```

including its canonical zones, core documents, manifests, and optional example records.

The product succeeds when a user can generate a valid SMI subsystem in a fresh target workspace without manually reconstructing the specification.

By default, the target workspace is the current working directory. When no explicit target path is provided, the generator should create:

```text
./Command_Environment/System_Memory_Index
```

---

## Users

Primary users:

- the ecosystem architect creating or bootstrapping Command Environments
- developers or operators who need a compliant SMI subsystem in a new workspace
- future tools or agents that rely on a stable generated SMI structure

---

## User Stories

- As an operator, I want to generate an SMI subsystem in a new workspace so I do not need to recreate the structure by hand.
- As an architect, I want the generated subsystem to match the published SMI specification so that the design remains authoritative.
- As a future tool builder, I want every generated SMI instance to have the same predictable layout so that tooling can rely on stable paths and conventions.
- As a maintainer, I want a repeatable generation path so that the SMI can be recreated anywhere, anytime, with minimal ambiguity.

---

## Functional Requirements

### FR1. Generate Canonical Structure

The product must generate the canonical SMI subtree inside `Command_Environment`, relative to the target workspace root:

```text
/Command_Environment/
└── /System_Memory_Index/
    ├── 00_Doctrine/
    ├── 01_SMI_Core/
    ├── 02_Ideation/
    └── 05_Archive/
```

### FR2. Install Core SMI Documents

The product must place the canonical SMI core documents into `System_Memory_Index/01_SMI_Core`.

These include at minimum:

- `ARCHITECTURE.md`
- `SMI_RECORD_SCHEMA.md`
- `IDEA_RECORD_TEMPLATE.md`
- `IDEA_ADDENDUM_SCHEMA.md`

### FR3. Generate Local Manifests

The product must create required local manifest files such as `index.md` for the relevant directories.

### FR4. Support Example Bootstrap Content

The product should be able to generate example records sufficient to prove the subsystem is operational.

At minimum, bootstrap content should include:

- one Idea Record
- one Idea Addendum targeting that Idea Record

### FR5. Validate Generated Output

The product must provide a way to confirm that generated output matches the expected structure and required document set.

### FR6. Be Re-runnable

The product must support repeated execution against fresh workspaces and should behave predictably when executed against partially initialized targets.

### FR7. Provide a Python Reference Implementation

The product must be implemented initially as a Python-based generator, exposed through a documented Python entry point such as a CLI or script invocation.

### FR8. Default to the Current Working Directory

When no explicit target path is supplied, the product must treat the current working directory as the workspace root and generate the SMI subtree relative to it.

---

## Non-Functional Requirements

- Deterministic output for the same inputs
- Minimal configuration surface
- Plain-text, filesystem-based output
- Human-readable generated artifacts
- Clear failure behavior when generation cannot proceed safely
- No requirement for databases or hosted services
- Python as the explicit reference implementation stack for the first release

---

## Non-Goals

This product does not aim to:

- build dashboards
- visualize the knowledge graph
- automate idea analysis
- provide conversational interfaces
- replace the SMI's file-backed model
- redesign the SMI's internal schema or zone layout

---

## Success Criteria

The product is successful when:

- a fresh target workspace can receive a valid SMI subsystem through a documented generation command or script
- generated structure matches the canonical SMI layout
- required core documents appear in the correct zone
- generated example records conform to the published templates and schema
- generation can be repeated in multiple locations with materially identical results

---

## Acceptance Criteria

- A documented invocation exists for generating the SMI subsystem.
- When invoked without a target path, generation occurs relative to the current working directory.
- Running the generator creates `Command_Environment/System_Memory_Index`.
- The generated subsystem contains `00_Doctrine`, `01_SMI_Core`, `02_Ideation`, and `05_Archive`.
- The generated `01_SMI_Core` contains the canonical architecture and schema/template documents.
- Required local manifests are present.
- An example Idea Record can exist in generated output and conform to the template.
- An example Idea Addendum can exist in generated output and reference the example Idea Record.
- A validation step can confirm that the generated output is structurally compliant.

---

## Risks

- drift between generator behavior and published SMI specification
- ambiguous overwrite behavior in existing workspaces
- hidden assumptions about filesystem layout
- accidental coupling between generated fixtures and canonical design

These risks should be addressed through a simple source-of-truth model and explicit validation.

---

## Future Directions

Possible later extensions include:

- upgrade flows for existing SMI subsystems
- stronger schema validation
- automated master index generation
- richer bootstrap packs for different use cases
- integration with agents that consume generated SMI structures

The first release should stay focused on one job: reliably generating the canonical SMI subsystem.
