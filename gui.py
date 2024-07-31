import tkinter as tk
import ttkbootstrap as ttk
from conversor import dollarToReal, realToDollar

class Gui:
    def __init__(self, dollar, date):
        self.dollar = dollar
        self.date = date
        self.window = ttk.Window(themename='darkly')
        self.window.title('Converter')
        self.width = 750
        self.height = 300
        self.screenWidth = self.window.winfo_screenwidth()
        self.screenHeight = self.window.winfo_screenheight()
        self.window.geometry(f'{self.width}x{self.height}+{int((self.screenWidth/2)-(self.width/2))}+{int((self.screenHeight/2)-(self.height/2))}')
        self.window.resizable(0, 0)
    
    def header(self):
        self.labelTitle = ttk.Label(master=self.window, text='Converter', font='Arial 36 bold')
        self.labelTitle.pack(pady=15)
        self.labelDollar = ttk.Label(master=self.window, text='1 United States Dollar equals', font='Arial 16')
        self.labelDollar.pack()
        self.labelReal = ttk.Label(master=self.window, text=f'{self.dollar} Brazilian Real', font='Arial 30')
        self.labelReal.pack()
        self.labelDate = ttk.Label(master=self.window,text=self.date, font='Arial 16')
        self.labelDate.pack()
    
    def frame1(self):
        self.frameDollar = ttk.Frame(master=self.window)
        self.frameDollarLabel = ttk.Label(master=self.frameDollar, text='Dollar', font='Arial 16 bold')
        self.frameDollarLabel.pack(side='left', padx=10)
        self.dollarVar = tk.IntVar()
        self.entryDollar = ttk.Entry(master = self.frameDollar, textvariable=self.dollarVar)
        self.entryDollar.pack(side='left')
        self.frameDollar.pack(pady=10)
    
    def frame2(self):
        self.frameReal = ttk.Frame(master=self.window)
        self.frameRealLabel = ttk.Label(master=self.frameReal, text='Real', font='Arial 16 bold')
        self.frameRealLabel.pack(side='left', padx=17)
        self.realVar = tk.IntVar()
        self.entryReal = ttk.Entry(master = self.frameReal, textvariable=self.realVar)
        self.entryReal.pack(side='left')
        self.frameReal.pack()

    def run(self):
        self.header()
        self.frame1()
        self.frame2()
        self.entryReal.bind('<Any-KeyPress>', lambda event: self.window.after_idle(self.realConvert))
        self.entryDollar.bind('<Any-KeyPress>', lambda event: self.window.after_idle(self.dollarConvert))
        self.window.mainloop()

    def dollarConvert(self, *args):
        try:
            self.value = float(self.entryDollar.get())
            self.result = dollarToReal(self.dollar, self.value)
            self.realVar.set(self.result)
        except:
            self.realVar.set(0)

    def realConvert(self, *args):
        try:
            self.value = float(self.entryReal.get())
            self.result = realToDollar(self.dollar, self.value)
            self.dollarVar.set(self.result)
        except:
            self.dollarVar.set(0)
