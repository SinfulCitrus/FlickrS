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
    f = open('flickrPhotoRES.txt','w')
    s_page = bs(source.content, "lxml")
    import re
    print("\n")
    for link in s_page.find_all(src=re.compile(".jpg")):
        print(link, "\n")
        res = str(link).split("\"")
        f.write("https:"+res[7]+"\n")
    f.close()

if len(sys.argv) > 1:
    print(sys.argv[1])
    extract_data(extract_source(sys.argv[1]))
else:
    print("You must pass in an argument.")