months = 576
rent = 0
properties = 0
saved = 0
for i in range(months):
    if (i + 1) % 12 == 0:
        properties += 1
    rent += properties * 100
    saved += 250 

print("rent",rent,"properties",properties,"saved",saved)

