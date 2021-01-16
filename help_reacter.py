from telebot import types
from base_reacter import BaseReacter
from constants import KEYWORDS, HELP_INFO


class HelpReacter(BaseReacter):
    def __init__(self):
        super().__init__()

    def need_react(self, message : types.Message):
        if message.text:
            return message.text.lower() == KEYWORDS.get('help', None)
        return False

    def reaction(self, message : types.Message, bot):
        bot.send_message(message.chat.id, HELP_INFO)