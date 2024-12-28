# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 20:13:27 2024

@author: duman
"""


num = int(input())
for _ in range(0,num):
    a = input().split(' ')
    n = int(a[0])
    m= int(a[1])
    r = int(a[2])
    c = int(a[3])
    sum = 0
    sum += (m-c)*1
    sum += (n-r)*m
    sum += (m-1)*(n-r)
    print(sum)

