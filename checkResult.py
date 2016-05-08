import urllib
from os import listdir
from os.path import isfile, join
import time



total_page_number = 31

for i in range(1, total_page_number+1):

    url_file_name = "url/url_" + str(i) + ".txt"
    urls = []
    with open(url_file_name) as f:
        urls = f.readlines()
    f.close()


    photo_path = "photos/"+str(i)+"/"
    onlyfiles = [f for f in listdir(photo_path) if isfile(join(photo_path, f))]

    if len(urls) == len(onlyfiles):
        print "the number of url and the number of files are the same: " + str(len(urls))
    else:
        print "let's find the different on the number: " + str(i)

    for a_url in urls:
        filename = a_url.split("/")[-1].strip()
        indexnumber = filename in onlyfiles
        if indexnumber == False:
            print filename

            remote_addr = a_url.strip()
            local_addr = photo_path + filename
            print remote_addr
            print local_addr

            try:
                urllib.urlretrieve(remote_addr, local_addr)
            except (urllib.ContentTooShortError, IOError), e:
                print remote_addr + " failed and we try download it again in 3 seconds."
                time.sleep(3)
                urllib.urlretrieve(remote_addr, local_addr)
