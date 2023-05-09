from Practice import *


# test if results are accurately calculated
# testcase_1: passes in elapsed_time = 60 seconds, error = 5 and total characters = 30
def test_should_calculate_words_per_minute_and_accuracy():
    result = calculate_results(60, 5, 30)
    assert result == ("6.0", "83.33%")


# testcase_1: passes in elapsed_time = 60 seconds, error = 0 and total characters = 0
def test_should_return_none_when_no_characters_typed():
    result = calculate_results(60, 0, 0)
    assert result is None


# check if test results are being saved
# testcase_1: WPM = 10, accuracy = 100%
def test_should_write_test_results_to_csv():
    clear_test_csv()

    write_result_to_csv("10", "100%", "test_scores.csv")

    with open("test_scores.csv", 'r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            assert row == ['10', '100%']


# check if words are printed with the correct colour
def test_should_print_differences_between_expected_input_and_actual_input(capsys):
    compare_expected_input_against_user_input_highlight_differences("this is mostly corrext",
                                                                    "this is mostly correct")

    output, err = capsys.readouterr()
    output_words = output.split(' ')

    # the second two words should be green text, because they match the expected input
    assert output_words[1] == "\x1b[32mis"
    assert output_words[2] == "\x1b[32mmostly"
    # the last word will be red because it does not match the expected input
    assert output_words[3] == "\x1b[31mcorrext"


# clear csv file to ensure no additional errors when pytest checks if assertion is true.
def clear_test_csv():
    f = open("test_scores.csv", "w")
    f.truncate()
    f.close()
