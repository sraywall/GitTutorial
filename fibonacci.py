# fibonaci.py
# accepts a number and gives the corresponding
# fibonacci value for that index

def main():
    n = int(input("Enter a number: "))
    prev = 1
    curr = 1
    n -= 1
    if n == 0:
        print(prev)
    elif n == 1:
        print(curr)
    else:
        for i in range(1,n):
           temp = prev
           prev = curr
           curr += temp
        print(curr)

if __name__ == "__main__":
    main()
