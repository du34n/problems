# -*- coding: utf-8 -*-
"""
Created on Mon Dec 25 15:52:38 2023

@author: duman
"""
#disarium sayısı

num = input()

a = 0
for i,j in enumerate(num):
    
    a += int(j)**(i+1)
    
    
if(a == int(num)):
    print('disarium')
else:
    print('not disarium')

