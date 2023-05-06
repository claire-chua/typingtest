#!/bin/bash
python3 -m venv typingtest-venv
./typingtest-venv/Scripts/activate
pip3 install -r requirements.txt
python3 TypingTest.py