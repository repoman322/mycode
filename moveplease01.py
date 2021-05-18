#!/usr/bin/env python3
""" A simple script to demonstrate file moving """

import shutil
import os

def main():
    os.chdir('/home/student/mycode/') # move into working directory
    # move the file or folder at the path source to the path destination and will return a string of the absolute path of the new location.
    shutil.move('raynor.obj', 'ceph_storage/')  
    # If there had been a raynor.obj file already in the destination folder ~/home/student/mycode/ceph_storage/, it would have been overwritten.
    # The following line will rename a file
    xname = input('What is the new name for kerrigan.obj? ')
    shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname) # copy kerrigan.org file to new location 
                                                                      # and new file name

main() # call the main function
