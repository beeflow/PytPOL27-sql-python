"""copyright (c) 2021 Beeflow Ltd.

Author Rafal Przetakowski <rafal.p@beeflow.co.uk>"""
from peewee import *

from common.base_model import BaseModel


class FirstName(BaseModel):
    name = CharField(max_length=15, column_name="first_name")

    def __str__(self):
        return self.name

    class Meta:
        table_name = "first_name"
