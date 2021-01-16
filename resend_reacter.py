from base_reacter import BaseReacter


class ResendReacter(BaseReacter):
    def __init__(self):
        super().__init__()

    def need_react(self, message):
        return message.text == 'тест'

    def reaction(self, message, bot):
        url = 'images/asia.jpeg'
        bot.send_photo(message.chat.id, url, 'хэлоу бразерс')