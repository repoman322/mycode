#!/usr/bin/env python3
import netifaces
   
print(netifaces.interfaces())

## returns just the IP address when passed an adapter name.
def getip(adaptorname):
   print(f"IP for {adaptorname} is: {(netifaces.ifaddresses(adaptorname)[netifaces.AF_INET])[0]['addr']}") 

## returns just the MAC address when passed an adapter name.
def getmac(adaptorname):
    print(f"MAC Address for {adaptorname} is: {(netifaces.ifaddresses(adaptorname)[netifaces.AF_LINK])[0]['addr']}")    
for i in netifaces.interfaces():
    print('\n****** details of interface - ' + i + ' ******')
    try:
        print('MAC: ', end='') # This print statement will always print MAC without an end of line
        print((netifaces.ifaddresses(i)[netifaces.AF_LINK])[0]['addr']) # Prints the MAC address
        print('IP: ', end='')  # This print statement will always print IP without an end of line
        print((netifaces.ifaddresses(i)[netifaces.AF_INET])[0]['addr']) # Prints the IP address
    except:          # This is a new line
        print('Could not collect adapter information') # Print an error message
        
getip('ens3') 
getmac('lo')
