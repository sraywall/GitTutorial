def main():
    fileName = input("What file are the numbers in? ")
    infile = open(fileName,'r')
    total = 0
    count = 0
    line = infile.readline()
    while line != "":
        # update the total and count for values in line
        for xStr in line.split(","):
            total += float(xStr)
            count += 1
        line = infile.readline()
    print("\nThe average of the numbers is", total / count)

if __name__ == "__main__":
    main()
