#!/usr/bin/python3
# check if a letter is lowercase
def islower(c):
    if ord(c) >= 97 and ord(c) <= 122:
        return True
    else:
        return False
