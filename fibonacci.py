# fibonaci.py
# accepts a number and gives the corresponding
# fibonacci value for that index

def main():
    n = int(input("Enter a number: "))
    prev = 1
    curr = 1
    if n == 1:
        print("number",n,"fibonacci number is",prev)
    elif n == 2:
        print("number",n,"fibonacci number is",curr)
    else:
        for i in range(1,n-1):
            prev, curr = curr, curr + prev
        print("number",n,"fibonacci number is",curr)

if __name__ == "__main__":
    main()
