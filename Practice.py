from readchar import readkey, key
from wonderwords import RandomSentence
from colour import Color

generate = RandomSentence()
sentence = generate.sentence().lower()


# standard_colour = Color("white")
# error_colour = Color("red")


def practice_test():
    print(sentence)
    error = 0
    user_input = print("Please type the sentence shown above. \n")
    sentence_cursor = 0
    error_character = ""
    updated_sentence = ""

    while True:
        k = readkey()
        if k == key.BACKSPACE:
            sentence_cursor -= 1
            updated_sentence = updated_sentence.rstrip(updated_sentence[-1])
            # print('test2', end='\r')

        elif k != sentence[sentence_cursor]:
            error = error + 1
            # print("error")
            sentence_cursor += 1
            error_character = "" + k
            # print("I've printed the error")
            updated_sentence = (updated_sentence[:sentence_cursor - 1] + error_character)
            # print(updated_sentence[:sentence_cursor] + '|', end='\r')
            # print('test3', end='\r')

        elif k == sentence[sentence_cursor]:
            sentence_cursor += 1
            updated_sentence = updated_sentence + k
            # print(updated_sentence[:sentence_cursor] + '|', end='\r')
            # print('test5', end='\r')

        print_user_input_on_one_line(updated_sentence, sentence_cursor)


def print_user_input_on_one_line(current_input, cursor):
    print('\x1b[2K\r', end='\r')
    print(current_input[:cursor] + '|', end='\r')

    # if error, replace letter with error character, add colour
    # if correct, change colour
    # print to the same line
    # fix git repository
