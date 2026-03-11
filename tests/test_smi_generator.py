import tempfile
import unittest
from pathlib import Path

from smi_generator import (
    CANONICAL_DIRS,
    COMMAND_ENVIRONMENT,
    CORE_DOC_SOURCES,
    FIXTURE_SOURCES,
    SUBSYSTEM,
    generate,
    parse_args,
    validate_structure,
)


class SmiGeneratorTests(unittest.TestCase):
    def test_parse_args_defaults_to_current_directory(self) -> None:
        args = parse_args([])
        self.assertEqual(".", args.target)
        self.assertFalse(args.no_examples)

    def test_generate_and_validate_with_examples(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            workspace = Path(tmp)
            source_root = Path(__file__).resolve().parents[1]

            result = generate(workspace_root=workspace, source_root=source_root)
            self.assertGreater(len(result.created), 0)

            subsystem = workspace / COMMAND_ENVIRONMENT / SUBSYSTEM
            self.assertTrue(subsystem.exists())

            for zone in CANONICAL_DIRS:
                self.assertTrue((subsystem / zone).is_dir())
                self.assertTrue((subsystem / zone / "index.md").is_file())

            for doc in CORE_DOC_SOURCES:
                self.assertTrue((subsystem / "01_SMI_Core" / doc).is_file())

            for fixture in FIXTURE_SOURCES:
                self.assertTrue((subsystem / "02_Ideation" / fixture).is_file())

            self.assertFalse((subsystem / "01_SMI_Core" / "PRD.md").exists())
            self.assertFalse((subsystem / "01_SMI_Core" / "SPRINT-1-SCOPE.md").exists())
            self.assertEqual([], validate_structure(workspace))

    def test_generate_without_examples_can_validate_when_requested(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            workspace = Path(tmp)
            source_root = Path(__file__).resolve().parents[1]

            generate(workspace_root=workspace, source_root=source_root, include_examples=False)
            self.assertEqual([], validate_structure(workspace, require_examples=False))

    def test_second_run_is_stable(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            workspace = Path(tmp)
            source_root = Path(__file__).resolve().parents[1]

            generate(workspace_root=workspace, source_root=source_root)
            second = generate(workspace_root=workspace, source_root=source_root)

            self.assertEqual([], second.created)
            self.assertEqual([], second.updated)
            self.assertGreater(len(second.unchanged), 0)


if __name__ == "__main__":
    unittest.main()
