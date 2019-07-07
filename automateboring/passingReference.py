#!/usr/bin/python3
import sys
def eggs(someParameter):
    someParameter.append(sys.argv[1])

if __name__ == '__main__':
    spam = [1, 2, 3]
    eggs(spam)
    print(spam)
