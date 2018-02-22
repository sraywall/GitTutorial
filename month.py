months = "JanFedMarAprMayJunJulAugSepOctNovDec"
def getAbbrev(pos):
    pos = (pos - 1) * 3
    monthAbbrev = months[pos:pos+3]
    return monthAbbrev
def main():
    num = int(input("Enter the number of the month: "))
    print("The abbreviation for",num,"is",getAbbrev(num))

main()
