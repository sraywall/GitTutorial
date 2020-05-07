def main():
    word = input("Enter a word to permute: ")
    perm(word,len(word))

def perm(word,n):
    if n == 0:
        print (word)
        return
    for i in range(n):
        word2 =  word[:i]+word[i+1:]+ word[i:i+1]
        perm(word2,n-1)
        
        
        
        
    
if __name__ == "__main__":
    main()
