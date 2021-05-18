#!/usr/bin/env python3
""" check entered hostname aginst expected value """

## collect input from user
hostname = input("What value should we set for hostname? ")

## use the str.lower() method to return a lowercase string
if hostname.lower() == "mtg":
    print("The hostname was found to be mtg")
    print(" hostname matches expected config")

# always print this before exiting
print(" Exiting the script...")
