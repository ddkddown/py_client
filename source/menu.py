import os


class Menu():
    def __init__(self):
        pass

    def login_menu(self):
        os.system('clear')
        print("---------------------------------")
        print("hello, this is somewhere you can hide your secret by typping them")
        print("now, which way you want to go ?")
        print("1---     login the somewhere system")
        print("2---     see you later then\n")

    def login_input_message(self):
        os.system('clear')
        print("---------------------------------")
        print("please input username")
        username = input("username:")
        print("please input password")
        password = input("password:")
        return username, password


