import requests
import re
from urlfinder import URL_REGEX
from bs4 import BeautifulSoup
import time
import datetime

today = datetime.date.today().isoformat()

def fwrite(s, filename='this.txt',fresh=False): # an added variable `fresh` for appending links to the same file
    if not fresh:
        f = open(filename,'a+')
    else:
        f = open(filename,'w+')

    if type(s)==list:
        for foo in s:
            f.write("%s\n"%str(foo))
    # elif isinstance(s,unicode):
    #         f.write(s)
    else:
            f.write(s.encode("utf-8"))
    f.close()


def get_links(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text,"lxml")

    tpaper = soup.find_all("div", class_="tpaper")
    # print tpaper
    tpaper_links = re.findall(URL_REGEX,str(tpaper))

    # tpaper_links =  [t.find('a')['href'] for t in tpaper if t is not None]
    # fwrite(tpaper_links)
    return tpaper_links


def build_hindu(date=today):

    url = 'http://www.thehindu.com/todays-paper/tp-index/?date=' + str(date)
    print url
    all_links = get_links(url)

    print "getting all links ... "
    now = datetime.datetime.now()
    filename = now.strftime("%Y-%m-%d %H-%M-%S")+ ".txt"
    fwrite(all_links,filename)

    return all_links

if __name__ == '__main__':
    build_hindu()
