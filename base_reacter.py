from telebot import types


class BaseReacter:
    reacters = []
    def __init__(self):
        BaseReacter.reacters.append(self)

    def need_react(self, message : types.Message):
        return False

    def reaction(self, message : types.Message, bot):
        return