#words = input("Enter text: ")
from sys import *
filename, words = argv
for c in words:
    if c <="M" and c >= "A":
        print(chr(ord(c)+13),end="")
    elif c > "M" and c <= "Z":
        print(chr(ord(c)-13),end="")
    elif  c <="m" and c >= "a":
        print(chr(ord(c)+13),end="")
    elif c > "m" and c <= "z":
        print(chr(ord(c)-13),end="")
    else:
        print(c,end="")
print()
