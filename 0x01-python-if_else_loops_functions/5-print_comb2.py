#!/usr/bin/python3
# print number 0 to 99 seperated by comma
for num in range(0, 100):
    if num == 99:
        print("{}".format(num))
    else:
        print("{:02}".format(num), end=", ")
