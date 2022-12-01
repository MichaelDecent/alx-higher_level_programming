#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    lent = len(argv)
    if lent == 1:
        print("{}".format(lent - 1))
    else:
        i = 1
        result = 0
        while i < lent:
            result += int(argv[i])
            i += 1
        print("{}".format(result))
