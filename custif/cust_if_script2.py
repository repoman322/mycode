#!/usr/bin/env python3
""" A program that prints a menu of possible SAN networking commands, and then prompts the user for input. 
    The script then asks for an interface to perform the command on."""

menu = ["symcfg list", "symdev list -noprt -notinsg", "symrdf list", "symcfg list -v", "symcfg discover"]

print("Please select from the following commands:")
for x in range(5):
  print(" Press", x, "for", menu[x])

selection = "0"
while selection not in range(5):
    selection = input("selection: ")
    print(" your selection: ", end='')
    if selection == "1":
        print("1 for symcfg list")
        break
    elif selection == "2":
        print("2 for symdev list -noprt -notinsg")
        break
    elif selection == "3":
        print("3 for symrdf list")
        break
    elif selection == "4":
        print("4 for symcfg list -v")
        break
    elif selection == "5":
        print("5 for symcfg discover")
        break
    else:
        print(" :-(  you made an invalid selection...")
    
