"""copyright (c) 2021 Beeflow Ltd.

Author Rafal Przetakowski <rafal.p@beeflow.co.uk>"""
from peewee import *

from library.settings import DATABASE_NAME, DATABASE_CONFIG

mysql = MySQLDatabase(DATABASE_NAME, **DATABASE_CONFIG)


class BaseModel:
    id = AutoField()

    class Meta:
        database = mysql
        legacy_table_name = False

    def __str__(self):
        return str(self.id)
