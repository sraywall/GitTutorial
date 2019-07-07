#!/usr/bin/python3
from fantasyinventory import displayInventory

def addToInventory(inventory, addedItems):
    for i in addedItems:
        num = inventory.setdefault(i,0)
        inventory[i] = num + 1
        
def main():
    inv = {'gold coin': 42, 'rope': 1}
    dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
    addToInventory(inv, dragonLoot)
    displayInventory(inv)

if __name__ == "__main__":
    main()
