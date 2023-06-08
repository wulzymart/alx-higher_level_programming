#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    length = len(argv)
    if length > 1:
        str = "arguments" if length > 2 else "argument"
        print(f"{length - 1} {str}:")
        for i, arg in enumerate(argv):
            if i > 0:
                print(f"{i}: {arg}")
    else:
        print("0 arguments.")
