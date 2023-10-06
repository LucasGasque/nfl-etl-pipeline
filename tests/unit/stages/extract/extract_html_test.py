import pytest
from unittest.mock import patch
from src.stages.extract.extract_html import ExtractHtml
from src.stages.contracts.extract_contract import ExtractContract
from src.drivers.http_requester import HttpRequester
from src.drivers.html_collector import HtmlCollector


def test_extract():
    with patch.object(
        HtmlCollector, "collect_essential_information", return_value=[{"key": "value"}]
    ) as html_collector, patch.object(
        HttpRequester, "request_from_page", return_value="<h1>Olá Mundo</h1>"
    ) as http_requester:
        extract_html = ExtractHtml(http_requester, html_collector)

    response = extract_html.extract()

    assert isinstance(response, ExtractContract)


def test_extract_error():
    http_requester = "Error"
    html_collector = HtmlCollector()

    with pytest.raises(Exception) as extract_error:
        ExtractHtml(http_requester, html_collector).extract()

    assert isinstance(extract_error.value, Exception)
