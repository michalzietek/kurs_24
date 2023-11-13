import random
# age = int(input("Podaj mi swój wiek: "))
# salary = int(input("Podaj mi swoją wypłatę: "))
# if age > 18:
#     is_adult = True
# else:
#     is_adult = False
#
# is_adult_2 = True if age > 18 else False # jednolinijkowa instrukcja warunkowa
# netto_salary = salary * 0.80 if salary < 4000 else salary * 0.50
# # zmienna = wartosc prawdziwa <instrukcja warunkowa> wartosc nieprawdziwa/taka co wchodzi nam w elsie
#
# if is_adult_2:
#     print("Uzytkownik jest pelnoletni")
# else:
#     print("Uzytkownik nie jest pelnoletni")
# print(netto_salary)

##############################################################
#list comprehension
# [<wartosc, ktora chcemy dodac do listy> for <zmienna> in <struktura iterowalna>]
# students = ["Michal", "andrzej", "Jan", "Wojtek"]
# grades_list = []
# students_set = {"Michal", "Jacek", "Adam"}
# #print(students_set)
# for student in students:
#     grades_list.append(random.randint(1,6))
#
# grades_list_2 = [random.randint(1, 6) for student in students]
#
# students_capitalize = [student.capitalize() for student in students]
#
# #print(students_capitalize)
#
#
# students_set_lower_names = {student.lower() for student in students_set}
# #print(grades_list)
# #print(grades_list_2)
# #print(students_set_lower_names)
# numbers_to_pow = [1, 5, 10, 14, 22, 17]
# numbers_after_calculation = [number**2 for number in numbers_to_pow]
# #print(numbers_after_calculation)
#
# #############################################################
# # list comprehansion z instrukcja warunkowa tzw filtrowanie wynikow
#
# students_without_capitalized_name = [student for student in students if student[0].isupper()]
# students_without_capitalized_name_old_fashion = []
#
# for student in students:
#     if student[0].isupper():
#         students_without_capitalized_name_old_fashion.append(student)
#     else:
#         #kalkulacje itp.
#         pass
#
# # [<zmienna, ktora chcemy dodac> <petla for> <instrukcja warunkowa>]
#
# print(students_without_capitalized_name)

################################################################
# dict comprehension

students = ["Michal", "andrzej", "Jan", "Wojtek"] # 4 wartosci
surnames = ["Zietkowski", "Kowalczyk", "Zięba"] # 3 wartosci

students_with_grades = {name: random.randint(1,6) for name in students}
# slownik = {klucz:wartosc for zmienna in struktura iterowalna}
print(students_with_grades)
students_with_surnames = {name: surname for name in students for surname in surnames}
print(students_with_surnames)
# czyms nie musicie sie martwic
zzipowani_uczniowie = zip(students, surnames)
for uczen in zzipowani_uczniowie:
    print(uczen)
