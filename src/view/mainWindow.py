from tkinter import *
from tkinter import ttk

class MainWindow:

    def __init__(self, root, controller):
        self.root = root
        self.controller = controller
        self.menus = {}        
        self.render_widgets()

    def render_widgets(self):
        
        frame = Frame(self.root)

        menuBar = Menu(self.root)

        menuFile = Menu(menuBar, tearoff=0)
        menuFile.add_command(label="AFD", command=self.nothing)
        menuFile.add_command(label="AFND", command=self.nothing)
        menuFile.add_command(label="GR", command=self.nothing)
        menuFile.add_command(label="ER", command=self.nothing)
        menuFile.add_separator()
        menuFile.add_command(label="Sair", command=self.root.quit)

        menuSave = Menu(menuBar, tearoff=0)
        menuSave.add_command(label="Salvar Original", command=self.nothing)
        menuSave.add_command(label="Salvar Novo", command=self.nothing)
                
        menuAFD = Menu(menuBar, tearoff=0)
        menuAFD.add_command(label="Futuras acoes sobre AFDs")

        menuAFND = Menu(menuBar, tearoff=0)
        menuAFND.add_command(label="Futuras acoes sobre AFNDs")

        menuGR = Menu(menuBar, tearoff=0)
        menuGR.add_command(label="Futuras acoes sobre GR")

        menuER = Menu(menuBar, tearoff=0)
        menuER.add_command(label="Futuras acoes sobre ERs")

        menuBar.add_cascade(label="Abrir", menu=menuFile)
        menuBar.add_cascade(label="Salvar", menu=menuSave)
        menuBar.add_cascade(label="AFD", menu=menuAFD)
        menuBar.add_cascade(label="AFND", menu=menuAFND)
        menuBar.add_cascade(label="GR", menu=menuGR)
        menuBar.add_cascade(label="ER", menu=menuER)

        self.menuBar = menuBar
        

        """
        self.menus["menuFile"] = menuFile
        self.menus["menuSave"] = menuSave
        self.menus["menuAFD"] = menuAFD
        self.menus["menuAFND"] = menuAFND
        self.menus["menuGR"] = menuGR
        self.menus["menuER"] = menuER
        """

        #self.disable_menus()
        self.root.config(menu=menuBar)


        frameTop = Frame(frame)
        frameBottom = Frame(frame)

        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_rowconfigure(0, weight=1)


        frame.grid(column=0, row=0, sticky="news")
        frame.grid_columnconfigure(0, weight=1)
        frame.grid_rowconfigure(0, weight=1)

        
        frameTop.grid(column=0, row=0, sticky="news")
        frameBottom.grid(column=0, row=1, sticky="nes")

        frameTop.grid_columnconfigure(0, weight=10)
        frameTop.grid_columnconfigure(1, weight=10)        
        frameTop.grid_rowconfigure(1, weight=1)        
        
        self.textOriginal = Text(frameTop, borderwidth=5, relief="ridge")
        self.textNew = Text(frameTop, borderwidth=5, relief="ridge")

        labelOriginal = Label(frameTop, text="Original")
        labelNovo = Label(frameTop, text="Novo")       

        self.textOriginal.grid(column=0, row=1, padx=(0,5), sticky="news")        
        self.textNew.grid(column=1, row=1, padx=(5,0), sticky="news")

        labelOriginal.grid(column=0, row=0, sticky="w")
        labelNovo.grid(column=1, row=0, padx=(5,0), sticky="w")
        

    def openFile(self):
                

        

    
    def disable_menus(self):
        self.menuBar.entryconfig("AFD", state="disabled")
        self.menuBar.entryconfig("AFND", state="disabled")
        self.menuBar.entryconfig("GR", state="disabled")
        self.menuBar.entryconfig("ER", state="disabled")        

    def nothing(self):
        print("nothing")

