#!/usr/bin/python3
# pw.py - An insecure password locker program.
import sys
from pyperclip import copy

PASSWORDS = {"email": "F7minlBDDuvMJuxESSKHFhTxFtjVB6",
        "blog": "VmALvQyKAxiVH5G8vo1if1MLZF3sdt",
        "luggage": "12345"}

def main():
    if len(sys.argv) < 2:
        print("Usage: python pw.py [account] - copy account password")
        sys.exit()

    
    account = sys.argv[1] # first command line arg is the account name

    if account in PASSWORDS:
        copy(PASSWORDS[account])
        print("Password for {} copied to clipboard.".format(account))
    else:
        print("There is no account named",account)

if __name__ == "__main__":
    main()
