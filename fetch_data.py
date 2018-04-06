# -*- coding: utf-8 -*-
import urllib2
from bs4 import BeautifulSoup
import re


def cleaner(link, songname, compiledsong):
	#The link_finder through semi_clean I basically just ripped off of the Beautiful Soup webpage.
	link_finder = urllib2.urlopen('%s' % (link))
	link_opener = link_finder.read()
	soup = BeautifulSoup(link_opener,'html.parser')
	semi_clean = soup.get_text().encode('utf-8')

	#This only works with the site azlyrics.  They always start their actual lyrics with the song name lyrics and end it with several new lines.
	startlyric = '"%s" lyrics' % (songname)

	stoplyric = """

"""
	#Pray searches for the start lyric and then continously searches for any letters (a-z), any numbers (\d), any white spaces (\s), or any punctuation (everything else there) until it reaches the several new
	#lines that signify the end of the song.
	pray = re.search(r'%s[a-z|\s|A-Z|\d|\"|\'|\-|\?|!|\,|\.|\(|\)|\[|\]|\{|\}|\—|ë]+%s' % (startlyric,stoplyric), semi_clean)
	if pray:
		zlines = '%s' % pray.group(0)
		zlines.replace("—","-").replace("ë","e")
		compiledsong.append(zlines)