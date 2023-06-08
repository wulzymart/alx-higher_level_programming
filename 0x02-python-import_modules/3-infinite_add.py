#!/usr/bin/python3
from sys import argv
sum = 0
for i, _ in enumerate(argv):
    if i != 0:
        sum += int(_)
print(sum)
