def convert(s, numRows):
    matrix = [[] for i in range(numRows)]
    i = 0
    while len(s) > 0:
        #down
        while len(s) > 0 and i < numRows:
            ch = s[0]
            matrix[i].append(ch)
            i += 1
            s = s[1:]
        if s == "":
            break
        #zag
        i = numRows - 2
        while len(s) > 0 and i >= 1:
            ch = s[0]
            matrix[i].append(ch)
            i -= 1
            s = s[1:]

    print("".join([ "".join(row) for row in matrix]))

if __name__ == "__main__":
    convert("PAYPALISHIRING",4)

