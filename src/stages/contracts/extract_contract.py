from pydantic import BaseModel, Field, validator
from datetime import date


class InformationContent(BaseModel):
    rank: int = Field(alias="Rk")
    player: str = Field(alias="Player")
    team: str = Field(alias="Tm")
    age: int = Field(alias="Age")
    position: str = Field(alias="Pos")
    games: int = Field(alias="G")
    games_started: int = Field(alias="GS")
    record: str = Field(alias="QBrec")
    completed: int = Field(alias="Cmp")
    attempted: int = Field(alias="Att")
    completion_percentage: float = Field(alias="Cmp%")
    total_yards: int
    touchdowns: int = Field(alias="TD")
    touchdowns_percentage: float = Field(alias="TD%")
    interceptions: int = Field(alias="Int")
    interceptions_percentage: float = Field(alias="Int%")
    first_down_passes: int = Field(alias="1D")
    passing_success_rate: float = Field(alias="Succ%")
    longest_completed_pass: float = Field(alias="Lng")
    yards_per_pass_attempt: float = Field(alias="Y/A")
    adjusted_yards_per_pass_attempt: float = Field(alias="AY/A")
    yards_per_pass_completed: float = Field(alias="Y/C")
    yards_per_game: float = Field(alias="Y/G")
    rate: float = Field(alias="Rate")
    QBR: float
    times_sacked: int = Field(alias="Sk")
    yards_lost_due_to_sacks: int = Field(alias="Yds")
    times_sacked_percentage: float = Field(alias="Sk%")
    net_yards_per_pass_attempt: float = Field(alias="NY/A")
    adjusted_net_yards_per_pass_attempt: float = Field(alias="ANY/A")
    fourth_quater_comeback: int = Field(alias="4QC")
    game_winning_drive: int = Field(alias="GWD")
    extraction_date: date | None = None

    @validator(
        "rank",
        "age",
        "games",
        "games_started",
        "completed",
        "attempted",
        "total_yards",
        "touchdowns",
        "interceptions",
        "first_down_passes",
        "times_sacked",
        "yards_lost_due_to_sacks",
        "fourth_quater_comeback",
        "game_winning_drive",
        pre=True,
    )
    def convert_to_int(cls, v):
        try:
            return int(v)
        except ValueError:
            return 0

    @validator(
        "completion_percentage",
        "touchdowns_percentage",
        "interceptions_percentage",
        "passing_success_rate",
        "longest_completed_pass",
        "yards_per_pass_attempt",
        "adjusted_yards_per_pass_attempt",
        "yards_per_pass_completed",
        "yards_per_game",
        "rate",
        "QBR",
        "times_sacked",
        "times_sacked_percentage",
        "net_yards_per_pass_attempt",
        "adjusted_net_yards_per_pass_attempt",
        pre=True,
    )
    def convert_to_float(cls, v):
        try:
            return float(v)
        except ValueError:
            return 0


class ExtractContract(BaseModel):
    raw_information_content: list[InformationContent]
    extraction_date: date = date.today()


class RestResponse(BaseModel):
    status_code: int
    html: str
