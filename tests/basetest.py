import os
from framework.http.HttpClientImpl import HttpClientImpl


class BaseTest:
    def setup_method(self):
        self.http_client = HttpClientImpl()
        self.access_token = os.getenv('APIKEY')
