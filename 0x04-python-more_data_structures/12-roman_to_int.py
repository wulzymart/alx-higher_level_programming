#!/usr/bin/python3
def roman_to_int(roman_string):
    num = 0
    r_num = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
    if isinstance(roman_string, str):
        rev = roman_string[::-1]

        for i, c in enumerate(rev):
            if c not in r_num:
                return 0
            val = r_num[c]
            prev = r_num[rev[0]] if i == 0 else r_num[rev[i - 1]]
            num = num + val if val >= prev else num - val
    return num
