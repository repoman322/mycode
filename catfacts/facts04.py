#!/usr/bin/env python3
"""Alta3 Research | Author: RZFeeser@alta3.com"""

# imports always go at the top of your code
import requests

def main():
    """Run time code"""
    ## create r, which is our request object
    r = requests.get('http://api.open-notify.org/astros.json')
    print("People who have been in space: ")
    ## catfact is our iterable -- that just means it will take on the values found within
    ## r.json()["all"], one after the next-- which happens to be a dictionary
    ## the code within the loop, says, "from that single dictionary
    ## print the value associated with text"
    space = r.json()
    for each in space.get("people"):
        print(each.get("name"))  # the .get() method returns NONE if key not found

    stock = requests.get('https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=demo')
    print(stock.json().get('Meta Data'))
    #print(stock.json())
    print("\n")
    poke = requests.get("https://pokeapi.co/api/v2/pokemon/pikachu")
    pokedata = poke.json()
    #print(poke.url)
    print(type(pokedata))
    print(f"Keys are: {pokedata.keys()}\n")
    print(f"Abilities: {pokedata.get('abilities')}\n")
    games = pokedata.get('abilities')
    print("Pikachu can use these abilities: ")
    for game in games:
        #print(type(game))
        #print(f"game is: {game}")
        print(game.get('ability').get('name'))
main()

