# -*- coding: utf-8 -*-
"""
Created on Fri Oct 14 10:14:20 2016

@author: SIDDU_Pandu
"""

def solution(A):
    # write your code in Python 2.7
    '''
    input: a non-empty array that can be assumed as a list/tuple
    output: minimum difference of the differences between  the values of array
    '''
    distances = []
    reference = 0
    distance = 0
    minimum_distance = 0
    
    for i in range(len(A)):
        reference = A[i]
        ACopy = A[:]
        ACopy.remove(A[i])
        for i in range(len(ACopy)):
            distance = abs(reference - ACopy[i])
            distances.append(distance)
    
    minimum_distance = min(distances)
    
    return (minimum_distance)
        
        
print(solution([7,21,3,42,3,7]))