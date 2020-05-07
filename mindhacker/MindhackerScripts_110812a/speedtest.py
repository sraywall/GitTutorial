#!/usr/bin/python3
import time
import os

f = open("multiplication_table.csv");
items = [line.strip().split('\t') for line in f.readlines()]
f.close()
entiretime = 0
for item in items:
    start = time.time()
    a = input(item[0]+": ")
    end = time.time()
    if a == item[1]:
        item[2] = str(int(item[2]) + 1)
    else:
        print("Incorrect!")
        item[3] = str(int(item[3]) + 1)
        input()
    totaltime = (end - start)
    entiretime = totaltime + entiretime
    item[4] = str((float(item[4]) + totaltime))
    item[5] = str(float(item[4])/(float(item[2])+ float(item[3])))
    os.system('clear')

def wrong_slow(element):
    return (element[3],element[5])
f = open("multiplication_table.csv","w+");
items.sort(key = wrong_slow, reverse = True)
for item in items:
    f.write("\t".join(item)+"\n")

print("entire time spent: ",entiretime)
f.close()
