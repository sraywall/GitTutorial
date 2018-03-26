# imports argv from sys
from sys import argv
#sets script to ex20.py and input_file to argument 1
script, input_file = argv
#defines the funtion print_all which takes a file and prints its contents
def print_all(f):
    print(f.read())
# defines the function rewind which takes a file and puts the 'readhead' back to the start of the input_file
def rewind(f):
    f.seek(0)
# defines the function print_a_line which takes a line number and a file and prints the number and a line of text
def print_a_line(line_count, f):
    print(line_count, f.readline(),end="")
# opens a file and assigns it to current_file
current_file = open(input_file)
# prints a string on one line and has an extra return
print("First let's print the whole file:\n")
# invokes the print_all function on the file current_file and prints its contents
print_all(current_file)
#prints a string
print("Now let's rewind, kind of like a tape.")
# invokes the rewind function whichs puts the seek back at 0
rewind(current_file)
# prints a string
print("Let's print three lines:")
# assigns an int to 1
current_line = 1
# prints a line number and line from a file by invoking print_a_line
print_a_line(current_line, current_file)
# increments the line_count variable which represents a line number
current_line += 1
print_a_line(current_line,current_file)

current_line += 1
print_a_line(current_line, current_file)
