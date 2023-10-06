from abc import ABC, abstractmethod
from typing import Union


class HttpRequesterInterface(ABC):
    @abstractmethod
    def request_from_page(self) -> dict[str, Union[int, str]]:
        ...
