from console.console import AuthBankAccountConsole, CashMachineConsole
from utils import clear, header
import os

os.environ['CASH_MACHINE_ID'] = "1"


def main():
    clear()
    header()

    if AuthBankAccountConsole.is_auth():
        clear()
        header()

        CashMachineConsole.call_operation()
    else:
        print('Conta inválida')


if __name__ == '__main__':
    while True:
        main()

        input('Pressione <ENTER> para continuar...')
