# -*- coding: utf-8 -*-
"""w5ppa6.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1qDp_xCQFg55Y4auGSqR4U_y7leAamKVT
"""

def type_of_sequence(L):
    """
    determine the type of a sequence
    
    Argument:
        L: list of strings
    Return:
        seq_type: string
    """
    k = 0
    for x in L:
        if mysterious(x):
            k += 1
            
    if k < 2:
        return 'mildly mysterious'
        
    if 2<=k<5:
        return 'moderately mysterious'
        
    if k>= 5:
        return 'most mysterious'