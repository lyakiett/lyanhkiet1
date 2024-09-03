# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 00:59:39 2024

@author: Windows
"""


a = int(input("Nhập số a: "))
b = int(input("Nhập số b: "))
c = int(input("Nhập số c: "))
d= 0
if a > b:
    d = a
    a = b
    b = d
if a > c:
    d = a
    a = c
    c = d
if b > c:
    d = b
    b = c
    c = d
print("Thứ tự tăng dần là:", a, b, c) 