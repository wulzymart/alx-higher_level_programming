#!/usr/bin/python3
for _ in range(122, 96, -1):
    _ = _ if _ % 2 == 0 else _ - 32
    print("{}".format(chr(_)), end='')
