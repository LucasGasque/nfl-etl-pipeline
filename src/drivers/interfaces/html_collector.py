from abc import ABC, abstractmethod


class HtmlCollectorInterface(ABC):
    @abstractmethod
    def collect_essential_information(self, html: str) -> list[dict[str, str]]:
        ...
