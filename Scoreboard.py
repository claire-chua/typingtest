import csv
from Practice import *


def scoreboard():
    with open("scores.csv", 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)