

import urllib
from bs4 import BeautifulSoup
import re


def fetch_data(Url):
	url = Url
	html = urllib.request.urlopen(url).read()
	soup = BeautifulSoup(html,'lxml')
	text = soup.get_text()

	# break into lines and remove leading and trailing space on each
	lines = (line.strip() for line in text.splitlines())
	# break multi-headlines into a line each
	chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
	# drop blank lines
	text = '\n'.join(chunk for chunk in chunks if chunk)
	return text
	