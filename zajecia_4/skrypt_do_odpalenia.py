import subprocess

# Run the other
print("Witaj w naszym programie matematycznym")
print("Opcje, które możesz wykonać to:\n"
      "1. Dodawanie"
      "2. Odejmowanie")
opcja = input("Wybierz opcję: ")
pierwsza_liczba = input("Podaj pierwszą liczbę: ")
druga_liczba = input("Podaj drugą liczbę: ")
subprocess.run(["python", "skrypt.py", opcja, pierwsza_liczba, druga_liczba])