import configparser

config = configparser.RawConfigParser()
filepath = "G:\\OrangeHRM\\configuration\\config.ini"
config.read(filepath)

class Readconfig:
    @staticmethod
    def GetUserName():
        username = config.get('common data', 'Username')
        return username

    @staticmethod
    def GetPassword():
        password = config.get('common data', 'Password')
        return password