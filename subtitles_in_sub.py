# -*- coding: utf-8 -*-
"""
Created on Mon Jan  1 16:29:29 2024

@author: duman
"""

def find(string,substring):
    lst = []
    for i in range(0,len(string)):
        for j in range(len(string),0,-1):
            if i < j:
                lst.append(string[i:j])
    num = lst.count(substring)
    return num 
string = 'ABCDCD'
substring = 'CD'
a = find(string,substring)
print(a)    