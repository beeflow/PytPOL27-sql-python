"""copyright (c) 2021 Beeflow Ltd.

Author Rafal Przetakowski <rafal.p@beeflow.co.uk>"""
from peewee import *

from common.base_model import BaseModel
from models.book import Book


class Status(BaseModel):
    name = CharField(max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        table_name = "book_status"


class BookCopy(BaseModel):
    book = ForeignKeyField(Book, backref="copies")
    status = ForeignKeyField(Status, backref="books")

    def __str__(self):
        return str(self.book)

    class Meta:
        table_name = "book_copy"
