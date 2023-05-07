from readchar import readkey, key
from wonderwords import RandomSentence
from termcolor import colored

generate = RandomSentence()
sentence = generate.sentence().lower()


def practice_test():
    print(sentence)
    error = 0
    user_input = print("Please type the sentence shown above. \n")
    sentence_cursor = 0
    error_character = ""
    updated_sentence = ""

    while sentence_cursor < len(sentence):
        k = readkey()
        if (k == key.BACKSPACE):
            sentence_cursor -= 1
            updated_sentence = updated_sentence.rstrip(updated_sentence[-1])


        elif (k != sentence[sentence_cursor]):
            error = error + 1
            # print("error")
            sentence_cursor += 1
            error_character = "" + k
            # print("I've printed the error")
            updated_sentence = (updated_sentence[:sentence_cursor - 1] + error_character)
            # print(updated_sentence[:sentence_cursor] + '|', end='\r')
            # print('test3', end='\r')

        elif (k == sentence[sentence_cursor]):
            sentence_cursor += 1
            updated_sentence = updated_sentence + k
            # print(updated_sentence[:sentence_cursor] + '|', end='\r')
            # print('test5', end='\r')



        print(calculate_score)

        print_user_input_on_one_line(updated_sentence, sentence, sentence_cursor)
        # compare_strings(updated_sentence, sentence)



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
