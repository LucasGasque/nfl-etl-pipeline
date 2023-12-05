from sqlmodel import Field, SQLModel

from datetime import date
from typing import Optional


class QbStats(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    rank: int
    player: str
    team: str
    age: int
    position: str
    games: int
    games_started: int
    record: str
    completed: int
    attempted: int
    completion_percentage: float
    total_yards: int
    touchdowns: int
    touchdowns_percentage: float
    interceptions: int
    interceptions_percentage: float
    first_down_passes: int
    passing_success_rate: float
    longest_completed_pass: float
    yards_per_pass_attempt: float
    adjusted_yards_per_pass_attempt: float
    yards_per_pass_completed: float
    yards_per_game: float
    rate: float
    QBR: float
    times_sacked: int
    yards_lost_due_to_sacks: int
    times_sacked_percentage: float
    net_yards_per_pass_attempt: float
    adjusted_net_yards_per_pass_attempt: float
    fourth_quater_comeback: int
    game_winning_drive: int
    extraction_date: date
