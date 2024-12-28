# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 14:45:02 2024

@author: duman
"""

n = int(input())
tic_tac_toe = []
i = 0
while(i<n):
    row_input = list(map(int,input()))
    tic_tac_toe.append(row_input)
    i +=1

first_mark = 0
second_mark = 0 
def result(site_map):
    row=0
    trig=False
    while(row < len(site_map)):
        col = 0
        while(col < len(site_map)):
            #print(col)
            i=1
            identity = site_map[row][col]
            if(identity == 1):
                if(col < len(site_map)-1):
                    trig=False
                    while(site_map[row][col+i] == identity):
                        trig=True
                        i+=1
                        if(col+i >= len(site_map)):
                            col += i
                            print(i)
                            trig = False
                            break
                    if(trig):
                        col += i-1
                        print(i)
                        
            elif(identity == 2):
                if(col < len(site_map)-1):
                    trig=False
                    while(site_map[row][col+i] == identity):
                        trig=True
                        i+=1
                        if(col+i >= len(site_map)):
                            col += i
                            print(i)
                            trig = False
                            break
                    if(trig):
                        col += i-1
                        print(i)
                        
            col += 1
        row += 1
            
result(tic_tac_toe)