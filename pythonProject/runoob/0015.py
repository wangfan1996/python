#!/usr/bin/python3

import os

res = os.access('0015.py', os.F_OK)
print(res)

res = os.access('0015.py', os.R_OK)
print(res)

res = os.access('0015.py', os.W_OK)
print(res)


res = os.access('0015.py', os.X_OK)
print(res)







