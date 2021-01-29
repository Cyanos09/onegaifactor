from urllib import request
from bs4 import BeautifulSoup
import re

def prepare():
    n = input("put a number: ")
    url = 'http://factordb.com/index.php?query='+str(n)
    id = ""
    print(url)
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
    print(data)
    printfactor(data)

    
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
    faclist2 = []
    for fac in faclist:
        #print(fac)
        if("index.php?id=" in fac):
            if("..." in fac):
                bigfactor(fac)
            else:
                faclist2.append((re.search('">.+<',fac).group()))

    for fact in faclist2:
        fact = fact.replace('"><font color="#002099">','')
        fact = fact.replace('"><font color="#000000">','')
        #print()
        print(fact.rstrip('<'))


if __name__ == '__main__':
    url = prepare()
    soup = scraping(url)
    tables = soup.findAll("table")
    scr = find(tables)
    data = scr[2].split(",")
    print(data)
    printfactor(data)
