#!/usr/bin/python3

def lister(l):
    return ", ".join(l[:-1]) + ' and ' + l[-1]

if __name__ == '__main__':
    print(lister(['apples','bannanas','tofu','cats']))
