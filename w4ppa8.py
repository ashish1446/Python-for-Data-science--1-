# -*- coding: utf-8 -*-
"""w4ppa8.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1U6VeRSn04lH8PvN_tjezT9aZjTX2ZvvA
"""

n = int(input())

l =[]
imatrix =[]

  


for r in range(n):
  l = []
  for c in range(n):
    
    if r == c:
      l.append(1)

    else:
      l.append(0)
      #imatrix[r][c] = 1

  imatrix.append(l)

for i in range(len(imatrix)):
  for j in range (len(imatrix)):
    
    if j == len(imatrix)-1:
      print(imatrix[i][j])
    else:
      print(imatrix[i][j], end =',')

