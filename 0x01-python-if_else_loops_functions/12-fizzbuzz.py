#!/usr/bin/python3
def fizzbuzz():
    for _ in range(1, 101):
        if _ % 15 == 0:
            print("FizzBuzz", end="")
        elif _ % 5 == 0:
            print("Buzz", end="")
        elif _ % 3 == 0:
            print("Fizz", end="")
        else:
            print(_, end="")
        if _ == 100:
            print("")
        else:
            print(" ", end="")
