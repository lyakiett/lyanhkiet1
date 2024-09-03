# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 15:43:02 2024

@author: Windows
"""
BS =float(input("Nhập biển số xe của bạn: "))
a= BS//10000
b= (BS%10000)//1000
c= ((BS%10000)%1000)//100
d= (((BS%10000)%1000)%100)//10
e= (((BS%10000)%1000)%100)%10
X=(a+b+c+d+e)%10
print ("Số nút của xe bạn là: ", X)