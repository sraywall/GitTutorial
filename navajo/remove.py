f = open("English.csv")
for line in f.readlines():
	if line != "\n":
		print(line)
