# -*- coding: utf-8 -*-
"""
Created on Mon Jan  1 16:34:12 2024

@author: duman
"""

def values_of_target(nums):
    nums = nums.split()
    index_list = []
    for i in nums:
        for j in nums:
            if i != j and int(i) + int(j) == int(target) and i < j :
                index_list.append(nums.index(i))  
                index_list.append(nums.index(j))
                
    return index_list
                
        
nums = input()
target = input()

print(values_of_target(nums))

    