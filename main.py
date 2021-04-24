"""copyright (c) 2021 Beeflow Ltd.

Author Rafal Przetakowski <rafal.p@beeflow.co.uk>"""
from models.first_name import FirstName
from models.user import User

if __name__ == '__main__':
    # statuses = Status.select().filter(name="wypożyczona").execute()
    # for status in statuses:
    #     for book in status.books:
    #         print(book)

    names = FirstName.select().filter(name="rafał").execute()
    for name in names:
        for user in name.users:
            print(user.last_name)

    # for user in User.select().execute():
    #     print(user)
