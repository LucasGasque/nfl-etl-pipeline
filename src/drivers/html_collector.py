from bs4 import BeautifulSoup


class HtmlCollector:
    @classmethod
    def collect_essential_information(cls, html: str) -> list[dict[str, str]]:
        soup = BeautifulSoup(html, "html.parser")

        players_stats_table = soup.find(class_="table_container").find("table")

        trs = players_stats_table.find("thead").find("tr")

        column_names = [th.text for th in trs.find_all("th")]

        player_table_rows = players_stats_table.find("tbody").find_all("tr")

        essential_information = []

        for row in player_table_rows:
            columns = row.find_all(["th", "td"])

            columns_texts = [collumn.text for collumn in columns]

            if columns_texts:
                row_dict = dict(zip(column_names, columns_texts))

                essential_information.append(row_dict)

        return essential_information
