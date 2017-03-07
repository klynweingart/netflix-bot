from Telegram_bot import *


class Netflix_and_chill_bot(Telegram_bot):
    
    def __init__(self, Token):
        super(Netflix_and_chill_bot, self).__init__(Token)
        
	
	def add_movie(self, bot, update, args):
		
		## TO - DO
		
		## add_function to actual bot.
		self.add_function(self.add_movie, "add")
		
	def get_movies(self):
		## TO - DO
		
		
		## add_function to actual bot.
		self.add_function(self.get_movies, "get")


## Initialize bot by http token given by Telegram    
token = "345755230:AAGtmDv9w6MsDFePYsjUdCvhqObT8-NIPYw"        
bot = Netflix_and_chill_bot(token)

## Set-up start message (using super-class function)
start_message = ''' Hi there ! I'm a bot designed for NetflixAndChill's hardest task, choosing what to watch !
        talk to me for help!'''
        
bot.define_start_message(start_message)


## Set-up error handling message (non-existing function called)
## ATENTION ! ERROR MESSAGE SHOULD ALWAYS BE AT LAST !
error_message = "Sorry, I didn't understand that command."
bot.define_error_message(error_message)


## START RUNNING
bot.run()
