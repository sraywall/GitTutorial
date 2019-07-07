#!/usr/bin/python3

allGuests = {'Alice': {'apples': 5, 'pretzels':12},
        'Bob': {'apples': 2, 'ham sandwiches':3},
        'Carol': {'apple pies': 1, 'cups':3},
        }

def totalBrought(guests, item):
    numBrought = 0
    for k,v in allGuests.items():
        numBrought += v.get(item,0)
    return numBrought

def main():
    print('Number of things being brought:')
    print(' -','Apples'.ljust(15),totalBrought(allGuests, 'apples'))
    print(' -','Cups'.ljust(15),totalBrought(allGuests, 'cups'))
    print(' -','Cakes'.ljust(15),totalBrought(allGuests, 'cakes'))
    print(' -','Ham Sandwiches'.ljust(15),totalBrought(allGuests, 'ham sandwiches'))
    print(' -','Apple Pies'.ljust(15),totalBrought(allGuests, 'apple pies'))

if __name__ == "__main__":
    main()
