users_list = ["Michal", "Adam", "Jacek", "Bogdan", "Arek", "Mateusz", "Filip"]

def show_nth_user_in_our_program(users, user_number):
    print(users[user_number])

selected_user = input("Podaj mi numer użytkownika, którego chcesz wyświetlić ")

#show_nth_user_in_our_program(users_list, int(selected_user))

try:
    show_nth_user_in_our_program(users_list, int(selected_user))
except IndexError:
    print("Niestety nie mamy takiego użytkownika")
except ValueError:
    print("Podana wartosc jest wartoscia nienumeryczna")
finally:
    print("Zakonczylem dzialanie programu")
    print("zamykam polaczenie")
