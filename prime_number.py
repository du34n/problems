# -*- coding: utf-8 -*-
"""
Created on Mon Dec 25 20:14:40 2023

@author: duman
"""

#asal sayı 

num = int(input())

counter = 0
for i in range(num+1):
    if(num % (i+1) == 0):
        counter +=1
    
if counter == 2:
    print('the number prime')
else:
    print('not prime')