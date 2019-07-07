#!/usr/bin/python3
theBoard = {'top-L': ' ','top-M': ' ','top-R': ' ',
        'mid-L': ' ','mid-M': ' ','mid-R': ' ',
        'low-L': ' ','low-M': ' ','low-R': ' ',
        }

def printBoard(board):
    print(board['top-L'],'|',board['top-M'],'|',board['top-R'],sep='')
    print('-+-+-') 
    print(board['mid-L'],'|',board['mid-M'],'|',board['mid-R'],sep='')
    print('-+-+-') 
    print(board['low-L'],'|',board['low-M'],'|',board['low-R'],sep='')

def main():
    printBoard(theBoard)
    turn = 'X'
    for i in range(9):
        print('Turn for',turn,'Move on which space?')
        move = input()
        theBoard[move] = turn
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'
        printBoard(theBoard)


if __name__ == "__main__":
    main()
