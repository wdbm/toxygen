import platform
import json
import os


class Settings(object):

    def __init__(self):
        self.path = Settings.get_default_path() + 'toxygen.json'
        with open(self.path) as fl:
            data = fl.read()
        self.data = json.loads(data)

    def __get__(self, attr):
        return self.data[attr]

    def save(self):
        text = json.dumps(self.data)
        with open(self.path, 'w') as fl:
            fl.write(text)

    @staticmethod
    def get_default_path():
        name = platform.system()
        if name == 'Linux':
            return os.getenv('HOME') + '/.config/tox/'
        elif name == 'Windows':
            return os.getenv('APPDATA') + '/Tox/'

