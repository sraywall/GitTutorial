#!/usr/bin/python3

stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        print(str(v).ljust(4),k)
        item_total += v
    # FILL THIS PART IN
    print("Total number of items:",item_total)

def main():
    displayInventory(stuff)

if __name__ == "__main__":
    main()
