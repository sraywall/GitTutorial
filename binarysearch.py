#binarysearch.py find something binarly
from random import randint

def search(x, nums):
    low = 0
    high = len(nums) - 1
    while low <= high:
        mid = (low + high) // 2
        item = nums[mid]
        if x == item:
            return mid
        elif x < item:
            high = mid - 1
        else:
            low = mid + 1
    return -1
if __name__ == "__main__":
    size = 1000000
    while True:
        size += 1000000
        x = randint(0,size)
        nums = list(range(size))
        print("Testing list of size:",size)
        print("Found at index",search(x,nums))
