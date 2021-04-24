"""copyright (c) 2021 Beeflow Ltd.

Author Rafal Przetakowski <rafal.p@beeflow.co.uk>"""
import datetime

from common.base_model import BaseModel
from peewee import *

from models.book_copy import BookCopy
from models.user import User


class UserBookRent(BaseModel):
    book_copy = ForeignKeyField(BookCopy)
    user = ForeignKeyField(User)
    rented_on = DateField(default=datetime.date)
    returned_on = DateField(null=True)
