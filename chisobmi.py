# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 15:24:26 2024

@author: Windows
"""
a=float(input("Nhập cân nặng của bạn (kg): "))
b=float(input("Nhập chiều cao của bạn (m): "))
BMI= a/b**2
print("Chỉ số BMT của bạn là: ", a/b**2)
if BMI <16:
    print("Bạn gầy cấp độ III ")
elif BMI >=16 and BMI <17:
    print("Bạn gầy cấp độ II")
elif BMI >=17 and BMI <18.5:
    print("Bạn gầy cấp độ I")
elif BMI >=18.5 and BMI <25:
    print("Bạn có thể trạng bình thường")
elif BMI >=25 and BMI <30:
    print("Bạn hơi thừa cân ")
elif BMI >=30 and BMI <35:
    print("Bạn thừa cân cấp độ I")
elif  BMI >=35 and BMI <40:
    print("Bạn thừa cân cấp độ II")
else:
    print("Bạn bị béo phì rồi :))")