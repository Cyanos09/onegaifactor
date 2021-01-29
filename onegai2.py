from urllib import request
from bs4 import BeautifulSoup
import re
n = input("put a number: ")

url = 'http://factordb.com/index.php?query='+str(n)
print(url)
response = request.urlopen(url)
soup = BeautifulSoup(response,"lxml")
response.close()

tables = soup.findAll("table")
scr = []
count = 0
for table in tables:
    for r in table.findAll('tr'):
        if(count == 1):
            d = r.findAll("td")
            scr.append(str(d))
    count+=1

data = scr[2].split(",")

factmp = ''
for i,factor in enumerate(data):
    if(i==2):
        factmp = factor
       
faclist = []
faclist = factmp.split("</a>")
faclist2 = []

for fac in faclist:
    print(fac)
    if("index.php?id=" in fac) and (")^" not in fac):
        faclist2.append((re.search('">.+<',fac).group()))
    elif("index.php?id=" in fac):
        faclist2.append((re.search('\)^.+',fac).group()))


for fact in faclist2:
    #if("^" in fac):
    #    fact = fact.replace('"><font color="#002099">','')
    print(fact)
    fact = fact.replace('"><font color="#002099">','')
    fact = fact.replace('"><font color="#000000">','')
    print(fact.rstrip('<'))

