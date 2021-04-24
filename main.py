"""copyright (c) 2021 Beeflow Ltd.

Author Rafal Przetakowski <rafal.p@beeflow.co.uk>"""
from peewee import *

DATABASE_CONFIG = {
    "host": "localhost",
    "user": "user",
    "password": "password",
    "port": 3306
}
DATABASE_NAME = "container_db"

mysql = MySQLDatabase(DATABASE_NAME, **DATABASE_CONFIG)


class Book:
    class Meta:
        database = mysql
        legacy_table_name = False

    id = AutoField(column_name="book_id")
    title = CharField(max_length=250, null=False, column_name="book_title")
    isbn = CharField(max_length=13, null=True, column_name="book_isbn")
    pages = IntegerField(column_name="book_pages", null=True)
    published_on_year = IntegerField(column_name="book_publish_year", null=True)

    def __str__(self):
        return self.title

if __name__ == '__main__':
    pass