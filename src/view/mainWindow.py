from tkinter import *

class MainWindow:

    def __init__(self, root, controller):
        self.root = root
        self.controller = controller
        self.render_widgets()

    def render_widgets(self):
        
        frame = Frame(self.root)

        menuBar = Menu(frame)

        menuFile = Menu(menuBar)
        menuFile.add_command(label="AFD", command=)
        menuFile.add_command(label="AFND", command=)
        menuFile.add_command(label="GR", command=)
        menuFile.add_command(label="ER", command=)
        menuFile.add_separator()
        menuFile.add_command(label="Sair", command=self.root.quit)

        menuSave = Menu(menuBar)
        menuSave.add_command(label="Salvar", command=)
        menuSave.add_command(label="Salvar como", command=)
                
        menuAFD = Menu(menuBar)
        menuAFD.add_command(label="Futuras acoes sobre AFDs")

        menuAFND = Menu(menuBar)
        menuAFND.add_command(label="Futuras acoes sobre AFNDs")

        menuGR = Menu(menuBar)
        menuGR.add_command(label="Futuras acoes sobre GR")

        menuER = Menu(menuBar)
        menuER.add_command(label="Futuras acoes sobre ERs")

        menuBar.add_cascade(label="Abrir", menu=menuFile)
        menuBar.add_cascade(label="Salvar", menu=menuSave)
        menuBar.add_cascade(label="AFD", menu=menuAFD)
        menuBar.add_cascade(label="AFND", menu=menuAFND)
        menuBar.add_cascade(label="GR", menu=menuGR)
        menuBar.add_cascade(label="ER", menu=menuER)

        frame.config(menu=menuBar)



