# -*- coding: utf-8 -*-
"""w9ppa1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1x7_M042zwV55DlTaoCavvHK0c0t9-2UP
"""

def read_file(filename):
    """
    Read the file and print each line

    Argument:
        filename: string, name of the file to be read
    Return:
        None
    """
    f = open(filename,'r')
    s = 0
    while s!= '':
        s = f.readline()
        
        print(s, end = '')
    f.close()