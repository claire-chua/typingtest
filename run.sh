#!/bin/bash
pip install virtualenv
python -m virtualenv env
source venv/bin/activate
pip install -r requirements.txt
pytest Test/
python3 TypingTestMenu.py

