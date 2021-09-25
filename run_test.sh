#!/bin/bash

echo '###### mypy ######'
poetry run mypy rhi/

if [ $? != 0 ]; then
    echo 'mypy failed'
    exit 1
fi

echo '###### flake8 ######'
poetry run flake8 rhi/

if [ $? != 0 ]; then
    echo 'flake8 failed'
    exit 1
else
    echo 'flake8 passed'
fi

echo '###### pytest ######'
poetry run pytest

if [ $? != 0 ]; then
    echo 'pytest failed'
    exit 1
fi
