#euclid.py
# this program takes two numbers m and n
# and then finds the greatest common divisor

def main():
    n = int(input("Enter a number n: "))
    m = int(input("Enter a number m: "))
    while m != 0:
        n, m = m, n%m
        #n, m = m, n % m

    print("GCD is",n)

if __name__ == "__main__":
    main()
