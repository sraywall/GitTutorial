#!/usr/bin/python3
import argparse
from os import system
import random
# :set noexpandtab
def ask(q,a):
    response = input(q)
    if response == a:
        print("correct")
    else:
        print("incorrect,",a)
    input()
    system("clear")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("file",help="a tsv file containing info to be quizzed on")
    parser.add_argument("-r","--range",type=int,nargs=2,help="range of questions to be asked")
    parser.add_argument("-q","--question",nargs="*",help="which header names or numbers to include in questions")
    parser.add_argument("-j","--hint",nargs="*",help="which header names or numbers to include in hints")
    args = parser.parse_args()
    f = open(args.file)
    headers = f.readline().strip().split("\t")
    rows = [row.strip().split("\t") for row in f.readlines()]
    if(args.range):
        start = args.range[0]
        stop = args.range[1]
    else:
        start = 0
        stop = len(rows)
    for row in rows[start:stop]:
        while True:
            q = args.question[random.randrange(len(args.question))]
            if q.isdigit():
                q = headers[int(q)]
            a = row[headers.index(q)] 
            h = args.hint[random.randrange(len(args.hint))] 
        #so you don't ask 
        #"quick what's the number for 911?"
        #like little rascals
            if q != h:
                break;
        if h.isdigit():
            h = row[int(h)]
        else:
            h = headers.index(h)
            h = row[h]
        ask("What is the {} of/for \"{}\"? ".format(q,h),a)


if __name__ == "__main__":
    main()
