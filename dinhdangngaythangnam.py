# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 00:35:08 2024

@author: Windows
"""

day = int(input("Nhập ngày sinh: "))
month = int(input("Nhập tháng sinh: "))
year = int(input("Nhập năm sinh: "))
a = f"{day}/{month}/{year}"
print(f"Định dạng ngày/tháng/năm: {a}")
b = f"{day}/{month}/{year % 100:02}"
print(f"Định dạng ngày/tháng/năm(2socuoi): {b}")
c = f"{year}/{month}/{day}"
print(f"Định dạng năm/tháng/ngày: {c}")