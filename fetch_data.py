import urllib2
from bs4 import BeautifulSoup	

def cleaner(link, songname):
	response_IGSM = urllib2.urlopen('%s' % (link))
	html = response_IGSM.read()
	soup = BeautifulSoup(html,'html.parser')
	tomato = str(soup.get_text())
	print tomato
	startlyric = 'Queen Lyrics "%s"' % (songname)

	stoplyric = "if  ("



	pass


cleaner("https://www.azlyrics.com/lyrics/queen/imgoingslightlymad.html","I'm Going Slightly Mad")