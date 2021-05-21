#!/usr/bin/env python3
"""
Author: Kurt Eggert
Script to search for words in text pulled from web
"""
import argparse
import socket
from datetime import datetime

def server(port, t):
    x = f"Your choice was server and it will run on port {port} using {t}" 
    return x

def client(port, t):
    x = f"Your choice was client and it will run on port {port} using {t}" 
    return x

if __name__ == '__main__':
    choices = {'client': client, 'server': server}
    parser = argparse.ArgumentParser(description='Send and receive UDP locally')
    parser.add_argument('role', choices=choices, help='which role to play')
    parser.add_argument('-p', metavar='PORT', type=int, default=1060,
                        help='UDP port (default 1060)')
    parser.add_argument('-t', default='UDP', help='UDP used by default')
args = parser.parse_args()
function = choices[args.role]
print(function(args.p,args.t))
