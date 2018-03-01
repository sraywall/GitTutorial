# average5.py

def main():
    total = 0.0
    count = 0
    xStr = input("Enter a number (<Enter> to quit)  >> ")
    while xStr != "":
        x = float(xStr)
        total += x
        count += 1
        xStr = input("Enter a number (<Enter> to quit) >> ")
    print("\nThe average of the numbers is", total / count)

if __name__ == "__main__":
    main()
