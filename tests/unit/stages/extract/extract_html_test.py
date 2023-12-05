import pytest
from unittest.mock import patch
from src.stages.extract.extract_html import ExtractHtml
from src.stages.contracts.extract_contract import ExtractContract
from src.drivers.http_requester import HttpRequester
from src.drivers.html_collector import HtmlCollector
from tests.mocks.htttp_requester import mock_request_from_page
from tests.mocks.essential_information import essetial_information


def test_extract():
    with patch.object(
        HtmlCollector,
        "collect_essential_information",
    ) as html_collector, patch.object(
        HttpRequester, "request_from_page", return_value=mock_request_from_page()
    ) as http_requester:
        html_collector.collect_essential_information.return_value = essetial_information

        extract_html = ExtractHtml(http_requester, html_collector)

    response = extract_html.extract()

    assert isinstance(response, ExtractContract)


def test_extract_error():
    http_requester = "Error"
    html_collector = HtmlCollector()

    with pytest.raises(Exception) as extract_error:
        ExtractHtml(http_requester, html_collector).extract()

    assert isinstance(extract_error.value, Exception)
