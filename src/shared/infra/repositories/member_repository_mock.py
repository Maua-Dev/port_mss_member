from typing import List

from src.shared.domain.enums.state_enum import STATE
from src.shared.domain.repositories.member_repository_interface import IMemberRepository
from src.shared.helpers.errors.usecase_errors import NoItemsFound


class MemberRepositoryMock(IMemberRepository):

    def __init__(self):
        pass