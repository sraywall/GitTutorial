#text2numbers.py
# A program to convert a textual messge into a sequence of
# numbers, utilizing the unterlying Unicode encoding.

def main():
    print("This program converts a textual message into a sequence")
    print("of numbers representing the Unicode encoding of the message.\n")

    #Get the message to encode
    message = input("\nHere are the Unicode codes:")

    # Loop through the messge and print out the Unicode values
    for ch in message:
        print(ord(ch),end=" ")

    print() # blank line before prompt

main()
