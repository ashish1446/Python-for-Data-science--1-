# -*- coding: utf-8 -*-
"""w10ppa5.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1x7_M042zwV55DlTaoCavvHK0c0t9-2UP
"""

class Vector():
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def print_info(self):
        print(f'({self.x},{self.y})')
    
    def scale(self,arg):
        self.x = arg*self.x
        self.y = arg*self.y

    def reflect_about_X(self):
        self.y = -self.y

    def reflect_about_Y(self):
        self.x = -self.x
    
    def add(self, new):

        sum_x = self.x + new.x
        sum_y = self.y + new.y
        return Vector(sum_x,sum_y)

