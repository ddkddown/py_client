from message import Message
from message import Respond
from sock import Sock
import tkinter as tk
import tkinter.scrolledtext as tst
import tkinter.filedialog


class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.createWidgets()
        self.__root = master

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
        connect.load_message(Message(type='2', content=str1))
        connect.send_message()
        # 暂不保存到本地
        '''
        fname = tk.filedialog.asksaveasfilename(filetypes=[('文本文件', '.txt')])
        with open(fname, 'w') as f:
            f.write(str1)
        '''

    def funcQuit(self):
        self.__root.destroy()
