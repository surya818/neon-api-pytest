from framework.http.HttpClientImpl import HttpClientImpl
import os
import configparser
class BaseService:
    def __init__(self):
        config = configparser.ConfigParser()
        config.read('tests/config.properties')
        self.http_client = HttpClientImpl()
        config = configparser.ConfigParser()
        config_file_path = os.path.join(os.path.dirname(__file__), '..', '..', 'resources', 'testdata.properties')
        print('File exists: '+config_file_path + " : "+str(os.path.exists(config_file_path)))
        config.read(config_file_path)
        base_url = config.get('TEST', 'base_url')
        print("BASE URL: " + config.get('TEST', 'base_url'))
        self.base_url = base_url

   