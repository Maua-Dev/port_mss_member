from abc import ABC, abstractmethod
from typing import List

class IMemberRepository(ABC):

    @abstractmethod
    def get_member(self, ra: str) -> Member:
        pass
