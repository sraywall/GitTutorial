# bowlingscores.py

def main():
    name = []
    score = []
    inText = input("Enter a name and a score, enter to quit. ")
    while inText != "":
        inText = inText.split()
        name.append(inText[0])
        score.append(int(inText[1]))
        inText = input("Enter a name and a score, enter to quit. ")
    printAsEntered(name, score)
    printByScores(name, score)
    
def printAsEntered(name, score, file=None):
    print("\nNames and scores as entered.\n--------------------")
    for i in range(len(name)):
        if score[i] == 300:
            print("*{:10}{:3}".format(name[i], score[i]), file=file)
        else:
            print(" {:10}{:3}".format(name[i], score[i]), file=file)

def printByScores(name, score, file=None):
    print("\nNames and scores in order of score, highest first.\n--------------------")
    sortedName, sortedScore = sortByScore(name, score)
    for i in range(len(name)):
        if score[i] == 300:
            print("*{:10}{:3}".format(sortedName[i], sortedScore[i]), file=file)
        else:
            print(" {:10}{:3}".format(sortedName[i], sortedScore[i]), file=file)

def sortByScore(name, score):
    start = 0
    end = len(name)-1
    sortedName = name
    sortedScore = score
    while start < end:
        highest = start
        lowest = end
        for i in range(start, end+1):
            if sortedScore[i] > sortedScore[highest]:
                highest = i
        sortedScore[start], sortedScore[highest] = sortedScore[highest], sortedScore[start]
        sortedName[start], sortedName[highest] = sortedName[highest], sortedName[start]
        for i in range(start, end+1):
            if sortedScore[i] < sortedScore[lowest]:
                lowest = i
        sortedScore[end], sortedScore[lowest] = sortedScore[lowest], sortedScore[end]
        sortedName[end], sortedName[lowest] = sortedName[lowest], sortedName[end]
        start += 1
        end -= 1
    return sortedName, sortedScore    
    
main()
