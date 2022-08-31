#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or type(roman_string) != str:
        return 0
    values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    arabic = 0
    for j in range(len(roman_string)):
        if j > 0 and values[roman_string[j]] > values[roman_string[j - 1]]:
            arabic += values[roman_string[j]] - 2 * \
                        values[roman_string[j - 1]]
            continue
        arabic += values[roman_string[j]]
    return arabic
