# -*- coding: utf-8 -*-
"""w6gppa8.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1qDp_xCQFg55Y4auGSqR4U_y7leAamKVT
"""

def factors():
    l =[]
    n = int(input())
    for i in range(1,n+1):
        if n%i==0:
            l.append(i)
    fac = set(l)
    return fac

def common_factors():
    com_a = factors()
    com_b = factors()
    print(com_a,com_b)

    l = []
    for fact in com_a:
        if fact in com_b:
            l.append(fact)
    comfac = set(l)
    return comfac

print(common_factors())

