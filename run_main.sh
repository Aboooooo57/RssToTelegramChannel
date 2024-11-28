#!/bin/bash

source .venv/bin/activate

export PYTHONPATH=$(pwd)/src

export $(grep -v '^#' .env | xargs)

python main.py