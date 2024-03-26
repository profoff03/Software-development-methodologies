from dataclasses import dataclass

@dataclass(frozen=True)
class Status:
    name: str