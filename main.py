"""copyright (c) 2021 Beeflow Ltd.

Author Rafal Przetakowski <rafal.p@beeflow.co.uk>"""
from pydoc import locate

from common.view import View
from library import settings


# każdy widok podłącza się do menu automatycznie

# #######################################
# Funkcjonalności aplikacji "Biblioteka":
# #######################################
# 1. Wyszukiwanie książek (Po autorze i tytule)
# 2. Wypożyczenie książki -> znajdź użytkownika, znajdź książkę -> wypożycz książkę użytkownikowi
# 3. Zwrot książki
# 4. Wyszukiwanie użytkownika
# 5. Dodawanie użytkownika
# 6. Dodawanie książek
# 7. Dodawanie autorów

def main():
    views = []

    for key, view_class in enumerate(settings.INSTALLED_APPS):
        view: View = locate(view_class)()
        views.append(view)
        print(f"{key}. {view.get_menu_item()}")

    try:
        option = int(input("Select option: "))
    except ValueError:
        print("Co za bzdury...")
        return

    try:
        views[option].get()
    except IndexError:
        print("Nie znam takiej opcji :P")


if __name__ == '__main__':
    while True:
        main()
