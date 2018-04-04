from random import randrange
nums = list(range(65,90))+list(range(97,122))+list(range(48,57))

numquest = int(input("Enter the number of questions: "))
#lower = input("Enter the lower bounds of letters: ")
#higher = input("Enter the upper bounds of letters: ")

for q in range(numquest):
    n = nums[randrange(len(nums))]
    print(n,":",end="")
    a = input()
    if a == chr(n):
        print("Correct!")
    else:
        print("Incorrect!",chr(n))

