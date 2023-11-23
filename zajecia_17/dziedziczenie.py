class Human:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def change_name(self, name):
        print("zmiana w klasie Human")
        self.name = name

    def change_surname(self, surname):
        self.surname = surname

    def __str__(self):
        return f"{self.name}, {self.surname}"


class User:
    # def __init__(self, username, password):
    #     self.username = username
    #     self.password = password

    def change_name(self, new_name):
        print("zmiana w klasie User")
        self.username = new_name


class Student(User, Human):
    def __init__(self, name, surname, students_class, grades):
        super().__init__(name, surname)
        self.classname = students_class
        self.grades: list = grades

    def add_grade(self, new_grade):
        self.grades.append(new_grade)

    # def change_name(self, name):
    #     print("zmienilem wewnatrz ucznia")
    #     self.name = name


class Teacher(Human):
    def __init__(self, name, surname, teaching_classes):
        super().__init__(name, surname)
        self.teaching_classes = teaching_classes


student = Student(name="Jan", surname="Nowak", students_class="1a", grades=[1, 4, 5, 3, 2])
student.change_name("Marek")
print(student)
teacher = Teacher(name="Jacek", surname="Kowalski", teaching_classes=["1a", "2b", "3c"])
print(teacher)