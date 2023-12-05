from src.stages.contracts.extract_contract import ExtractContract, InformationContent


class TransformRawData:
    def __filter_data(
        self, extract_contract: ExtractContract
    ) -> list[InformationContent]:
        extraction_date = extract_contract.extraction_date
        data_content = extract_contract.raw_information_content

        transformed_information = []

        for player_data in data_content:
            if (
                player_data.record
                and player_data.player.lower() != "player"  # noqa: W503
                and player_data.position.lower() == "qb"  # noqa: W503
            ):
                player_data.extraction_date = extraction_date

                transformed_information.append(player_data)

        return transformed_information

    def __sort_list(self, list: list[InformationContent]) -> list[InformationContent]:
        return sorted(list, key=lambda d: d.total_yards, reverse=True)

    def transform(self, data: ExtractContract) -> list[InformationContent]:
        filtered_data = self.__filter_data(data)

        sorted_data_list = self.__sort_list(filtered_data)

        for i, player_data in enumerate(sorted_data_list):
            player_data.rank = i + 1

        return sorted_data_list
