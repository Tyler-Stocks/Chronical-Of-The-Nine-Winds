import Project.gather_user_information.age, Project.gather_user_information.name, Project.gather_user_information.gender

class GetUserInformation:

    def __init__(self):
        pass

    def main(self) -> None:
        Age = Project.gather_user_information.age.Age()
        Name = Project.gather_user_information.name.Name()
        Gender = Project.gather_user_information.gender.Gender()

GetUserInformation_Obj = GetUserInformation().main()
