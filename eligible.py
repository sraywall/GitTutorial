#this program takes input
#from user and determines eligibity
# for the Senate and House

def main():
    age = int(input("Enter your age: "))
    citizenship = int(input("How long have you been a US citizen? "))

    if age >= 30 and citizenship >= 9:
        print("You are eligible for both the Senate and House")
    elif age >=25 and citizenship >= 7:
        print("You are eligible for the House")
    else:
        print("You aren't eligible for the House or Senate")

if __name__ == "__main__":
    main()
