# script to download photos from unsplash
import sys

from bs4 import BeautifulSoup
import requests
import os

if len(sys.argv) > 1:
	tag = sys.argv[1]
	if len(sys.argv) > 2:
		limit = int(sys.argv[2])
	else:
		limit = 0
	link = "https://unsplash.com/search/photos/"+tag

	print("Downloading images for {}...".format(tag))
	r=requests.get(link)
	html=r.content
	soup = BeautifulSoup(html, "html.parser")
	if limit:
		allImages = [x.get("src") for x in soup.findAll("img")][:limit]
	else:
		allImages = [x.get("src") for x in soup.findAll("img")]
	images = [x.split("?")[0] for x in allImages if "images.unsplash.com" in x and "profile" not in x]
	# wget the files
	for x in images:
		os.system("wget -q --no-check-certificate -c -P photos/{} {}".format(tag, x))

	# the files are without any extension

	os.chdir("photos/"+tag.split()[0])
	files = os.listdir(".")
	for f in files:
		if not f.endswith(".jpg"):
			os.rename(f,f+".jpg")
else:
	print("Enter tag.\nUsage: python unsplash.py tag\n")
