#!/usr/bin/python3
import argparse
import sys

def main():
    if len(sys.argv) == 2:
        if sys.argv[1] == "-h" or sys.argv[1] == "--help":
            print("Pass with commandline arguments!")
        elif sys.argv[1]== "-t":
            pass 
        elif sys.argv[1]== "-l":
            pass
        elif sys.argv[1]== "-q":
            pass



if __name__ == "__main__":
    main()
