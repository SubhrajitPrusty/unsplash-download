# script to download photos from unsplash

import sys
from bs4 import BeautifulSoup
import requests
import os
import click


@click.command()
@click.argument("tag", type=click.STRING)
@click.option("--limit", default=0, help="limit the number of photos to get")
def cli(tag, limit):
	tag = tag.replace(" ", "-")  # unsplash preferred
	link = "https://unsplash.com/search/photos/"+tag

	print("Downloading images for {}...".format(tag))
	r = requests.get(link)
	soup = BeautifulSoup(r.content, "html.parser")
	allImages = [x.get("src") for x in soup.findAll("img")]
	images = [x.split(
		"?")[0] for x in allImages if "images.unsplash.com" in x and "profile" not in x and "avatar" not in x]

	print("Found {} images".format(len(images)))

	if limit !=0 and limit < len(images):
		images = images[:limit]
	
	# wget the files
	for x in images:
		os.system(
			"wget -q --no-check-certificate -c -P photos/{} {}".format(tag, x))
		print("Downloaded {}".format(x))

	# the files are without any extension
	os.chdir("photos/"+tag)
	files = os.listdir(".")
	for f in files:
		if not f.endswith(".jpg"):
			os.rename(f, f+".jpg")

	print("\nFiles downloaded into photos/{}".format(tag))
