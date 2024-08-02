class Converter:
    def __init__(self, exchange) -> None:
        '''
        Inicializa a instância da classe Converter com a taxa de câmbio do dólar.
        
        :param dollar: Taxa de câmbio do dólar em relação ao real. 
        '''
        self.exchange = exchange
        self.value = None

    def dollarToReal(self, value) -> float:
        '''
        Converte um valor de dólares para reais usando a taxa de câmbio fornecida.
        
        :param value: Valor em dólares a ser convertido.
        :return: Valor convertido em reais, arredondado para 2 casas decimais.
        :raises ValueError: Se o valor em dólares for negativo.
        '''
        # Armazena o valor em dólar 
        self.value = value
        if self.value < 0:
            # Levanta uma exceção se o valor for negativo
            raise ValueError('The Dollar value must be positive')
        # Converte o valor em dólares para reais multiplicando pela taxa de câmbio
        # O resultado é arredondado para 2 casas decimais
        return round(self.exchange * self.value, 2)

    def realToDollar(self, value) -> float:
        # Armazena o valor em reais
        self.value = value
        if self.value < 0:
            # Levanta uma exceção se o valor for negativo
            raise ValueError('The Real value must be positive')
        # Converte o valor em reais para dólares dividindo pela taxa de câmbio
        # O resultado é arredondado para 2 casas decimais
        return round(self.value / self.exchange, 2)
