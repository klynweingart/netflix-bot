class Telegram_bot(object):
	
	def __init__(self, Token):
		from telegram.ext import Updater
		self.updater = Updater(token = Token)
		self.dispatcher = self.updater.dispatcher
		import logging
		logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
     
	def define_start_message(self, message):
		def start(bot, update):
			bot.sendMessage(chat_id=update.message.chat_id, text=message)
			
		from telegram.ext import CommandHandler
		start_handler = CommandHandler('start', start)
		self.dispatcher.add_handler(start_handler)
		self.run()

	def run(self):
		self.updater.start_polling()
