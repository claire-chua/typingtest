## Typing Test

Source code repository link: https://github.com/claire-chua/typingtest.git

### Features

Feature 1: Do the words match?
This feature will consistently track if the user input matches the generated sentence, highlight any errors in red and
matched.

Feature 2: Results
This feature will calculate the user’s accuracy and words per minute (WPM) by collecting the elapsed time, matched words
and any errors made.

Feature 3: Scoreboard
This feature will automatically save the user’s results, which will be accessible even after the application has been
restarted.

### Implementation Plan:

All requirements for the development of an implementation plan are fulfilled on trello board below.
https://trello.com/invite/b/o9iDh76N/ATTIee791c2cdcb5d2c4e171762a7ab5e7625CC64F14/typing-test

### Documentation

Please download Python and Ubuntu, if not already installed on your computer.
Then, open the src folder in the submitted zip file.
Run ./run.sh in the Ubuntu terminal, this will open up the virtual environment and download any requirements needed
automatically. Thus, allowing the application to run.

This will bring the user to the menu, which will allow the user to select options by selecting their corresponding
numbers.If the typing test is picked, the timer will begin once the first letter is pressed, and results will be
calculated when the ‘enter’ key is pressed. If the user selects the scoreboard, this will allow the user to access their
previous results.

### Dependencies

- colorama == 0.4.6
- readchar == 4.0.5
- pytest == 7.3.1
- cursor == 1.3.5
- wonderwords == 2.20

### System requirements

- pytest: Python 3.7+ or PyPy3
- wonderwords: >= Python 3.6
- colorama: Python !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*, !=3.5.*, !=3.6.*, >=2.7
- readchar: Python >=3.7

### References

https://peps.python.org/pep-0008/
https://docs.pytest.org/en/7.1.x/how-to/capture-stdout-stderr.html
https://automationpanda.com/2017/03/14/python-testing-101-pytest/#:~:text=Pytests%20may%20be%20written%20either,or%20any%20other%20base%20class.
https://blog.finxter.com/how-to-overwrite-the-previous-print-to-stdout-in-python/
https://stackoverflow.com/questions/17069007/how-do-i-force-pytest-to-write-color-output