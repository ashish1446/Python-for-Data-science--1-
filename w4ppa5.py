# -*- coding: utf-8 -*-
"""w4ppa5.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1U6VeRSn04lH8PvN_tjezT9aZjTX2ZvvA
"""

L = input().split(',')
nums = []
for x in L:
  nums.append(float(x))

for i in range(len(nums)-1):
  print(int(nums[i]), end = ',')
print(int(nums[-1]))

int(5.55555)