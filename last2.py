from sys import argv
def last2(str):
	for i in range(len(str)-2):
		for j in range(i+1,len(str)-3):
			if str[i:i+2] == str[j:j+2]:
				print(str[i:i+2])

if __name__ == "__main__":
	last2(argv[1])
