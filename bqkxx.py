from bs4 import BeautifulSoup
import requests, time
target = 'http://www.biqukan.com/1_1094'
server = 'http://www.biqukan.com'
req = requests.get(url = target)
html = req.text
div_bf = BeautifulSoup(html, "html.parser")
div = div_bf.find_all('div', class_ = 'listmain')
a_bf = BeautifulSoup(str(div[0]), "html.parser")
a = a_bf.find_all('a')

def writer(name, path):
    req = requests.get(url = path)
    html = req.text
    bf = BeautifulSoup(html, "html.parser")
    texts = bf.find_all('div', class_ = 'showtxt')
    try:
        texts = texts[0].text.replace('\xa0'*8,'\n\n')
        fo = open(name+ ".txt","w")
        fo.write(texts)
        fo.close()
    except:
        pass
    print(name, path)
    
#for each in a[16:-4]:
for each in a[16:117]:
    writer(each.string, server+each.get("href"))
    


