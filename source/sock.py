from message import Message
from message import Respond
import socket


class Sock():

    def __init__(self, server_ip="127.0.0.1", server_port=7796):
        self.__ip = server_ip
        self.__port = server_port
        self.__address = (self.__ip, self.__port)
        self.__sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__respond_size = 2

    def __handle_respond(self):
        success = False
        try:
            self.__respond = self.__sock.recv(self.__respond_size)
            print(self.__respond.decode()[1])
            self.__respond = self.__respond.decode()
            if self.__respond[1] == '1':
                success = True

        except socket.error as ex:
            success = False
            print("recv message error:", ex)
        finally:
            return success

    def load_message(self, mess: Message):
        self.__message: Message = mess

    def send_message(self):
        success = False
        try:
            self.__sock.connect(self.__address)
            self.__sock.sendall(self.__message.get_message().encode());
            success = self.__handle_respond()
        except Exception as ex:
            success = False
            print("send message error:", ex)
            return
        finally:
            self.__sock.close()
            return success
