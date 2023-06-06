#!/usr/bin/python3
def uppercase(str):
    for _ in str:
        value = ord(_)
        value = value - 32 if value in range(97, 123) else value
        print(chr(value), end="")
    print("")
