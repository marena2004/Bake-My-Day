from product import Product
import random
from datetime import datetime
from user import Customer


class Orders:
    def __init__(self):
        self.__item = {}

    @property
    def item(self):
        return self.__item

    @item.setter
    def item(self, item):
        self.__item = item

    def add_menu(self, choose):
        """
        This function will add item into customer cart. it will get input if product's id ,
        and then check whether that product is available or not
        :param choose:
        :return:
        """
        for data in Product().readfile():
            if choose == data["id"]:
                amount = int(input(f"How many {data['menu']} do you want?: "))
                if Product().check_stock(int(data["stock"]), amount):  # check whether menu available or not
                    Product().update_stock(int(data["stock"]), amount)  # update stock
                    self.__item.update({data["menu"]: {"id": data["id"],  # update cart
                                                       "quantity": amount,
                                                       "subtotal": int(data["price"]) * amount}})
                    print(f"Add {amount} {data['menu']} to the cart.")
                    return self.__item
                else:
                    return False

    def delete(self):
        """
        This function will delete unwanted item from customer cart
        :return:
        """
        choose = input("Which one do you want to delete?: ")
        for menu, info in self.__item.copy().items():
            # check whether product that customer chooses is in the cart or not
            if choose == info["id"]:
                # check whether customer really want to remove item
                sure = input(f"Are you sure do you want to remove {menu}?(y/n) ")
                if sure == "y":
                    self.__item.pop(menu)  # remove unwanted menu from cart
                    print(f'{menu} has been removed.')
                    break
                elif sure == "n":
                    break

    def cancel(self):
        self.__item.clear()  # delete all orders
        print("Cancel successfully.")

    def subtotal(self):
        total_price = 0
        for menu, info in self.__item.items():
            total_price += int(info["subtotal"])
        return total_price

    def discount(self):
        if self.subtotal() >= 300:  # check whether customer purchase more than 300 or not.
            dis = self.subtotal() * 0.1
            return dis
        return 00.00

    def total(self):
        if self.subtotal() >= 300:
            total = self.subtotal() - self.discount()
            return total
        return self.subtotal()

    def get_id_order(self):
        upper_case = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        number = '1234567890'
        use_for = upper_case + number
        length = 15
        id_order = ''.join(random.sample(use_for, length))  # create order id's for customer.
        return id_order

    def receipt(self):
        """
        This function will print receipt for customer
        :return:
        """
        now = datetime.now()
        day = now.date()
        time = now.strftime("%H:%M")
        with open("order_receipt.txt", "w") as f:  # write receipt in text file
            f.write(f"\n")
            f.write(" " * 28 + "B A K E  M Y  D A Y\n\n")
            f.write(" " * 21 + "Thank you for ordering our product!\n\n")
            f.write(f"Order #{self.get_id_order()}\n\n")
            f.write("Menu" + " " * 30 + "Quantity" + " " * 30 + "Price\n")
            f.write("-" * 80 + "\n")
            for k, v in self.__item.items():
                f.write(f"{k}".ljust(37, " ") + f"{v['quantity']}".ljust(35, " ") + f"{v['subtotal']}.-\n")
            f.write("-" * 80 + "\n")
            pay = input("Do you want to pay by Bank Transfer(b) or Credit Card(c)?: ")
            while True:
                if pay == 'b':
                    f.write(f"Subtotal: {self.subtotal():.2f}฿".ljust(58, " ") + f"Payment: Bank Transfer\n")
                    break
                elif pay == 'c':
                    f.write(f"Subtotal: {self.subtotal():.2f}฿".ljust(58, " ") + f"Payment: Credit Card\n")
                    break
                elif not pay == 'b' or 'c':
                    print("Please enter b or c only")
                    pay = input("Do you want to pay by Bank Transfer(b) or Credit Card(c)?: ")
            f.write(f"Shipping fee: 0.00฿" + " ".ljust(39, " ") + f"Order date: {day}\n")
            f.write(f"Discount: {self.discount():.2f}฿".ljust(58, " ") + f"Time: {time}\n")
            f.write(f"Total: {self.total():.2f}฿\n\n")
            f.write(f"Shipping to:\n")
            c = Customer()
            c.customer_detail()
            f.write(f"{c.name.title()}\n")
            f.write(f"{c.phone}\n")
            f.write(f"{c.address.title()}\n")
            f.write("-" * 80 + "\n")
            f.write(" " * 24 + "H A V E  A  N I C E  D A Y!")
