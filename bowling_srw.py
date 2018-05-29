# Stephen Wall CS 1400 Bowling Team 4/21/2018
# Read in user input of Bowler's and their scores, then
# print them out in 3 ways, first in the order entered,
# second ordered by score, finally in alphabetical order
# an asterisk placed before the name of a bowler with a perfect
# score.  After printing the lists, a congratulatory message
# and message of consolation are displayed to the winner and 
# loser respectively.  Finally a team average is printed
# rounded to the nearest pin.  All of these items are also put
# into a file called 'game_results.txt'
# Major Steps
# 1 Reading input and making collection of Bowlers
# 2 Sorting the bowlers
# 3 Printing to a file
# Lessons learned
# *importing itemgetter from operator makes sorting a list of tuples easy
# *using tuples can be easier than objects if the ammount of data is small
# *accumulator pattern aids in obtaining an average
from operator import itemgetter
def main():
    team = []
    line = input("Enter a name followed by score or enter to quit: ")
    while line != "":
        arr = line.split()
        name = arr[0]
        score = int(arr[1])
        team.append((name,score))
        line = input("Enter a name followed by score or enter to quit: ")

    printFile(team) # writing to std out
    outfile = open("game_results.txt","w")
    printFile(team,outfile) # writing to game_results.txt

def printBowlers(team, outfile = None):
    for tup in team:
        if tup[1] == 300:
            print("*",end="",file=outfile)
        else:
            print(" ",end="",file=outfile)
        print("{:10}{:3}".format(tup[0],tup[1]),file=outfile)

def printFile(team,outfile=None):
    print("\nNames and scores as entered.\n--------------------",file=outfile)
    printBowlers(team,outfile)
    print("\nNames and scores in order of score, highest first.\n--------------------",file=outfile)
    team.sort(key = itemgetter(1),reverse=True) # sorting by score which is second element in tuple
    printBowlers(team,outfile)
    print("\nNames and scores in alphabetical order.\n--------------------",file=outfile)
    team.sort(key = itemgetter(0)) # sorting by name which is first element in tuple
    printBowlers(team,outfile)
    team.sort(key = itemgetter(1),reverse=True)
    print("\nCongratulations, {}. Your score of {} was the highest."
          .format(team[0][0], team[0][1]),file=outfile)
    print("Sorry, {}. Your score of {} was the lowest."
          .format(team[-1][0], team[-1][1]),file=outfile)
    total = 0
    for i in range(len(team)):
        total += team[i][1]
    print("Average team score: ", total//len(team),file=outfile)
   
if __name__ == "__main__":
    main()
