"""copyright (c) 2021 Beeflow Ltd.

Author Rafal Przetakowski <rafal.p@beeflow.co.uk>"""
from models.author import Author
from models.book import Book
from models.first_name import FirstName
from models.last_name import LastName


def find_book(search_param):
    # @todo FIXME :P
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
    return Book.select().left_outer_join(BookAuthor).left_outer_join(Author).where(
        (Book.title == search_param) | (
                (Author.first_name == first_name) | (Author.last_name == last_name)
        )
    )
