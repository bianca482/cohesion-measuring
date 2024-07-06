# Cohesion Calculator

This project contains the definitions of the `cohesion_calculator` library which calculates Sensitive Class Cohesion Metric (SCOM) based on provided JSON input. The folder `cohesion\cohesion_calculator` provides the full implementation code for this. You can adjust and expand this implementation for your needs.

If you do make adjustments, you have to build and install the library.

## Setup

### Install dependencies

Create a text file named requirements.txt with following content:

`
build 
setuptools
wheel
twine
pytest
pytest-runner`
Install all neccessary requirements using `pip install -r requirements.txt`

### Build library

Following command builds the library according to the definition provided in `setup.py`: `python -m build --wheel`

### (Optional) Run tests

`pytest tests.py`

### Install library

In the `dist` folder, a new whl-file should have been generated. Adjust the name accordingly.

`pip install "dist\cohesion_measuring-0.1-py3-none-any.whl"`

### Use library

The library can be imported like `import cohesion_calculator`

For later:

### Publish to PyPI

`twine upload dist/\*`
`pip install cohesion_measuring`
