# -*- coding: utf-8 -*-
"""
Created on Mon Jan  1 16:55:48 2024

@author: duman
"""

def roman_to_integer(roman):
    counter = 0
    for i in roman:
        if i == 'I':
            counter +=1 
        elif i == 'V':
            counter += 5
        elif i == 'X':
            counter +=10
        elif i == 'L':
            counter += 50
        elif i == 'C':
            counter += 50
        elif i == 'D':
            counter += 500
        else:
            counter += 1000
            
    return counter

roman = input()            
            
print(roman_to_integer(roman))