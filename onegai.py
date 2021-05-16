from urllib import request
from bs4 import BeautifulSoup
import re

def prepare():
    n = input("put a number: ")
    url = 'http://factordb.com/index.php?query='+str(n)
    id = ""
    return url

def scraping(url):
    response = request.urlopen(url)
    soup = BeautifulSoup(response,"lxml")
    response.close()
    return soup

def bigfactor(fac):
    urltmp = 'http://factordb.com/index.php?showid='
    id = re.search('id=.+"><',fac).group()
    id = id.lstrip('id=')
    id = id.rstrip('"><')
    urltmp += str(id)
    soup = scraping(urltmp)
    tables = soup.findAll("table")
    scr = find(tables)
    data = scr[2].split(",")
    data = re.findall(r"\d+",data[1])
    return ''.join(data)

def expfactor(fac):
    exp = re.findall('(\d+) =',fac)
    return exp[0]

def find(tables):
    scr = []
    count = 0
    for table in tables:
        for r in table.findAll('tr'):
            if(count == 1):
                d = r.findAll("td")
                scr.append(str(d))
        count+=1
    return scr

def printfactor(data):
    factmp = ''
    for i,factor in enumerate(data):
        if(i==2):
            factmp = factor

    faclist = []
    faclist = factmp.split("</a>")
    formed_faclist = []
    search = re.search('">.+<',faclist.pop(0)).group()
    search = search.rstrip('<')
    for fac in faclist:
        if("index.php?id=" in fac):
            if("..." in fac):
                formed_faclist.append(bigfactor(fac))
            elif (")^" in fac):
                formed_faclist.append(search + "^" + expfactor(fac))
                break
            else:
                formed_faclist.append((re.search('">.+<',fac).group()))

    for fact in formed_faclist:
        fact = re.sub('"><font color="#\d+">','',fact)
        print(fact.rstrip('<'))


if __name__ == '__main__':
    url = prepare()
    soup = scraping(url)
    tables = soup.findAll("table")
    scr = find(tables)
    data = scr[2].split(",")
    print("---------------------------------------------------------------------")
    printfactor(data)
