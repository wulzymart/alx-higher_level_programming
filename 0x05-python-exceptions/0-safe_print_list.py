#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    if my_list:
        try:
            i = 0
            for _ in range(x):
                print("{}".format(my_list[_]), end='')
                i += 1
        except Exception as exception:
            pass
        print("")
        return i
    return 0
