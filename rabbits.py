#Stephen Wall CS1400 Rabbits, Rabbits, Rabbits 3/3/2018
#Helps a a scientist know the population growth of
#lab rabbits over months and when the
#500 cages will run out
#major steps were printing in a nice table,
#a while loop that ends when rabbit population exceeds 500
#multiple assignment statement that essentially made a fibonacci sequence
#Lessons Learned:
#1)I learned how the multiple assignment works
#2)I learned rabbit population growth can be modeled by the fibonacci sequence
#3)I learned when while loops terminate
#4)I learned that tabs can format things nicely

months = 1
breedables = 1
newborns = 0
def printmonth():
    print("{}\t".format(months),end="")
    print("{}\t".format(breedables),end="")
    print("{}\t".format(newborns),end="")
    print("{}\t".format(breedables+newborns))
print()
print("-"*19)
print("\nTable of rabbit pairs")
print("\nMonth\tAdults\tBabies\tTotal")
while(breedables + newborns<= 500):
    printmonth()
    breedables,newborns = breedables+newborns,breedables
    months += 1
printmonth()
print("\nCages will run out in month {}.\n".format(months))
print("-"*31)
