#!/usr/bin/python3

n = 0
for ch in range(ord('z'), ord('a') - 1, -1):
    print("{}".format(chr(ch - n)), end="")
    n = 32 if n == 0 else 0


