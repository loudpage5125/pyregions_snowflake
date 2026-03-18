#!/usr/bin/env bash

python3 -m build -s -x 

python3 -m twine upload -r local dist/* --verbose