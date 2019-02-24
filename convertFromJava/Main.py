from Course import Course
from Student import Student
from PostGraduate import PostGraduate


def main():

    students = []
    s1 = Student.Student("John", "mai19046")
    s2 = Student.Student("Marios", "mai19022")
    s3 = PostGraduate.PostGraduate("Mike", "mai19086", "Roberts")
    s4 = PostGraduate.PostGraduate("Nick", "mai19458", "Mathews")
    c1 = Course.Course("Python")

    students.append(s1)
    students.append(s2)
    students.append(s3)
    students.append(s4)

# students = [s1, s2]
    for i in students:
        i.printInfo()


if __name__ == '__main__':
    main()
