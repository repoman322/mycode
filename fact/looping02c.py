#!/usr/bin/env python3

# open file in read mode
with open("dnsservers.txt", "r") as dnsfile: # this will read each line in the file, one at a time
    # no need to save this as a list unless you need it:
    # indent to keep the dnsfile object open
    # loop across the lines in the file
    for svr in dnsfile:
        #print and end without a newline
        print(svr, end="")
# no need to close our file - closed automatically

