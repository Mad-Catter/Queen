import urllib2
from bs4 import BeautifulSoup
import re


def cleaner(link, songname):
	response_IGSM = urllib2.urlopen('%s' % (link))
	html = response_IGSM.read()
	soup = BeautifulSoup(html,'html.parser')
	tomato = str(soup.get_text())
	print tomato
	


	startlyric = '"%s" lyrics' % (songname)

	stoplyric = "if  \("

	normie = re.compile(r"%s[a-z|\s|A-Z|\n]+ %s" % (startlyric, stoplyric))
	norm_match = normie.finditer(tomato)
	for match in norm_match:
		print match.span()
		print match.group(0)
		print match
		print norm_match.group(0)
		print("Is this even triggering?")
	print norm_match
	print 0x05BB8110

	pray = re.search(r'%s[a-z|\s|A-Z|\n|\"|\'|\-|\?|!|\,]+%s' % (startlyric,stoplyric), tomato)
	if pray:
		print pray.group(0)
	else:
		print("No match")
	print normie
	#print(r"%s[.|\s]+ %s" % (startlyric, stoplyric))


	pass


cleaner("https://www.azlyrics.com/lyrics/queen/imgoingslightlymad.html","I\'m Going Slightly Mad")