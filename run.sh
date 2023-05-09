#!/bin/bash
pip install virtualenv
python -m virtualenv env
source venv/bin/activate
pip install -r requirements.txt
pytest tests/tests.py --color=yes
python3 TypingTestMenu.py