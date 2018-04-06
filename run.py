from markov_python.cc_markov import MarkovChain
from fetch_data import cleaner
#I'm importing MarkovChain from the premade code academy markov chain creator, and I'm importing my cleaner from fetch_data.

#The list songs will be used for storing all of the lyrics for randomization.
songs = []

#These are all the songs I'm currently using.  Calling cleaner to get the lyrics and then putting them all into the songs list.
songs.append(cleaner("https://www.azlyrics.com/lyrics/queen/imgoingslightlymad.html","I\'m Going Slightly Mad")) 
songs.append(cleaner("https://www.azlyrics.com/lyrics/queen/dontstopmenow.html","Don\'t Stop Me Now"))
songs.append(cleaner("https://www.azlyrics.com/lyrics/queen/wewillrockyou.html", "We Will Rock You"))
songs.append(cleaner("https://www.azlyrics.com/lyrics/queen/sheerheartattack.html", "Sheer Heart Attack"))
songs.append(cleaner("https://www.azlyrics.com/lyrics/queen/youtakemybreathaway.html", "You Take My Breath Away"))
songs.append(cleaner("https://www.azlyrics.com/lyrics/queen/iwantitall.html","I Want It All"))
songs.append(cleaner("https://www.azlyrics.com/lyrics/queen/theshowmustgoon.html", "The Show Must Go On"))
songs.append(cleaner("https://www.azlyrics.com/lyrics/queen/killerqueen.html", "Killer Queen"))
songs.append(cleaner("https://www.azlyrics.com/lyrics/queen/bohemianrhapsody.html","Bohemian Rhapsody"))
songs.append(cleaner("https://www.azlyrics.com/lyrics/queen/anotheronebitesthedust.html", "Another One Bites The Dust"))

#Victory is just changing the function name to something barely shorter than MarkovChain.
victory = MarkovChain()


i =0
victory.add_string(str(songs))
mc = victory.generate_text(400)
while i < 400:
	lasso =" ".join(mc[i:i +6])
	i +=7
	lasso = str(lasso)
	print lasso.replace("\\n"," ").replace("\\'","'").replace("\\r","").replace("queen lyrics","").replace("lyrics","")