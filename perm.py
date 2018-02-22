word = input("Enter a word: ")
chars = [ch for ch in word]
chars.sort()
word = "".join(chars)
print(word)
