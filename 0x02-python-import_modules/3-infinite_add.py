#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv
    argv_len = len(argv)
    total = 0
    for i in range(argv_len - 1):
        total = total + int(argv[i + 1])
    print(total)
