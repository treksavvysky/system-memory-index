# System Memory Index Generator

The Python reference generator creates a compliant `System_Memory_Index` subsystem inside `Command_Environment`.

## Entry point

```bash
python3 smi_generator.py
```

## Default behavior

Running with no arguments uses the current working directory as the workspace root and generates:

```text
./Command_Environment/System_Memory_Index
```

The generator:

- creates the canonical SMI zone directories
- installs the generated SMI core payload into `01_SMI_Core`
- creates local `index.md` manifests
- generates example Idea Record fixtures by default

## Usage

Generate relative to the current working directory:

```bash
python3 smi_generator.py
```

Generate in a different workspace root:

```bash
python3 smi_generator.py path/to/workspace
```

Skip example fixtures:

```bash
python3 smi_generator.py --no-examples
```

Validate an existing generated structure:

```bash
python3 smi_generator.py --validate-only
```
