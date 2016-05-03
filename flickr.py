import flickrapi
import webbrowser
import threading

api_key = u'Hello'
api_secret = u'World'


flickr = flickrapi.FlickrAPI(api_key, api_secret, format='json')

print('Step 1: authenticate')

# Only do this if we don't have a valid token already
if not flickr.token_valid(perms='read'):

    # Get a request token
    flickr.get_request_token(oauth_callback='oob')

    # Open a browser at the authentication URL. Do this however
    # you want, as long as the user visits that URL.
    authorize_url = flickr.auth_url(perms=u'read')
    webbrowser.open_new_tab(authorize_url)

    # Get the verifier code from the user. Do this however you
    # want, as long as the user gives the application the code.
    verifier = unicode(raw_input('Verifier code: '))

    # Trade the request token for an access token
    flickr.get_access_token(verifier)

print('Step 2: use Flickr')

answer_0 = flickr.test.login()


import json
raw_json = flickr.people.getPhotos(user_id=u'user_foo', per_page=500)
parsed = json.loads(raw_json.decode('utf-8'))
total_pages_nubmer = parsed["photos"]["pages"]

print('step 3: got page number')
print total_pages_nubmer

class getURLThread( threading.Thread):
    def __init__(self, threadID):
        threading.Thread.__init__(self)
        self.threadID = threadID
    def run(self):
        idfilename = "id/id_" + str(self.threadID) + ".txt"
        urlfilename = "url/url_" + str(self.threadID) + ".txt"
        photoids = []
        with open(idfilename) as f:
            photoids = f.readlines()
        f.close()

        print "length of id list : " + str(len(photoids))
        for i in range(len(photoids)):
            photoids[i] = photoids[i].strip()
            # if photoids[i] == "":
            #     del photoids[i]
        urls = []
        for x in range(len(photoids)):
            the_photoid = photoids[x].strip()
            raw_json = flickr.photos.getInfo(photo_id=the_photoid, extras='url_o')
            parsed = json.loads(raw_json.decode('utf-8'))
            format = parsed["photo"]["originalformat"].encode("utf-8")
            o_secret = parsed["photo"]["originalsecret"].encode("utf-8")
            farmid = parsed["photo"]["farm"]
            serverid = parsed["photo"]["server"].encode("utf-8")
            the_url = "https://farm" + str(farmid) + ".staticflickr.com/" + serverid + "/" + the_photoid + "_" + o_secret + "_o." + format
            # print the_url
            urls.append(the_url)


        urlFile = open(urlfilename, "w")
        for s in urls:
            urlFile.write("%s\n" % s)
        urlFile.close()

# threads = []
# for i in range(total_pages_nubmer):
#     t = getURLThread( i+1 )
#     t.start()
#     threads.append(t)
#
# for t in threads:
#     t.join()

print('step 4: got all the original url')

for filenumber in range(9,total_pages_nubmer):
    idfilename = "id/id_" + str(filenumber+1) + ".txt"
    urlfilename = "url/url_" + str(filenumber+1) + ".txt"
    photoids = []
    with open(idfilename) as f:
        photoids = f.readlines()
    f.close()

    print "length of id list : " + str(len(photoids))
    for i in range(len(photoids)):
        photoids[i] = photoids[i].strip()
        # if photoids[i] == "":
        #     del photoids[i]
    urls = []
    for x in range(len(photoids)):
        print str(filenumber) + "  " + str(x)
        print photoids[x]
        the_photoid = photoids[x].strip()
        raw_json = flickr.photos.getInfo(photo_id=the_photoid, extras='url_o')
        parsed = json.loads(raw_json.decode('utf-8'))
        format = parsed["photo"]["originalformat"].encode("utf-8")
        o_secret = parsed["photo"]["originalsecret"].encode("utf-8")
        farmid = parsed["photo"]["farm"]
        serverid = parsed["photo"]["server"].encode("utf-8")
        the_url = "https://farm" + str(
            farmid) + ".staticflickr.com/" + serverid + "/" + the_photoid + "_" + o_secret + "_o." + format
        # print the_url
        urls.append(the_url)

    urlFile = open(urlfilename, "w")
    for s in urls:
        urlFile.write("%s\n" % s)
    urlFile.close()

print "End"
