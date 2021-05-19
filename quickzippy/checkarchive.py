#!/usr/bin/env python3
import os
import zipfile

iszip = input("What file would you like to check? ")
zipfileobj = zipfile.is_zipfile(iszip)
if zipfileobj is True:
    print(f"File {iszip} is a valid .zip file")
if zipfile.is_zipfile(iszip) is True:
    print(f"File {iszip} is also a valid .zip file")
