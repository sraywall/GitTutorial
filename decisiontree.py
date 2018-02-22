from random import *
def max4(x1,x2,x3,x4):
    maxval = x4
    if x1 >= x2:
        if x1 >= x3:
            if x1 >= x4:
                maxval = x1
        elif x3 >= x4:
            maxval = x3
    elif x2 >= x3:
        if x2 >= x4:
            maxval = x2
    else:
        if x3 >= x4:
            maxval = x3
    return maxval


def main():
    x1,x2,x3,x4 = eval(input("Enter 4 numbers: "))
    print("Max: ",max4(x1,x2,x3,x4))

def test():
    for i in range(100):
        x1,x2,x3,x4 = randint(1,100),randint(1,100),randint(1,100),randint(1,100)
        assert max4(x1,x2,x3,x4) == max(x1,x2,x3,x4), "{} {} {} {}".format(x1,x2,x3,x4)

if __name__ == "__main__":
    main()
