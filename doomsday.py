#!/usr/bin/python3 
from os import system,remove
import sys
import argparse
import random
import math
import datetime
import calendar
days = ['Su','Mo','Tu','We','Th','Fr','Sa']

def randomday(lower=datetime.MINYEAR,upper=datetime.MAXYEAR):
    month = random.randint(1,12)
    year = random.randint(lower,upper)
    cal = calendar.Calendar().itermonthdates(year,month)
    days = [day for day in cal if day.month == month]
    d = random.choice(days)
    return d

def centurydoomsday(century):
    if abs(century - 1800) % 400 == 0:
        return 5
    elif abs(century - 1900) % 400 == 0:
        return 3
    elif abs(century - 2000) % 400 == 0:
        return 2
    elif abs(century - 2100) % 400 == 0:
        return 0

def ask(q,a):
    response = input(q)
    if type(a)(response) == a:
        print("correct")
    else:
        print("incorrect,",a)
    
def main():
    parser = argparse.ArgumentParser(description="Quiz the day of the week for a random date")
    parser.add_argument("-y", "--year", type=int, nargs=2,
            help="lower and upper bounds for year")
    parser.add_argument("-n", "--number", type=int,default=1,
            help="number of questions to be quizzed")
    parser.add_argument("-s", "--steps",type=int,nargs="*",
            help="goes step-by-step how to do the algorithm",)
    #change the steps argument to take number parameters for which steps to test
    args = parser.parse_args()
       
    for i in range(args.number):
        if args.year:
            dt = randomday(lower=args.year[0],upper=args.year[1])
        else:
            dt = randomday()
        if args.steps or args.steps == []:
            print("{}/{}/{}: ".format(dt.month,dt.day,dt.year))
            tens = int(str(dt.year)[-2:]) #years of a century
            step1,step2 = divmod(tens,12)
            if len(args.steps) == 0 or 1 in args.steps:
                ask("How many times does 12 fit as a whole into {}?"
                    .format(tens),step1)

            if len(args.steps) == 0 or 2 in args.steps:
                ask("What is the difference between {} and {} ({})?"
                    .format(tens, step1 * 12, "{} x 12".
                        format(step1)),
                    step2)

            step3 = step2 // 4
            if len(args.steps) == 0 or 3 in args.steps:
                ask("How many times does the number 4 fit into {}?".
                    format(step2),step3)

            century = int(str(dt.year)[:-2]+"00")
            step4 =  centurydoomsday(century)
            
            if len(args.steps) == 0 or 4 in args.steps:
                ask("What is the anchor day for the {}'s?".
                    format(century),step4)
            
            step5 = step1 + step2 + step3 + step4
            if len(args.steps) == 0 or 5 in args.steps:
                ask("What is {} + {} + {} + {}? ".
                    format(step1, step2, step3, step4),step5)

            step6 = step5 % 7
            if len(args.steps) == 0 or 6 in args.steps:
                ask("What is {} % 7 ? ".format(step5),step6)

            if len(args.steps) == 0 or 7 in args.steps:
                ask("What is the doomsday for {}? ".
                    format(dt.year),days[step6])

            if len(args.steps) == 0 or 8 in args.steps:
                weekday = (dt.weekday()+1)%7
                difference = step6 - weekday
                if abs(difference) >= 4:
                    if difference < 0:
                        difference += 7
                    else:
                        difference -= 7
                delta = datetime.timedelta(days=difference)
                nearest = dt + delta
                #wrong year
                if nearest.year < dt.year:
                    nearest += datetime.timedelta(days=7)
                elif nearest.year > dt.year:
                    nearest += datetime.timedelta(days=-7)
                nearest = "{}/{}".format(nearest.month,nearest.day)
                ask("What is the nearest {} to {}/{}? ".
                        format(days[step6],dt.month,dt.day),nearest)
            if len(args.steps) == 0 or 9 in args.steps:
                ask("What day of the week is {}/{}/{}? ".
                        format(dt.month,dt.day,dt.year),days[(dt.weekday()+1)%7])
        else:
            ask("{}/{}/{}: ".format(dt.month,dt.day,dt.year),
                    days[(dt.weekday()+1)%7])
        input()
        system('clear')


if __name__ == "__main__":
    main()
