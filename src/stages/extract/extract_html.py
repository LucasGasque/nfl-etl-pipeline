from src.drivers.interfaces.http_requester import HttpRequesterInterface
from src.drivers.interfaces.html_collector import HtmlCollectorInterface
from src.stages.contracts.extract_contract import ExtractContract


class ExtractHtml:
    def __init__(
        self,
        http_requester: HttpRequesterInterface,
        html_collector: HtmlCollectorInterface,
    ) -> None:
        self.__http_requester = http_requester
        self.__html_collector = html_collector

    def extract(self) -> ExtractContract:
        html_information = self.__http_requester.request_from_page()

        essential_information = self.__html_collector.collect_essential_information(
            html_information.get("html")
        )

        return ExtractContract(
            raw_information_content=essential_information,
        )
