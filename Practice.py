import csv
import time

import cursor
from colorama import Fore
from readchar import readkey, key

cursor.hide()


def timed_test(sentence):
    error = 0
    print("Please type the sentence shown below. The timer will begin once you press a key. "
          "Press 'enter' to calculate results. \n")
    print(sentence)
    sentence_cursor = 0
    updated_sentence = ""
    elapsed_time = 0
    start_time = 0
    timer_started = False
    user_exited = False
    total_characters = 0

    while sentence_cursor < len(sentence) + 1 and user_exited is not True:
        k = readkey()
        if not timer_started:
            start_time = time.time()
            timer_started = True

        current_time = time.time()
        elapsed_time = current_time - start_time
        try:
            if k == key.BACKSPACE:
                sentence_cursor -= 1
                updated_sentence = updated_sentence.rstrip(updated_sentence[-1])
            elif k == key.ENTER:
                user_exited = True
                continue

            elif k != sentence[sentence_cursor]:
                total_characters += 1
                error = error + 1
                sentence_cursor += 1
                error_character = "" + k
                updated_sentence = (updated_sentence[:sentence_cursor - 1] + error_character)

            elif k == sentence[sentence_cursor]:
                total_characters += 1
                sentence_cursor += 1
                updated_sentence = updated_sentence + k
        except IndexError:
            print("Unable to execute function, please try again")

        compare_expected_input_against_user_input_highlight_differences(updated_sentence, sentence)

    print(elapsed_time, end="\r")
    result = calculate_results(elapsed_time, error, total_characters)
    write_result_to_csv(result[0], result[1], "scores.csv")


def calculate_results(elapsed_time, error, total_characters):
    wpm = str(round((((total_characters / 5) / elapsed_time) * 60), 2))
    try:
        accuracy = str(round((((total_characters - error) / total_characters) * 100), 2)) + "%"
        print("\nresults are:")
        print("\ntotal time taken: " + str(round(elapsed_time, 2)) + "s")
        print("\nwords per minute (WPM): " + wpm)
        print("\ntyping accuracy: " + accuracy)
        return wpm, accuracy
    except ZeroDivisionError:
        print("Error, need more than 0 characters to calculate results. ")


try:
    def write_result_to_csv(wpm, accuracy, file_path):
        with open(file_path, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([wpm, accuracy])
            file.flush()
        file.close()
except TypeError:
    print("Due to error in results being generated, score was not be added to scoreboard")


def compare_expected_input_against_user_input_highlight_differences(current_input, expected_input):
    print('\x1b[2K\r', end='\r')

    expected_words = current_input.split()
    actual_words = expected_input.split()

    for expected_word, actual_word in zip(expected_words, actual_words):
        if expected_word == actual_word:
            print(Fore.GREEN + expected_word, end=' ')
        else:
            print(Fore.RED + expected_word, end=' ')

    print(end='\r')
