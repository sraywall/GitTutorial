# bowlingscores_obj.py

from bowler import Bowler

def main():
    team = []
    inText = input("Enter a name and a score, enter to quit. ")
    while inText != "":
        inText = inText.split()
        team.append(Bowler(inText[0], int(inText[1])))
        inText = input("Enter a name and a score, enter to quit. ")
    printAsEntered(team)
    sortedScores = printByScores(team)
    printByNames(team)
    printSummary(sortedScores)
    outFile = open("game_results.txt", "w")
    printAsEntered(team, outFile)
    printByScores(team, outFile)
    printByNames(team, outFile)
    printSummary(sortedScores, outFile)
    outFile.close()
    
def printTeam(team, file):
    for i in range(len(team)):
        if team[i].getScore() == 300:
            print("*{:10}{:3}"
                  .format(team[i].getName(), team[i].getScore()), file=file)
        else:
            print(" {:10}{:3}"
                  .format(team[i].getName(), team[i].getScore()), file=file)

def printAsEntered(team, file=None):
    print("\nNames and scores as entered.\n--------------------", file=file)
    printTeam(team, file)

def printByScores(team, file=None):
    print("\nNames and scores in order of score, highest first.\n--------------------", file=file)
    sortedScores = team[:]
    sortedScores.sort(key=Bowler.getScore, reverse=True)
    printTeam(sortedScores, file)
    return sortedScores

def printByNames(team, file=None):
    print("\nNames and scores in alphabetical order.\n-----------------------\n", file=file)
    sortedNames = team[:]
    sortedNames.sort(key=Bowler.getName)
    printTeam(sortedNames, file)
    
def printSummary(team, file=None):
    print("\nCongratulations, {}. Your score of {} was the highest."
          .format(team[0].getName(), team[0].getScore()), file=file)
    print("Sorry, {}. Your score of {} was the lowest."
          .format(team[-1].getName(), team[-1].getScore()), file=file)
    total = 0
    for i in range(len(team)):
        total += team[i].getScore()
    print("Average team score: ", total//len(team), file=file)

main()
