import urllib2
from bs4 import BeautifulSoup
import re


def cleaner(link, songname):
	link_finder = urllib2.urlopen('%s' % (link))
	link_opener = link_finder.read()
	soup = BeautifulSoup(link_opener,'html.parser')
	semi_clean = str(soup.get_text())
	print semi_clean
	startlyric = '"%s" lyrics' % (songname)

	stoplyric = """

"""
	pray = re.search(r'%s[a-z|\s|A-Z|\"|\'|\-|\?|!|\,|\.|\(|\)]+%s' % (startlyric,stoplyric), semi_clean)
	if pray:
		print pray.group(0)
	else:
		print("No match")
	pass