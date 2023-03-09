import requests
from bs4 import BeautifulSoup
import pprint

def sort_stories_by_votes(hnlist):
    return sorted(hnlist,key=lambda x: x['votes'],reverse=True)

def create_custom_hn(links,subtext):
    hn = []
    for idx,item in enumerate(links):
        title = item.getText()
        href = item.get('href',None)
        vote = subtext[idx].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points',''))
            if points>=100:
                hn.append({'title':title,'link':href,'votes':points})
    return hn

ls=[]
nrpages=int(input("Number of pages: "))
for i in range(nrpages):
    res=requests.get('https://news.ycombinator.com/news?p='+str(i+1))
    soup=BeautifulSoup(res.text,'html.parser')
    links=soup.select('.titleline > a')
    subtext = soup.select('.subtext')
    ls.extend(create_custom_hn(links,subtext))
pprint.pprint(sort_stories_by_votes(ls))