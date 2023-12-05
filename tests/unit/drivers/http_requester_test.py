from src.drivers.http_requester import HttpRequester


def test_requeste_from_page(requests_mock):
    url = "https://www.pro-football-reference.com/years/2020/passing.htm"
    reponse_context = "<h1>Olá Mundo</h1>"
    requests_mock.get(url, status_code=200, text=reponse_context)

    http_requester = HttpRequester()

    response = http_requester.request_from_page()

    assert response.status_code == 200
    assert response.html == reponse_context
