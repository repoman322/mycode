#!/usr/bin/env python3
import sys

def main():
    args = sys.argv
    print("Username: " + args[1])
    print("Password: " + args[2])
    print("IP Address: " + args[3])
    print("Gateway: " + args[4])
    print("Oh by the way, your script is named:", args[0])

if __name__ == "__main__":
    main()
