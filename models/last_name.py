"""copyright (c) 2021 Beeflow Ltd.

Author Rafal Przetakowski <rafal.p@beeflow.co.uk>"""
from peewee import *

from common.base_model import BaseModel


class LastName(BaseModel):
    name = CharField(max_length=50, column_name="last_name")

    def __str__(self):
        return self.name

    class Meta:
        table_name = "last_name"
