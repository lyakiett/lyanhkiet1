# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 00:52:10 2024

@author: Windows
"""

a = int(input("Nhập số nguyên a: "))
b = int(input("Nhập số nguyên b: "))
c = int(input("Nhập số nguyên c: "))

ln=a
if ln<b:
    ln=b
elif ln<c:
    ln=c
print(f"giá trị lớn nhẩt là: {ln}")