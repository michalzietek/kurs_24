import sys
import os
import math
import random
import decimal
import datetime
import re



arguments = sys.argv # lista
# wiek = input("Podaj mi swój wiek") #stdin
# print("Witamy w programie") #stdout

# print(os.getcwd())
# file_path = input("Podaj proszę plik, który chcesz otworzyć")
# path_to_my_file = f"{os.getcwd()}/{file_path}"
# os.chmod()
# with open(path_to_my_file) as file:
#     print(file.read())
#os.chdir("..")
#os.mkdir("Katalog_pythona")
# os.system("mkdir systemowo")
# print(math.pow(2, 3)) # potegowanie 2**3
# print(round(18/7, 0))
# print(type(round(18/7, 0)))
# print(math.floor(18/7))#zaokraglamy w dol
# print(math.ceil(18/7))# zaokraglenie w gore
# print(19.6666)
#
# wyniki_lotto = []
# twoje_wyniki = []
# trafione_liczby = []
# for number in range(6):
#     wyniki_lotto.append(random.randint(0, 60))# pamietac ze nasze wyniki sie nie moga dublowac
# print(wyniki_lotto)
# for twoj_numer in range(6):
#     wybrany_numer = input("Podaj mi swoj numer")
#     twoje_wyniki.append(int(wybrany_numer))
#
# for liczba in twoje_wyniki:
#     if liczba in wyniki_lotto:
#         trafione_liczby.append(liczba)
#
# print(f"Liczby lotto: {wyniki_lotto}, twoje liczby: {twoje_wyniki}, trafiles {len(trafione_liczby)}")
# now = datetime.datetime.now()
# print(datetime.datetime.now())
# print(now.strftime("%D-%H:%M:%S"))
# format = "%H:%M:%S"
# our_day = "18:31:16"
# datetime_from_string = datetime.datetime.strptime(our_day, format)
# print(datetime_from_string)
# d - jeden dzien #D data dnia
adres_email = "michalzietkowski9@gmail.com"

pattern = r'[\w]+@[\w]+.[\w]+'

znaleziony_adres_email = re.search(pattern, adres_email)
print(znaleziony_adres_email)