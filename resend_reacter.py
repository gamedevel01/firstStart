import urllib
from telebot import types
from base_reacter import BaseReacter


class ResendReacter(BaseReacter):
    def __init__(self):
        super().__init__()

    def need_react(self, message : types.Message):
        return message.caption == 'test'

    @staticmethod
    def download(message : types.Message, bot, path):
        photo = message.photo[-1]
        photo_path = bot.get_file(photo.file_id).file_path
        downloaded_file = bot.download_file(photo_path)
        filename = '{}/{}'.format(path, photo_path.split('/')[-1])
        with open(filename, 'wb') as img:
            img.write(downloaded_file)
        return filename

    def reaction(self, message : types.Message, bot):
        path = self.download(message, bot, 'images')
        bot.send_photo(message.chat.id, path, 'hi bro')
