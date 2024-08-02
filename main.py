from scripts.api import Api
from scripts.gui import MainGui, ErrorGui

class Main:
    def __init__(self, api) -> None:
        # Inicializa a instância da classe Main com um objeto da classe API
        self.api = api
        # Inicializa o atribuido GUI como Nome, que será usado para armazenar a instância da GUI
        self.gui = None
    
    def processData(self):
        # Chama o método getData da instância da API e armazena o resultado em getData
        getData = self.api.getData()
        # Armazena os dados retornados pela API no atributo info
        self.info = self.api.data
        if getData:
            #Extrai a data e a taxa de câmbio do dólar dos dados da API
            self.date = self.info['USDBRL']['create_date']
            self.exchange = round(float(self.info['USDBRL']['ask']), 2)
            return True
        # Retorna False se a chamada da API falhar
        return False
            
    def setupGui(self, validation) -> None:
        if validation:
            # Se a validação for bem-sucedida, inicializa a GUI principal
            self.gui = MainGui(self.exchange, self.date)
        else:
            # Se a validação falhar, inicializa a GUI de erro com a mensagem de erro
            self.gui = ErrorGui(self.info)

    def run(self) -> None:
        # Executa o método processData e armazena o resultado em validation
        validation = self.processData()
        # Configura a GUI apropriada com base no resultado da validação
        self.setupGui(validation)
        # Executa a GUI
        self.gui.run()

if __name__ == '__main__':
    # Cria uma instância da classe API com a URL da API de taxas de câmbio
    api = Api(r'https://economia.awesomeapi.com.br/json/last/USD-BRL')
    # Cria uma instância da classe Main com a instância da classe API
    main = Main(api)
    # Chama o método run da instância da classe Mainn para iniciar a aplicação
    main.run()
