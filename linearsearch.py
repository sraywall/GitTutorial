#linearsearch.py find something linearly
from random import randint

def search(x, nums):
    try:
        return nums.index(x)
    except:
        return -1

if __name__ == "__main__":
    size = 1000000
    while True:
        size += 1000000
        x = randint(0,size)
        nums = list(range(size))
        print("Testing list of size:",size)
        print("Found at index",search(x,nums))
