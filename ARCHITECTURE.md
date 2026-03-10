# SMI Generator Architecture

## Purpose

This document defines the architecture of the system that generates the System Memory Index (SMI) as a subsystem within a broader `Command_Environment` workspace.

The product being built is not a single hand-crafted SMI instance. The product is the generation capability itself: a reproducible mechanism that can create a compliant `System_Memory_Index` subtree anywhere, anytime, with the same canonical structure and documents.

The internal design of the generated SMI remains unchanged. The generator's responsibility is to materialize that design faithfully.

The reference implementation of this generator is Python.

---

## System Context

The generator operates on a target workspace and produces the following structure:

```text
/Command_Environment/
└── /System_Memory_Index/
    ├── 00_Doctrine/
    ├── 01_SMI_Core/
    ├── 02_Ideation/
    └── 05_Archive/
```

Within that generated subsystem:

- `00_Doctrine` holds doctrine records
- `01_SMI_Core` holds architecture, schemas, templates, and system-level artifacts
- `02_Ideation` holds Idea Records
- `05_Archive` holds deprecated or historical records

The generator is responsible for creating this structure, placing the canonical documents, and optionally producing example fixture records for validation.

In the default case, the target workspace is the current working directory. That means the generator should normally materialize the subsystem at:

```text
./Command_Environment/System_Memory_Index
```

---

## Architectural Principles

- Reproducibility: the same inputs must produce the same compliant output structure.
- Determinism: generation should avoid hidden state and environment-specific behavior.
- Fidelity: the generated subsystem must preserve the canonical SMI design exactly.
- Simplicity: the implementation should remain understandable without heavy infrastructure.
- Idempotence: rerunning generation against the same target should not corrupt an existing valid subsystem.
- Portability: the generator should be usable in any suitable filesystem workspace.
- Pragmatism: the first implementation should use plain Python and the standard library where practical.

---

## System Boundary

The generator is responsible for:

- creating the `System_Memory_Index` subtree within `Command_Environment`
- creating required directories and local manifests
- installing core SMI documents into `System_Memory_Index/01_SMI_Core`
- providing canonical templates and schemas in generated output
- optionally generating example records for validation or bootstrapping
- validating that generated output conforms to the structural contract

The generator is not responsible for:

- dashboards, visualization layers, or graph UIs
- runtime agent orchestration
- automated reasoning over SMI content
- business workflows outside SMI creation
- replacing the SMI's record model with a different storage mechanism

---

## Output Contract

The generator's primary output is a filesystem subtree rooted at:

```text
Command_Environment/System_Memory_Index
```

That subtree must include:

- the canonical SMI zones
- the canonical core documents in `01_SMI_Core`
- local `index.md` manifest files for required directories
- no deviation from the published directory names without explicit configuration support

The generator may additionally create:

- sample Idea Records
- sample Idea Addendums
- fixture manifests or example master indexes

These optional artifacts must remain clearly identifiable as generated examples or bootstrap content.

---

## Logical Components

### 1. Entry Interface

The system should expose a single generation entry point, typically a Python CLI command or script invocation.

Its job is to accept the target path and any allowed configuration, then invoke generation in a predictable order.

If no target path is supplied, the entry interface should default to the current working directory.

### 2. Configuration Resolver

This component resolves the generation target and any supported options.

Initial configuration should be minimal. At minimum, the generator must know:

- the root target workspace, defaulting to the current working directory
- whether example records should be included

The architecture should prefer convention over configuration.

In the reference implementation, this resolver should be implemented in Python with a minimal argument surface.

### 3. Structure Generator

This component creates the required directory tree under `Command_Environment/System_Memory_Index`.

It must own the canonical mapping between conceptual zones and concrete paths.

### 4. Document Installer

This component writes or copies the canonical SMI core documents into `01_SMI_Core`.

It is responsible for ensuring that the generated subsystem contains the architecture, schemas, templates, and other required artifacts that define SMI behavior.

### 5. Manifest Generator

This component creates required local manifests such as `index.md` in each relevant directory.

These manifests provide navigational context for humans and future tools.

### 6. Fixture Generator

This optional component creates example records used to prove that the generated subsystem is operational.

Examples include:

- one valid Idea Record
- one valid Idea Addendum referencing that Idea Record

### 7. Validator

This component checks generated output for compliance.

Validation should confirm:

- required directories exist
- required documents are present in the expected locations
- example records, if generated, conform to schema expectations
- output paths match the canonical SMI layout

---

## Generation Flow

The expected flow is:

1. Resolve target workspace path.
   If no path is provided, use the current working directory.
2. Resolve generator options.
3. Create `Command_Environment` if needed.
4. Create `System_Memory_Index` and its required zones.
5. Install core SMI documents into `01_SMI_Core`.
6. Generate local manifests.
7. Optionally generate example records.
8. Run structural validation.
9. Report success or validation failures.

This flow should be executable repeatedly with predictable results.

---

## Idempotency and Overwrite Rules

The generator should be safe to rerun.

Preferred behavior:

- create missing directories without error
- avoid destructive overwrites by default
- overwrite generated files only when behavior is explicit and predictable
- fail clearly when encountering conflicting unexpected state

If overwrite modes are later introduced, they must be explicit and narrowly scoped.

---

## Source of Truth

The canonical SMI design remains defined by the SMI documents themselves.

The generator does not invent a new memory model. It encodes and materializes the published design:

- directory structure
- record schemas
- templates
- manifest expectations

In effect, the generator is an implementation of the SMI specification.

---

## Extensibility

The architecture should allow future additions without breaking the core contract.

Likely future extensions include:

- richer validation rules
- generation of additional record zones
- automated master index generation
- upgrade or migration commands for existing SMI subsystems
- integration with agent workflows that consume generated output

These capabilities must layer on top of the core generator rather than replace it.

---

## Non-Goals for the Initial Architecture

The initial generator architecture does not require:

- a database
- a web service
- a GUI
- remote orchestration
- dynamic schema negotiation
- automated graph analysis
- a non-Python reference implementation

The first objective is a reliable filesystem generator.

---

## Architectural Summary

The system being built is a deterministic generator for the `System_Memory_Index` subsystem inside `Command_Environment`.

Its role is to produce the same canonical SMI structure on demand, preserving the SMI's internal design while making that design reproducible as code. Once this capability exists, future tooling can build on a stable and repeatable memory substrate instead of relying on one-off manual setup.
