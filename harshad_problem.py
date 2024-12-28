# -*- coding: utf-8 -*-
"""
Created on Mon Dec 25 14:40:19 2023

@author: duman
"""

# harshad sayısı


num = input()
a = 0
for i in num:
    a += int(i)

if int(num) % a == 0:
    print('harshad')
else:
    print('not harshad')