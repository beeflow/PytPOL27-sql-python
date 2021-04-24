"""copyright (c) 2021 Beeflow Ltd.

Author Rafal Przetakowski <rafal.p@beeflow.co.uk>"""
from peewee import *

from common.base_model import BaseModel
from models.first_name import FirstName
from models.last_name import LastName


class Author(BaseModel):
    first_name = ForeignKeyField(FirstName, backref="authors")
    last_name = ForeignKeyField(LastName, backref="authors")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
