from abc import ABC, abstractmethod
import requests


class HttpMethods(ABC):
    @abstractmethod
    def get(self, url: str, params: dict = None, headers: dict = None) -> dict:
        pass

    @abstractmethod
    def post(self, url: str, params: dict = None, headers: dict = None, body: object = None) -> dict:
        pass

    @abstractmethod
    def patch(self, url: str, params: dict = None, headers: dict = None, body: object = None) -> dict:
        pass

    @abstractmethod
    def delete(self, url: str, params: dict = None, headers: dict = None) -> dict:
        pass