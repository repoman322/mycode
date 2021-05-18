#!/usr/bin/env python3
""" A program that prints a menu of possible SAN networking commands, and then prompts the user for input. 
    The script then asks for an interface to perform the command on."""

print("Please select from the following commands:")
print("  Press 1 for symcfg list")
print("  Press 2 for symdev list -noprt -notinsg")
print("  Press 3 for symrdf list")
print("  Press 4 for symcfg list -v")
print("  Press 5 for symcfg discover")

selection = input("selection: ")
print(" your selection:")
if selection == "1":
    print("1 for symcfg list")
elif selection == "2":
    print("2 for symdev list -noprt -notinsg")
elif selection == "3":
    print("3 for symrdf list")
elif selection == "4":
    print("4 for symcfg list -v")
elif selection == "5":
    print("5 for symcfg discover")
else:
    print(" :-(  you made an invalid selection...")
