# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 00:58:39 2024

@author: Windows
"""

var = input("Nhập một chữ cái: ")
if var.islower():
    print(var.upper())
elif var.isupper():
    print(var.lower())
else:
    print("Đây không phải là một chữ cái hợp lệ.")