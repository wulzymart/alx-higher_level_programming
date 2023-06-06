#!/usr/bin/python3
import random
number = random.randint(-10, 10)
str
if number == 0:
    str = "{:d} is zero"
elif number < 0:
    str = "{:d} is negative"
else:
    str = "{:d} is positive"
print(str.format(number))
