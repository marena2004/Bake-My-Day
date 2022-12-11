from manage import Orders
from user import Customer
from product import Product


def interface():
    print("\n(=^‥^)ノ Hello welcome to BAKE MY DAY 🍞\n")
    cart = Orders()
    while True:
        print("(1) Show menu\n(2) Add menu\n(3) Delete menu\n(4) Cancel\n(5) Payment\n(6) Exit")
        choices = str(input("Please select the choices: "))
        if choices == "1":
            Product().show_menu()

        if choices == "2":
            choose = input("Please choose your happiness: ")

            if not cart.add_menu(choose):
                print("Not found, please try again.")

        if choices == "3":
            for k, v in cart.item.items():
                print(k, v)
            cart.delete()

        if choices == "4":
            if cart.item == {}:
                print("Your cart is empty, please select menu.")

            else:
                cart.cancel()
                break

        if choices == "5":
            cart.receipt()
            print(open("order_receipt.txt").read())

            break

        if choices == "6":
            break


if __name__ == '__main__':
    Customer().login()
    interface()
