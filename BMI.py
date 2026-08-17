height=float(input("Enter your height in cm"))
weight=float(input("Enter your weight in kg"))
BMI=weight/(height/100)**2
print("Your BMI is",BMI)
if BMI<18.4:
    print("You are underweight")
elif BMI<24.9:
    print("You are really healthy")
elif BMI<29.9:
    print("You are overweight")
elif BMI<34.9:
    print("You are seriously overweight")
elif BMI<39.9:
    print("You are obese")
else:
    print("You are really obese")
        