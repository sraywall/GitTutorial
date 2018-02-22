# month2.py
# A program to print the month abbreviation, given its number.
#months is a list used as a lookup table

def main():
    months = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
    n = int(input("Enter a month number (1 - 12): "))
    print("The month abbreviation is", months[n-1] + ".")

main()
