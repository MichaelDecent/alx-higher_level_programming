#!/usr/usr/python3

def roman_to_int(roman_string):
    if type(roman_string) != str or not roman_string:
        return 0

    result = 0
    roman_dict = dict(M=1000, D=500, L=50, V=5, C=100, X=10, I=1)
    for roman in reversed(roman_string):
        num = roman_dict[roman]
        result += num if result < num * 5 else -num

    return result
