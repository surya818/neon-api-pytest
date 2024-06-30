from abc import ABC, abstractmethod

from requests import Response

from framework.http.HttpMethods import HttpMethods
import requests


class HttpClientImpl(HttpMethods):
    def patch(self, url: str, params: dict = None, headers: dict = None, body: object = None) -> Response:
        headers.update({"Accept": "application/json"})
        headers.update({"Content-Type": "application/json"})
        response = requests.patch(url, params=params, headers=headers, data=body)
        print("Response: " + str(response.json()))
        return response

    def get(self, url: str, params: dict = None, headers: dict = None) -> Response:
        headers.update({"Accept": "application/json"})
        response = requests.get(url, params=params, headers=headers)
        return response

    def delete(self, url: str, params: dict = None, headers: dict = None) -> Response:
        headers.update({"Accept": "application/json"})
        response = requests.delete(url, params=params, headers=headers)
        return response

    def post(self, url: str, params: dict = None, headers: dict = None, body: object = None) -> Response:
        headers.update({"Accept": "application/json"})
        headers.update({"Content-Type": "application/json"})
        response = requests.post(url, params=params, headers=headers, data=body)
        print("Response: " + str(response.json()))
        return response
