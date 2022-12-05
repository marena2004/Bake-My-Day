# Bake-My-Day
- Bake my day is a bakery shop that only sell on online platform.

Overview of Bake my day: 
- we have 26 of bakery menu and 8 of drinks. 
- Customer have to register or login before order the menu
- After customer purchase our product successfully, the program will create receipt for customer

### 1. Module `customer.py`
This module contains the `Database` class for collect an information of username and password of customer.
This class contains 3 functions.
- def login(self): this function will ask input of username and password, 
and check whether this data is in json file or not.
- def register(self): this function will ask name of customer and let them create new account, and store 
data of username and password in json file.
- def user(self): this function will let customers choose whether they want to log in or register.

### 2. Module `menu.csv`
This module contains id,menu,price,and stock of product.

### 3. Module `product.py`
This module contains the `Product` class for check and update stock.
This class contain 3 functions.
- def readfile(self): this function will read csv file and collect menu data in list.
- def check_stock(self, stock: int, use: int): this function will get input of stock and use,
then check whether stock is enough to sell or not.
- def update_stock(self, stock: int, use: int): this function will get input of stock and use,
then update stock.

### 4. Module `manage.py`
This module contains the `Orders` class for manage order in shop.
This class contains 8 functions.
- def add_menu(self, choose): this function will add menu that customer chooses into order cart.
- def delete(self, choose): this function will delete unwanted menu of customers.
- def cancel(self): this function will clear all order in cart. 
- def subtotal(self): this function will get subtotal price of order.
- def discount(self): this function will check whether customer get discount or not.
- def total(self): this function will final total price. 
- def get_id_order(self): this function will get id order for customer.
- def receipt(self): this function will print receipt for customer.

### 5. Module `main.py`
This module is for run the program; it contains 3 functions.
- def readfile(): this function will read menu csv file and collect in list
- def show_menu(): this functions will create menu bar and show it to customers.
- def purchase(): this function will let customers select the choices and purchase product.

### 6. Module `users.json`
This menu will collect data of username and password of customer.



  