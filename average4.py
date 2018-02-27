# average4.py

def main():
    arr = []
    while True:
        try: 
            arr.append(int(input("Enter a number :")))
        except ValueError:
            break
    print("Average:",sum(arr)/len(arr))

if __name__ == "__main__":
    main()
