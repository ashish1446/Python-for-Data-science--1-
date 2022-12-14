# -*- coding: utf-8 -*-
"""oppe_mock3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1x7_M042zwV55DlTaoCavvHK0c0t9-2UP
"""

def matrix_type(M):
    is_diagonal = True
    m = len(M)
    for i in range(m):
        for j in range(m):
            if i!=j and M[i][j] != 0:
                is_diagonal = False
                break
    if is_diagonal:
        is_scalar = True
    else:
        is_scalar = False
    
    f = M[0][0] 
    for i in range(m):
        if M[i][i] != f:
            is_scalar = False
            break

    if is_scalar:
        is_identical = True
    else:
        is_identical = False
    
    for i in range(m):
        if M[i][i] != 1:
            is_identical = False
            break

    if not is_diagonal:
        return 'non diagonal'
    
    if is_identical:
        return 'identity'
        
    if is_scalar:
        return 'scalar'
    

    return 'diagonal'
        
M = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]

matrix_type(M)

