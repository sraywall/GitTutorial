#!/usr/bin/python3
def main():	
	f = open("tblNavajo.tsv",mode='r+',encoding='UTF-8')
	contents = f.read()
	contents = contents.replace('\uf101','\u0105\u0301')\
		.replace('\uf103','\u0119\u0301')\
		.replace('\uf105','\u00ed\u0328')\
		.replace('\uf107','\u00f3\u0328')\
		.replace('_x000d_','')
	f.close()
	f = open("tblNavajo.csv",mode="w", encoding='UTF-8')
	f.write(contents)
	f.close()

if __name__ == "__main__":
	main()
