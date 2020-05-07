#!/usr/bin/python3
from os import system
from os import remove
import sys
import argparse
#given month day year a corresponding day of the week is returned
def dayfromfile(filename,day):
    f = open(filename)
    days = ['Su','Mo','Tu','We','Th','Fr','Sa']
    for l in f.readlines():
        if day.lstrip("0") in l.split():
            f.close()
            return days[l.split().index(day.lstrip("0"))]

def main():
    system('cal {} {} > tempcal'.format(sys.argv[1],sys.argv[3]))
    print(dayfromfile('tempcal',sys.argv[2]))
    remove('tempcal')
   
if __name__ == "__main__":
    main()
