from readchar import readkey, key
from wonderwords import RandomSentence
from colour import Color

generate = RandomSentence()
sentence = generate.sentence().lower()

#standard_colour = Color("white")
#error_colour = Color("red")

def practice_test():
    print(sentence)
    error = 0
    user_input = print("Please type the sentence shown above. \n")
    sentence_cursor = 0
    error_character =""
    while True:
        k = readkey()

        if k == key.BACKSPACE:
            sentence_cursor -= 1
            print(sentence[:sentence_cursor] + '|' + sentence[sentence_cursor:])
        elif k != sentence[sentence_cursor]:
            error = error + 1
            print("error")
            sentence_cursor += 1
            error_character = "" + k
            print("I've printed the error")
            updated_sentence = (sentence[:sentence_cursor - 1] + error_character + sentence[sentence_cursor:])
            print(updated_sentence[:sentence_cursor] + '|' + updated_sentence[sentence_cursor:])
        elif k == sentence[sentence_cursor]:


            sentence_cursor += 1
            print(sentence[:sentence_cursor] + '|' + sentence[sentence_cursor:])


    #if error, replace letter with error character, add colour
    #if correct, change colour
    #print to the same line
    #fix git repository
        

    




