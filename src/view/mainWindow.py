from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import os

class MainWindow:

    def __init__(self, root, controller):
        self.root = root
        self.controller = controller
        self.menus = {}
        self.currentOriginalFilePath = ""
        self.currentOriginalFile = None
        self.currentNewFilePath = ""
        self.currentNewFile = None
        self.render_widgets()

    def render_widgets(self):
        
        frame = Frame(self.root)

        menuBar = Menu(self.root)

        menuFile = Menu(menuBar, tearoff=0)
        menuFile.add_command(label="Abrir", command=self.openOriginalFile)
        menuFile.add_command(label="AFD", command=self.nothing, state="disabled")
        menuFile.add_command(label="AFND", command=self.nothing, state="disabled")
        menuFile.add_command(label="GR", command=self.nothing, state="disabled")
        menuFile.add_command(label="ER", command=self.nothing, state="disabled")
        menuFile.add_separator()
        menuFile.add_command(label="Sair", command=self.root.quit)

        menuSave = Menu(menuBar, tearoff=0)
        menuSave.add_command(label="Salvar Original", command=self.saveOriginalFile)
        menuSave.add_command(label="Salvar Original Como", command=lambda: self.saveOriginalFile(True))
        menuSave.add_command(label="Salvar Novo", command=self.saveNewFile)
        menuSave.add_command(label="Salvar Novo Como", command=lambda: self.saveNewFile(True))
                
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
        

    def openOriginalFile(self):        
        self.currentOriginalFilePath = filedialog.askopenfilename(initialdir=".", title="Selecione o arquivo")        
        self.currentOriginalFile = open(self.currentOriginalFilePath, "r+")
        self.textOriginal.delete(INSERT, END)
        self.textOriginal.insert(INSERT, self.currentOriginalFile.read())
        #print(self.currentOriginalFile.read())
    
    def saveOriginalFile(self, saveAs=False):
        if saveAs or self.currentOriginalFilePath == "" or self.currentOriginalFile == None:
            self.currentOriginalFilePath = filedialog.asksaveasfilename(initialdir=".", title="Salvar como")
            if self.currentOriginalFile != None:
                self.currentOriginalFile.close()
            self.currentOriginalFile = open(self.currentOriginalFilePath, "w+")
        #print(self.textOriginal.get("1.0",END))
        self.currentOriginalFile.seek(0)
        self.currentOriginalFile.write(self.textOriginal.get("1.0",END))
        self.currentOriginalFile.truncate()
        self.currentOriginalFile.flush()        
        os.fsync(self.currentOriginalFile.fileno())

    def saveNewFile(self, saveAs=False):
        if saveAs or self.currentNewFilePath == "" or self.currentNewFile == None:
            self.currentNewFilePath = filedialog.asksaveasfilename(initialdir=".", title="Salvar como")
            if self.currentNewFile != None:
                self.currentNewFile.close()
            self.currentNewFile = open(self.currentNewFilePath, "w+")
        self.currentNewFile.seek(0)
        self.currentNewFile.write(self.textNew.get("1.0", END))
        self.currentNewFile.truncate()
        self.currentNewFile.flush()
        os.fsync(self.currentNewFile.fileno())
        
    
    def disable_menus(self):
        self.menuBar.entryconfig("AFD", state="disabled")
        self.menuBar.entryconfig("AFND", state="disabled")
        self.menuBar.entryconfig("GR", state="disabled")
        self.menuBar.entryconfig("ER", state="disabled")        

    def nothing(self):
        print("nothing")

