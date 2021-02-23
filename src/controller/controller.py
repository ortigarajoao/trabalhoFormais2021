from tkinter import *
from view.mainWindow import MainWindow

class Controller:
    
    def __init__(self):
        self.root = Tk()
        self.root.title("Trabalho INE5421")
        self.window = MainWindow(self.root, self)
        self.root.mainloop()
