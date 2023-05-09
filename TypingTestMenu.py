from wonderwords import RandomSentence

from Practice import timed_test
from Scoreboard import scoreboard

print("Keyboard Warrior")

sentence_generator = RandomSentence()
sentence = ""

for index in range(25):
    sentence += sentence_generator.sentence().lower() + " "


def typetest_menu():
    print("Start - 1")
    print("Scoreboard - 2")
    print("Exit - 3")
    choice = input("Please enter the number that corresponds with your choice: ")
    return choice


player_choice = ""
try:
    while player_choice != "3":
        player_choice = typetest_menu()
        if player_choice == "1":
            timed_test(sentence)
        elif player_choice == "2":
            scoreboard()
        elif player_choice == "3":
            print("Keyboard Warrior")
except ValueError:
    print("Invalid response. please ensure to enter a number a number that corresponds with your choice")
