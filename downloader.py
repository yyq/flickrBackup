import urllib
from multiprocessing import Pool
from multiprocessing.dummy import Pool as ThreadPool
import datetime
import os
import time

for i in range(17,30):
    number = i + 1

    os.mkdir("photos/" + str(number) + "/")

    print str(number) + ": begins: "
    print "start time"
    starttime = datetime.datetime.now()
    print starttime
    urlfilename = "url/url_" + str(number) + ".txt"
    urls = []
    with open(urlfilename) as f:
        urls = f.readlines()
    f.close()

    def downloadimage( url ):
        remote_addr = url.strip()
        local_addr = "photos/" + str(number) +"/" + remote_addr.split("/")[-1]
        # print remote_addr + "===>" +local_addr
        try:
            urllib.urlretrieve(remote_addr, local_addr)
        except (urllib.ContentTooShortError, IOError), e:
            print remote_addr + " failed and we try download it again in 3 seconds."
            time.sleep(3)
            urllib.urlretrieve(remote_addr, local_addr)


    pool = ThreadPool(20)
    result = pool.map(downloadimage, urls)

    print "end time"
    endtime = datetime.datetime.now()
    print endtime
    print "Duration:"
    print (endtime-starttime).seconds

# 300 photos by Nikon D7000
# 20 threads   283 seconds
# 18 threads   315 seconds
# 10 threads   428 seconds
# 25 threads   349 seconds
