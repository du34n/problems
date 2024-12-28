# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 10:26:54 2024

@author: duman
"""


def solve():
    n, s, m = map(int, input().split())

    i1 = list(map(int,input().split()))
    i2 = list(map(int,input().split()))
    i3 = list(map(int,input().split()))
    if(i1[0]-0>=s or i2[0]-i1[1]>=s or i3[0]- i2[1]>=s or m-i3[1] >=s):
        print("yes")
    else:
        print("no")
        
    
            
num = int(input())
for _ in range(num):
    solve()
    
    
    """
    gives an error test2 im gonna do more complex
    
    """