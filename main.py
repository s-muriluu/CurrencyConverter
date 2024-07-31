from api import getData
from menu import run

apiUrl = r'https://economia.awesomeapi.com.br/json/last/USD-BRL'
info = getData(apiUrl)
date = info['USDBRL']['create_date']
dollar = round(float(info['USDBRL']['ask']), 2)

run(dollar, date)
