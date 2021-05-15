"""copyright (c) 2021 Beeflow Ltd.

Author Rafal Przetakowski <rafal.p@beeflow.co.uk>"""
from models.first_name import FirstName
from models.last_name import LastName
from models.user import User


def find_user(search_param):
    # 1. zapytanie o nazwisko
    try:
        last_name = LastName.get(LastName.name == search_param)
        return User.select().where(User.last_name == last_name)
    except LastName.DoesNotExist:
        pass

    # 2. zapytanie o imię
    try:
        first_name = FirstName.get(FirstName.name == search_param)
        return User.select().where(User.first_name == first_name)
    except FirstName.DoesNotExist:
        pass

    return []
