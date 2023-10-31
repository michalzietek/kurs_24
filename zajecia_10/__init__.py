"""
Rozszerzmy nasz program do systemu księgowego.
Zamiast pisać i czytać ze standardowego wejścia/wyjścia rezultat czyta i zapisuje do podanego pliku.
Wszystkie założenia dotyczące wykonywania operacji saldo, zakup, sprzedaż, konto, magazyn i przegląd pozostają bez zmian.
Program jest wywoływany w następujący sposób:
a) python saldo.py <plik><int wartosc> <str komentarz>
b) python sprzedaz.py <plik><str identyfikator produktu> <int cena> <int liczba sprzedanych>
c) python zakup.py <plik> <str identyfikator produktu> <int cena> <int liczba zakupionych>
d) python konto.py <plik>
e) python magazyn.py <plik><str identyfikator produktu 1> <str identyfikator produktu 2> <str identyfikator produktu 3> ...
f) python przeglad.py <plik>

Wymienione pliki powinny importować i korzystać co najmniej z jednej zaimportowanej funkcji / lub klasy.
"""