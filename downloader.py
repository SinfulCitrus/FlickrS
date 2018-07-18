import urllib.request
import pathlib
import json
import sys
import os
import errno
import fullFile

# takes the photo urls stored in flickrPhotoRES_FULL.txt and downloads them to a dir /images
def download():
    f = open('flickrPhotoRES_FULL.txt','r')
    newPath = os.getcwd()+'/images'
    pathlib.Path(newPath).mkdir(parents=True, exist_ok=True)
    os.chdir(newPath)
    count = 0
    for url in f:
        urllib.request.urlretrieve(url,'img'+str(count)+'.jpg')
        count+=1
    f.close()

# given a user id returns a list of all the photo id's
def get_json_photo(id):

    page_num = 1    # number of pages of images
    per_page = 10   # number of images per page     THESE NUMBERS ARE LOW AS THIS SCRIPT IS QUITE SLOW AT THE MINUTE
    page_limit = False

    photo_ids = list()
    while not page_limit:
        api_link = "https://api.flickr.com/services/rest/?method=flickr.people.getPhotos&api_key=cf7c3c09f36b8243029b6b322400c817&user_id="+str(id)+"&per_page="+str(per_page)+"&page="+str(page_num)+"&format=json&nojsoncallback=1"
        with urllib.request.urlopen(api_link) as url:
            data = json.loads(url.read().decode())
            print("Page: "+str(page_num))
            for inf in data['photos']['photo']:
                photo_ids.append(inf['id'])
            if data['photos']['pages'] is page_num or page_num is 10:   # change for more pages
                page_limit = True
            else:
                page_num+=1
    return photo_ids

# given a user profile name returns the user id
def get_json_name(name):
    api_link = "https://api.flickr.com/services/rest/?method=flickr.people.findByUsername&api_key=cf7c3c09f36b8243029b6b322400c817&username="+str(name)+"&format=json&nojsoncallback=1"
    with urllib.request.urlopen(api_link) as url:
        data = json.loads(url.read().decode())
        return data['user']['id']

def main():
    if len(sys.argv) > 1:
        print("\nSource: "+sys.argv[1]+"\n")
        name = get_json_name(sys.argv[1])
        fullFile.getPhoto(name, get_json_photo(name))
        download()
    else:
        print("You must pass in an argument.")

if __name__ == "__main__":
    main()