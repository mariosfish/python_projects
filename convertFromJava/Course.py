from . import Student


class Course:
    name = ''
    enrolledStudents = []

    def __init__(self, name):
        self.name = name

    def printCourseDetails(self):
        print("Course name: " + self.name)
