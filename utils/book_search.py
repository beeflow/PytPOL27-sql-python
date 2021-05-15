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
    LastName.select().where(LastName.name == "King")

    # 2. zapytanie o imię

    # 3. zapytanie o autora o imieniu lub nazwisku

    # 4. zapytanie o książkę o tytule lub autorze

    return Book.select().join(BookAuthor).join(Author).where(
        (Book.title == search_param) | (
                (Author.first_name.name == search_param) | (Author.last_name.name == search_param)
        )
    )
