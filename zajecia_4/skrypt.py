import sys

wybor_programu_do_odpalenia = sys.argv[1]
pierwsza_liczba = int(sys.argv[2])
druga_liczba = int(sys.argv[3])
if int(wybor_programu_do_odpalenia) == 1:
    #program do dodawania
    print(pierwsza_liczba+ druga_liczba)
elif int(wybor_programu_do_odpalenia) == 2:
    print(pierwsza_liczba - druga_liczba)
else:
    print("Nie wybrales programu")
