#!/usr/bin/env python3

round = 0

while True:

    round = round + 1
    print('Finish the movie title, "Monty Python\'s The Life of ______"')
    answer = input("Your guess--> ")
    if answer.lower() == 'brian':
        print("Correct")
        break
    elif round == 3:
        print("Sorry, the answer was Brian.")
        break
    elif answer.lower() == "shrubbery":
        print("Conratulations! You gave the super secret answer!")
        break
    else:
        print("Sorry! Try again!")
