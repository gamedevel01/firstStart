import json


KEYWORDS = {
    'help': 'помощь'
}

HELP_INFO = 'при нажатии на кнопку помощь, появляется список возможных действий'

with open('settings/config.json') as config:
    data = json.load(config)
    TOKEN = data['token']