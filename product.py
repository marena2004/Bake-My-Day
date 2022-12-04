import csv


class Product:
    def __init__(self):
        self.__data_lst = []

    @property
    def data_lst(self):
        return self.__data_lst

    @data_lst.setter
    def data_lst(self, data_lst):
        self.__data_lst = data_lst

    def readfile(self):
        with open("menu.csv", "r") as f:
            menu_ = csv.DictReader(f)
            for i in menu_:
                self.__data_lst.append(i)
        return self.__data_lst

    def check_stock(self, stock: int, use: int):
        if stock >= use:
            return True
        return False

    def update_stock(self, stock: int, use: int):
        stock -= use
        return stock
