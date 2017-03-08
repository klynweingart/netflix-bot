# -*- coding: utf-8 -*-
from Telegram_bot import *
from netflix_list import *
from db import DBMS

class Netflix_and_chill_bot(Telegram_bot):
    
    ## Constructor using superclass
	def __init__(self, Token):
		super(Netflix_and_chill_bot, self).__init__(Token)
		self.name = "NetflixAndChillBot"
		self.version = "1.0"
		self.db = DBMS.DBMS()
	
	def add_movie_to_db(self, movie_name, update):
		row = (update.message.chat_id, self.get_movie_id(movie_name), movie_name)
		self.db.insert_film(row)

	def delete_movie_from_db(self, movie_name, update):
		movie_id = get_movie_id(movie_name) # TODO fix / get real ID
		row = (update.message.chat_id, movie_id, movie_name)
		return self.db.delete_film(row)

	def get_priority(self, movie_name):
		return 1 # TODO Fix in a proper way...

	def get_movie_id(self, movie_name):
		return hash(movie_name)  # TODO fix / get real ID

	def add_movie(self, bot, update, args):
		movie_name = ' '.join(args)
		film_id = self.get_movie_id(movie_name)

		row = (update.message.chat_id, film_id, movie_name)
		film_existed = self.db.film_exists(row)

		if film_existed:
			text_answer = "<< " + movie_name + " >>" + " already in watchlist!"
		else:
			self.add_movie_to_db(movie_name, update)
			text_answer = "<< " + movie_name + " >>" + " added to your watchlist!"

		bot.sendMessage(chat_id=update.message.chat_id, text=text_answer)


	def delete_movie(self, bot, update, args):
		movie_name = ' '.join(args)
		film_existed = self.delete_movie_from_db(movie_name, update)

		if not film_existed:
			text_answer = "<< " + movie_name + " >>" + " not in watchlist!"
		else:
			text_answer = "<< " + movie_name + " >>" + " removed from watchlist!"

		bot.sendMessage(chat_id=update.message.chat_id, text=text_answer)
		
	def tell_bernardo_i_want(self, bot, update, args):
		text_answer = "Bernardo, Katelyn says she wants " + ' '.join(args) + " ;)"
		bot.sendMessage(chat_id=update.message.chat_id, text=text_answer)
	
	def tell_Katelyn_i_want(self, bot, update, args):
		text_answer = "Katelyn, Bernardo says he wants " + ' '.join(args) + " ;)"
		bot.sendMessage(chat_id=update.message.chat_id, text=text_answer)
		
	## Main function #2, displays some (one or more ? ) movies to the user.
	def get_movies(self, bot, update, args):
		number_of_movies = ''.join(args)
		try:
			if len(number_of_movies) == 0:
				number_of_movies = 1
				pass
			number_of_movies = int(number_of_movies)
		except ValueError:
			bot.sendMessage(chat_id=update.message.chat_id, text=" \
			You should add a number after the get command...")
			return
		
		bot_text = "Here they are! the next " + str(number_of_movies) + \
		" movies to watch ! \n"
		for movie in self.db.get_rows(update.message.chat_id, number_of_movies):
			bot_text += "* " + movie + '\n'
				
		
		bot.sendMessage(chat_id=update.message.chat_id, text=bot_text)
			
	## List of functions to add to the bot! 	
	def add_functions(self):
		## Receives as parameter the name of the function and the command
		self.add_function(self.add_movie, "add")
		self.add_function(self.delete_movie, "delete")
		self.add_function(self.get_movies, "get")
		self.add_function(self.tell_bernardo_i_want, "tellBernardoIWant")
		self.add_function(self.tell_Katelyn_i_want, "tellKatelynIWant")

		
		
#------------------------------------------------------------#
## Initialize bot by http token given by Telegram    
token = "345755230:AAGtmDv9w6MsDFePYsjUdCvhqObT8-NIPYw"        
bot = Netflix_and_chill_bot(token)
#------------------------------------------------------------#

## Set-up start message (using super-class function)
start_message = '''Hi Kate rofl :P! I'm a bot designed for NetflixAndChill's \
hardest task, choosing what to watch! Talk to me for help!'''
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
