# this program gives a letter grade from a score
# using a decision tree
import random
def getGrade(score):
    if score >= 3 :
        if score == 4:
            return "B"
        elif score > 4:
            return "A"
        else:
            return "C"
    else:
        if score == 2:
            return "D"
        else:
            return "F"
def test():
    grades = ["F","F","D","C","B","A"]
    for i in range(100):
        num = random.randint(0,5)
        assert getGrade(num) == grades[num], "{} != {}".format(getGrade(num),grades[num])
def main():
    score = int(input("Enter your quiz score: "))
    #grades = ["F","F","D","C","B","A"]
    #print("Your grade is:",grades[score])
    print("Your grade is:",getGrade(score))
    # if score >= 3 :
    #     if score == 4:
    #         print("Your grade is: B")
    #     elif score > 4:
    #         print("Your grade is: A")
    #     else:
    #         print("Your grade is: C")
    # else:
    #     if score == 2:
    #         print("Your grade is: D")
    #     else:
    #         print("Your grade is F")


if __name__ == "__main__":
    main()
