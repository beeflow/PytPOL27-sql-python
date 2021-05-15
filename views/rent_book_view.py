"""copyright (c) 2021 Beeflow Ltd.

Author Rafal Przetakowski <rafal.p@beeflow.co.uk>"""

from common.view import View
from models.book_copy import BookCopy, Status
from models.user_book_rent import UserBookRent
from utils.book_search import find_book
from utils.user_search import find_user


class RentBookView(View):
    def get_menu_item(self):
        return "Rent book"

    def get(self):
        search_param = input(" User name or surname: ")

        users = 0
        for user in find_user(search_param):
            print(f"User: {user}, card number: {user.card_number}")
            users += 1

        if users > 1:
            search_param = input(" Select user by card number: ")
            user = [u for u in find_user(search_param)][0]

        search_param = input(" book title or author name: ")


        books = 0
        for book in find_book(search_param):
            print(f"[ID: {book.id}] Title: {book.title}")
            books += 1

        if books > 1:
            search_param = input(" Select book by ID: ")
            book = [u for u in find_book(search_param)][0]

        book_copy = BookCopy.get(book=book, status=Status.get(name="Dostępna"))
        print(book_copy)

        UserBookRent.create(book_copy=book_copy, user=user)

        print()
