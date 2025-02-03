height = float(input("enter your height in m: "))
weight = int(input("enter your weight in kg: "))
BMI = weight / (height ** 2) 
BMI = round(BMI, 2)
print(BMI)

if BMI < 18.5:
    print(f"Your bmi is {BMI} You are Underweight")
elif BMI < 25:
    print(f"Your bmi is {BMI} You have a normal weight")
elif BMI < 30:
    print(f"Your bmi is {BMI} You are overweight")
elif BMI < 35:
    print(f"Your bmi is {BMI} You are obese")
else:
    print(f"Your bmi is {BMI} You are clinically obese")