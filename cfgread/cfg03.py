#!/usr/bin/env python3
## create file object in "r"ead mode
cnt = 0
file = input("Enter the file name: ")
with open(file, "r") as configfile:
    #with open("vlanconfig.cfg", "r") as configfile:
    ## readlines() creates a list by reading target
    ## file line by line
    configlist = configfile.readlines()

## file was just auto closed (no more indenting)
for line in configlist:
    cnt += 1
## each item of the list now has the "\n" characters back
print(configlist)
print(f"I counted {cnt} lines")
for line in configlist:
    print(line.strip())
