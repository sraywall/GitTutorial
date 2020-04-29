f = open("tblNavajo.csv")
for line in f.readlines():
	if line != "\n":
		print(line)
