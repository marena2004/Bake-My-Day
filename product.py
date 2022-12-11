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
        if stock >= use:  # check whether the products in stock are enough for sale or not.
            return True
        return False

    def update_stock(self, stock: int, use: int):
        stock -= use
        return stock

    def show_menu(self):  # create menu bar
        p = Product()
        p.readfile()

        while True:
            print(" (1) PASTRIES/BREAD\n (2) CAKE\n (3) CHEESECAKE\n (4) COOKIES\n (5) DRINKS")
            choose = str(input('Please select number or back[b]: '))

            if choose == "1":
                print("\n" + " " * 9 + "B A K E  M Y  D A Y")
                print("-" * 36 + "\n" + "🥐 PASTRIES/BREAD\n" + "-" * 36)
                print("|NO|" + " " * 2 + "|MENU|" + " " * 17 + "|PRICE|")
                for a in p.data_lst[:8]:
                    print(" " + a["id"].ljust(4, " ") + " " + a["menu"].ljust(24, " ") + " " + a["price"] + ".-")
                print("-" * 36)
                break
            elif choose == "2":
                print("\n" + " " * 9 + "B A K E  M Y  D A Y")
                print("-" * 36 + "\n" + "🍰 CAKE\n" + "-" * 36)
                print("|NO|" + " " * 2 + "|MENU|" + " " * 17 + "|PRICE|")
                for a in p.data_lst[8:13]:
                    print(" " + a["id"].ljust(4, " ") + " " + a["menu"].ljust(24, " ") + " " + a["price"] + ".-")
                print("-" * 36)
                break
            elif choose == "3":
                print("\n" + " " * 11 + "B A K E  M Y  D A Y")
                print("-" * 38 + "\n" + "🧀 CHEESECAKE\n" + "-" * 38)
                print("|NO|" + " " * 2 + "|MENU|" + " " * 19 + "|PRICE|")
                for a in p.data_lst[13:17]:
                    print(" " + a["id"].ljust(4, " ") + " " + a["menu"].ljust(26, " ") + " " + a["price"] + ".-")
                print("-" * 38)
                break
            elif choose == "4":
                print("\n" + " " * 13 + "B A K E  M Y  D A Y")
                print("-" * 45 + "\n" + "🍪 COOKIES\n" + "-" * 45)
                print("|NO|" + " " * 2 + "|MENU|" + " " * 25 + "|PRICE|")
                for a in p.data_lst[17:26]:
                    print(" " + a["id"].ljust(4, " ") + " " + a["menu"].ljust(32, " ") + " " + a["price"] + ".-")
                print("-" * 45)
                break
            elif choose == "5":
                print("\n" + " " * 4 + "B A K E  M Y  D A Y")
                print("-" * 29 + "\n" + "☕ DRINKS\n" + "-" * 29)
                print("|NO|" + " " * 2 + "|MENU|" + " " * 10 + "|PRICE|")
                for a in p.data_lst[26:]:
                    print(" " + a["id"].ljust(4, " ") + " " + a["menu"].ljust(17, " ") + " " + a["price"] + ".-")
                print("-" * 29)
                break
            elif choose == "b":
                break
            else:
                print("Please enter number 1-5 or 'b' to go back.")

