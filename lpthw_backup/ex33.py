numbers = []
def appendlist(stop,step, arr):
    i = 0
    for i in range(0,stop,step):
        print(f"At the top i is {i}")
        arr.append(i)

        i = i + 1
        print("Numbers now: ", arr)
        print(f"At the bottom i is {i}")

appendlist(6,1, numbers)
print("The numbers: ")

for num in numbers:
    print(num)
