#change2.py
#A program to calculate the value of some change in dollars

def main():
    print("Change Counter")
    print()
    print("Please enter the count of each coin type.")
    quarters = int(input("Quarters: "))
    dimes = int(input("Dimes: "))
    nickels = int(input("Nickels: "))
    pennies = int(input("Pennies: "))
    total = .25 * quarters + .1 * dimes + .05 * nickels + .01 * pennies
    print()
    print("The total value of your change is",total)

main()
