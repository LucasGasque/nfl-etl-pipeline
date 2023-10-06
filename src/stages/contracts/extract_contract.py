from pydantic import BaseModel
from datetime import date


class ExtractContract(BaseModel):
    raw_information_content: list[dict]
    extraction_date: date = date.today()
