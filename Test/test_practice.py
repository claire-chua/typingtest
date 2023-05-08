# spy mocker
# matched word


def print_user_input_on_one_line(current_input, expected_input):
    print('\x1b[2K\r', end='\r')
    expected_words_total = ""
    actual_words_total = ""
    expected_words = current_input.split()
    actual_words = expected_input.split()

    for expected_word, actual_word in zip(expected_words, actual_words):
        if expected_word == actual_word:
            print(colored(expected_word, 'green'), end=' ')
            actual_words_total += expected_word
            return actual_words_total
        else:
            print(colored(expected_word, 'red'), end=' ')


def test_matched_words():
    output = print_user_input_on_one_line("i am tired", "i am very tired")
    assert output == ("i am tired")
