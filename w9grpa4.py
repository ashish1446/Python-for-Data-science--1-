# -*- coding: utf-8 -*-
"""w9grpa4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1x7_M042zwV55DlTaoCavvHK0c0t9-2UP
"""

def num_to_words(mat):
    """
    Convert matrix to file

    Argument: 
        mat: list of lists
    Return:
        None
    """
    f = open('words.csv','w')
    unit = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'}
    M = mat # [[1,2],[3,4]]
    for i in range(len(M)):
        for j in range(len(M)):
            if i == len(M):
                if j == len(M)-1:
                    num = unit[M[i][j]]
                    f.write(num)
                else:
            	
            	    num =  unit[M[i][j]]
            	    f.write(num)
            	    f.write(',')

            


            else:
                if j == len(M)-1:
                    num = unit[M[i][j]]
                    f.write(num)
                    f.write('\n')
                else:
            
            	    num = unit[M[i][j]]
            	    f.write(num)
            	    f.write(',')
    f.close()