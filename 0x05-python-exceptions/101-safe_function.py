#!/usr/bin/python3
def safe_function(fct, *args):
    try:
        result = fct(args[0], args[1])
    except ZeroDivisionError as err:
        print("Exception: {}".format(err))
        result = None
    except IndexError as err1:
        print("Exception: {}".format(err1))
        result = None

    return (result)

