import urllib2
from bs4 import BeautifulSoup
import re


def cleaner(link, songname):
	response_IGSM = urllib2.urlopen('%s' % (link))
	html = response_IGSM.read()
	soup = BeautifulSoup(html,'html.parser')
	tomato = str(soup.get_text())
	print tomato
	


	startlyric = '''Queen Lyrics




"%s"''' % (songname)

	stoplyric = "if  \("

	normie = re.compile(r"%s[.|\s]+ %s" % (startlyric, stoplyric))
	norm_match = normie.finditer(tomato)
	for match in norm_match:
		print match
	print normie
	print(r"%s[.|\s]+ %s" % (startlyric, stoplyric))


	pass


cleaner("https://www.azlyrics.com/lyrics/queen/imgoingslightlymad.html","I'm Going Slightly Mad")