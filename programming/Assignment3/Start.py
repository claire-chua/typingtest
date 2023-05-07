from Practice import practice_test
def start():
    test_type = input("Practice - 1 or Test - 2: \n ")
    if test_type == "1":
        practice_test()
    elif test_type =="2":
        test()
    else: 
        print("Invalid response. please ensure to enter a number a number that corresponds with your choice")

    



