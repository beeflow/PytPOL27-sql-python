"""copyright (c) 2021 Beeflow Ltd.

Author Rafal Przetakowski <rafal.p@beeflow.co.uk>"""
from common.view import View
from models.book import Book


class BooksView(View):
    def get_menu_item(self):
        return ("Books list")

    def get(self):
        for book in Book.select():
            print(book.title)

        print()
