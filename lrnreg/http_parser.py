#!/usr/bin/env python3
import urllib.request
import re

def main():
    """ use this to search the entered inputs """
    
    while True:
        # ask user for web site
        print("where should we search? type 'q' to quit ")
        url = input()  # get URL 
        if url.lower() == 'q':
            break

        print(f"Great! So we'll try to open this url {str(url)}  to search for the phrase:")
        searchFor = input()
        searchMe = urllib.request.urlopen(url).read().decode("utf-8")
        if re.search(searchFor, searchMe):
            print("Found a match!")
        else:
            print("No match!")
        cnt = len(re.findall(searchFor, searchMe))
        print(f"I counted {cnt} matches in URL {url}")
        
        mylist = searchFor.split() 
        cust3 = urllib.request.urlopen(url).readlines()
        print(len(cust3))
        lines = 0
        mylist = searchFor.split()
        for line in cust3[0:5]:
            #print(type(line))
            each = 0
            #print(f'each is {each},len is {len(mylist)} and line is {line}')
            for word in mylist:
                #print(f'  looking for word: {word}')
                if re.search(word, str(line)):
                    each += 1
            #print(f'each is {each},len is {len(mylist)} and line is {line}')
            if each == len(mylist):
                lines += 1

        print(f"total number of lines with all words is {lines}")

main()
