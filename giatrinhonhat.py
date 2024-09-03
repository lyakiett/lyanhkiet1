# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 00:50:53 2024

@author: Windows
"""

a = int(input("Nhập số nguyên a: "))
b = int(input("Nhập số nguyên b: "))
c = int(input("Nhập số nguyên c: "))
d = int(input("Nhập số nguyên d: "))

nn=a
if b<nn:
    nn=b
elif c<nn:
    nn=c
elif d<nn:
    nn=d
print(f"gia tri nho nhat la {nn}")
    