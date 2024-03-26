from dataclasses import dataclass


@dataclass(frozen=True)
class Deadline:
    start_date: str
    end_date: str