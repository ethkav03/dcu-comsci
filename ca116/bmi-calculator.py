#!/usr/bin/env python3

weight = int(input())
height = int(input())

bmi = round(weight / (height * height) * 10000)

if bmi < 18.5:
   print("underweight")
elif bmi >= 18.5 and bmi <= 25.0:
   print("normal")
elif bmi > 25 and bmi <= 29.9:
   print("overweight")
else:
   print("obese")
