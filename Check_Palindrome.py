# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 14:52:41 2020

@author: Daniel
"""
'''
Determine whether an integer is a palindrome.
An integer is a palindrome when it reads the same backward as forward.


Example 1 Input: 121 Output: true


Example 2 Input: 121 Output: false Explanation: From left to right, it reads 121.
From right to left, it becomes 121. Therefore it is not a palindrome.


Example 3 Input: 10 Output: false Explanation : Reads 01 from right to left.
Therefore it is not a palindrome.
'''
#defining function palindrome
def palindrome(num):
    """
    :type num: int
    :return type: bool
    
    """
    forward = str(num) #casting integer num to a string type
   
    #Base Cases
    if len(forward) == 1: #single digits are palindromes
        return True
    if forward[0] == "-": #negative integers are not palindromes
        return False
        
    backward = "".join(reversed(forward)) #reversing the string
    
    if forward == backward: #checking if palindrome
        return True
    else:
        return False
    
'''Test cases'''
print(palindrome(121))
#Output: True
print(palindrome(10))
#Output: False
print(palindrome(-525))
#Output: False