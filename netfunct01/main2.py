#!/usr/bin/env python3
# netfunct02/main.py
"""Alta3 Research || Author: RZFeeser@alta3.com"""
import crayons

# function to push commands
def commandpush(devicecmd): # devicecmd==list
    for coffeetime in devicecmd.keys():
        print('Handshaking. .. ... connecting with ' + crayons.red(coffeetime))
        # we'll learn to write code that connects to devices here
        for mycmds in devicecmd[coffeetime]:
            print('Attempting to sending command --> ' + crayons.green(mycmds, bold=True))
            # we'll learn to write code that sends cmds to device here
            
def devicereboot(iplist): # list of IPs to reboot
    for device in iplist:
        print('Connecting to ' + crayons.red(device,bold=True) + crayons.blue(' REBOOTING NOW'))
        print(f'Connecting to {crayons.blue(device,bold=True)} {crayons.red(" REBOOTING NOW!!!")}')
        # we'll learn to write code that connects to devices here

# start our main script
def main():
    work2do = {"10.1.0.1":["interface eth1/2", "no shutdown"], "10.2.0.1":
    ["interface eth1/1", "shutdown"], "10.3.0.1":["interface eth1/5", "no shutdown"]} 
    # data that replaces data stored in file

    print("Welcome to the network device command pusher") # welcome message

    ## get data set
    print("\nData set found\n") # replace with function call that reads in data from file

    ## run
    commandpush(work2do) # call function to push commands to devices
    devicereboot(work2do.keys())  # call the reboot function

# call our main function
main()
