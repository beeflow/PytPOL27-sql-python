"""copyright (c) 2021 Beeflow Ltd.

Author Rafal Przetakowski <rafal.p@beeflow.co.uk>"""
from models.book_copy import Status

if __name__ == '__main__':
    statuses = Status.select().filter(name="wypożyczona").execute()
    for status in statuses:
        for book in status.books:
            print(book)
