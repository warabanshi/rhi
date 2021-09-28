#!/bin/bash

INST=$1

mypy() {
    echo '###### mypy ######'
    poetry run mypy rhi/

    if [ $? != 0 ]; then
        echo 'mypy failed'
        exit 1
    fi
}

black() {
    echo '###### black #####'
    poetry run black rhi/
}

flake8() {
    echo '###### flake8 ######'
    poetry run flake8 rhi/

    if [ $? != 0 ]; then
        echo 'flake8 failed'
        exit 1
    else
        echo 'flake8 passed'
    fi
}

pytest() {
    echo '###### pytest ######'
    poetry run pytest -s

    if [ $? != 0 ]; then
        echo 'pytest failed'
        exit 1
    fi
}

case $INST in
    "mypy")
        mypy;;
    "black")
        black;;

    "flake8")
        flake8;;
    "pytest")
        pytest;;
    *)
        mypy
        black
        flake8
        pytest
esac
