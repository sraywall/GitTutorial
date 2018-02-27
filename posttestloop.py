#posttestloop.py

def main():
    while True:
        number = float(input("Enter a positive number: "))
        if number >= 0:
            break # Exit loop if number is valid
        else:
            print("The number you entered was not positive")


if __name__ == "__main__":
    main()
