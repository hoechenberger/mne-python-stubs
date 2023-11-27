# Type stubs for MNE-Python

These are type stubs for MNE-Python. They contain docstrings for
a more convenient user experience when using static analysis tools
like Pylance in VS Code.

## Installation

```shell
pip install https://github.com/hoechenberger/mne-python-stubs/archive/refs/heads/main.zip
```

## Development

Clone this repository and `cd` into it.

```shell
pip install ".[dev]"
```
Running `python gen_type_stubs.py` re-generates the type stubs.

## Notes

* The name of this repository is `mne-python-stubs`,
* the package name is `types-mne`, and
* the stubs will be deployed into a directory named `mne-stubs` inside the
  Python `site-packages` directory.

Except for the first point, this is consistent with [typeshed](https://github.com/python/typeshed).
