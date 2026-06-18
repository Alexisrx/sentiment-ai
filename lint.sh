#!/bin/sh
pip install flake8 -q
flake8 src/ --max-line-length=100
