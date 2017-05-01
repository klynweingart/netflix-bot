# -*- coding: utf-8 -*-
from Telegram_bot import *
from db import DBMS
from omdb import omdb


class Netflix_and_chill_bot(Telegram_bot):
    ## Constructor using superclass
    def __init__(self, Token):
        super(Netflix_and_chill_bot, self).__init__(Token)
        self.name = "NetflixAndChillBot"
        self.version = "3.0"
        self.db = DBMS.DBMS()

    def add_movie_to_db(self, movie_name, category, update):
        if category == "NULL":
            row = (update.message.chat_id, self.get_movie_id(movie_name), movie_name)
            return self.db.insert_film(row, False)
        else:
            row = (update.message.chat_id, self.get_movie_id(movie_name), movie_name, category)
            return self.db.insert_film(row, True)

    def delete_movie_from_db(self, movie_name, update):
        movie_id = self.get_movie_id(movie_name)  # TODO fix / get real ID
        row = (update.message.chat_id, movie_id, movie_name)
        return self.db.delete_film(row)

    def get_priority(self, movie_name):
        return 1  # TODO Fix in a proper way...

    def get_movie_id(self, movie_name):
        return hash(movie_name)  # TODO fix / get real ID

    def add_movie(self, bot, update, args):
        message = ' '.join(args)
        category = "NULL"

        # users last word with caps means adding a category!
        if len(args) > 1:
            if args[-1] == args[-1].upper():  # is written in caps?
                category = args[-1]
                movie_name = ' '.join(args[:-1])

        if category == "NULL":
            movie_name = ' '.join(args)

        film_id = self.get_movie_id(movie_name)

        correctly_added = self.add_movie_to_db(movie_name, category, update)

        if not correctly_added:
            text_answer = "<< " + movie_name + " >>" + " already in your watchlist (or maybe a database problem)!"
            bot.sendMessage(chat_id=update.message.chat_id, text= text_answer)
            return

        movie_found = self.respond_with_movie(bot, update, movie_name)
        if not movie_found:
            bot.sendMessage(chat_id=update.message.chat_id, text='Unable to find <<' + movie_name +
                                                                 '>> in IMDB database, but it has still been added to your list!')
            return

        if category != "NULL":
            text_answer = "<< " + movie_name + " >>" + " added to your watchlist inside the category: " + category + "!"
        else:
            text_answer = "<< " + movie_name + " >>" + " added to your watchlist without category!"

        bot.sendMessage(chat_id=update.message.chat_id, text=text_answer)

    def respond_with_movie(self, bot, update, movie_name):
        chat_id = update.message.chat_id
        film = omdb.get_film_by_title(movie_name)
        if film:
            text = 'For request ' + movie_name + ', found:'
            bot.sendMessage(chat_id=chat_id, text=text)
            bot.sendMessage(chat_id=chat_id, text='Title: ' + film.get_title() + '\nGenre: ' + film.get_genre() +
                                                  '\nIMDB Rating: ' + film.get_imdb_rating() + '\nDescription: ' + film.get_description())
            bot.sendPhoto(chat_id=chat_id, photo=film.get_poster())
            return True
        else:
            return False

    def get_info(self, bot, update, args):
        movie_name = ' '.join(args)
        self.respond_with_movie(bot, update, movie_name)

    def delete_movie(self, bot, update, args):
        movie_name = ' '.join(args)
        correctly_deleted = self.delete_movie_from_db(movie_name, update)

        if correctly_deleted:
            text_answer = "<< " + movie_name + " >>" + " removed from watchlist!"
        else:
            text_answer = "<< " + movie_name + " >>" + " not in watchlist!"

        bot.sendMessage(chat_id=update.message.chat_id, text=text_answer)

    def tell_bernardo_i_want(self, bot, update, args):
        text_answer = "Bernardo, Katelyn says she wants " + ' '.join(args) + " ;)"
        bot.sendMessage(chat_id=update.message.chat_id, text=text_answer)

    def tell_Katelyn_i_want(self, bot, update, args):
        text_answer = "Katelyn, Bernardo says he wants " + ' '.join(args) + " ;)"
        bot.sendMessage(chat_id=update.message.chat_id, text=text_answer)

    ## Main function #2, displays some (one or more ? ) movies to the user.
    def get_all_movies(self, bot, update, args):
        message = ' '.join(args)

        bot_text = "Here are all your movies-to-watch! \n"
        for movie in self.db.get_rows(update.message.chat_id, 10000, ""):
            bot_text += "* " + movie + '\n'

        bot.sendMessage(chat_id=update.message.chat_id, text=bot_text)

    ## Main function #2, displays some (one or more ? ) movies to the user.
    def get_movies(self, bot, update, args):
        message = ' '.join(args)
        try:
            if len(message) == 0:
                number_of_movies = 1
                pass
            else:
                number_of_movies = int(message[0])
        except ValueError:
            bot.sendMessage(chat_id=update.message.chat_id, text=" \
			You should add a number after the get command...")
            return
        if len(args) > 2:
            bot.sendMessage(chat_id=update.message.chat_id, text=" \
			This function accepts two arguments as maximum...")
            return
        elif len(args) == 2:
            category = args[1]
            bot_text = "Here they are! the next " + category + " " + str(number_of_movies) + \
                       " movies to watch ! \n"
        else:
            category = ""
            bot_text = "Here they are! the next " + str(number_of_movies) + \
                       " movies to watch ! \n"
        for movie in self.db.get_rows(update.message.chat_id, number_of_movies, category):
            bot_text += "* " + movie + '\n'

        bot.sendMessage(chat_id=update.message.chat_id, text=bot_text)

    ## List of functions to add to the bot!
    def add_functions(self):
        ## Receives as parameter the name of the function and the command
        self.add_function(self.add_movie, "add")
        self.add_function(self.delete_movie, "delete")
        self.add_function(self.get_info, "getinfo")
        self.add_function(self.get_movies, "get")
        self.add_function(self.get_all_movies, "getall")
        self.add_function(self.tell_bernardo_i_want, "tellBernardoIWant")
        self.add_function(self.tell_Katelyn_i_want, "tellKatelynIWant")


# ------------------------------------------------------------#
## Initialize bot by http token given by Telegram    
token = "345755230:AAGtmDv9w6MsDFePYsjUdCvhqObT8-NIPYw"
bot = Netflix_and_chill_bot(token)
# ------------------------------------------------------------#

## Set-up start message (using super-class function)
start_message = '''Hi there :P I'm a bot designed for NetflixAndChill's \
hardest task, choosing what to watch! Talk to me for help!'''
bot.define_start_message(start_message)
# ------------------------------------------------------------#
## Set-up of functions
bot.add_functions()
# ------------------------------------------------------------#
## Set-up error handling message (non-existing function called)
## ATENTION ! ERROR MESSAGE SHOULD ALWAYS BE AT LAST !
error_message = "Sorry, I didn't understand that command."
bot.define_error_message(error_message)
# ------------------------------------------------------------#

## START RUNNING
bot.run()

# ------------------------------------------------------------#
