from src.drivers.http_requester import HttpRequester
from src.drivers.html_collector import HtmlCollector
from src.stages.contracts.extract_contract import ExtractContract


class ExtractHtml:
    def __init__(
        self,
        http_requester: HttpRequester,
        html_collector: HtmlCollector,
    ) -> None:
        self.__http_requester = http_requester
        self.__html_collector = html_collector

    def extract(self) -> ExtractContract:
        html_information = self.__http_requester.request_from_page()

        essential_information = self.__html_collector.collect_essential_information(
            html_information.html
        )

        return ExtractContract.parse_obj(
            {"raw_information_content": essential_information}
        )
