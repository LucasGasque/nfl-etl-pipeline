import requests
from typing import Union


class HttpRequester:
    def __init__(self) -> None:
        self.__url = "https://www.pro-football-reference.com/years/2020/passing.htm"

    def request_from_page(self) -> dict[str, Union[int, str]]:
        response = requests.get(self.__url)

        return {"status_code": response.status_code, "html": response.text}
