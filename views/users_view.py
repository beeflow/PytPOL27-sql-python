"""copyright (c) 2021 Beeflow Ltd.

Author Rafal Przetakowski <rafal.p@beeflow.co.uk>"""

from common.view import View
from models.first_name import FirstName
from models.last_name import LastName
from models.user import User
from utils.user_search import find_user


class AddUserView(View):
    def get_menu_item(self):
        return "Add user"

    def get(self):
        email = input("  email: ")
        phone = input("  phone: ")
        first_name = input("  first name: ")
        last_name = input("  last name: ")

        first_name = FirstName.get_or_create(name=first_name)[0]
        last_name = LastName.get_or_create(name=last_name)[0]

        User.create(email=email, phone=phone, first_name=first_name, last_name=last_name)


class SearchUserView(View):
    def get_menu_item(self):
        return "Search user"

    def get(self):
        search_param = input(" User name or surname: ")

        for user in find_user(search_param):
            print(f"User: {user}, card number: {user.card_number}")

        print()
