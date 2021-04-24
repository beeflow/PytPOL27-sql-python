"""copyright (c) 2021 Beeflow Ltd.

Author Rafal Przetakowski <rafal.p@beeflow.co.uk>"""
from peewee import *

from common.base_model import BaseModel
from models.first_name import FirstName
from models.last_name import LastName


class User(BaseModel):
    email = CharField(max_length=100)
    phone = CharField(max_length=12, null=True)
    card_number = CharField(max_length=9)
    first_name = ForeignKeyField(FirstName, backref="users")
    last_name = ForeignKeyField(LastName, backref="users")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
