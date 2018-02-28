import urllib.request
import sys
import requests
from bs4 import BeautifulSoup as bs

def extract_source(url):
    # User agent for the website
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'}
    r = requests.get(url, headers=headers)
    return r

def extract_data(source):
    f = open('flickrPhotoRES_FULL.txt','w')
    s_page = bs(source.content, "lxml")
    linksFound = 0

    for link in s_page.findAll("script"):
        for keyWord in {"q","t","s","m","n","z","c","l","h","k"}:
            strg = str(link)
            res = strg.find("\""+keyWord+"\":") # must work on other id's
            start = "url\":"
            strg = strg[strg[res:].find(start)+res:]
            end = strg.find(",")
            strg = strg[6:end-1].replace("\\","")
            if len(strg) > 1:
                linksFound+=1
                f.write(strg+"\n")
                print(strg)

    print("\nImage links found: ",linksFound)
    f.close()

if len(sys.argv) > 1:
    print("\nSource: "+sys.argv[1]+"\n")
    extract_data(extract_source(sys.argv[1]))
else:
    print("You must pass in an argument.")