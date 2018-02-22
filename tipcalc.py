mealCost = float(input("Enter the cost of the meal: $"))
print("Cost of meal:","${:,.2f}".format(mealCost))
excelTip = mealCost * .2
avgTip = mealCost * .15
poorTip = mealCost * .1
print("Excellent service tip:","${:,.2f}".format(excelTip),"total:","${:,.2f}".format(mealCost+excelTip))
print("Average service tip:","${:,.2f}".format(avgTip),"total:","${:,.2f}".format(mealCost+avgTip))
print("Poor service tip:","${:,.2f}".format(poorTip),"total:","${:,.2f}".format(mealCost+poorTip))
