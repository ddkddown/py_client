import user
import message
import menu
import sock


class Client():
    def __init__(self):
        pass

    def start(self):
        # 显示初始菜单
        table = menu.Menu()
        table.login_menu()
        choose = input()
        if '1' == choose:
            nm_ps = table.login_input_message()
            id = user.User(nm_ps[0], nm_ps[1])
            #给服务端发送用户名密码消息
            
            print("--")
            pass
        elif '2' == choose:
            print("bye ~ see you then")
        else:
            print("wrong choose")
            print("bye ~ see you then")
