from markov_python.cc_markov import MarkovChain
from fetch_data import cleaner
from time import sleep
#I'm importing MarkovChain from the premade code academy markov chain creator, and I'm importing my cleaner from fetch_data.  I'm importing sleep to make the transition to new lines less jarring.
def final():
	#Variables used various times in final are being stored here.  Songs is a list storing the songs used for randomization.  Num is storing the amount of songs inside of songs.  Error is storing the amount of
	#times a user has failed to enter a valid option in a row.  Start and starter are being used as conditions for while loops.
	songs = []
	num = 0
	error = 1
	start = True
	starter = True
	def victory():
		#Mark is just changing the function name to something shorter than MarkovChain. I is being used to store the amount of words added to a song.
		mark = MarkovChain()
		i = 0
		#Add_string adds the list of songs to the generator to create markov chains.  Generate text generates the text.  400 is the limit on song length listed in the while loop and in generate text.
		mark.add_string(str(songs))
		mc = mark.generate_text(400)
		while i < 400:
			#This generates the song in multiples of 7.
			rnglyrics = " ".join(mc[i:i +6])
			i += 7
			#The long list of replacements gets rid of any usless text that gets into the randomly generated lyrics.
			print rnglyrics.replace("\\n"," ").replace("\\'","'").replace("\\r","").replace("queen lyrics","").replace("lyrics","")
	#A welcome message with a sleep to match the pace later in the code.
	sleep(1)
	print """This is a program used for making markov chains out of songs copied from the site azlyrics.  While this program was made specifically with Queen songs in mind, it should work with 
most other songs. (as long as they don't contain non-ASCII characters.)  """
	sleep(2)
	#Almost the entirety of final is within while loops.  This allows me to make the code a bit more user friendly by having the user not have to constantly restart the program.
	while start == True:
		menu = raw_input("\n If you want to see an example of a markov chain song enter T.  If you want to create your own markov chain song enter C.  If you want to exit the program enter X: ")
		#Menu.upper() is just to insure that the code will work even if the user enters lower case letters.
		menu = menu.upper()
		#The test is made of the songs I used when making my code, and I felt too attached to get rid of it.
		#So I reformated it to make it so that it will be able to show the user that the code is working properly.
		if menu == "T":
			sleep(1)
			#Error is the amount of times a user has entered an invalid option.  The reason I keep track of this is so that if a user is having some error with the code/keyboard, they will still have a way
			#to exit the loop.  The amount of errors it takes to kick a user is 3.  Since the user entered a valid option here, the error counter will reset.  THis happens on all valid options.
			error = 1
			print """\n The songs currently used in this test are: Don\'t Stop Me Now, I\'m Going Slightly Mad, We WIll Rock You, Sheer Heart Attack, You Take My Breath Away, I Want It All,
The Show Must Go On, Killer Queen, Bohemian Rhapsody, and Another One Bites The Dust.\n"""
			#These are all of the songs being used in the test.
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
			#Victory calls the generator.  Songs = [] resets the song list to an empty list, so that the test doesnt screw up other things.
			victory()
			songs = []
			sleep(3)
			print "\n"	
	
		elif menu == "C":
			sleep(1)
			error = 1
			#Entering a secondary menu for song creation.
			while starter == True:
				menu2 = raw_input("""\n You have entered %s songs.  If you want to add more songs enter A.
If you want to generate a song with the songs you have currently enter G.  If you want to erase your current list of songs enter E, or if you want to exit the program enter X: """ % (num))
				print "\n"
				menu2 = menu2.upper()
				if menu2 == "A":
					sleep(1)
					error = 1
					#Adding to num to keep track of the songs.
					num += 1
					#Getting the user's songs with raw input, useing cleaner to declutter them, and adding them to the song list.
					copy = raw_input("Please enter the azlyrics link to the song you want to add: ")
					print "\n"
					sleep(1)
					name = raw_input("""Please enter the name of the song you want to enter.
You will need to have exact capitalization, punctuation and spaces, and you will need to put a \\ before any punctuation: """)
					songs.append(cleaner(copy,name))
				elif menu2 == "G":
					error = 1
					#Num < 2 is to keep the generator from making nothing or merely reorganizing a single song.
					if num < 2:
						sleep(1)
						print"I'm sorry, but you must enter atleast two songs to generate a song."
						sleep(1)
					else:
						sleep(3)
						victory()
				elif menu2 == "E":
					#Erasing list is here so that the user doesn't have to restart the program if they want to remove their old songs.  Num = 0 resets the counter and songs = [] resets the entire list.
					print "Erasing list..."
					sleep(2)
					error = 1
					num = 0
					songs = []
				elif menu2 == "X":
					#The proper exit for the second menu.  Setting start to false ends the original loop.  Break is used to end the second loop because it is shorter, than =false.
					sleep(1)
					print"Hope you enjoyed this program!"
					start = False
					break
				elif error >= 3:
					#The improper exit for the second menu. 
					sleep(1)
					print "You have entered an invalid option three times.  The program will now shut down."
					start = False
					break
				else:
					#This resets the loop and adds one to the value of error.
					sleep(1)
					error += 1
					print "I'm sorry thats not a valid option.  If you enter an invalid option three times in a row, the program will shut down."
					sleep(1)
				
			
		elif menu == "X":
			#The proper exit for the first menu.  Break ends the loop.
			sleep(1)
			print"\n Hope you enjoyed this program!"
			break
		elif error >= 3:
			#The improper exit for the second menu.
			sleep(1)
			print "\n You have entered an invalid option three times.  The program will now shut down"
			break
		else:
			#This resets the loop and adds one to the value of error.
			sleep(1)
			print "\n I'm sorry thats not a valid option.  If you enter a invalid option three times in a row, the program will shut down."
			error += 1
			sleep(1)
#This starts the code.
final()