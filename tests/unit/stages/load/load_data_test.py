from sqlmodel import Session
from src.infra.db import engine
from src.infra.models import QbStats
from src.stages.contracts.extract_contract import InformationContent


class LoadData:
    def __init__(self) -> None:
        self.__engine = engine
        self.__model = QbStats

    def __create_object(self, qb_stats: InformationContent) -> QbStats:
        return self.__model(**qb_stats.dict())

    def post_qb_stats(self, qb_stats_lis: list[InformationContent]):
        with Session(self.__engine) as session:
            for qb_stats in qb_stats_lis:
                session.add(self.__create_object(qb_stats))

            session.commit()
