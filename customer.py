import json


class Database:
    def __init__(self):
        self.__username = ""
        self.__password = ""
        self.__name = ""

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, username):
        self.__username = username

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password):
        self.__password = password

    def login(self):
        self.__username = input("Please enter your username: ")
        self.__password = input("Please enter your password: ")
        try:
            with open("users.json", "r") as f:
                data = json.load(f)

        except FileNotFoundError:
            print("No data for your account")

        else:
            for k, v in data.items():
                if self.username in v["Username"] and self.password in v["Password"]:
                    print("Login successful!")

    def register(self):
        self.__name = input("Please enter your name: ")
        self.__username = input("Create your username: ")
        self.__password = input("Create your password: ")

        new_data = {self.__name: {"Username": self.__username,
                                  "Password": self.__password
                                  }
                    }
        try:
            with open("users.json", "r") as f:
                data = json.load(f)
        except FileNotFoundError:
            with open("users.json", "w") as f:
                json.dump(new_data, f, indent=4)
        else:  # create new account
            data.update(new_data)
            with open("users.json", "w") as f:
                json.dump(data, f, indent=4)
                print("Account created successfully!")

    def user(self):
        print("(1)Log in | (2)Register")
        select = int(input("Please select the number: "))
        while True:
            if select == "":
                print("Enter only number!")
                select = int(input("Please select the number: "))
            elif select == 1:
                return self.login()
            elif select == 2:
                return self.register()
            elif 1 > select or select > 2:
                print("Invalid number")
                select = int(input("Please select the number: "))

