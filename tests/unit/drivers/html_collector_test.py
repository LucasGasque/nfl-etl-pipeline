from src.drivers.html_collector import HtmlCollector
from tests.mocks.htttp_requester import mock_request_from_page


def test_collect_essential_information():
    http_request_response = mock_request_from_page()

    html_collector = HtmlCollector()

    essential_information = html_collector.collect_essential_information(
        http_request_response["html"]
    )

    assert isinstance(essential_information, list)
    assert isinstance(essential_information[0], dict)
    assert "Rk" in essential_information[0]
    assert "Player" in essential_information[0]
