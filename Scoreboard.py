from Practice import *
# import pandas as pd

opened_file = False
# check_file = pd.read_csv("scores.csv")
# or check_file.empty == True
if opened_file == False:
    with open("scores.csv", 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["WPM, Accuracy(%)"])
        opened_file == True

def scoreboard():
    with open("scores.csv", 'r', newline = '') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)