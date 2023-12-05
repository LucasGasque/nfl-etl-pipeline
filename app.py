from src.infra.db import create_db_and_tables
from src.main.main_pipeline import MainPipeline


if __name__ == "__main__":
    create_db_and_tables()

    MainPipeline().run_pipeline()
