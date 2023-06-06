#!/usr/bin/python3
for _ in range(100):
    if _ < 99:
        print("{:02d}".format(_), end=", ")
    else:
        print("{:02d}".format(_))
