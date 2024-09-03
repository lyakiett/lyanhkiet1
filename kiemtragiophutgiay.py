# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 00:57:54 2024

@author: Windows
"""

gio = int(input("Nhập giờ: "))
phut = int(input("Nhập phút: "))
giay = int(input("Nhập giây: "))
if 0 <= gio < 24 and 0 <= phut < 60 and 0 <= giay < 60:
    print("Thời gian hợp lệ.")
    print(gio,"h",phut"p",giay"s")
else:
    print("Thời gian không hợp lệ.")