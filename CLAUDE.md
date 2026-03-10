# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

The System Memory Index (SMI) is a file-backed, identity-driven knowledge graph for structured knowledge management. Records are plain-text Markdown files with YAML frontmatter metadata, tracked in Git. There is no application code, build system, or dependencies — this is a pure documentation/infrastructure project.

## Repository Structure

The planned directory layout follows a Fixed-Root, Variable-Leaf architecture:

```
/Command_Environment/
└── /System_Memory_Index/
    ├── 00_Doctrine/   # Guiding principles and enduring intellectual foundations
    ├── 01_SMI_Core/   # Architecture docs, schemas, templates, system-level artifacts
    ├── 02_Ideation/   # Idea Records capturing emerging ideas
    └── 05_Archive/    # Deprecated/historical records
```

`Command_Environment` is the parent workspace. `System_Memory_Index` is the subsystem being built within it, and it preserves the existing SMI zones shown above. Core SMI documents such as `ARCHITECTURE.md` and `SMI_RECORD_SCHEMA.md` belong within the subsystem, typically under `System_Memory_Index/01_SMI_Core/`.

## Record System

Every record is a Markdown file with two layers:

1. **YAML frontmatter** — machine-readable identity and relationship metadata
2. **Markdown body** — human-readable narrative content following a template

### Record Types

- **Idea Record** (`type: IDEA`): Primary record type. Sections: Raw Idea Capture, Clarified Concept, Context of Discovery, Potential Applications, Observations, Review Notes.
- **Idea Addendum** (`type: IDEA_ADDENDUM`): Append-only extension to an existing Idea Record. References a `target_uid`. Preserves original record integrity while documenting evolution.
- **Doctrine Record** (`type: DOCTRINE`): Guiding principles (planned).

### Identity Scheme

```
Format:  SMI-YYYYMMDD-XXX     (e.g., SMI-20260309-001)
Addendum: SMI-A-YYYYMMDD-XXX  (e.g., SMI-A-20260309-001)
```

UIDs are immutable and location-independent. Relationships use UID references, never file paths.

### Required Metadata Fields

All records must include: `uid`, `type`, `title`, `status`, `created`, `updated`.

Status values: `captured`, `incubating`, `exploring`, `pre-planning`, `active`, `completed`, `archived`.

Relationship fields (`parent_uid`, `related_uids`, `doctrine_uid`) may be null/empty but must be structurally valid YAML.

## Key Conventions

- Records are the source of truth; indexes/manifests are derived artifacts.
- Relationships live in metadata, not directory structure — the knowledge graph is decentralized.
- Addendums follow an append-only philosophy: extend ideas via addendums rather than rewriting original records.
- New ideas should immediately fill the Raw Idea Capture section to preserve the original thought.
- UID references must point to existing records (tools should validate for broken links/orphan nodes).

## Specification Files

| File | Defines |
|------|---------|
| ARCHITECTURE.md | System boundary, structure, design principles, interaction model |
| SMI_RECORD_SCHEMA.md | Canonical metadata schema for all records |
| IDEA_RECORD_TEMPLATE.md | Template for creating new Idea Records |
| IDEA_ADDENDUM_SCHEMA.md | Schema for idea evolution addendums |
| MISSION.md | Sprint 1 objectives and success criteria |
| PROJECT-CHARTER.md | Project authorization and scope |
| VISION.md | Long-term strategic vision |
| FEATURE-PROPOSAL.md | Idea Record Registry feature spec |

Note: `IDEA_ADDENDUM_SCHEMA.md` has a leading space in its filename (` IDEA_ADDENDUM_SCHEMA.md`).
