#endoffileloop.py
from sys import *
def main():
    program, fileName = argv
    infile = open(fileName)
    line = infile.readline()
    while line != "":
        # process line
        line = infile.readline()
        print(line,end="")

if __name__ == "__main__":
    main()
