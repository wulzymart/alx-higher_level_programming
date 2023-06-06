#!/usr/bin/python3
for _ in range(100):
    if _ < 99:
        print(f"{_:02d}", end=", ")
    else:
        print(f"{_:02d}")
