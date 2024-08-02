# O script da classe API foi projetado de forma genérica e pode ser utilizado com qualquer URL de API que retorne dados no formato JSON

import requests

class Api:
    def __init__(self, url) -> None:
        # Inicializa a instância da classe API com a URL fornecida
        self.url = url
        # Inicializa o atributo data como None para armazenar os dados da resposta ou a mensagem de erro
        self.data = None
    
    def getData(self) -> bool:
        try:
            # Faz uma requisição GET para a URL fornecida
            self.response = requests.get(self.url)
            # Levanta uma exceção se a resposta contiver um status code de erro
            self.response.raise_for_status()
        except requests.RequestException as e:
            # Em casod e exceção, armazena a mensagem de erro no atributo data
            self.data = f'Network error: {e}'
            return False
        try:
            # Converte a resposta da requisição para JSON
            self.data = self.response.json()
            return True
        except ValueError:
            # Em caso de exceção ao converter para JSON, armazena a mensagem de erro no atributo data
            self.data = 'Failed to parse JSON response'
            return False
