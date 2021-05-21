#!/usr/bin/env python3
"""
Author:  keg
program to cheat at dice
"""
# import specific Classes from 'cheatdice'      
from cheatdice import Player
from cheatdice import Cheat_Swapper
from cheatdice import Cheat_Loaded_Dice

def main():
    """ main program """
    # create Cheat_Swapper object
    cheater1 = Cheat_Swapper()
    # create Cheat_Loaded_Dice object
    cheater2 = Cheat_Loaded_Dice()
    
    # dice roll for each player object
    cheater1.roll()
    cheater2.roll()
    # run specific cheat for player
    cheater1.cheat()
    cheater2.cheat()
    
    print(f"Cheater 1 rolled {cheater1.get_dice()}")
    print(f"Cheater 2 rolled {cheater2.get_dice()}")
    
    # evaluate winner
    if sum(cheater1.get_dice()) == sum(cheater2.get_dice()):
        print("Draw!")
    
    elif sum(cheater1.get_dice()) > sum(cheater2.get_dice()):
        print("Cheater 1 wins!")
    
    else:
        print("Cheater 2 wins!")

# if script run directly, run main()
if __name__ == "__main__": 
    main()
