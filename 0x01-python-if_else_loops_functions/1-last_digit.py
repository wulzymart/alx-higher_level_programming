#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
abs_number = number if number >= 0 else 0 - number
last_digit = abs_number % 10
last_digit = last_digit if number > 0 else last_digit * -1
str
if last_digit == 0:
    str = "Last digit of {:d} is {:d} and is 0"
elif last_digit < 6:
    str = "Last digit of {:d} is {:d} and is less than 6 and not 0"
else:
    str = "Last digit of {:d} is {:d} and is greater than 5"
print(str.format(number, last_digit))
