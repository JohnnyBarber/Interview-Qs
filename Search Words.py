# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 16:14:05 2019

@author: Jiaqi Li
"""

import numpy as np

# initialize the matrix 
mat = [["A", "B", "C", "D","I"],
       ["X", "B", "D", "P","N"],
       ["W", "D", "H", "A","I"],
       ["G", "Y", "X", "Z","I"],
       ["A", "E", "F", "C","D"]]

word = ["P","A","I","N"]

def search(mat, word):
    result = len(word)
    row = len(mat)
    col = len(mat[0])
    count = 0
    pos = [0]*result
    for i in range(result):
        id = 0
        for j in range(row):
            for k in range(col):
                if (word[i] == mat[j][k]):
                    count += 1
                    pos[i] = 1
                    id = 1
                    break
            if (id == 1):
                break
    if (count == result):
        print('All words are found!')
        return None
    elif (count == result - 1):
        out = [x for x,y in zip(word,pos) if y == 1]
        print('Words',out,'is not found')
        return None
    else:
        out = [x for x,y in zip(word,pos) if y == 1]
        print('Words',out,'are not found')
    return None
        