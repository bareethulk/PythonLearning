# pylint: disable=invalid-name
''' this project is BMI calculator'''
weight = float(input('enter your weight in kg: '))
height_cm = float(input('enter your heigh in cm: '))
height_m = height_cm / 100
bmi = weight/(height_m ** 2)
print(f"Your BMI is {bmi:.2f}")
if bmi < 18.5:
    print("You are underweight.")
elif bmi < 25:
    print("You have a normal weight.")
elif bmi < 30:
    print("You are overweight.")
else:
    print("You are obese.")
