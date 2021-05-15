"""copyright (c) 2021 Beeflow Ltd.

Author Rafal Przetakowski <rafal.p@beeflow.co.uk>"""
DATABASE_CONFIG = {
    "host": "localhost",
    "user": "change_me",
    "password": "change_me",
    "port": 3306
}
DATABASE_NAME = "change_me"

INSTALLED_APPS = [
    "views.books_view.BooksView",
    "views.users_view.AddUserView",
    "views.users_view.SearchUserView",
    "views.exit_view.ExitView",
]
