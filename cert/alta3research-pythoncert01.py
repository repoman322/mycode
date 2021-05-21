#!/usr/bin/env python3
"""
Author: Kurt Eggert
Script to search for words in text pulled from web
"""
import urllib.request
import re

def main():
    """ use this to search the entered inputs """
    # loop through until user is finished
    while True:
        # ask user for web site  http://www.gutenberg.org/files/98/98-0.txt
        print("where should we search? type 'q' to quit ")
        url = input()  # get URL
        if url.lower() == 'q':
            break

        print(f"Great! So we'll try to open this url {str(url)}\n")
        print("Enter the words to search for with a space in between (in any order): ")
        searchfor = input()
       
        # pull requested web data in file line by line parsing
        cust3 = urllib.request.urlopen(url).readlines()
        # print to screen quick explanation of what the program is doing
        print(f"Searching {len(cust3)} lines for all of these words '{searchfor}'")
        lines = 0 # track the number of lines the words are found in, start with 0
        # make a list of words to serach for
        mylist = searchfor.split()
        for line in cust3: # when printing, only print these by changing: cust3 to cust3[0:15]:
            #print(type(line))
            each = 0  # track the number of words are found in the line, start with 0
            #print(f'each is {each},len is {len(mylist)} and line is {line}')
            for word in mylist:
                if re.search(word, str(line)):
                    each += 1
            if each == len(mylist):
                lines += 1

        print(f"total number of lines with all words is {lines}")

main()
