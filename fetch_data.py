# -*- coding: utf-8 -*-
import urllib2
from bs4 import BeautifulSoup
import re
#The comment at the top of the program allows python to properly encode non-ASII characters.
#I'm importing urllib2 to access the sites to take lyrics from.  Because urllib2 copies everything from a site including code, I have to import bs4 to clean up the text.  I'm importing re because bs4 doesn't
#properly get rid of all the code in the text(probably because I'm using it wrong).  So I'm using re to selectivly take the bits of text I want from the site.

def cleaner(link, songname):
	#The link_finder through soup I basically just ripped off of the Beautiful Soup webpage.  So I'm afraid I dont know much on how it works.  The "encode('utf-8')" is more instructions for python on how to
	#encode the non-ASII characters, 
	link_finder = urllib2.urlopen('%s' % (link))
	link_opener = link_finder.read()
	soup = BeautifulSoup(link_opener,'html.parser')
	semi_clean = soup.get_text().encode('utf-8')

	#The site I'm using to acquire the lyrics is called "azlyrics".  The semi_clean string still has lots of code I don't want, so narrowing the text down to just the lyrics and the code in them is necessary.
	#The azlyrics always starts the song with "songname lyrics" and then ends it with several new lines.  I'm using these to get the lyrics alone.
	startlyric = '"%s" lyrics' % (songname)

	stoplyric = """

"""
	#Pray starts of by searching for startlyric and discards everything before startlyric in the text.  Then re kicks in.  Re searches for any character in that long list after the first %s and then adds it to
	#group(0).  If anything it finds a character that isn't in the list, not add it.  It will continue adding and discarding until it reaches stoplyric.  So then group(0) holds all of the text lyrcics we want
	#without the code inside them.
	pray = re.search(r'%s[a-z|\s|A-Z|\d|\"|\'|\-|\?|!|\,|\.|\(|\)|\[|\]|\{|\}|\—|ë]+%s' % (startlyric,stoplyric), semi_clean)
	if pray:
		#Group(0) is not a string, but putting it into a string with %s is a convoluted way to make it a string.
		zlines = '%s' % pray.group(0)
		#I'm replacing some of the non-ASCII characters that I've encountered on azlyrics.  So that when I move into run.py I dont have to mess around with encoding there.
		zlines.replace("—","-").replace("ë","e")
		return zlines