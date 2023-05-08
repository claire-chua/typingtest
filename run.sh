#!/bin/bash
pip install virtualenv
python -m virtualenv env
source venv/bin/activate
pip install -r requirements.txt
python3 TypingTestMenu.py

