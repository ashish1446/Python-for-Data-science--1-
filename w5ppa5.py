# -*- coding: utf-8 -*-
"""w5ppa5.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1qDp_xCQFg55Y4auGSqR4U_y7leAamKVT
"""

def first_three(l):
    sorted = []
    sorted.append(l[0])
    for i in range(1,len(l)):
        flag = True
        for j in range(len(sorted)):

            if l[i]>sorted[j]:

                beforej = sorted[:j]
                afterj = sorted[j: ]
                insert = [l[i]]
                
                sorted = beforej+insert+afterj
                flag = False
                break
            

        if flag:
            sorted.append(l[i])
                
    return sorted[0], sorted[1], sorted[2]
    
l = [-1,8,7,3]
first_three(l)

