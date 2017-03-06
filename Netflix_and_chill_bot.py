from Telegram_bot import *


class Netflix_and_chill_bot(Telegram_bot):
    
    def __init__(self, Token):
        super(Netflix_and_chill_bot, self).__init__(Token)
        

    
token = "345755230:AAGtmDv9w6MsDFePYsjUdCvhqObT8-NIPYw"        
bot = Netflix_and_chill_bot(token)

start_message = ''' Hi there ! I'm a bot designed for NetflixAndChill's hardest task, choosing what to watch !
        talk to me for help!'''
bot.define_start_message(start_message)



