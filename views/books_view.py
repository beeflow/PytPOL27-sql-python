"""copyright (c) 2021 Beeflow Ltd.

Author Rafal Przetakowski <rafal.p@beeflow.co.uk>"""
from common.view import View
from utils.book_search import find_book


class BooksView(View):
    def get_menu_item(self):
        return "Search books"

    def get(self):
        search_param = input(" book title or author name: ")

        for book in find_book(search_param):
            print(f"Title: {book.title}")

        print()
