class Student:
    def __init__(self, name, surname, students_class, grades):
        self.name = name
        self.surname = surname
        self.classname = students_class
        self.grades: list = grades

    def add_grade(self, new_grade):
        self.grades.append(new_grade)

    def change_name(self, name):
        print("zmienilem wewnatrz ucznia")
        self.name = name


class Teacher:
    def __init__(self, name, surname, teaching_classes):
        self.name = name
        self.surname = surname
        self.teaching_classes = teaching_classes

    def change_name(self, name):
        print("zmienilem wewnatrz nauczyciela")
        self.name = name


def change_value_inside_object(object, name):
    object.change_name(name)

student = Student(name="Jan", surname="Nowak", students_class="1a", grades=[1, 4, 5, 3, 2])
student.change_name("Marek")
print(student)
teacher = Teacher(name="Jacek", surname="Kowalski", teaching_classes=["1a", "2b", "3c"])
print(teacher)
change_value_inside_object(teacher, "Maria")
change_value_inside_object(student, "Piotr")
print(teacher.name)
print(student.name)