import pytest
from src.shared.domain.entities.member import Member
from src.shared.domain.entities.project import Project
from src.shared.domain.enums.active_enum import ACTIVE
from src.shared.domain.enums.course_enum import COURSE
from src.shared.domain.enums.role_enum import ROLE
from src.shared.domain.enums.stack_enum import STACK
from src.shared.helpers.errors.domain_errors import EntityError


class Test_Member:
    
    def test_member(self):
        member = Member(
            name="Vitor Guirão MPNTM",
            email="vsoller.devmaua@gmail.com",
            email_maua="21.01731-0@maua.br",
            ra="21017310",
            role=ROLE.DIRECTOR,
            stack=STACK.INFRA,
            year=1,
            cellphone="11991758098",
            course=COURSE.ECA,
            hired_date=1671728165,
            active=ACTIVE.FREEZE,
            projects=[
                Project(
                    code="MF",
                    name="Maua Food",
                    description="É um aplicativo #foramoleza"
                )
            ]
        )
        
        assert member.name == "Vitor Guirão MPNTM"
        assert member.email == "vsoller.devmaua@gmail.com"
        assert member.email_maua == "21.01731-0@maua.br"
        assert member.ra == "21017310"
        assert member.role == ROLE.DIRECTOR
        assert member.stack == STACK.INFRA
        assert member.year == 1
        assert member.cellphone == "11991758098"
        assert member.course == COURSE.ECA
        assert member.hired_date == 1671728165
        assert member.active == ACTIVE.FREEZE
        assert len(member.projects) == 1
        assert member.projects[0] == Project(
                    code="MF",
                    name="Maua Food",
                    description="É um aplicativo #foramoleza"
                )
        assert member.linkedin_url == None
        assert member.github_url == None
        assert member.is_admin == False
            
    def test_member_name_not_str(self): 
        with pytest.raises(EntityError):
            Member(
            name=1,
            email="vsoller.devmaua@gmail.com",
            email_maua="21.01731-0@maua.br",
            ra="21017310",
            role=ROLE.DIRECTOR,
            stack=STACK.INFRA,
            year=1,
            cellphone="11991758098",
            course=COURSE.ECA,
            hired_date=1671728165,
            active=ACTIVE.FREEZE,
            projects=[
                Project(
                    code="MF",
                    name="Maua Food",
                    description="É um aplicativo #foramoleza"
                )
            ]
        )
            
    def test_member_name_smaller_than_minimum(self): 
        with pytest.raises(EntityError):
            Member(
            name="V",
            email="vsoller.devmaua@gmail.com",
            email_maua="21.01731-0@maua.br",
            ra="21017310",
            role=ROLE.DIRECTOR,
            stack=STACK.INFRA,
            year=1,
            cellphone="11991758098",
            course=COURSE.ECA,
            hired_date=1671728165,
            active=ACTIVE.FREEZE,
            projects=[
                Project(
                    code="MF",
                    name="Maua Food",
                    description="É um aplicativo #foramoleza"
                )
            ]
        )

    def test_member_ra_not_str(self): 
        with pytest.raises(EntityError):
            Member(
            name="Vitor Guirão MPNTM",
            email="vsoller.devmaua@gmail.com",
            email_maua="21.01731-0@maua.br",
            ra=21017310,
            role=ROLE.DIRECTOR,
            stack=STACK.INFRA,
            year=1,
            cellphone="11991758098",
            course=COURSE.ECA,
            hired_date=1671728165,
            active=ACTIVE.FREEZE,
            projects=[
                Project(
                    code="MF",
                    name="Maua Food",
                    description="É um aplicativo #foramoleza"
                )
            ]
        )

    def test_member_ra_not_decimal(self): 
        with pytest.raises(EntityError):
            Member(
            name="Vitor Guirão MPNTM",
            email="vsoller.devmaua@gmail.com",
            email_maua="21.01731-0@maua.br",
            ra="210173A0",
            role=ROLE.DIRECTOR,
            stack=STACK.INFRA,
            year=1,
            cellphone="11991758098",
            course=COURSE.ECA,
            hired_date=1671728165,
            active=ACTIVE.FREEZE,
            projects=[
                Project(
                    code="MF",
                    name="Maua Food",
                    description="É um aplicativo #foramoleza"
                )
            ]
        )

    def test_member_lenght_ra_not_8(self): 
        with pytest.raises(EntityError):
            Member(
            name="Vitor Guirão MPNTM",
            email="vsoller.devmaua@gmail.com",
            email_maua="21.01731-0@maua.br",
            ra="221017310",
            role=ROLE.DIRECTOR,
            stack=STACK.INFRA,
            year=1,
            cellphone="11991758098",
            course=COURSE.ECA,
            hired_date=1671728165,
            active=ACTIVE.FREEZE,
            projects=[
                Project(
                    code="MF",
                    name="Maua Food",
                    description="É um aplicativo #foramoleza"
                )
            ]
        )


    def test_member_email_is_not_str(self): 
        with pytest.raises(EntityError):
            Member(
            name="Vitor Guirão MPNTM",
            email=1,
            email_maua="21.01731-0@maua.br",
            ra="21017310",
            role=ROLE.DIRECTOR,
            stack=STACK.INFRA,
            year=1,
            cellphone="11991758098",
            course=COURSE.ECA,
            hired_date=1671728165,
            active=ACTIVE.FREEZE,
            projects=[
                Project(
                    code="MF",
                    name="Maua Food",
                    description="É um aplicativo #foramoleza"
                )
            ]
        )
            
    def test_member_email_is_not_in_right_format(self): 
        with pytest.raises(EntityError):
            Member(
            name="Vitor Guirão MPNTM",
            email="vsollerdevmaua@gmail.com",
            email_maua="21.01731-0@maua.br",
            ra="21017310",
            role=ROLE.DIRECTOR,
            stack=STACK.INFRA,
            year=1,
            cellphone="11991758098",
            course=COURSE.ECA,
            hired_date=1671728165,
            active=ACTIVE.FREEZE,
            projects=[
                Project(
                    code="MF",
                    name="Maua Food",
                    description="É um aplicativo #foramoleza"
                )
            ]
        )
            
    
    def test_member_email_not_dev(self): 
        with pytest.raises(EntityError):
            Member(
            name="Vitor Guirão MPNTM",
            email="vitor.guirao@gmail.com",
            email_maua="21.01731-0@maua.br",
            ra="21017310",
            role=ROLE.DIRECTOR,
            stack=STACK.INFRA,
            year=1,
            cellphone="11991758098",
            course=COURSE.ECA,
            hired_date=1671728165,
            active=ACTIVE.FREEZE,
            projects=[
                Project(
                    code="MF",
                    name="Maua Food",
                    description="É um aplicativo #foramoleza"
                )
            ]
        )
    
    def test_member_email_maua_not_str(self):
       with pytest.raises(EntityError):
            Member(
            name="Vitor Guirão MPNTM",
            email="vsoller.devmaua@gmail.com",
            email_maua=1,
            ra="21017310",
            role=ROLE.DIRECTOR,
            stack=STACK.INFRA,
            year=1,
            cellphone="11991758098",
            course=COURSE.ECA,
            hired_date=1671728165,
            active=ACTIVE.FREEZE,
            projects=[
                Project(
                    code="MF",
                    name="Maua Food",
                    description="É um aplicativo #foramoleza"
                )
            ]
        )
    
    def test_member_email_maua_not_email(self):
        with pytest.raises(EntityError):
            Member(
            name="Vitor Guirão MPNTM",
            email="vsoller.devmaua@gmail.com",
            email_maua="21.01731-0maua.br",
            ra="21017310",
            role=ROLE.DIRECTOR,
            stack=STACK.INFRA,
            year=1,
            cellphone="11991758098",
            course=COURSE.ECA,
            hired_date=1671728165,
            active=ACTIVE.FREEZE,
            projects=[
                Project(
                    code="MF",
                    name="Maua Food",
                    description="É um aplicativo #foramoleza"
                )
            ]
        ) 

    def test_member_role_not_enum(self): 
        with pytest.raises(EntityError):
            Member(
            name="Vitor Guirão MPNTM",
            email="vsoller.devmaua@gmail.com",
            email_maua="21.01731-0@maua.br",
            ra="21017310",
            role="ROLE.DIRECTOR",
            stack=STACK.INFRA,
            year=1,
            cellphone="11991758098",
            course=COURSE.ECA,
            hired_date=1671728165,
            active=ACTIVE.FREEZE,
            projects=[
                Project(
                    code="MF",
                    name="Maua Food",
                    description="É um aplicativo #foramoleza"
                )
            ]
        )

    def test_member_stack_not_enum(self): 
        with pytest.raises(EntityError):
            Member(
            name="Vitor Guirão MPNTM",
            email="vsoller.devmaua@gmail.com",
            email_maua="21.01731-0@maua.br",
            ra="21017310",
            role=ROLE.DIRECTOR,
            stack="STACK.INFRA",
            year=1,
            cellphone="11991758098",
            course=COURSE.ECA,
            hired_date=1671728165,
            active=ACTIVE.FREEZE,
            projects=[
                Project(
                    code="MF",
                    name="Maua Food",
                    description="É um aplicativo #foramoleza"
                )
            ]
        )

    def test_member_year_not_int(self): 
        with pytest.raises(EntityError):
            Member(
            name="Vitor Guirão MPNTM",
            email="vsoller.devmaua@gmail.com",
            email_maua="21.01731-0@maua.br",
            ra="21017310",
            role=ROLE.DIRECTOR,
            stack=STACK.INFRA,
            year="2021",
            cellphone="11991758098",
            course=COURSE.ECA,
            hired_date=1671728165,
            active=ACTIVE.FREEZE,
            projects=[
                Project(
                    code="MF",
                    name="Maua Food",
                    description="É um aplicativo #foramoleza"
                )
            ]
        )
            
    def test_member_year_bigger_than_6(self): 
        with pytest.raises(EntityError):
            Member(
            name="Vitor Guirão MPNTM",
            email="vsoller.devmaua@gmail.com",
            email_maua="21.01731-0@maua.br",
            ra="21017310",
            role=ROLE.DIRECTOR,
            stack=STACK.INFRA,
            year=10,
            cellphone="11991758098",
            course=COURSE.ECA,
            hired_date=1671728165,
            active=ACTIVE.FREEZE,
            projects=[
                Project(
                    code="MF",
                    name="Maua Food",
                    description="É um aplicativo #foramoleza"
                )
            ]
        )
            
    def test_member_year_smaller_than_0(self): 
        with pytest.raises(EntityError):
            Member(
            name="Vitor Guirão MPNTM",
            email="vsoller.devmaua@gmail.com",
            email_maua="21.01731-0@maua.br",
            ra="21017310",
            role=ROLE.DIRECTOR,
            stack=STACK.INFRA,
            year=-2,
            cellphone="11991758098",
            course=COURSE.ECA,
            hired_date=1671728165,
            active=ACTIVE.FREEZE,
            projects=[
                Project(
                    code="MF",
                    name="Maua Food",
                    description="É um aplicativo #foramoleza"
                )
            ]
        )

    def test_member_cellphone_not_str(self): 
        with pytest.raises(EntityError):
            Member(
            name="Vitor Guirão MPNTM",
            email="vsoller.devmaua@gmail.com",
            email_maua="21.01731-0@maua.br",
            ra="21017310",
            role=ROLE.DIRECTOR,
            stack=STACK.INFRA,
            year=1,
            cellphone=11991758098,
            course=COURSE.ECA,
            hired_date=1671728165,
            active=ACTIVE.FREEZE,
            projects=[
                Project(
                    code="MF",
                    name="Maua Food",
                    description="É um aplicativo #foramoleza"
                )
            ]
        )

    def test_member_cellphone_not_in_right_format(self): 
        with pytest.raises(EntityError):
            Member(
            name="Vitor Guirão MPNTM",
            email="vsoller.devmaua@gmail.com",
            email_maua="21.01731-0@maua.br",
            ra="21017310",
            role=ROLE.DIRECTOR,
            stack=STACK.INFRA,
            year=1,
            cellphone="551991758098",
            course=COURSE.ECA,
            hired_date=1671728165,
            active=ACTIVE.FREEZE,
            projects=[
                Project(
                    code="MF",
                    name="Maua Food",
                    description="É um aplicativo #foramoleza"
                )
            ]
        )


    def test_member_course_not_enum(self): 
        with pytest.raises(EntityError):
            Member(
            name="Vitor Guirão MPNTM",
            email="vsoller.devmaua@gmail.com",
            email_maua="21.01731-0@maua.br",
            ra="21017310",
            role=ROLE.DIRECTOR,
            stack=STACK.INFRA,
            year=1,
            cellphone="11991758098",
            course="COURSE.ECA",
            hired_date=1671728165,
            active=ACTIVE.FREEZE,
            projects=[
                Project(
                    code="MF",
                    name="Maua Food",
                    description="É um aplicativo #foramoleza"
                )
            ]
        )


    def test_member_hired_date_not_int(self): 
        with pytest.raises(EntityError):
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
            hired_date="10/10/2002",
            active=ACTIVE.FREEZE,
            projects=[
                Project(
                    code="MF",
                    name="Maua Food",
                    description="É um aplicativo #foramoleza"
                )
            ]
        )
            
    def test_member_hired_date_less_than_zero(self): 
        with pytest.raises(EntityError):
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
            hired_date=-1671728165,
            active=ACTIVE.FREEZE,
            projects=[
                Project(
                    code="MF",
                    name="Maua Food",
                    description="É um aplicativo #foramoleza"
                )
            ]
        )
            
    def test_member_active_not_enum(self): 
        with pytest.raises(EntityError):
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
            hired_date=1671728165,
            active="ACTIVE.FREEZE",
            projects=[
                Project(
                    code="MF",
                    name="Maua Food",
                    description="É um aplicativo #foramoleza"
                )
            ]
        )
            
    def test_member_active_with_deactivated_date(self): 
        with pytest.raises(EntityError):
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
            hired_date=1671728165,
            deactivated_date=1671728165,
            active=ACTIVE.ACTIVE,
            projects=[
                Project(
                    code="MF",
                    name="Maua Food",
                    description="É um aplicativo #foramoleza"
                )
            ]
        )

    def test_member_projects_is_none(self): 
        member = Member(
            name="Vitor Guirão MPNTM",
            email="vsoller.devmaua@gmail.com",
            email_maua="21.01731-0@maua.br",
            ra="21017310",
            role=ROLE.DIRECTOR,
            stack=STACK.INFRA,
            year=1,
            cellphone="11991758098",
            course=COURSE.ECA,
            hired_date=1640192165,
            active=ACTIVE.FREEZE,
            deactivated_date=1671728165
        )
        
        assert member.projects == []
        

    def test_member_projects_is_not_list(self): 
        with pytest.raises(EntityError):
            Member(
            name="Vitor Guirão MPNTM",
            email="vsoller.devmaua@gmail.com",
            email_maua="21.01731-0@maua.br",
            ra="21017310",
            role=ROLE.DIRECTOR,
            stack=STACK.INFRA,
            year=2021,
            cellphone="11991758098",
            course=COURSE.ECA,
            hired_date=1671728165,
            active=ACTIVE.FREEZE,
            projects="[]"
            
        )

    def test_member_projects_is_not_list_of_projects(self): 
        with pytest.raises(EntityError):
            Member(
            name="Vitor Guirão MPNTM",
            email="vsoller.devmaua@gmail.com",
            email_maua="21.01731-0@maua.br",
            ra="21017310",
            role=ROLE.DIRECTOR,
            stack=STACK.INFRA,
            year=2021,
            cellphone="11991758098",
            course=COURSE.ECA,
            hired_date=1671728165,
            active=ACTIVE.FREEZE,
            projects=[
                "project1"
            ]
        )

    def test_member_projects_is_not_list_of_projects_with_2_items(self): 
        with pytest.raises(EntityError):
            Member(
                name="Vitor Guirão MPNTM",
                email="vsoller.devmaua@gmail.com",
                email_maua="21.01731-0@maua.br",
                ra="21017310",
                role=ROLE.DIRECTOR,
                stack=STACK.INFRA,
                year=2021,
                cellphone="11991758098",
                course=COURSE.ECA,
                hired_date=1671728165,
                active=ACTIVE.FREEZE,
                projects=[
                Project(
                    code="MF",
                    name="Maua Food",
                    description="É um aplicativo #foramoleza"
                ),
                1
            ]
            )
    
    def test_member_projects_is_list_of_projects_with_2_items(self): 
        
        member = Member(
            name="Vitor Guirão MPNTM",
            email="vsoller.devmaua@gmail.com",
            email_maua="21.01731-0@maua.br",
            ra="21017310",
            role=ROLE.DIRECTOR,
            stack=STACK.INFRA,
            year=1,
            cellphone="11991758098",
            course=COURSE.ECA,
            hired_date=1671728165,
            active=ACTIVE.FREEZE,
            projects=[
            Project(
                code="MF",
                name="Maua Food",
                description="É um aplicativo #foramoleza"
            ),
            Project(
                code="SM",
                name="SMILE",
                description="=D"
            )
        ]
        )            
        assert len(member.projects) == 2

    def test_member_deactivated_date_not_none_or_int(self): 
        with pytest.raises(EntityError):
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
                hired_date=1671728165,
                active=ACTIVE.DISCONNECTED,
                projects=[
                Project(
                    code="MF",
                    name="Maua Food",
                    description="É um aplicativo #foramoleza"
                ),
                Project(
                    code="SM",
                    name="SMILE",
                    description="=D"
                ),
            ],
                deactivated_date="10/10/2022"
            )     
                 
    def test_member_deactivated_date_smaller_than_hired_date(self): 
        with pytest.raises(EntityError):
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
                hired_date=1671728165,
                active=ACTIVE.DISCONNECTED,
                projects=[
                Project(
                    code="MF",
                    name="Maua Food",
                    description="É um aplicativo #foramoleza"
                ),
                Project(
                    code="SM",
                    name="SMILE",
                    description="=D"
                ),
            ],
                deactivated_date=1640192165
            )          
        
    def test_member_linkedin_not_none(self):
        member = Member(
        name="Vitor Guirão MPNTM",
        email="vsoller.devmaua@gmail.com",
        email_maua="21.01731-0@maua.br",
        ra="21017310",
        role=ROLE.DIRECTOR,
        stack=STACK.INFRA,
        year=1,
        cellphone="11991758098",
        course=COURSE.ECA,
        hired_date=1671728165,
        active=ACTIVE.FREEZE,
        projects=[
            Project(
                code="MF",
                name="Maua Food",
                description="É um aplicativo #foramoleza"
            )
        ],
        linkedin_url="https://www.linkedin.com/in/vitor-guirao-0b1b1b1b1/"
        )
        
        assert member.linkedin_url == "https://www.linkedin.com/in/vitor-guirao-0b1b1b1b1/"
        
    def test_member_linkedin_not_url(self):
        with pytest.raises(EntityError):
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
        hired_date=1671728165,
        active=ACTIVE.FREEZE,
        projects=[
            Project(
                code="MF",
                name="Maua Food",
                description="É um aplicativo #foramoleza"
            )
        ],
        linkedin_url="vitor-guirao-0b1b1b1b1"
        )

    def test_member_github_not_none(self):
        member = Member(
        name="Vitor Guirão MPNTM",
        email="vsoller.devmaua@gmail.com",
        email_maua="21.01731-0@maua.br",
        ra="21017310",
        role=ROLE.DIRECTOR,
        stack=STACK.INFRA,
        year=1,
        cellphone="11991758098",
        course=COURSE.ECA,
        hired_date=1671728165,
        active=ACTIVE.FREEZE,
        projects=[
            Project(
                code="MF",
                name="Maua Food",
                description="É um aplicativo #foramoleza"
            )
        ],
        linkedin_url="https://www.linkedin.com/in/vitor-guirao-0b1b1b1b1/",
        github_url="https://github.com/vsoller"
        )
        
        assert member.github_url == "https://github.com/vsoller"
    
    def test_member_github_not_url(self):
        with pytest.raises(EntityError):
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
        hired_date=1671728165,
        active=ACTIVE.FREEZE,
        projects=[
            Project(
                code="MF",
                name="Maua Food",
                description="É um aplicativo #foramoleza"
            )
        ],
        linkedin_url="https://www.linkedin.com/in/vitor-guirao-0b1b1b1b1/",
        github_url="vsoller"
        )
                
    def test_member_is_admin_not_none(self):
        member = Member(
        name="Vitor Guirão MPNTM",
        email="vsoller.devmaua@gmail.com",
        email_maua="21.01731-0@maua.br",
        ra="21017310",
        role=ROLE.DIRECTOR,
        stack=STACK.INFRA,
        year=1,
        cellphone="11991758098",
        course=COURSE.ECA,
        hired_date=1671728165,
        active=ACTIVE.FREEZE,
        projects=[
            Project(
                code="MF",
                name="Maua Food",
                description="É um aplicativo #foramoleza"
            )
        ],
        linkedin_url="https://www.linkedin.com/in/vitor-guirao-0b1b1b1b1/",
        github_url="https://github.com/vsoller",
        is_admin=True
        )
    
        assert member.is_admin == True
    
    def test_member_is_admin_not_bool(self):
        with pytest.raises(EntityError):
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
        hired_date=1671728165,
        active=ACTIVE.FREEZE,
        projects=[
            Project(
                code="MF",
                name="Maua Food",
                description="É um aplicativo #foramoleza"
            )
        ],
        linkedin_url="https://www.linkedin.com/in/vitor-guirao-0b1b1b1b1/",
        github_url="https://github.com/vsoller",
        is_admin="Sim"
        )