import requests
from src.stages.contracts.extract_contract import RestResponse


class HttpRequester:
    def __init__(self) -> None:
        self.__url = "https://www.pro-football-reference.com/years/2020/passing.htm"

    def request_from_page(self) -> RestResponse:
        response = requests.get(self.__url)

        return RestResponse(
            status_code=response.status_code,
            html=response.text,
        )
