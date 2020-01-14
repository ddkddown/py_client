from message import Message
from message import Respond
from sock import Sock
import tkinter as tk
import tkinter.scrolledtext as tst
import tkinter.filedialog
import logfile


class Application(tk.Frame):
    def __init__(self, master=None, username=''):
        tk.Frame.__init__(self, master)
        self.grid()
        self.createWidgets()
        self.username = username
        self.__root = master
        self.__logger = logfile.somewhere_logger()

    def createWidgets(self):
        self.textEdit = tst.ScrolledText(self, width=80, height=20)
        self.textEdit.grid(row=0, column=0, rowspan=6)
        self.btnOpen = tk.Button(self, text='打开', command=self.funcOpen)
        self.btnOpen.grid(row=1, column=1)
        self.btnSave = tk.Button(self, text='保存', command=self.funcSave)
        self.btnSave.grid(row=2, column=1)
        self.btnQuit = tk.Button(self, text='退出', command=self.funcQuit)
        self.btnQuit.grid(row=3, column=1)

    def funcOpen(self):
        self.textEdit.delete(1.0, tk.END)
        fname = tk.filedialog.askopenfilename(filetypes=[('文本文件', '.txt')])
        with open(fname, 'r') as f:
            str1 = f.read()
        self.textEdit.insert(0.0, str1)

    def funcSave(self):
        str1 = self.textEdit.get(1.0, tk.END)
        connect = Sock()
        if len(str1) >= 512:
            while len(str1) >= 512:
                str2 = str1[0:512]
                str1 = str1[512:]
                connect.load_message(Message(type='2', is_end='6', user_name=self.username,
                                             head='ddktest', content=str2))
                connect.send_message(wait=False)
        else:
            connect.load_message(Message(type='2', is_end='6', user_name=self.username, head='ddktest', content=str1))
            connect.send_message(wait=False)
        str2 = ''
        connect.load_message(Message(type='2', is_end='5', user_name=self.username, head='ddktest', content=str2))
        if connect.send_message():
            self.__logger.somewhere_info("send message success")
        else:
            self.__logger.somewhere_warning("send message failed!")


    def funcQuit(self):
        self.__root.destroy()
