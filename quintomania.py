# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 09:44:14 2024

@author: duman
"""


test = int(input())

for _ in range(test):
    melody_count = int(input())
    a = list(map(int, input().split(' ')))
    count = 1
    for i in range(melody_count-1):
        if(a[i] - a[i+1] in [-5,-7,5,7]):
            count +=1
        else:
            pass
    if (count == melody_count):
        print("YES")
    else:
        print("NO")
