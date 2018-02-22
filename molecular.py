def main():
    h = int(input("Enter the number of H: "))
    c = int(input("Enter the number of C: "))
    o = int(input("Enter the number of O: "))

    total = h * 1.00794 + c * 12.0107 + o * 15.9994

    print("The total molecular weight: ",total,"g",sep="")
    
main()
