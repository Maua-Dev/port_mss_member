from src.shared.domain.entities.member import Member
from src.shared.domain.enums.active_enum import ACTIVE
from src.shared.domain.enums.course_enum import COURSE
from src.shared.domain.enums.role_enum import ROLE
from src.shared.domain.enums.stack_enum import STACK
from src.shared.domain.enums.state_enum import STATE
from src.shared.helpers.errors.usecase_errors import NoItemsFound
from src.shared.infra.repositories.member_repository_mock import MemberRepositoryMock
import pytest


class Test_MemberRepositoryMock:
    
    def test_get_member(self):
        repo = MemberRepositoryMock()
        member = repo.get_member(ra=repo.members[1].ra)
        
        assert type(member) == Member
        assert member == repo.members[1]
        
    def test_get_member_not_found(self):
        repo = MemberRepositoryMock()
        member = repo.get_member(ra="21010101")
        
        assert member is None
        
    def test_create_member(self):
        repo = MemberRepositoryMock()
        member = Member(name="Teste", email="teste.devmaua@gmail.com", ra="12345678", role=ROLE.DEV, stack=STACK.BACKEND, year=2, cellphone="11912345678", course=COURSE.CIC, hired_date=1634526000000, active=ACTIVE.ACTIVE)
        len_before = len(repo.members)
        
        new_member = repo.create_member(member=member)
        
        assert len(repo.members) == len_before + 1
        assert new_member == member
        
    def test_get_members(self):
        repo = MemberRepositoryMock()
        ras = [repo.members[0].ra, repo.members[1].ra]
        members = repo.get_members(ras=ras)
        assert len(members) == len(ras)
        assert all([type(member) == Member for member in members])
        assert members == [repo.members[0], repo.members[1]]