from telegram_bot import TelegramBot
from constants import TOKEN
from help_reacter import HelpReacter


def load_reacters():
    HelpReacter()


def main():

    load_reacters()

    bot = TelegramBot(TOKEN)
    bot.polling(none_stop=None, interval=1)


if __name__ == '__main__':
    main()