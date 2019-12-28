from message import Message
from message import Respond
import tkinter as tk
import tkinter.scrolledtext as tst
import tkinter.filedialog
import socket
from editwindow import Application


class Sock():

    def __init__(self, server_ip="127.0.0.1", server_port=7796):
        self.__ip = server_ip
        self.__port = server_port
        self.__address = (self.__ip, self.__port)
        self.__sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__flag = False
        self.__respond_size = 2

    def __handle_respond(self):
        try:
            self.__respond = self.__sock.recv(self.__respond_size)
            print(self.__respond.decode()[1])
            self.__respond = self.__respond.decode()
            if self.__respond[1] == '1':
                self.__flag = True
                root = tk.Tk()
                root.title('somewhere')
                app = Application(master=root)
                app.mainloop()

        except socket.error as ex:
            print("recv message error:", ex)
            return
        finally:
            if self.__flag == True:
                print("byebye")
            else:
                print("recv false")
            return

    def load_message(self, mess: Message):
        self.__message: Message = mess

    def send_message(self):
        try:
            self.__sock.connect(self.__address)
            self.__sock.sendall(self.__message.get_message().encode());
            self.__handle_respond()
        except Exception as ex:
            print("send message error:", ex)
            return
        finally:
            self.__sock.close()
            return self.__flag
