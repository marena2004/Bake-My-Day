import csv
from manage import Orders
from customer import Database


def readfile():
    menu_lst = []
    with open("menu.csv", "r") as f:
        menu_ = csv.DictReader(f)
        for i in menu_:
            menu_lst.append([i["id"], i["menu"], i["price"]])
    return menu_lst


def show_menu():  # create menu bar
    print(" (1) PASTRIES/BREAD\n (2) CAKE\n (3) CHEESECAKE\n (4) COOKIES\n (5) DRINKS")
    choose = int(input('Please select number: '))
    while True:
        if choose < 1 or choose > 6:
            print("Please enter number 1-6 only!")
            choose = int(input('Please select number: '))
        if choose == 1:
            print(" " * 9 + "B A K E  M Y  D A Y")
            print("-" * 36 + "\n" + "🥐 PASTRIES/BREAD\n" + "-" * 36)
            print("|NO|" + " " * 2 + "|MENU|" + " " * 17 + "|PRICE|")
            for a in readfile()[:8]:
                print(" " + a[0].ljust(4, " ") + " " + a[1].ljust(24, " ") + " " + a[2] + ".-")
            print("-" * 36)
            break
        elif choose == 2:
            print(" " * 9 + "B A K E  M Y  D A Y")
            print("-" * 36 + "\n" + "🍰 CAKE\n" + "-" * 36)
            print("|NO|" + " " * 2 + "|MENU|" + " " * 17 + "|PRICE|")
            for a in readfile()[8:13]:
                print(" " + a[0].ljust(4, " ") + " " + a[1].ljust(24, " ") + " " + a[2] + ".-")
            print("-" * 36)
            break
        elif choose == 3:
            print(" " * 9 + "B A K E  M Y  D A Y")
            print("-" * 36 + "\n" + "🧀 CHEESECAKE\n" + "-" * 36)
            print("|NO|" + " " * 2 + "|MENU|" + " " * 17 + "|PRICE|")
            for a in readfile()[13:17]:
                print(" " + a[0].ljust(4, " ") + " " + a[1].ljust(24, " ") + " " + a[2] + ".-")
            print("-" * 36)
            break
        elif choose == 4:
            print(" " * 13 + "B A K E  M Y  D A Y")
            print("-" * 45 + "\n" + "🍪 COOKIES\n" + "-" * 45)
            print("|NO|" + " " * 2 + "|MENU|" + " " * 25 + "|PRICE|")
            for a in readfile()[17:26]:
                print(" " + a[0].ljust(4, " ") + " " + a[1].ljust(32, " ") + " " + a[2] + ".-")
            print("-" * 45)
            break
        elif choose == 5:
            print(" " * 4 + "B A K E  M Y  D A Y")
            print("-" * 29 + "\n" + "☕ DRINKS\n" + "-" * 29)
            print("|NO|" + " " * 2 + "|MENU|" + " " * 10 + "|PRICE|")
            for a in readfile()[26:]:
                print(" " + a[0].ljust(4, " ") + " " + a[1].ljust(17, " ") + " " + a[2] + ".-")
            print("-" * 29)
            break
        elif str(choose) == "q":
            break


def purchase():
    print("(=^‥^)ノ Hello welcome to BAKE MY DAY 🍞")
    print("(1) Show menu\n(2) Add menu\n(3) Delete menu\n(4) Cancel\n(5) Payment\n(6) Exit")
    choices = int(input("Please select the choices: "))
    cart = Orders()
    while True:
        if 1 > choices or choices > 5:
            print("Invalid number")
            print("(1) Show menu\n(2) Add menu\n(3) Delete menu\n(4) Cancel\n(5) Payment")
            choices = int(input("Please select the choices: "))
        if choices == 1:
            show_menu()
            print("(1) Show menu\n(2) Add menu\n(3) Delete menu\n(4) Cancel\n(5) Payment")
            choices = int(input("Please select the choices: "))

        if choices == 2:
            choose = input("Please choose your happiness: ")
            if not cart.add_menu(choose):
                print("Product out of stock, please select another menu.")
            else:
                print("(1) Show menu\n(2) Add menu\n(3) Delete menu\n(4) Cancel\n(5) Payment")
                choices = int(input("Please select the choices: "))

        if choices == 3:
            for k, v in cart.order.items():
                print(k, v)
            choose = input("Which one do you want to delete?: ")
            cart.delete(choose)
            print("(1) Show menu\n(2) Add menu\n(3) Delete menu\n(4) Cancel\n(5) Payment")
            choices = int(input("Please select the choices: "))

        if choices == 4:
            if cart.order == {}:
                print("Your cart is empty, please select menu.")
                print("(1) Show menu\n(2) Add menu\n(3) Delete menu\n(4) Cancel\n(5) Payment")
                choices = int(input("Please select the choices: "))
            else:
                cart.cancel()
                break

        if choices == 5:
            cart.receipt()
            print(open("order_receipt.txt").read())
            break

        if choices == 6:
            break


if __name__ == '__main__':
    Database().user()
    purchase()
