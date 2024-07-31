from conversor import *
from time import sleep

def menu(dollar, date):
    print('-'*30)
    print(f'''1 United States Dollar equals
{dollar} Brazilian Real
{date}''')
    print('-'*30)
    print('''[ 1 ] Convert Dollar to Real
[ 2 ] Convert Real to Dollar
[ 0 ] Exit''')

def option(dollar):
    choice = int(input('Option: '))
    match choice:
        case 0:
            print('-'*30)
            print('Exit...')
            print('-'*30)
            return False
        case 1:
            print('-'*30)
            print('Dollar to Real')
            try:
                value = float(input('Dollar Value: '))
            except Exception as e:
                print(f'Error: {e}')
            else:
                print(f'Real Value: {dollarToReal(dollar, value)}')
                sleep(2)
                return True
        case 2:
            print('-'*30)
            print('Real to Dollar')
            try:
                value = float(input('Real Value: '))
            except Exception as e:
                print(f'Error: {e}')
            else:
                print(f'Dollar Value: {realToDollar(dollar, value)}')
                sleep(2)
                return True
        case _:
            print('Choice needs to be between 1 and 2')
            sleep(2)
            return True

def run(dollar, date):
    running = True
    while running:
        menu(dollar, date)
        running = option(dollar)
