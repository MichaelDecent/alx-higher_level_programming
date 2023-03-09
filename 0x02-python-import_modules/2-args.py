#!/usr/bin/python3
if __name__ == "__main__":

    from sys import argv

    argv_len = len(argv)

    if (argv_len == 1):
        print(f"{argv_len - 1} arguments.")

    elif (argv_len == 2):
        print(f"{argv_len - 1} argument:")
        print(f"{argv_len - 1}: {argv[argv_len - 1]}")
    else:
        print(f"{argv_len - 1} arguments:")
        for i in range(argv_len - 1):
            print(f"{i + 1}: {argv[i + 1]}")
