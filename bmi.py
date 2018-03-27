#calculated BMI from imperial units entered
weight = float(input("Enter your weight (lbs): "))
weight = weight * 0.453592
height = float(input("Enter your height (inches): "))
height = height * 0.0254
bmi = weight / height ** 2
if bmi > 25:
    print("You are overweight with a bmi of:",bmi)
else:
    print("Your bmi is:",bmi)
