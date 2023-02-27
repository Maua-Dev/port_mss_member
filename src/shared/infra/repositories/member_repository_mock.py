from typing import List
from src.shared.domain.entities.member import Member
from src.shared.domain.entities.project import Project
from src.shared.domain.enums.active_enum import ACTIVE
from src.shared.domain.enums.course_enum import COURSE
from src.shared.domain.enums.role_enum import ROLE
from src.shared.domain.enums.stack_enum import STACK

from src.shared.domain.enums.state_enum import STATE
from src.shared.domain.repositories.member_repository_interface import IMemberRepository
from src.shared.helpers.errors.usecase_errors import NoItemsFound


class MemberRepositoryMock(IMemberRepository):
    members = List[Member]
    projects = List[Project]
    def __init__(self):
        self.projects = [
            Project(
                code="MF",
                name="Maua Food",
                description="É um aplicativo #foramoleza"
                ),
            Project(
                code="PT",
                name="Portfólio",
                description="É um site"
            ),
            Project(
                code="SF",
                name="Selfie Mauá",
                description="Aplicativo para reconhecimento facial"
            ),
            Project(
                code="SM",
                name="SMILE",
                description="Site do evento SMILE"
            ),
            Project(
                code="GM",
                name="Gameficação",
                description="Projeto para organização dos membros do DEV"
            )
        ]
        
        self.members = [
            Member(
            name="Vitor Guirão MPNTM",
            email="vsoller.devmaua@gmail.com",
            email_maua="21.01731-0@maua.br",
            ra="21017310",
            role=ROLE.DIRECTOR,
            stack=STACK.INFRA,
            year=1,
            cellphone="11991758098",
            course=COURSE.ECA,
            hired_date=1634576165000,
            active=ACTIVE.ACTIVE,
            projects=[
                self.projects[0]
            ]
            ),
            
            Member(
            name="Joao Branco",
            email="jbranco.devmaua@gmail.com",
            email_maua="21.01075-7@maua.br",
            ra="21010757",
            role=ROLE.HEAD,
            stack=STACK.BACKEND,
            year=3,
            cellphone="11991152348",
            course=COURSE.ECM,
            hired_date=1634921765000,
            active=ACTIVE.ACTIVE,
            projects=[
                self.projects[0],
                self.projects[1],
                self.projects[2]
            ]
            ),
            
            Member(
            name="Luigi Televisão",
            email="ltelevisao.devmaua@gmail.com",
            email_maua="22.01731-0@maua.br",
            ra="22017310",
            role=ROLE.DEV,
            stack=STACK.DATA_SCIENCE,
            year=2,
            cellphone="11991758228",
            course=COURSE.CIC,
            hired_date=1640192165000,
            active=ACTIVE.FREEZE,
            projects=[
            ]
            ),
            
            Member(
            name="Little Ronald",
            email="lronald.devmaua@gmail.com",
            email_maua="10.01731-0@maua.br",
            ra="10017310",
            role=ROLE.DIRECTOR,
            stack=STACK.FRONTEND,
            year=6,
            cellphone="11991759998",
            course=COURSE.ECM,
            hired_date=1293036965000,
            active=ACTIVE.ACTIVE,
            projects=[
                self.projects[0],
                self.projects[1],
                self.projects[2],
                self.projects[3]
            

            ]
            ),
            
            Member(
            name="Marcos Pereira Neto",
            email="mneto.devmaua@gmail.com",
            email_maua="19.01731-0@maua.br",
            ra="19017310",
            role=ROLE.PO,
            stack=STACK.PO,
            year=4,
            cellphone="11991753208",
            course=COURSE.EMC,
            hired_date=1545497765000,
            active=ACTIVE.DISCONNECTED,
            projects=[
            ],
            deactivated_date=1577033765000
            ),
            
            Member(
            name="Rubicks Cube",
            email="rcube.devmaua@gmail.com",
            email_maua="19.01731-1@maua.br",
            ra="19017311",
            role=ROLE.DEV,
            stack=STACK.BACKEND,
            year=3,
            cellphone="11911758098",
            course=COURSE.ECM,
            hired_date=1640192165000,
            active=ACTIVE.ACTIVE,
            projects=[
                self.projects[3],
                self.projects[2]
            ]
            ),
            
            Member(
            name="Django Fett",
            email="dfett.devmaua@gmail.com",
            email_maua="17.03373-0@maua.br",
            ra="17033730",
            role=ROLE.INTERNAL,
            stack=STACK.INTERNAL,
            year=2,
            cellphone="11915758098",
            course=COURSE.ECA,
            hired_date=1609606565000,
            active=ACTIVE.FREEZE,
            projects=[
            ]
            ),
            
            Member(
            name="Henrique Gustavo de Souza",
            email="hsouza.devmaua@gmail.com",
            email_maua="23.01731-0@maua.br",
            ra="23017310",
            role=ROLE.DEV,
            stack=STACK.UX_UI,
            year=1,
            cellphone="11991123498",
            course=COURSE.ECM,
            hired_date=1672592165000,
            active=ACTIVE.ACTIVE,
            projects=[
            ]
            )
        ]
        
    def get_member(self, ra: str) -> Member:
        for member in self.members:
            if member.ra == ra:
                return member
            
        return None
    
    def create_member(self, member: Member) -> Member:
        self.members.append(member)
        return member
    
    def get_members(self, ras: List[str]) -> List[Member]:
        members = []
        for member in self.members:
            if member.ra in ras:
                members.append(member)
                
        return members