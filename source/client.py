from editwindow import Application
import user
import message
import menu
import sock
import tkinter as tk
import tkinter.scrolledtext as tst
import tkinter.filedialog


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
            # 给服务端发送用户名密码消息
            connect = sock.Sock()
            connect.load_message(message.Message(type='1', is_end='5', message_length='0',
                                                 user_name=id.username, pass_word=id.password))
            if connect.send_message():
                root = tk.Tk()
                root.title('somewhere')
                app = Application(master=root, username=id.username)
                app.mainloop()



        elif '2' == choose:
            print("bye ~ see you then")
        else:
            print("wrong choose")
            print("bye ~ see you then")
