# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 01:01:14 2024

@author: Windows
"""

a=float(input("nhap chieu rong:"))
b=float(input("nhap chieu dai:"))
if a==b:
    print("dien tich hinh vuong la:",a**2)
    print("chu vi hinh vuong la:",a*4)
elif a>b or a<b:
    print("dien tich hinh chu nhat la:",a*b)
    print("chu vi hinh chu nhat la:",(a+b)*2) 