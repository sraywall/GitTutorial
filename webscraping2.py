import requests
import pickle as pkl
from bs4 import BeautifulSoup
import operator


#print(page.status_code)

#print(soup.prettify())
hacks = []
for i in range(1,100):
    url = "https://www.romhacking.net/homebrew/{}".format(i)
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    table = soup.find('table')
    d = {}
    print(i)                
    if table:
        trs = table.find_all('tr')
        if len(trs) >= 1:
            for tr in trs:
                th = tr.find('th')
                if th:
                    td = tr.find('td').get_text()
                    th = th.get_text()
                    if th == 'Downloads':
                        td = int(td)
                    #print(th.get_text(),'\t',td.get_text())
                    d[th] = td
                else:
                    pass
                    #center = tr.find(class_='center').find_all('div')
                    #name = center[0].get_text()
                    #d['Name'] = name
                    #hackof = center[1].get_text()
                    
                    #print(hackof)
                    #d['Hack of'] = hackof
                    
        d['url'] = url
        hacks.append(d)

hacks.sort(key=operator.itemgetter('Downloads'), reverse = True)
pkl.dump(hacks, open('homebrew.p',"wb"))
#print(hacks[3])
#for h in hacks:
#    print(h['url'],'\tName: ',h['name'],'\tHack of: ',h['Hack of'])
            
