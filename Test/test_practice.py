import Practice
from Practice import print_user_input_on_one_line


# def print_user_input_on_one_line(current_input, expected_input):
#     print('\x1b[2K\r', end='\r')
#
#     expected_words = current_input.split()
#     actual_words = expected_input.split()
#
#     for expected_word, actual_word in zip(expected_words, actual_words):
#         if expected_word == actual_word:
#             print(colored(expected_word, 'green'), end=' ')
#
#         else:
#             print(colored(expected_word, 'red'), end=' ')


def test_matched_words():
    output = print_user_input_on_one_line("i am very tired", "i am tired")
    # assert output == colored("i am", 'green') + " " + colored("very", 'red') + " " + colored("tired", 'green')

    # spy on print
    # or spy on practise
    # expect calling print on one line with particular params

    # run timed_test function
    # verify other functions in class are called with expected params

    # mock RandomSentence(), so that the sentences are expected
    # mock readkey so input can be specified

    Practice.timed_test()

    assert output is None
