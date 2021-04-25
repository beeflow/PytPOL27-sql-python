"""copyright (c) 2021 Beeflow Ltd.

Author Rafal Przetakowski <rafal.p@beeflow.co.uk>"""
import abc


class View(abc.ABC):
    @abc.abstractmethod
    def get_menu_item(self):
        pass

    @abc.abstractmethod
    def get(self):
        pass
