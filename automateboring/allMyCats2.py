#!/usr/bin/python3

catNames = []
while True:
    print('Enter the name of cat ' + str(len(catNames) + 1) +
            ' (Or enter nothing to stop.):')
    name = input()
    if name == '':
        break
    catNames.append(name)
print('The cat names are:')

for name in catNames:
    print('  ' + name)