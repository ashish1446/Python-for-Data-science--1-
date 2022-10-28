# -*- coding: utf-8 -*-
"""w6grpa2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1qDp_xCQFg55Y4auGSqR4U_y7leAamKVT
"""

def freq_to_words(L):
    '''
    Write a function named freq_to_words that accepts a list of words as argument.
    It should return a dictionary which has the following structure:
    key: frequency of words in the list 
    value: list of all words that have the above frequency
    '''


    freq = {}
    for word in L:
        if word not in freq:
            freq[word] = 1
        else:
            freq[word] += 1

    f = {}
    for key in freq:
        
        if freq[key] not in f:
            f[freq[key]] = []
        
        f[freq[key]].append(key)
            

    return f
            
L = ['a', 'random', 'collection', 'a', 'another', 'a', 'random']     

freq_to_words(L)