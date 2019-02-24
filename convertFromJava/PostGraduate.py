from . import Student


class PostGraduate(Student):

    # name = ""

    def __init__(self, supervisor):
        super().__init__(supervisor)
        # self.supervisor = supervisor

    def printInfo(self):
        super().printInfo()
        print("Supervisor: " + self.supervisor)
