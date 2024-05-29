from typing import List, Optional, TypeVar, Generic
from abc import ABC, abstractmethod
from pathlib import Path

T = TypeVar('T')

class RepositoryBase(ABC, Generic[T]):
    @abstractmethod
    def get_all(self) -> List[T]:
        pass

    @abstractmethod
    def get_by_id(self, item_id: int) -> Optional[T]:
        pass

    @abstractmethod
    def add(self, item: T) -> None:
        pass

    @abstractmethod
    def delete_by_id(self, item_id: int) -> None:
        pass

    @abstractmethod
    def update(self, item: T) -> None:
        pass