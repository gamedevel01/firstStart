class BaseReacter:
    reacters = []
    def __init__(self):
        BaseReacter.reacters.append(self)

    def need_react(self, message):
        return False

    def reaction(self, message, bot):
        return