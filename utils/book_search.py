"""copyright (c) 2021 Beeflow Ltd.

Author Rafal Przetakowski <rafal.p@beeflow.co.uk>"""
from peewee import JOIN

from models.author import Author
from models.book import Book
from models.first_name import FirstName
from models.last_name import LastName


def find_book(search_param):
    def where(result, first_name, last_name):
        """ @todo FIXME :P """
        if first_name:
            return result.where(Author.first_name == first_name)

        if last_name:
            return result.where (Author.last_name == last_name)

        return result.where(Book.title == search_param)

    BookAuthor = Book.authors.get_through_model()

    # 1. zapytanie o nazwisko
    try:
        last_name = LastName.get(LastName.name == search_param)
    except LastName.DoesNotExist:
        last_name = None

    # 2. zapytanie o imię
    try:
        first_name = FirstName.get(FirstName.name == search_param)
    except FirstName.DoesNotExist:
        first_name = None

    # 3. zapytanie o książkę o tytule lub autorze
    result = Book.select().join(BookAuthor, JOIN.LEFT_OUTER).join(Author, JOIN.LEFT_OUTER)
    result = where(result, first_name, last_name)

    return result
