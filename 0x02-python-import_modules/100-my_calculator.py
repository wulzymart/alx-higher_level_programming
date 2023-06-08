#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv
    length = len(argv)
    if length != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    a = int(argv[1])
    b = int(argv[3])
    op = argv[2]
    calculator = {
        "+": add,
        "-": sub,
        "*": mul,
        "/": div
    }
    if op not in calculator.keys():
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    calc = calculator[op]
    print(f"{a} {op} {b} = {calc(a,b)}")
