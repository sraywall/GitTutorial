#!/usr/bin/python3
from os import system
import argparse

def daydistance(month,day,month2,day2,year):
    days = ['Su','Mo','Tu','We','Th','Fr','Sa']
    numdays = {1:31,2:28,3:31,4:30,5:31,6:30,
            7:31,8:31,9:30,10:31,11:30,12:31}
    #leapyear
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                numdays[2] = 29
        else:
            numdays[2] = 29
    
    total = 0
    
    if month > month2:
        total += day + numdays[month2] - day2
    elif month < month2:
        total += day2 + numdays[month] - day
    else:
        total = abs(day - day2)

    if abs(month - month2) > 1:
        for i in range(month + 1,month2, -1 if month > month2 else 1):
            total += numdays[i]

    return total

def main():
    parser = argparse.ArgumentParser(description="returns the\
            number of days between two dates in the same year")
    parser.add_argument("month",type=int,help="first month")
    parser.add_argument("day",type=int,help="first day")
    parser.add_argument("month2",type=int,help="second month")
    parser.add_argument("day2",type=int,help="second month")
    parser.add_argument("year",type=int,help="year")
    args = parser.parse_args()
    print(daydistance(args.month,args.day,
        args.month2,args.day2,args.year))

if __name__ == "__main__":
    main()
