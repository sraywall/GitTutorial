# average6.py
from sys import *
def main():
    program,fileName = argv
    infile = open(fileName,'r')
    total = 0.0
    count = 0
    for line in infile:
        total += float(line)
        count += 1
    print("\nThe average of the numbers is", total/count)

if __name__ == "__main__":
    main()
