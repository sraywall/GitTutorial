from random import randint
import os
numquest = int(input("Enter the number of questions: "))
lower = int(input("Enter the lower range of questions: "))
upper = int(input("Enter the upper range of questions: "))

for i in range(numquest):
	os.system('clear')
	r = randint(lower,upper)
	n = bin(r)[2:].zfill(8)
	print("{}:".format(n),end="")
	a = input()
	if a == str(r):	
		print("Correct!")
	else:
		print("Wrong!",r)
	input()
os.system('clear')
