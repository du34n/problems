# -*- coding: utf-8 -*-
"""
Created on Tue Jan  9 10:19:38 2024

@author: duman
"""



def sum_int(num):
    
    toplam = 0
    for i in str(num):
        toplam += int(i)
    
    if(toplam % 2 == 0):
        return toplam
    else:
        return sum_int(toplam)
    
    
    
num = input()

print(sum_int(num))