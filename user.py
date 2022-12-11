import json


class Customer:

    def __init__(self):
        self.__name = ""
        self.__address = ""
        self.__phone = ""

    @property
    def name(self):
        return self.__name

    @property
    def phone(self):
        return self.__phone

    @property
    def address(self):
        return self.__address

    def customer_detail(self):
        """
        This is the function will get input of customer information
        :return:
        """

        self.__name = str(input("Please enter your name: "))
        self.__address = str(input("Please enter your address: "))
        self.__phone = str(input("Please enter your phone number: "))

        while True:
            if not self.__phone.isdigit():  # check whether all input are numbers
                print("Phone number must numbers!")
                self.__phone = input("Enter your phone number: ")
            elif len(self.__phone) < 10: # phone number not more than 10
                print("Invalid phone number")
                self.__phone = input("Enter your phone number: ")
            else:
                break

        return self.__name, self.address, self.__phone

    def new_user(self):
        """
        This function will create new account for customer
        :return:
        """
        self.__name = str(input("Please enter your name: "))
        username = input("Create your username: ")
        password = input("Create your password: ")

        new_data = {self.__name: {"Username": username,
                                  "Password": password
                                  }

                    }
        try:
            with open("user_login_data.json", "r") as f:
                data = json.load(f)

        except FileNotFoundError:
            with open("user_login_data.json", "w") as f:
                json.dump(new_data, f, indent=4)
                print("Account created successfully!")

        else:
            data.update(new_data)
            with open("user_login_data.json", "w") as f:
                json.dump(data, f, indent=4)
                print("Account created successfully!")

    def old_user(self):
        """
        This function will check whether customer's username and password are in database or not
        :return:
        """
        username = input("Please enter your username: ")

        try:
            with open("user_login_data.json", "r") as f:
                data = json.load(f)

        except FileNotFoundError:
            print("No data for your account")

        else:
            for k, v in data.items():
                if username in v["Username"]:
                    password = input("Please enter your password: ")
                    if password == v["Password"]:
                        print("Login successful!")
                        break
                    elif password != v["Password"]:
                        print("Incorrect password, please try again.")

    def login(self):
        print("(1)Log in | (2)Register")
        while True:
            select = str(input("Please select the number: "))
            if select == '1':
                return self.old_user()
            if select == '2':  # if customer don't have an account, they have to register first.
                return self.new_user()
            else:
                print("Enter number 1 or 2 only!")
