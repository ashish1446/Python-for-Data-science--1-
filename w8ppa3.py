# -*- coding: utf-8 -*-
"""w8ppa3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1x7_M042zwV55DlTaoCavvHK0c0t9-2UP
"""

def multiply(a,b): 

    if b ==  1:
        return a
    else:
        return a + multiply(a,b-1)

multiply(-5,2)

