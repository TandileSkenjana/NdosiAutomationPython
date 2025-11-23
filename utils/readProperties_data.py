import configparser

config=configparser.RawConfigParser()
config.read("./Configurations/data.ini")

class ReadCongig_data():

    def getURLS(self):
        return config.get('URLS','dev_url')





