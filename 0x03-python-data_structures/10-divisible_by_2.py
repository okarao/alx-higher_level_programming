#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    multiples = []
    for n in my_list:
        if my_list[n] % 2 == 0:
            multiples[n] = True
        else:
            multiples[n] = False
    return (multiples)
