#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for _ in range(len(matrix)):
        length = len(matrix[_])
        index = 0
        for i in matrix[_]:
            ending = " " if index != length - 1 else ""
            print("{:d}{}".format(i, ending), end="")
            index += 1
        print("")
