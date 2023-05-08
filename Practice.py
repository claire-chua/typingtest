import time, csv
from readchar import readkey, key
from wonderwords import RandomSentence
from termcolor import colored

generate = RandomSentence()
sentence = generate.sentence().lower()


def timed_test():
    print(sentence)
    global error
    error = 0
    print("Please type the sentence shown above. The timer will begin once you press a key. Press 'enter' to submit. \n")
    sentence_cursor = 0
    updated_sentence = ""
    elapsed_time = 0
    start_time = 0
    timer_started = False
    user_exited = False
    global total_characters
    total_characters = 0

#sentence_cursor < len(sentence))
    while (user_exited is not True):
        k = readkey()
        if not timer_started:
            start_time = time.time()
            timer_started = True

        current_time = time.time()
        elapsed_time = current_time - start_time
        if k == key.BACKSPACE:
            sentence_cursor -= 1
            updated_sentence = updated_sentence.rstrip(updated_sentence[-1])
        elif k == key.ENTER:
            user_exited = True
            continue
        elif k != sentence[sentence_cursor]:
            total_characters += 1
            error = error + 1
            # print("error")
            sentence_cursor += 1
            error_character = "" + k
            # print("I've printed the error")
            updated_sentence = (updated_sentence[:sentence_cursor - 1] + error_character)
            # print(updated_sentence[:sentence_cursor] + '|', end='\r')
            # print('test3', end='\r')
        elif k == sentence[sentence_cursor]:
            total_characters += 1
            sentence_cursor += 1
            updated_sentence = updated_sentence + k
            # print(updated_sentence[:sentence_cursor] + '|', end='\r')
            # print('test5', end='\r')
        # get time module
        # create accuracy + wpm
        # save input for file handling
        total_character_count = total_characters
        print_user_input_on_one_line(updated_sentence, sentence, sentence_cursor)
        # compare_strings(updated_sentence, sentence)

    # print(elapsed_time, end ="\r")
    calculate_results(elapsed_time)

def calculate_results(elapsed_time):
    # calculate WPM
    # calculate accuracy
    # global WPM
    # global accuracy
    WPM = (((total_characters/5)/elapsed_time)*60)
    accuracy = (((total_characters - error)/ total_characters)* 100)
    print("\nresults are:")
    print("\ntotal time taken: " + str(elapsed_time))
    print("\nwords per minute (WPM): " + str(((total_characters/5)/elapsed_time)*60))
    print("\ntyping accuracy: " + str(((total_characters - error)/ total_characters)* 100) + "%")

    with open("scores.csv", 'a', newline = '') as file:
        writer = csv.writer(file)
        writer.writerow([WPM,accuracy])

def print_user_input_on_one_line(current_input, expected_input, cursor):
    print('\x1b[2K\r', end='\r')



    # index = 0
    # for character in current_input:
    #     if(character == expected_input[0]):
    #         cprint(character, "green", "on_red", end='\r')
    #         index+=1

    # print(current_input[:cursor] + '|', end='\r')

    # if error, replace letter with error character, add colour
    # if correct, change colour
    # print to the same line
    # fix git repository

    expected_words = current_input.split()
    actual_words = expected_input.split()

    for expected_word, actual_word in zip(expected_words, actual_words):
        if expected_word == actual_word:
            print(colored(expected_word, 'green'), end=' ')

        else:
            print(colored(expected_word, 'red'), end=' ')

    print(end='\r')
