def happy_number(happy):
    happy = input("Please enter a number to see if it is happy or sad: ")
    for number in range(len(happy)):
        if int(happy) ** 2 == 1:
            print("This is a happy number.")

        else:
            print("This is a sad number")


number_happy = happy_number("")