https://leetcode.com/problems/roman-to-integer/

class Solution:
    def romanToInt(self, s: str) -> int:
        roman_dict = {'I': 1, 'V':5,'X':10,'L':50, 'C':100,'D':500,'M':1000, '':0}
        
        int_value = 0
        prev_roman_char = ''
        for roman_char in s[::-1]:
            if roman_dict.get(prev_roman_char) <= roman_dict.get(roman_char):
                int_value = int_value+ roman_dict.get(roman_char)
            else:
                int_value = int_value - roman_dict.get(roman_char)
            prev_roman_char = roman_char
        return int_value
    
    def romanToInt_best(self, s: str) -> int:
        roman_to_integer = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }
        s = s.replace("IV", "IIII").replace("IX", "VIIII").replace("XL",                        "XXXX").replace("XC", "LXXXX").replace("CD", "CCCC").replace("CM", "DCCCC")
        return sum(map(lambda x: roman_to_integer[x], s))
            