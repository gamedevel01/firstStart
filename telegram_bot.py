from base_reacter import BaseReacter
from telebot import TeleBot
import urllib


class TelegramBot(TeleBot):
    def __init__(self, token : str):
        super().__init__(token)
        
        @self.message_handler(content_types=['text'])
        def send_answer(message):
            self.send_answer(message)

    def send_photo(self, chat_id, path, caption):
        with open(path, 'rb') as img:
            self.send_photo(chat_id, img, caption=caption)

    def send_photo_by_url(self, chat_id, url, caption = None):
        if url is None:
            return False
        with open('temp.out', 'wb') as img:
            img.write(urllib.request.urlopen(url).read())
        self.send_photo(chat_id, 'temp.out', caption)
        return True

    def send_answer(self, message):
        for reacter in BaseReacter.reacters:
            if reacter.need_react(message):
                reacter.reaction(message, self)
                return
