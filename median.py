fname = input("Enter a file name: ")
ifile = open(fname)
w = int(ifile.readline())
x = int(ifile.readline())
y = int(ifile.readline())
z = int(ifile.readline())

# change the above code so that the use enters a file name form which to read
# the four values, then read the four values from the file
# next, write code using if statements to determine the largest value
biggest = w
if x > biggest:
    biggest = x
if y > biggest:
    biggest = y
if z > biggest:
    biggest = z
ofile = open("out.txt","w")
# change the next line to print to a text file called out.txt
#print("The largest value is {0}".format(max))
print("The largest value is {0}".format(biggest),file=ofile)
def median():
    l = [w,x,y,z]
    l.sort()
    print("The median is:",(l[1]+l[2])/2)
median()
input("Press any key to exit...")
