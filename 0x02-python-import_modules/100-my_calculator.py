#!/usr/bin/python3
if (__name__ == "__main__"):
    from calculator_1 import add, sub, mul, div
    import sys
    arg = sys.argv
    noArg = len(arg)
    operators = ["+", "-", "*", "/"]

    if (noArg != 4):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    elif (arg[2] not in operators):
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    else:
        operations = arg[2]
        a = int(arg[1])
        b = int(arg[3])

        if (operations == "+"):
            print("{} {} {} = {}".format(a, operations, b, add(a, b)))
        elif (operations == "-"):
            print("{} {} {} = {}".format(a, operations, b, sub(a, b)))
        elif (operations == "*"):
            print("{} {} {} = {}".format(a, operations, b, mul(a, b)))
        else:
            print("{} {} {} = {}".format(a, operations, b, div(a, b)))
            sys.exit(1)

