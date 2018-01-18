# script to download photos from unsplash

from bs4 import BeautifulSoup
from splinter import Browser
import os

tag = input("Enter tag : ")
link = "https://unsplash.com/search/photos/"+tag

with Browser("firefox",headless=True) as browser:
	browser.visit(link)
	html = browser.html
	soup = BeautifulSoup(html, "html.parser")
	allImages = [x.get("src") for x in soup.findAll("img")]
	images = [x.split("?")[0] for x in allImages if "images.unsplash.com" in x]
	# wget the files
	for x in images:
		os.system("wget --no-check-certificate -c -P photos/ {}".format(x))

# the files are without any extension

files = os.listdir("photos")
for f in files:
	os.rename(f,f+"jpg")