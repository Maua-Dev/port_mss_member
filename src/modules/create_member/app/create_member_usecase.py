from src.shared.domain.entities.member import Member
from src.shared.domain.repositories.member_repository_interface import IMemberRepository
from src.shared.helpers.errors.usecase_errors import DuplicatedItem


class CreateMemberUsecase:
    def __init__(self, repo: IMemberRepository):
        self.repo = repo
    
    def __call__(self, member: Member) -> Member:
        
        if self.repo.get_member(ra=member.ra) is not None:
            raise DuplicatedItem('ra')
        
        return self.repo.create_member(member)
    