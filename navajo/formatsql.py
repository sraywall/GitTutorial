import pymysql
def main():	
	f = open("English.csv",mode='r+',encoding='UTF-8')
	contents = f.readline()
	line = f.readline()
	i = 0
	contents += "\n<item>"
	while line:
		i += 1
		line = line.split('\t')
		contents += "\n"+pymysql.escape_string("('{}','{}','{}'),".format(\
		line[0],line[1].replace("'","''"),\
		line[2].replace("'","''")))
		line = f.readline()
	f.close()
	f = open("English.tsv",mode="w", encoding='UTF-8')
	f.write(contents)
	f.close()



if __name__ == "__main__":
	main()
