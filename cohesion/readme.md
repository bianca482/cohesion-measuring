# Cohesion Calculator

This project contains the definitions of the `cohesion_calculator` library which calculates Sensitive Class Cohesion Metric (SCOM) based on provided JSON input. The folder `cohesion\cohesion_calculator` provides the full implementation code for this.

The library can be installed by running `pip install cohesion_measuring`.

You can adjust and expand this implementation for your needs. If you want to make adjustments you have to build and install the library as described in the following.

## Setup

### Install dependencies

1. Create a text file named requirements.txt with following content: `build  setuptools wheel twine pytest pytest-runner`

2. Install all neccessary requirements using `pip install -r requirements.txt`

### Build library

Following command builds the library according to the definition provided in `setup.py`: `python -m build --wheel`

### (Optional) Run tests

`pytest tests.py`

### Install library

In the `dist` folder, a new whl-file should have been generated. Adjust the name accordingly.

`pip install "dist\cohesion_measuring-0.1-py3-none-any.whl"`

### Use library

The library can be imported like `import cohesion_calculator`

### Publish to PyPI

- Build: `python setup.py sdist bdist_wheel`
- Check if everything works: `twine check dist/*`
- Upload to PyPI via Twine `twine upload dist/\*`
- Install: `pip install cohesion_measuring`
