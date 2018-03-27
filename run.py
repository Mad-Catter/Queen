from markov_python.cc_markov import MarkovChain
from fetch_data import cleaner

songs = []

cleaner("https://www.azlyrics.com/lyrics/queen/imgoingslightlymad.html","I\'m Going Slightly Mad", songs) 
cleaner("https://www.azlyrics.com/lyrics/queen/dontstopmenow.html","Don\'t Stop Me Now", songs)
cleaner("https://www.azlyrics.com/lyrics/queen/wewillrockyou.html", "We Will Rock You", songs)
cleaner("https://www.azlyrics.com/lyrics/queen/sheerheartattack.html", "Sheer Heart Attack", songs)
cleaner("https://www.azlyrics.com/lyrics/queen/youtakemybreathaway.html", "You Take My Breath Away", songs)
cleaner("https://www.azlyrics.com/lyrics/queen/iwantitall.html","I Want It All", songs)
cleaner("https://www.azlyrics.com/lyrics/queen/theshowmustgoon.html", "The Show Must Go On", songs)
cleaner("https://www.azlyrics.com/lyrics/queen/killerqueen.html", "Killer Queen", songs)
cleaner("https://www.azlyrics.com/lyrics/queen/bohemianrhapsody.html","Bohemian Rhapsody", songs)
cleaner("https://www.azlyrics.com/lyrics/queen/anotheronebitesthedust.html", "Another One Bites The Dust", songs)
victory = MarkovChain()
for song in songs:
	victory.add_string(str(songs))
	print victory.generate_text(200)

