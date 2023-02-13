from typing import List

from src.shared.domain.enums.state_enum import STATE
from src.shared.domain.repositories.user_repository_interface import IUserRepository
from src.shared.helpers.errors.usecase_errors import NoItemsFound


class MemberRepositoryMock(IUserRepository):

    def __init__(self):
        pass