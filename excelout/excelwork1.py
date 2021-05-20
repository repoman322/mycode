#!/usr/bin/env python3

## sudo apt install python3-pip

## python3 -m pip install pyexcel
## python3 -m pip install pyexcel-xls
import pyexcel

# set up columns needed
def get_columns():
    columns = []
    cols = int(input("How many columns would you like to create? "))
    for x in range(cols):
        name = input(f"\nEnter the name of column {x}: ")
        columns.append(name.strip())
    return columns

# Request data from user
def get_ip_data(column):
    dets = {}
    for x in column:
        input_1 = input(f"\nEnter {x}: ")
        dets.update({x : input_1})
    print(dets)
    return dets

column = get_columns()

data = []
#more = True
while True:
    data.append(get_ip_data(column))
    yn = input("Add another row? (y/n) ")
    if yn.lower() == "n":
    #if 'y' not in yn:
        #more = False
        break
        
print(data)
