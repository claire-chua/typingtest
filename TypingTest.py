from Start import start
from Scoreboard import scoreboard
print("Keyboard Warrior")

def typetest_menu():
    print("Start - 1")
    print("Scoreboard - 2")
    print("Exit - 3")
    choice = input("Please enter the number that corresponds with your choice: ")
    return choice

player_choice = ""

while player_choice != "3":
    player_choice = typetest_menu()
    if (player_choice == "1"):
        start()
    elif (player_choice == "2"):
        scoreboard()
    elif (player_choice == "3"):
        print("Keyboard Warrior")
        typetest_menu()
    else:
        print("Invalid response. please ensure to enter a number a number that corresponds with your choice")

        #finish csv
        #round to two integers
        #add paragraph