from message import Message
from message import Respond
import socket
import logfile


class Sock():

    def __init__(self, server_ip="127.0.0.1", server_port=7796):
        self.__ip = server_ip
        self.__port = server_port
        self.__address = (self.__ip, self.__port)
        self.__sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__respond_size = 2
        self.__logger = logfile.somewhere_logger()

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
            self.__logger.somewhere_error("recv message error:", ex)
        finally:
            return success

    def load_message(self, mess: Message):
        self.__message: Message = mess

    def send_message(self, wait=True):
        success = True
        try:
            self.__sock.connect(self.__address)
            self.__sock.sendall(self.__message.get_message().encode())
            if wait:
                success = self.__handle_respond()
        except Exception as ex:
            success = False
            self.__sock.close()
            self.__logger.somewhere_error("send message error:", ex)
        finally:
            if wait:
                self.__sock.close()
            return success
