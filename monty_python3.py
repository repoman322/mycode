#!/usr/bin/env python3
rnd = 0           # integer round initiated to 0

answer = " "

while rnd < 3 and answer != "Brian" and answer != "Shrubbery":
# sets up an infinite loop condition
    rnd = rnd + 1     # increase the round counter
    print('Finish the movie title, "Monty Python\'s The Life of ______"')
    answer = input("Your guess--> ")    # string ans collected from user
    answer = answer.capitalize()
    if answer == 'Brian': # logic to check if user gave correct answer
        print('Correct!')
    elif round == 3:    # logic to ensure round has not yet reached 3
        print('Sorry, the answer was Brian.')
    elif answer.lower() == "shrubbery":
        print("Conratulations! You gave the super secret answer!")
    else:
        print('Sorry. Try again!')

