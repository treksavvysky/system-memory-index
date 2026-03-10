# System Memory Index Generator (Python Reference)

This repository includes a reference Python generator for creating the SMI subsystem inside a workspace.

## Entry point

- `python3 smi_generator.py`

## Default behavior

Running with no arguments generates this structure relative to the current working directory:

- `./Command_Environment/System_Memory_Index/00_Doctrine`
- `./Command_Environment/System_Memory_Index/01_SMI_Core`
- `./Command_Environment/System_Memory_Index/02_Ideation`
- `./Command_Environment/System_Memory_Index/05_Archive`

It also installs canonical core documents into `01_SMI_Core` and writes local `index.md` manifests.

## Usage

Generate in current directory:

```bash
python3 smi_generator.py
```

Generate in another workspace root:

```bash
python3 smi_generator.py path/to/workspace
```

Validation only:

```bash
python3 smi_generator.py --validate-only
```

## Determinism and reruns

The generator is rerunnable and deterministic:

- Recreates missing directories.
- Rewrites files only when content differs.
- Produces stable manifest ordering.

