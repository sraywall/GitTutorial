y = int(input("Enter the number of credits you have: "))
left = int(input("Enter the number of credits you have left: "))
currentgpa =float(input("Enter current gpa: "))
remainingcreditsgpa = float(input("Enter gpa for remaining credits: "))

print("GPA would be: ",(2.99*y+remainingcreditsgpa * left) /(left + y))
