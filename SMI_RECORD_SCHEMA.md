# System Memory Index Record Schema

Purpose

This document defines the canonical metadata schema used by records within the System Memory Index (SMI). The schema ensures that every record contains consistent identity and relationship information that can be parsed by tools, scripts, and future AI agents.

Records consist of two layers: machine-readable metadata stored in YAML frontmatter and human-readable narrative sections contained in the body of the document.

The metadata layer provides the structural information necessary for indexing, graph construction, and validation.

⸻

Record Identity Fields

Every record must contain immutable identity fields.

uid
A globally unique identifier assigned at the creation of the record. The identifier never changes.

Example:

SMI-20260309-001

type
Defines the category of the record.

Typical values include:
	•	IDEA
	•	DOCTRINE
	•	PROJECT
	•	TELEMETRY
	•	SYSTEM
	•	MISSION

Only IDEA and DOCTRINE are required in the initial implementation.

title
Human-readable name of the record.

status
Current lifecycle state of the record.

Typical values include:
	•	captured
	•	incubating
	•	exploring
	•	pre-planning
	•	active
	•	completed
	•	archived

created
Date the record was first created.

updated
Date of the most recent modification.

author
Optional field identifying the creator of the record.

⸻

Relationship Fields

Relationships allow records to connect across domains.

parent_uid
Identifies the upstream record that this record belongs to.

related_uids
List of peer records that share conceptual relationships.

doctrine_uid
Reference to a doctrine record that justifies the existence of this record.

Relationships use UID references rather than file paths to maintain stability when files move.

Example:

related_uids:
  - SMI-20260309-004
  - SMI-20260308-002


⸻

Metadata Example

Example YAML frontmatter for an Idea Record.

uid: SMI-20260309-001
type: IDEA
title: System Memory Index
status: captured
created: 2026-03-09
updated: 2026-03-09
author: George

parent_uid: null

related_uids:
  - SMI-20260308-002

doctrine_uid: null


⸻

Schema Rules

All records must include:
	•	uid
	•	type
	•	title
	•	status
	•	created
	•	updated

Relationship fields may be empty but must remain structurally valid.

UID references must always refer to existing records.

Tools interacting with the SMI may validate schema compliance and detect broken links or orphan nodes.

⸻

Design Philosophy

The schema prioritizes simplicity, stability, and machine readability.

Metadata should remain minimal but expressive enough to support graph relationships and automated indexing.

The narrative sections of each record preserve context and reasoning, while the metadata provides the structural backbone for the SMI knowledge graph.

⸻

