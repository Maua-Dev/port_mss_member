from abc import ABC, abstractmethod
from typing import List

from src.shared.domain.entities.member import Member

class IMemberRepository(ABC):

    @abstractmethod
    def create_member(self, member: Member) -> Member:
        pass

    @abstractmethod
    def get_member(self, ra: str) -> Member:
        pass
