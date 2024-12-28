# -*- coding: utf-8 -*-
"""
Created on Mon Dec 25 14:25:20 2023

@author: duman
"""

num1 = int(input())
num2 = int(input())


counter1 = 0
counter2 = 0

while(num1 != 1):
    if num1 % 2 == 0:
        num1 = num1 / 2
            
    else:
        num1 = (num1 *3) + 1
    counter1 += 1
    
    

while(num2 != 1):
    if num2 % 2 ==0:
        num2 = num2 / 2
            
    else:
        num2 = (num2 *3) + 1
    counter2 += 1    

print(counter1)
print(counter2)    