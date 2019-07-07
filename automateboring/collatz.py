#!/usr/bin/python3
import sys

def collatz(number):
    if number % 2 == 0:
        out = number // 2
        print(out)
        return out
    else:
        out = 3 * number + 1
        print(out)
        return out


def main():
    try:
        num = int(sys.argv[1])
    except ValueError:
        print('User must enter an integer')
        sys.exit()

    while num != 1:
        num = collatz(num)


if __name__ == '__main__':
    main()
