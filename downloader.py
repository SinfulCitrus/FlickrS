import urllib.request
import pathlib
import sys
import os
import errno

def main():
    f = open('flickrPhotoRES_FULL.txt','r')
    newPath = os.getcwd()+'/images'
    pathlib.Path(newPath).mkdir(parents=True, exist_ok=True)
    os.chdir(newPath)
    count = 0
    for url in f:
        urllib.request.urlretrieve(url,'img'+str(count)+'.jpg')
        count+=1
    f.close()

if __name__ == "__main__":
    main()