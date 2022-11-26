# -*- coding: utf-8 -*-
"""w12ppa4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1OSpEQeErZ_jlxyowUlAJ0Rzui5u9rlQt
"""

def std_dev(X):
    import math 

    def square(x):
        return(x*x)
    
    mean = sum(X)/len(X)
   
    p = sum([square(num-mean) for num in X])
    stddev = math.sqrt(p/(len(X)-1))
    print(f'standard deviation = {stddev:.2f}')
    return stddev
X = [1,2,3,4,5,6,7,8,9]
std_dev(X)
