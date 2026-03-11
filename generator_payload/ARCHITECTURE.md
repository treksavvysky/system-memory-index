# System Memory Index (SMI)

## Purpose

The System Memory Index is a file-backed memory subsystem inside the broader `Command_Environment`.

Its purpose is to capture durable knowledge artifacts as structured Markdown records with stable identity, machine-readable metadata, and human-readable narrative content.

---

## Subsystem Structure

The canonical subsystem layout is:

```text
System_Memory_Index/
├── 00_Doctrine/
├── 01_SMI_Core/
├── 02_Ideation/
└── 05_Archive/
```

Each directory represents a conceptual zone rather than a strict hierarchy of meaning. Relationships between records live in metadata, not in filesystem paths.

---

## Core Design Rules

- Records are plain Markdown files with YAML frontmatter.
- UIDs are immutable and location-independent.
- Relationships use UID references rather than file paths.
- Templates define the canonical record structure.
- Indexes and manifests are derived navigational artifacts; records remain the source of truth.

---

## Core Zones

`00_Doctrine`

Contains doctrine records representing guiding principles and enduring intellectual foundations.

`01_SMI_Core`

Contains schemas, templates, architecture material, and other documents that define how the SMI operates.

`02_Ideation`

Contains Idea Records and related addendums for captured concepts and conceptual development.

`05_Archive`

Contains deprecated, completed, or historical records retained for reference.

---

## Record Model

Each record combines:

- YAML frontmatter for identity and relationship metadata
- Markdown body content for human-readable meaning and context

This design keeps the subsystem durable, inspectable, and easy for future tools or agents to parse.

---

## Interaction Model

Tools interact with the SMI by reading the filesystem, parsing frontmatter, and constructing relationships from UIDs.

Because the subsystem is file-based, it remains compatible with simple scripts, version control workflows, and future agent tooling without requiring a database.
