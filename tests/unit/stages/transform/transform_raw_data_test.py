from src.stages.transform.transform_raw_data import TransformRawData
from tests.mocks.extract_contract import extract_contract_mock


def test_filter_data():
    response = TransformRawData()._TransformRawData__filter_data(extract_contract_mock)

    assert len(response) == 2


def test_sort_list():
    response = TransformRawData()._TransformRawData__sort_list(
        extract_contract_mock.raw_information_content
    )

    assert response[0].total_yards > response[1].total_yards


def test_transform():
    transform_raw_data = TransformRawData()

    transformed_data = transform_raw_data.transform(extract_contract_mock)

    assert transformed_data[0].rank == 1 and transformed_data[0].player == "Tom Brady"
    assert transformed_data[1].rank == 2 and transformed_data[1].player == "Bom Trady"
    assert transformed_data[0].extraction_date
