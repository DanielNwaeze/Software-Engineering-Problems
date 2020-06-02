# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 14:31:08 2020

@author: Daniel
"""
'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = 2, 7, 11, 15, target = 9, Because nums[0] + nums[1] = 2 + 7 = 9, return 0, 1.
'''

#defining function sums
def sums(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :return type: List [int]
    
    """
    
    #checking invalid inputs
    if len(nums)==0: #empty list input
        return "List is empty."
    if len(nums)==1: #list input without two or more items
        return "Input another number to the list"
    
    remainder = 0 #initializing remainder
    seen = {} #empty set for checking if the sum of two numbers equals target
    
    #One Pass Solution
    for i, number in enumerate(nums):
        remainder = target - number #finding needed value to sum to target
        if remainder in seen: #if needed value exists in seen set
            return [seen[remainder], i] 
        else:
            seen[number] = i #if needed value does not yet exist

'''Test case'''
nums = [2, 7, 11, 15]
target = 9
print ("The indices of the respective numbers are:\n", sums(nums, target))
"""
Output:
The indices of the respective numbers are:
 [0, 1]   
"""