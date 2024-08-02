import tkinter as tk
import ttkbootstrap as ttk
from scripts.converter import Converter

class Gui:
    def __init__(self) -> None:
        '''
        Inicializa a janela principal da aplicação
        '''
        # Cria a janela principal com o tema 'darkly'
        self.window = ttk.Window(themename='darkly')
        # Define o título da janela
        self.window.title('Currency Converter')
        # Dimensões da janela
        self.width = 750
        self.height = 300
        # Obtém largura e altura da tela
        self.screenWidth = self.window.winfo_screenwidth()
        self.screenHeight = self.window.winfo_screenheight()
        # Define e centraliza a janela na tela
        self.window.geometry(f'{self.width}x{self.height}+{int((self.screenWidth/2)-(self.width/2))}+{int((self.screenHeight/2)-(self.height/2))}')
        self.window.resizable(0, 0)

class MainGui(Gui):
    def __init__(self, exchange, date) -> None:
        '''
        Inicializa a interface gráfica principal com as informações de taxa de câmbio e data.
        
        :param exchange: A taxa de câmbio do dólar em relação ao real.
        :param date: A data em que a taxa de câmbio foi registrada.
        '''
        # Chama o contrutor da classe base Gui
        super().__init__()
        self.exchange = exchange
        self.date = date
        # Cria uma instância da classe Converter com a taxa de câmbio fornecida
        self.converter = Converter(self.exchange)
    
    def header(self) -> None:
        '''
        Cria e exibe o cabeçalho da interface gráfica com o título e as informações da taxa de câmbio.
        '''
        # Título principal
        self.labelTitle = ttk.Label(master=self.window, text='Converter', font='Arial 36 bold')
        self.labelTitle.pack(pady=15)
        # Texto explicativo
        self.labelDollar = ttk.Label(master=self.window, text='1 United States Dollar equals', font='Arial 16')
        self.labelDollar.pack()
        # Taxa de câmbio
        self.labelReal = ttk.Label(master=self.window, text=f'{self.exchange} Brazilian Real', font='Arial 30')
        self.labelReal.pack()
        # Data
        self.labelDate = ttk.Label(master=self.window,text=self.date, font='Arial 16')
        self.labelDate.pack()
    
    def frame1(self) -> None:
        '''
        Cria o primeiro quadro da interface gráfica para entrada de valor em dólares.
        '''
        # Cria um quadro para o campo de entrada de dólares
        self.frameDollar = ttk.Frame(master=self.window)
        self.frameDollarLabel = ttk.Label(master=self.frameDollar, text='Dollar', font='Arial 16 bold')
        self.frameDollarLabel.pack(side='left', padx=10)
        # Cria uma variável para armazenar o valor em dólares
        self.dollarVar = tk.IntVar()
        # Cria um campo de entrada para o valor em dólares
        self.entryDollar = ttk.Entry(master = self.frameDollar, textvariable=self.dollarVar)
        self.entryDollar.pack(side='left')
        # Posiciona o quadro na janela
        self.frameDollar.pack(pady=10)
    
    def frame2(self) -> None:
        '''
        Cria o segundo quadro da interface gráfica para entrada de valor em reais.
        '''
        # Cria um quadro para o campo de entrada de reais
        self.frameReal = ttk.Frame(master=self.window)
        self.frameRealLabel = ttk.Label(master=self.frameReal, text='Real', font='Arial 16 bold')
        self.frameRealLabel.pack(side='left', padx=17)
        # Cria uma variável para armazenar o valor em reais
        self.realVar = tk.IntVar()
        # Cria um campo de entrada para o valor em reais
        self.entryReal = ttk.Entry(master = self.frameReal, textvariable=self.realVar)
        self.entryReal.pack(side='left')
        # Posiciona o quadro na janela
        self.frameReal.pack()

    def run(self) -> None:
        '''
        Inicializa e executa a interface gráfica, configurando a interação entre os campos de entrada.
        '''
        # Configura e exibe os componentes da interface gráfica
        self.header()
        self.frame1()
        self.frame2()
        # Configura a conversão de valores em reais quando a tecla é pressionada no campo de entrada de reais
        self.entryReal.bind('<Any-KeyPress>', lambda event: self.window.after_idle(self.realConvert))
        # Configura a conversão de valores em dólares quando a tecla é pressionada no campo de entrada de dólares
        self.entryDollar.bind('<Any-KeyPress>', lambda event: self.window.after_idle(self.dollarConvert))
        # Inicia o loop principal da interface gráfica
        self.window.mainloop()

    def dollarConvert(self, *args) -> None:
        '''
        Converte o valor em dólares para reais e atualiza o campo de entrada de reais.
        '''
        try:
            # Obtém o valor em dólares do campo de entrada
            self.value = float(self.entryDollar.get())
            # Converte o valor para reais
            self.result = self.converter.dollarToReal(self.value)
            # Atualiza o campo de entrada de reais com o resultado
            self.realVar.set(self.result)
        except:
            # Se houver um erro, define o valor do campo de reais como 0
            self.realVar.set(0)

    def realConvert(self, *args) -> None:
        '''
        Converte o valor em reais para dólares e atualiza o campo de entrada de dólares.
        '''
        try:
            # Obtém o valor em reais do campo de entrada
            self.value = float(self.entryReal.get())
            # Converte o valor para dólares
            self.result = self.converter.realToDollar(self.value)
            # Atualiza o campo de entrada de dólares com o resultado
            self.dollarVar.set(self.result)
        except:
            # Se houver um erro, define o valor do campo de dólares como 0
            self.dollarVar.set(0)

class ErrorGui(Gui):
    def __init__(self, errorMsg) -> None:
        '''
        Inicializa a interface gráfica para exibir mensagens de erro.
            
        :param errorMsg: A mensagem de erro a ser exibida.
        '''
        # Chama o costrutor da classe base Gui
        super().__init__()
        self.errorMsg = errorMsg
    
    def message(self) -> None:
        '''
        Cria e exibe a mensagem de erro na interface gráfica.
        '''
        # Título
        self.labelTitle = ttk.Label(master=self.window, text='Converter', font='Arial 36 bold')
        self.labelTitle.pack(pady=15)
        # Mensagem de erro
        self.labelTitle = ttk.Label(master=self.window, text=self.errorMsg, font='Arial 16')
        self.labelTitle.pack()
    
    def run(self) -> None:
        # Configura e exibe a mensagem de erro
        self.message()
        # Inicia o loop principal da interface gráfica
        self.window.mainloop()
