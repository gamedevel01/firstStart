from base_reacter import BaseReacter
from telebot import TeleBot


class TelegramBot(TeleBot):
    def __init__(self, token : str):
        super().__init__(token)
        
        @self.message_handler(content_types=['text'])
        def send_answer(message):
            self.send_answer(message)

    def send_answer(self, message):
        for reacter in BaseReacter.reacters:
            if reacter.need_react(message):
                reacter.reaction(message, self)
                return
