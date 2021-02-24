from view.mainWindow import MainWindow
from tkinter import *

class Controller:
    
    def __init__(self):
        self.root = Tk()
        self.root.title("Trabalho INE5421")
        self.root.geometry("800x500")
        self.root.minsize(800,500)
        self.window = MainWindow(self.root, self)
        self.root.mainloop()
