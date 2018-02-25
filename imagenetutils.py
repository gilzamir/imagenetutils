import urllib.request
import os

GET_SYNSETSURLS_TEMPLATE = "http://www.image-net.org/api/text/imagenet.synset.geturls?wnid={}"
GET_SYNSETSURLS_BBOX = "http://www.image-net.org/api/download/imagenet.bbox.synset?wnid={}"

'''
	Get synset with WordNet ID how shown in http://image-net.org/download-imageurls.
'''
def get_urls(synsetWNID):
	url = GET_SYNSETSURLS_TEMPLATE.format(synsetWNID)
	response = urllib.request.urlopen(url)
	data = response.read()
	text = data.decode("utf8").split('\n')
	return list(filter(lambda x: len(x)>0, list(map(lambda l: l.strip(), text))))

'''
	Download images from location url and save in local file system.
'''
def download_image(url, path):
	try:
		urllib.request.urlretrieve(url, path);
		return True	
	except:
		return False

def fetch_synset_box(wnid):
	urls = get_urls(wnid)
	id = 0
	path = "bbox/{}_{}.{}".format(wnid, "{}", "{}")
	for url in urls:
		if showProgress:
			if os.system("clear") != 0 :
				os.system("cls")
			print("*"*(id+1))
		
		ext = url.split(".")[-1]
		if (not download_image(url, path.format(id, ext))) and showProgress:
			print("It is not possible dowload image {}".format(url))

		id = id + 1

def fetch_images(wnid, showProgress=None):
	urls = get_urls(wnid)
	id = 0
	path = "images/{}_{}.{}".format(wnid, "{}", "{}")
	for url in urls:
		if showProgress:
			print("-*"*(id+1))
		
		ext = url.split(".")[-1]
		if (not download_image(url, path.format(id, ext))) and showProgress:
			print("It is not possible dowload image {}".format(url))

		id = id + 1

		if showProgress:
			if os.system("clear") != 0 :
				os.system("cls")
