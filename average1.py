# program gets the average of a series of numbers

def main():
    average = 0
    num = int(input("Enter the ammount of numbers: "))
    for i in range(num):
        average += int(input("Enter number {}: ".format(i+1)))
    average /= num
    print("The average is:",average)
if __name__ == "__main__":
    main()
