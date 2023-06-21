#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    a = int(sys.argv[1])
    ops = sys.args[2]
    b = int(sys.argv[3])

    result = 0

    if ops == '+':
        result = add(a, b)
    elif ops =='-':
        result = sub(a, b)
    elif ops == '*':
        result = mul(a, b)
    elif ops == '/':
        result = div(a, b)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    print("{} {} {} = {}".format(a, ops, b, result))
