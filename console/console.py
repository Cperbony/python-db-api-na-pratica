import getpass

from auth import AuthBankAccount
from console.operations import CashMachineOperation


class AuthBankAccountConsole:

    @staticmethod
    def is_auth():
        agency_number_typed = input("Digite sua Agência: ")
        account_number_typed = input('Digite sua conta: ')
        password_typed = getpass.getpass('Digite sua senha: ')

        return AuthBankAccount.authenticate(
            agency_number_typed, account_number_typed, password_typed
        )


class CashMachineConsole:

    @staticmethod
    def call_operation():
        CashMachineConsole.__show_user_welcome()
        option_typed = CashMachineConsole.__get_menu_options_typed()
        CashMachineOperation.do_operation(option_typed)

    @staticmethod
    def __get_menu_options_typed():
        print("%s - Saldo" % CashMachineOperation.OPERATION_SHOW_BALANCE)
        print("%s - Saque" % CashMachineOperation.OPERATION_WITHDRAW)
        bank_account = AuthBankAccount.bank_account_authenticated
        if bank_account.user.admin:
            print('%s - Inserir cédulas' % CashMachineOperation.OPERATION_INSERT_MONEY_BILL)
        return input('Escolha uma das opções acima: ')

    @staticmethod
    def __show_user_welcome():
        user = AuthBankAccount.bank_account_authenticated.user
        print('Olá %s, seja bem vindo!' % user.name)


