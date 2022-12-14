# -*- coding: utf-8 -*-
"""sort_list_recursion.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1eTf40H_w8PbZPLGnuNFsmXYe68Q_fzN0
"""

def alr1(L):
    #ascending list recursion
    if L!= []:
        mini = min(L)
        L.remove(mini)
        return [mini] + alr1(L)
    else:
        return L

def alr2(L):
    #ascending list recursion
    if L != []:
        min_index = L.index(min(L))
        L[0],L[min_index] = L[min_index],L[0]
        return [L[0]] + alr2(L[1:])
    else:
        return L

def alr3(L):
    #ascending list recursion
    if L != []:
        max_index = L.index(max(L))
        L[-1],L[max_index] = L[max_index],L[-1]
        return alr3(L[:-1]) + L[-1:]
    else:
        return L

print(alr1([5,99,3,0,65,-1,-99,-1000,22,6,35,30000,-2]))
print(alr2([5,99,3,0,65,-1,-99,-1000,22,6,35,30000,-2]))
print(alr3([5,99,3,0,65,-1,-99,-1000,22,6,35,30000,-2]))