# Bake-My-Day
- Bake my day is a bakery shop that only sells on the online platform.

Overview of Bake my day:
- we have 26 bakery menus and 8 drinks.
- Customer has to register or login before ordering the menu
- After the customer purchase our product successfully, the program will create a receipt for the customer
- 
### 1. Module `users.py`
This module contains the `Customer` class for collecting information on the name, address, and phone number of customer.
This class contains 4 functions.
- def customer_detail(self): this function will ask for input of the name, address, and phone number of the customer
- def new_user(self): This function is for a customer that doesn't have an account. it will let the customer create a username and password, then collect them in a JSON file
- def old_user(self): This function is for customer that already registers; it will change aks username and password of the customer for login.
- def login(self): this function will let customers choose whether they want to log in or register.



### 2. Module `menu.csv`
This module contains the id, menu, price, and stock of the product.

### 3. Module `product.py`
This module contains the `Product` class for checking and updating stock.
This class contains 4 functions.
- def readfile(self): this function will read CSV file and collect menu data in the list.
- def check_stock(self, stock: int, use: int): this function will get input of stock and use,
then check whether the stock is enough to sell or not.
- def update_stock(self, stock: int, use: int): this function will get input of stock and use,
then update stock.
- def show_menu(self): this function will create a menu bar and show it to the customer


### 4. Module `manage.py`
This module contains the `Orders` class for managing orders in the shop.
This class contains 8 functions, and have 2 additional modules.
- def add_menu(self, choose): this function will add the menu that the customer chooses to the order cart.
- def delete(self, choose): this function will delete the unwanted menu of customers from the customer's cart.
- def cancel(self): this function will clear all orders in the cart.
- def subtotal(self): this function will get the subtotal price of the order.
- def discount(self): this function will check whether the customer gets a discount or not; the customer has to purchase more than 300 in order to get a discount.
- def total(self): this function will calculate the final price.
- def get_id_order(self): this function will get the order's id for the customer.
- def receipt(self): this function will print receipts for customers.
- module `random`: I use this module to create an order id for customers from random letters and numbers.
- module `DateTime`: I use this module to specify the date and time that customer purchase products from bake my day

### 5. Module `main.py`
This module is for running the program; it contains 1 function.
- def interface(): this function will let customers select the choices and purchase products.

### 6. Module `user_login_data.json`
This menu will collect the data of the username and password of the customer.





  