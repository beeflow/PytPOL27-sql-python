"""copyright (c) 2021 Beeflow Ltd.

Author Rafal Przetakowski <rafal.p@beeflow.co.uk>"""
from common.view import View


class ExitView(View):
    def get_menu_item(self):
        return "Exit"

    def get(self):
        exit()
