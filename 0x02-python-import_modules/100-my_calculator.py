#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv, exit
    from calculator_1 import add, sub, mul, div

    argv_len = len(argv)
    ops_func = {'+': add, '-': sub, '*': mul, '/': div}

    if argv_len != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    if argv[2] not in list(ops_func.keys()):
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    a = int(argv[1])
    b = int(argv[3])
    print(f"{a} {argv[2]} {b} = {ops_func[argv[2]](a, b)}")
