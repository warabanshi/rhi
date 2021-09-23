#!/bin/bash

echo '###### mypy ######'
poetry run mypy rfind/

echo '###### flake8 ######'
poetry run flake8 rfind/

echo '###### pytest ######'
poetry run pytest
