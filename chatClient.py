#python internet chat room client
import socket
from Tkinter import *
class MyApp(object):
    def __init__(self):
        self.root = Tk()
        self.root.wm_title("Z Chat")
        self.user_input = StringVar()
        self.user_inputarea = Entry(self.root, textvariable=self.user_input)
        self.user_inputarea.bind("<Return>", self.entry_input)
        self.user_inputarea.pack(pady=10,padx=10)
        self.root.mainloop()
    def entry_input(self, a):
        self.user_entered = self.user_input.get()
        print self.user_entered
        self.user_input.set('')
        
MyApp()