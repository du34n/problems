# -*- coding: utf-8 -*-
"""
Created on Fri Jan  5 15:28:46 2024

@author: duman
"""

#perfect_number

def perfect_num(num):
    a = 0
    for i in range(1,num):
        if(num % i == 0):
            a +=i
    
    return a == num 
            
        

for i in range(1,1001):
    if(perfect_num(i)):
        print('mükemmel sayı: ',i)