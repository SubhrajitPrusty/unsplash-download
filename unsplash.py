# script to download photos from unsplash
import sys

from bs4 import BeautifulSoup
import requests
import os

if len(sys.argv) > 1:
	tag = sys.argv[1]
	link = "https://unsplash.com/search/photos/"+tag

	print("Downloading images for {}...".format(tag))

	with requests.get(link) as r:
		html = r.content
		soup = BeautifulSoup(html, "html.parser")
		allImages = [x.get("src") for x in soup.findAll("img")]
		images = [x.split("?")[0] for x in allImages if "images.unsplash.com" in x]
		# wget the files
		for x in images:
			os.system("wget --no-check-certificate -c -P photos/{} {}".format(tag, x))

	# the files are without any extension

	os.chdir("photos/"+tag)
	files = os.listdir(".")
	for f in files:
		if not f.endswith(".jpg"):
			os.rename(f,f+".jpg")
else:
	print("Enter tag.\nUsage: python unsplash.py tag\n")