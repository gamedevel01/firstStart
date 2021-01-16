from telegram_bot import TelegramBot
from constants import TOKEN
from help_reacter import HelpReacter
from resend_reacter import ResendReacter


def load_reacters():
    HelpReacter()
    ResendReacter()


def main():

    load_reacters()

    bot = TelegramBot(TOKEN)
    bot.polling(none_stop=None, interval=1)


if __name__ == '__main__':
    main()