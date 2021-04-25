"""copyright (c) 2021 Beeflow Ltd.

Author Rafal Przetakowski <rafal.p@beeflow.co.uk>"""
from models.author import Author
from models.book import Book


def find_book(search_param):
    # @todo FIXME :P
    BookAuthor = Book.authors.get_through_model()

    return Book.select().join(BookAuthor).join(Author).where(
        (Book.title == search_param) | (
                (Author.first_name.name == search_param) | (Author.last_name.name == search_param)
        )
    )
