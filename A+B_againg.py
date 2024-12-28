# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 12:34:37 2024

@author: duman
"""

def solve():
    num1 = input()
    add =0
    for i in num1:
        add += int(i)
    
    print(add)
    

num = int(input())

for _ in range(num):
    solve()