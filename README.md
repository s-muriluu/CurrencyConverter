# Currency Converter

Este projeto é uma aplicação de conversão de moeda que permite converter entre Dólares e Reais usando uma taxa de câmbio fornecida por uma API externa. A aplicação possui uma interface gráfica desenvolvida com Tkinter e `ttkbootstrap`.

## Estrutura do Projeto

- `scripts/api.py`: Define a classe `Api` para buscar dados de taxa de câmbio de uma API.
- `scripts/converter.py`: Define a classe `Converter` para realizar a conversão entre Dólares e Reais.
- `scripts/gui.py`: Define as classes `Gui`, `MainGui`, e `ErrorGui` para a interface gráfica da aplicação.
- `main.py`: O script principal que configura a aplicação e executa a interface gráfica.

## Dependências

Para executar o projeto, é necessário instalar as seguintes bibliotecas:

- `ttkbootstrap`: Biblioteca para temas modernos com Tkinter.
- `requests`: Biblioteca para realizar requisições HTTP.
- `tkinter`: Biblioteca para criação de interfaces gráficas (integrada no Python).

Instale as dependências executando:

```bash
pip install ttkbootstrap requests
```

## Como Usar

### Executar o Script Principal

Execute o script principal para iniciar a aplicação:

```bash
python main.py
```

### Executável

Para facilitar o uso em máquinas que não possuem Python instalado, você pode usar o executável incluído no projeto.
- **Localização**: Na pasta `dist`, você encontrará o executável da aplicação.
- **Execução**: Basta executar o arquivo CurrencyConverter.exe (ou o nome equivalente para o seu sistema operacional) para iniciar a aplicação.

## Funcionamento

- A aplicação obtém a taxa de câmbio atual do Dólar para o Real usando a API [https://economia.awesomeapi.com.br/json/last/USD-BRL](https://economia.awesomeapi.com.br/json/last/USD-BRL).
- Exibe a taxa de câmbio e a data da última atualização na interface gráfica.
- Permite a conversão entre Dólares e Reais diretamente na interface gráfica.

## Interface Gráfica

- **Campo de Dólares**: Insira um valor em Dólares para converter para Reais.
- **Campo de Reais**: Insira um valor em Reais para converter para Dólares.

  A conversão é atualizada automaticamente enquanto você digita.

## Tratamento de Erros

Se a API não puder ser acessada ou se ocorrer um erro de conversão, a interface gráfica exibirá uma mensagem de erro apropriada.

## Estrutura do Código

### `scripts/api.py`

Define a classe `Api` para buscar dados de taxa de câmbio da API.

Métodos:
- `get_data()`: Obtém e retorna os dados da API. Lança uma exceção em caso de erro.

### `scripts/converter.py`

Define a classe `Converter` para realizar conversões entre Dólares e Reais.

Métodos:
- `dollar_to_real(value)`: Converte um valor em Dólares para Reais.
- `real_to_dollar(value)`: Converte um valor em Reais para Dólares.

### `scripts/gui.py`

Define a interface gráfica usando Tkinter e `ttkbootstrap`.

Classes:
- `Gui`: Classe base para a janela principal.
- `MainGui`: Extensão da classe `Gui` para a interface de conversão de moeda.
- `ErrorGui`: Extensão da classe `Gui` para exibir mensagens de erro.

### `main.py`

Configura e executa a aplicação principal. Configura a API, cria a interface gráfica e gerencia a lógica de conversão.
