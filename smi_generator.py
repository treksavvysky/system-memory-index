#!/usr/bin/env python3
"""Reference generator for the System Memory Index (SMI) subsystem."""

from __future__ import annotations

import argparse
import hashlib
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

COMMAND_ENVIRONMENT = "Command_Environment"
SUBSYSTEM = "System_Memory_Index"

CANONICAL_DIRS = (
    "00_Doctrine",
    "01_SMI_Core",
    "02_Ideation",
    "05_Archive",
)

CANONICAL_CORE_DOCS = (
    "ARCHITECTURE.md",
    "SMI_RECORD_SCHEMA.md",
    "IDEA_RECORD_TEMPLATE.md",
    "IDEA_ADDENDUM_SCHEMA.md",
    "MISSION.md",
    "PROJECT-CHARTER.md",
    "VISION.md",
    "FEATURE-PROPOSAL.md",
    "PRD.md",
    "SPRINT-1-SCOPE.md",
    "SPRINT-1-WBS.md",
)


@dataclass(frozen=True)
class GenerationResult:
    created: list[Path]
    updated: list[Path]
    unchanged: list[Path]


def _hash_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _write_if_changed(destination: Path, content: str) -> str:
    destination.parent.mkdir(parents=True, exist_ok=True)
    new_bytes = content.encode("utf-8")

    if destination.exists():
        old_hash = _hash_bytes(destination.read_bytes())
        new_hash = _hash_bytes(new_bytes)
        if old_hash == new_hash:
            return "unchanged"
        destination.write_bytes(new_bytes)
        return "updated"

    destination.write_bytes(new_bytes)
    return "created"


def _build_index(title: str, entries: Iterable[str]) -> str:
    lines = [f"# {title}", "", "## Contents", ""]
    entry_list = list(entries)
    if entry_list:
        lines.extend(f"- [{entry}]({entry})" for entry in entry_list)
    else:
        lines.append("- _No records yet._")
    lines.append("")
    return "\n".join(lines)


def _render_root_index() -> str:
    lines = [
        "# System Memory Index",
        "",
        "## Zones",
        "",
        "- [00_Doctrine](00_Doctrine/index.md)",
        "- [01_SMI_Core](01_SMI_Core/index.md)",
        "- [02_Ideation](02_Ideation/index.md)",
        "- [05_Archive](05_Archive/index.md)",
        "",
    ]
    return "\n".join(lines)


def generate(workspace_root: Path, source_root: Path) -> GenerationResult:
    created: list[Path] = []
    updated: list[Path] = []
    unchanged: list[Path] = []

    subsystem_root = workspace_root / COMMAND_ENVIRONMENT / SUBSYSTEM
    subsystem_root.mkdir(parents=True, exist_ok=True)

    for zone in CANONICAL_DIRS:
        (subsystem_root / zone).mkdir(parents=True, exist_ok=True)

    status = _write_if_changed(subsystem_root / "index.md", _render_root_index())
    _append_by_status(subsystem_root / "index.md", status, created, updated, unchanged)

    core_dir = subsystem_root / "01_SMI_Core"
    copied_docs: list[str] = []
    for doc_name in CANONICAL_CORE_DOCS:
        source_doc = source_root / doc_name
        if not source_doc.exists() and doc_name == "IDEA_ADDENDUM_SCHEMA.md":
            source_doc = source_root / " IDEA_ADDENDUM_SCHEMA.md"
        if not source_doc.exists():
            raise FileNotFoundError(f"Canonical source document not found: {doc_name}")
        content = source_doc.read_text(encoding="utf-8")
        destination = core_dir / doc_name
        status = _write_if_changed(destination, content)
        _append_by_status(destination, status, created, updated, unchanged)
        copied_docs.append(doc_name)

    zones = {
        "00_Doctrine": [],
        "01_SMI_Core": sorted(copied_docs),
        "02_Ideation": [],
        "05_Archive": [],
    }

    for zone_name, entries in zones.items():
        zone_dir = subsystem_root / zone_name
        zone_index = zone_dir / "index.md"
        content = _build_index(zone_name, entries)
        status = _write_if_changed(zone_index, content)
        _append_by_status(zone_index, status, created, updated, unchanged)

    return GenerationResult(created=created, updated=updated, unchanged=unchanged)


def validate_structure(workspace_root: Path) -> list[str]:
    """Return a list of validation errors, empty if compliant."""
    errors: list[str] = []
    subsystem_root = workspace_root / COMMAND_ENVIRONMENT / SUBSYSTEM

    if not subsystem_root.exists():
        return [f"Missing subsystem root: {subsystem_root}"]

    for zone in CANONICAL_DIRS:
        zone_dir = subsystem_root / zone
        if not zone_dir.is_dir():
            errors.append(f"Missing canonical directory: {zone_dir}")
        index_file = zone_dir / "index.md"
        if not index_file.is_file():
            errors.append(f"Missing zone index: {index_file}")

    root_index = subsystem_root / "index.md"
    if not root_index.is_file():
        errors.append(f"Missing subsystem index: {root_index}")

    core_dir = subsystem_root / "01_SMI_Core"
    for doc_name in CANONICAL_CORE_DOCS:
        if not (core_dir / doc_name).is_file():
            errors.append(f"Missing canonical core doc: {core_dir / doc_name}")

    return errors


def _append_by_status(path: Path, status: str, created: list[Path], updated: list[Path], unchanged: list[Path]) -> None:
    if status == "created":
        created.append(path)
    elif status == "updated":
        updated.append(path)
    else:
        unchanged.append(path)


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "target",
        nargs="?",
        default=".",
        help="Workspace root where Command_Environment will be created (default: current directory)",
    )
    parser.add_argument(
        "--source-root",
        default=str(Path(__file__).resolve().parent),
        help="Directory containing canonical source documents (default: repository root)",
    )
    parser.add_argument(
        "--validate-only",
        action="store_true",
        help="Run validation only against an existing generated structure.",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv or sys.argv[1:])
    workspace_root = Path(args.target)
    source_root = Path(args.source_root)

    if args.validate_only:
        errors = validate_structure(workspace_root)
        if errors:
            print("Validation failed:")
            for err in errors:
                print(f"- {err}")
            return 1
        print("Validation passed.")
        return 0

    result = generate(workspace_root=workspace_root, source_root=source_root)
    errors = validate_structure(workspace_root)

    print(f"Created: {len(result.created)}")
    print(f"Updated: {len(result.updated)}")
    print(f"Unchanged: {len(result.unchanged)}")

    if errors:
        print("Validation failed:")
        for err in errors:
            print(f"- {err}")
        return 1

    print("Validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
