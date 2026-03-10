import tempfile
import unittest
from pathlib import Path

from smi_generator import (
    CANONICAL_CORE_DOCS,
    CANONICAL_DIRS,
    COMMAND_ENVIRONMENT,
    SUBSYSTEM,
    generate,
    validate_structure,
)


class SmiGeneratorTests(unittest.TestCase):
    def test_generate_and_validate(self) -> None:
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

            for doc in CANONICAL_CORE_DOCS:
                self.assertTrue((subsystem / "01_SMI_Core" / doc).is_file())

            errors = validate_structure(workspace)
            self.assertEqual([], errors)

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
