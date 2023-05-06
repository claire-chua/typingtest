from readchar import readkey, key
from wonderwords import RandomSentence
from colour import Color

generate = RandomSentence()
sentence = generate.sentence().lower()

# sentence = generate.sentence()

#standard_colour = Color("white")
#error_colour = Color("red")

# def slice_sentence(string, start, end):
#     return string[start:end]

def practice_test():
    print(sentence)
    error = 0
    user_input = print("Please type the sentence shown above. \n")
    sentence_cursor = 0

    #print (sentence[:sentence_cursor+1] + '|' + sentence[sentence_cursor+1:])

    while True:
        # k = readkey()
        # if k == "a":
        #     print("hi")
        # if k == key.DOWN:
        #     print("hi")
        # if k == key.ENTER:
        #     break
        k = readkey()

        if k == key.BACKSPACE:
            sentence_cursor -= 1
            print("you're trying to backspace")
        elif k != sentence[sentence_cursor]:
            error = error + 1
            print("error")
            sentence_cursor += 1
        elif k == sentence[sentence_cursor]:
            sentence_cursor += 1

        print (sentence[:sentence_cursor] + '|' + sentence[sentence_cursor:])

    

        

        # print (slice_sentence(sentence, sentence_cursor, len(sentence)))

        # for i in range(sentence_cursor, len(sentence)):
        #     print sentence[i:i+3]

        

            #character.error_colour
        # elif keyboard.is_pressed("enter"):
        #     print('Key pressed')
        #     break
        # else:
        #     none
        #         #character.standard_colour
    




