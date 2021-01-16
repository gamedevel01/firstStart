from base_reacter import BaseReacter
from telebot import TeleBot
import urllib


class TelegramBot(TeleBot):
    def __init__(self, token : str):
        super().__init__(token)
        
        @self.message_handler(content_types=['text'])
        def send_answer(message):
            self.send_answer(message)

    @staticmethod
    def is_url(path):
        return ('http://' in path) or ('https://' in path)

    def send_photo(self, chat_id, path, caption):
        if self.is_url(path):
            super().send_photo(chat_id, path, caption)
        else:
            with open(path, 'rb') as img:
                super().send_photo(chat_id, img, caption=caption)

    def send_answer(self, message):
        for reacter in BaseReacter.reacters:
            if reacter.need_react(message):
                reacter.reaction(message, self)
                return
