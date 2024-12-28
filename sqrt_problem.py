# -*- coding: utf-8 -*-
"""
Created on Mon Dec 25 19:59:04 2023

@author: duman
"""

#sqrt problem

import math
num = int(input())


counter = 0  

while(num >= 2):
    num = math.sqrt(num)
    counter +=1
    
print(counter)