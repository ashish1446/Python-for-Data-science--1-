# -*- coding: utf-8 -*-
"""w5ppa2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1qDp_xCQFg55Y4auGSqR4U_y7leAamKVT
"""

def check_leap_year(year):
    flag = False
    if year % 100 == 0:
        if year % 400 == 0:
            flag = True
    else:
        if year % 4 == 0:
            flag = True
    return flag
check_leap_year(2021)

