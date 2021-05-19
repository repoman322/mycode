#!/usr/bin/env python3
######## EXPLORE READ ##########
## create file object in "r"ead mode
configfile = open("vlanconfig.cfg", "r")

## display file to the screen - .read()
print(configfile.read())

## close file
configfile.close()

######## EXPLORE READLINES ##########
## re-create file object to explore new method
configfile = open("vlanconfig.cfg", "r")

## make a list of file lines - .readlines()
configlist = configfile.readlines()
print(configlist)

## Iterate through configlist
for x in configlist:
    #print(x, end="")  # readline includes the trailing line feed, so no need to have print() add line feed
    print(x.strip())  # readline includes the trailing line feed, so no need to have print() add line feed
## Always close your file
for x in configlist:
    #print(x, end="")  # readline includes the trailing line feed, so no need to have print() add line feed
    print(x.splitlines()) 
configfile.close()

