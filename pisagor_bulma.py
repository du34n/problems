# -*- coding: utf-8 -*-
"""
Created on Fri Jan  5 15:37:55 2024

@author: duman
"""

#pisagor triangle


def pisagor_bulma():
    
    pisagor_listesi  = list()
    for i in range(1,101):
        for j in range(1,101):
            
            c = (i**2 + j**2)** 0.5
            
            if(c == int(c)):
                pisagor_listesi.append((i,j,int(c)))
                
    return pisagor_listesi 


for i in pisagor_bulma():
    print(i)