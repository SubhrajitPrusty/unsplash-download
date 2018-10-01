# script to download photos from unsplash
import sys

from bs4 import BeautifulSoup
import requests
import os

if len(sys.argv) > 1:
	tag = sys.argv[1]
	link = "https://unsplash.com/search/photos/"+tag

	print("Downloading images for {}...".format(tag))
	os.chdir("photos/")
	with requests.get(link) as r:
		html = r.content
		soup = BeautifulSoup(html, "html.parser")
		allImages = [x.get("src") for x in soup.findAll("img")]
		images = [x.split("?")[0] for x in allImages if "images.unsplash.com" in x]
		# wget the files
		counter=0
		for x in images:
			r=requests.get(x)
			open(str(counter)+'.jpg', 'wb').write(r.content)
			counter+=1

	# the files are without any extension

	files = os.listdir(".")
	for f in files:
		if not f.endswith(".jpg"):
			os.rename(f,f+".jpg")
else:
	print("Enter tag.\nUsage: python unsplash.py tag\n")