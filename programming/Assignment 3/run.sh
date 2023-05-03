#!/bin/bash
echo 'do we see this stuff?'
python3 -m venv typingtest-venv
./Scripts/activate
pip3 install -r Scripts/requirements.txt
python3 TypingTest.py