# -*- coding: utf-8 -*-
"""w9ppa12.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1eTf40H_w8PbZPLGnuNFsmXYe68Q_fzN0
"""

def write_pattern(n):
    """
    Write a pattern to file

    Argument:
        n: integer
    Return:
        None
    """
    f = open('pattern.csv', 'w')
    for i in range(n):
        for j in range(n):
            if i == j or i + j == (n-1):
                f.write('1')
            else:
                f.write('0')

            if j != (n-1):
                f.write(',')
        if i != (n-1):
            f.write('\n')
    f.close()