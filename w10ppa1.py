# -*- coding: utf-8 -*-
"""w10ppa1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1x7_M042zwV55DlTaoCavvHK0c0t9-2UP
"""

class Student():
    '''
    a class with two attributes name, marks and two methods __init__ and print_info
    '''
    def __init__(self,name, marks):
        self.name = name
        self.marks = marks

    def print_info(self):
        
        print(f'{self.name}:{self.marks}')
s = Student('ashish',50)
s.print_info()

