# -*- coding: utf-8 -*-
"""
Created on Tue Jan  9 09:52:05 2024

@author: duman
"""

def bubble_sort(lst):
    n =len(lst)
    for i in range(len(lst)):
        for j in range(0,n-i-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst
    
    
    
lst = [3,2,1,7,0]

print(bubble_sort(lst))