import json


class Customer:
    def __init__(self, name, username, password):
        self.__username = username
        self.__password = password
        self.__name = name

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
                if v["Username"] == self.__username and v["Password"] == self.__password:
                    print("Login successful!")

                elif v["Username"] and v["Password"] not in data:
                    print("No data for your account, please register.")

                else:
                    print("Incorrect password or username, please try again")

    def register(self):
        self.__name = input("Please enter your name: ")
        self.__username = input("Create your username: ")
        self.__password = input("Create your password: ")

        new_data = {self.__name: {"Username": self.__username,
                                  "Password": self.__password}

                    }
        try:
            with open("users.json", "r") as f:
                data = json.load(f)
        except FileNotFoundError:
            with open("users.json", "w") as f:
                json.dump(new_data, f, indent=4)
                print("Account created successfully!")

        else:
            data.update(new_data)
            with open("users.json", "w") as f:
                json.dump(data, f, indent=4)
                print("Account created successfully!")

    def remove(self, name):
        self.__name == input("Please enter your name: ")
        try:
            with open("users.json", "r") as f:
                data = json.load(f)

        except FileNotFoundError:
            print("No data for your account")

        else:
            if name == self.__name:
                for n in list(data):
                    data.pop(n)
                    with open("users.json", "w") as f:
                        json.dump(data, f, indent=4)
            else:
                print("No data for your account")

