# imports the argv things from sys
from sys import argv
#sets filename to commandline argument and script to ex15.py
script, filename = argv
# opens the file and assigns it to txt
txt = open(filename)
# prints a string with the filename in it
print(f"Here's your file {filename}:")
#prints the contents of the file
print(txt.read())
txt.close()
# prints a prompt
#print("Type the filename again:")
#gets a string from the user
#file_again = input("> ")
# opens a file named after the string and assigns it to txt_again
#txt_again = open(file_again)
# prints the contents of a file
#print(txt_again.read())
