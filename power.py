# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 00:05:53 2024

@author: duman
"""

def fak(a,b):
    
    if b==0:
        return 1
    
    else:
        return a * fak(a, b-1)
    
    
    
    
a = 4
b= 4

print(fak(a,b))