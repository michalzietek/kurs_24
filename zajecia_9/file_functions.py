# with open(file="uczniowie.txt", mode="w+") as file2:
#     for line in file2:
#         print(line)
#     file2.write("Nowy podpis2")


class OtworzPiwo:
    def __enter__(self):
        print("Otworzyłem piwo")

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Zamknij piwo")


# with OtworzPiwo() as piwo:
#     print(piwo)
#     print("Pijemy piwko")


with open("slowniki3.txt", mode="r+") as new_file:
    new_file.write("raz dwa trzy")
    for line in new_file:
        print(line)
