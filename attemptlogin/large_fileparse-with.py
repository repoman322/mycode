#!/usr/bin/python3
# large_fileparse-with.py
# parse keystone.common.wsgi and return number of failed login attempts
""" Create the following script. When you open using with, you must indent, however, when you stop indenting, your file is auto-closed! 
This helps prevent forgetting to close your file. """
loginfail = 0 # counter for fails
loginpass = 0 # counter for success

# open the file for reading
with open("/home/student/mycode/attemptlogin/keystone.common.wsgi") as kfile:

    # loop over the file
    for line in kfile:
        # if this 'fail pattern' appears in the line...
        if "- - - - -] Authorization failed" in line:
            # test to determine type to know what to use next... print(line, type(line))
            # capture the IP from the end of the failure line
            login = line.split()
            print(f"failed login attempt from IP: {login[-1]}")
            loginfail += 1 # this is the same as loginfail = loginfail + 1
        elif "-] Authorization failed" in line:
            loginpass += 1 # this is the same as loginpass = loginpass + 1

print("The number of failed log in attempts is", loginfail)
print("The number of successeful log in attempts is", loginpass)
