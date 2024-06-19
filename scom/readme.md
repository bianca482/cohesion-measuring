# Cohesion Calculator

Calculates SCOM metric

## Setup

### Install dependencies

Create a text file named requirements.txt with following content:

{
build
setuptools
wheel
twine
pytest
pytest-runner
}

`pip install -r requirements.txt`

### Build library

`python -m build --wheel`

### Run tests (optional)

`pytest tests.py`

### Install library

Adjust path to whl-File (in dist-folder)

`pip install "dist\cohesion_scom-0.1-py3-none-any.whl"`

### Use library

The library can be imported like `import cohesion_scom`

For later:

### Publish to PyPI

`twine upload dist/\*`
`pip install cohesion_scom`
