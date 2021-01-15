from base_reacter import BaseReacter
from constants import KEYWORDS, HELP_INFO


class HelpReacter(BaseReacter):
    def __init__(self):
        super().__init__()

    def need_react(self, message):
        return message.text.lower() == KEYWORDS.get('help', None)

    def reaction(self, message, bot):
        bot.send_message(message.chat.id, HELP_INFO)