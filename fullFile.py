import urllib.request
import sys
import requests
import time
from bs4 import BeautifulSoup as bs

time_test = 0 # flag for the time performance test

def extract_source(url):
    # User agent for the website
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'}
    r = requests.get(url, headers=headers)
    return r

def extract_data(source,file):

    s_page = bs(source.content, "lxml")
    linksFound = 0
    imageExists = 0 # only looks for the highest res image
    
    if time_test == 1:
        t0 = time.time()
    
    # images are delivered through JS
    for link in s_page.findAll("script",{"class":"modelExport"}):
        for keyword in ['k','h','l','c','z','n','m','s','t','q']:
            
            # look for a specific keyword in the sites source code
            strg = str(link)
            res = strg.find("\""+keyword+"\":")
            start = "url\":"
            strg = strg[strg[res:].find(start)+res:]
            end = strg.find(",")
            strg = strg[6:end-1].replace("\\","")
            
            if len(strg) > 1:
                linksFound+=1
                file.write("https:"+strg+"\n")
                #print(strg)
                imageExists = 1

            if imageExists == 1:
                break

        if imageExists == 1:
            break
    
    if time_test == 1:
        print("\nTime: ",time.time()-t0)

    #print("\nImage links found: ",linksFound)

def getPhoto(id,photo_ids):
    f = open('flickrPhotoRES_FULL.txt','w')
    for pid in photo_ids:
        extract_data(extract_source("https://www.flickr.com/photos/"+str(id)+"/"+str(pid)+"/"),f)
    f.close()