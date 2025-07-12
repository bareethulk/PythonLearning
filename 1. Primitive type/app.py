# pylint: disable=invalid-name
''' this project is BMI calculator'''
weight = float(input('enter your weight in kg: '))
height_cm = float(input('enter your heigh in cm: '))
height_m = height_cm / 100
bmi = weight/(height_m ** 2)
print(bmi)
