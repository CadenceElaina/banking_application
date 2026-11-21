SETUP

## Pytest

- python -m venv .venv # create a virtual environment in project root
- source .venv/bin/activate # activate it

- pip install pytest
- pip install --upgrade pip
- touch pyproject.toml # so tets can import from src/

Name test files test\_\*.py

## Run them

- pytest # runs everything
- pytest -v # lists eeach test by name
- pytest -k parse # runs only tests with "parse" in the name
- pytest tests/test_todo.py::test_ad_returns_incrementing_ids # runs one test
