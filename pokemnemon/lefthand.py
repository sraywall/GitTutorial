#!/usr/bin/python3
# lefthand.py 
# quizzes on the left hand of pokemon binary
from random import randrange
import os

arr = [('00010000','Pidgey'),
        ('00100000','NidoranM'),
        ('00110000','Venonat'),
        ('01000000','Kadabra'),
        ('01010000','Slowbro'),
        ('01100000','Drowzee'),
        ('01110000','Rhydon'),
        ('10000000','Tauros'),
        ('10010000','Articuno'),
        ('10100000','Feraligatr'),
        ('10110000','Togetic'),
        ('11000000','Sunflora'),
        ('11010000','Steelix'),
        ('11100000','Octillery'),
        ('11110000','Magby')]

numquest = int(input("Enter the number of questions: "))
for i in range(numquest):
    os.system('clear')
    r = randrange(len(arr))
    q = arr[r][0]
    a = arr[r][1]
    if randrange(2):
        q,a = a,q
    guess = input("{}: ".format(q))
    if guess == a:
        print("Correct!")
    else:
        print("Wrong!",a)
    input()
