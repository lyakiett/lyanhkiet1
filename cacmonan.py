# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 16:57:36 2024

@author: Windows
"""

print("============ MENU ============")
print("   1. Hu tieu")
print("   2. Chao long")
print("   3. Banh canh")
print("   4. Bun rieu")
print("   5. Pho bo")
print("==============================")
a=int(input("Mon ban chon la: "))
if a==1:
    print("Mon ban chon la hu tieu")
elif a==2:
    print("Mon ban chon la chao long")
elif a==3:
    print("Mon ban chon la banh canh")
elif a==4:
    print("Mon ban chon la pho bo")
elif a>5 or a<1:
    print("Mon an khong co trong menu, moi ban chon lai mon ")
print("Han hanh duoc phuc vu quy khach!")