#!/usr/bin/python3
from sys import argv
lent = len(argv)
if lent == 1:
    print("{} arguments.".format(lent - 1))
elif lent == 2:
    print("{} argument:".format(lent - 1))
    print("{}: {}".format(lent - 1, argv[1]))
else:
    print("{} arguments:".format(lent - 1))
    i = 1
    while i < lent: 
        print("{}: {}".format(i, argv[i]))
        i += 1
