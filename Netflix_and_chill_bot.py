from Telegram_bot import *


class Netflix_and_chill_bot(Telegram_bot):
    
    ## Constructor using superclass
	def __init__(self, Token):
		super(Netflix_and_chill_bot, self).__init__(Token)
		self.name = "NetflixAndChillBot"
		
	## Main function #1, adds a movie to the To-Watch list
	def add_movie(self, bot, update, args):
		movie_name = ''.join(args)
		bot.sendMessage(chat_id=update.message.chat_id, text="Now I'm supossed to add a movie called " + movie_name)
		## TO - DO
		
		
	## Main function #2, displays some (one or more ? ) movies to the user.
	def get_movies(self, bot, update, args):
		bot.sendMessage(chat_id=update.message.chat_id, text="Now I'm supossed show you some options...")
		## TO - DO
			
	## List of functions to add to the bot! 	
	def add_functions(self):
		## Receives as parameter the name of the function and the command
		self.add_function(self.add_movie, "add")
		self.add_function(self.get_movies, "get")
#------------------------------------------------------------#
## Initialize bot by http token given by Telegram    
token = "345755230:AAGtmDv9w6MsDFePYsjUdCvhqObT8-NIPYw"        
bot = Netflix_and_chill_bot(token)
#------------------------------------------------------------#

## Set-up start message (using super-class function)
start_message = ''' Hi there ! I'm a bot designed for NetflixAndChill's hardest task, choosing what to watch !
        talk to me for help!'''
bot.define_start_message(start_message)
#------------------------------------------------------------#
## Set-up of functions
bot.add_functions()
#------------------------------------------------------------#
## Set-up error handling message (non-existing function called)
## ATENTION ! ERROR MESSAGE SHOULD ALWAYS BE AT LAST !
error_message = "Sorry, I didn't understand that command."
bot.define_error_message(error_message)
#------------------------------------------------------------#

## START RUNNING
bot.run()

#------------------------------------------------------------#
