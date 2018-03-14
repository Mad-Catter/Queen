import urllib2
from bs4 import BeautifulSoup


response_IGSM = urllib2.urlopen('https://www.azlyrics.com/lyrics/queen/imgoingslightlymad.html')
html = response_IGSM.read()
soup = BeautifulSoup(html,'html.parser')
print soup.get_text()	

def cleaner(semiclean, songname):
	startlyric = 'Queen Lyrics




	"%s"' % (songname)

	stoplyric = "if  ("

	
	pass

tomato = str(soup.get_text())

