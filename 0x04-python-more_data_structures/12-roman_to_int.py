#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string == None or type(roman_string) != str:
        return 0
    rom_dic = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    string_rev = reversed(roman_string)
    integer_sum = 0
    for letter in string_rev:
        digit = rom_dic[letter]
        integer_sum += digit if integer_sum < digit * 5 else -digit
    return (integer_sum)

