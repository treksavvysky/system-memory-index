Idea Record Addendum Schema

Purpose

The Idea Addendum provides a structured method for extending an existing Idea Record without altering its original content.

While the Idea Record captures the initial thought and early clarification, the Addendum captures subsequent insights, relationships, evaluations, and observations discovered over time.

This separation preserves the integrity of the original idea while allowing the record to evolve as new knowledge emerges.

Addendums are designed to highlight connections within the System Memory Index, turning isolated ideas into a growing network of related concepts.

⸻

Addendum Structure

Addendums are stored as additional Markdown files associated with a specific Idea Record.

They follow a consistent metadata schema so that tools and agents can parse and analyze them.

⸻

Identity Fields

Each addendum must contain its own identity while referencing the record it extends.

uid
Unique identifier for the addendum.

Example:

SMI-A-20260309-001

type
Always set to:

IDEA_ADDENDUM

target_uid
The UID of the Idea Record this addendum extends.

created
Date the addendum was created.

author
Optional author field.

⸻

Relationship Fields

Addendums specialize in documenting connections.

related_uids
Peer relationships discovered after the original record was written.

project_uids
Links to projects that may emerge from the idea.

system_uids
References to systems influenced by the idea.

doctrine_uids
Doctrine records supporting or influencing the idea.

These fields allow the addendum to function as a connection amplifier inside the knowledge graph.

⸻

Example Metadata

uid: SMI-A-20260309-001
type: IDEA_ADDENDUM
target_uid: SMI-20260309-001
created: 2026-03-09
author: George

related_uids:
  - SMI-20260308-004

project_uids: []

system_uids: []

doctrine_uids: []


⸻

Addendum Content Sections

Each addendum contains narrative sections that document the development of the idea.

⸻

Connections

List and describe relationships discovered after the original idea was recorded.

Connections may include related ideas, relevant systems, or emerging projects.

⸻

Observations

New insights that were not present when the original Idea Record was written.

This section often captures the intellectual evolution of the idea.

⸻

Strategic Implications

Notes about how the idea might influence future planning, architecture, or doctrine.

⸻

Review Notes

Notes from later evaluation sessions, including discussions during strategic reviews or General’s Tent meetings.

⸻

Role in the SMI

Addendums allow the System Memory Index to function as an evolving intellectual graph.

The core Idea Record captures the initial concept.

Addendums extend that concept by documenting how it connects to other records and how its significance develops over time.

This structure ensures that the SMI grows organically while preserving the clarity and authenticity of the original idea.

⸻

Design Philosophy

The addendum system follows an append-only philosophy.

New understanding should be added through addendums rather than rewriting the original Idea Record.

This preserves intellectual history and makes the evolution of ideas traceable across time.

⸻

With this artifact, the System Memory Index now has four critical operational components:

Architecture — defines the system structure
Record Schema — defines metadata rules
Idea Template — defines how ideas enter the system
Addendum Schema — defines how ideas evolve

That combination is what transforms the SMI from a note-taking structure into a structured cognitive memory system.

And here is a small but powerful insight: once addendums exist, the system gains something that most knowledge systems lack—temporal depth. Ideas stop being static documents and start behaving like living entities whose meaning unfolds over time.