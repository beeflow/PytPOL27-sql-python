"""copyright (c) 2021 Beeflow Ltd.

Author Rafal Przetakowski <rafal.p@beeflow.co.uk>"""
DATABASE_CONFIG = {
    "host": "localhost",
    "user": "user",
    "password": "password",
    "port": 3306
}
DATABASE_NAME = "container_db"

INSTALLED_APPS = [
    "views.books_view.BooksView",
    "views.exit_view.ExitView",
]