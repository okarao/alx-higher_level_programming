#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    argSum = 0
    for i in range(len(sys.argv) - 1):
        argSum += int(sys.argv[i + 1])
    print("{}".format(argSum))
