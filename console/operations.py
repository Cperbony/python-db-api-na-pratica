from auth import AuthBankAccount
from cash_machine import CashMachineWithDraw, CashMachineInsertMoneyBill


class CashMachineOperation:
    OPERATION_SHOW_BALANCE = '1'
    OPERATION_WITHDRAW = '2'
    OPERATION_INSERT_MONEY_BILL = '10'

    @staticmethod
    def do_operation(option):
        bank_account = AuthBankAccount.bank_account_authenticated
        if option == CashMachineOperation.OPERATION_SHOW_BALANCE:
            ShowBalanceOperation.do_operation()
        elif option == CashMachineOperation.OPERATION_WITHDRAW:
            WithDrawOperation.do_operation()
        elif option == CashMachineOperation.OPERATION_INSERT_MONEY_BILL and bank_account.user.admin:
            InsertMoneyBillOperation.do_operation()


class ShowBalanceOperation:

    @staticmethod
    def do_operation():
        bank_account = AuthBankAccount.bank_account_authenticated
        print('Seu saldo é %s' % bank_account.value)


class WithDrawOperation:

    @staticmethod
    def do_operation():
        value_typed = input('Digite o valor a ser sacado: ')
        value_int = int(value_typed)
        bank_account = AuthBankAccount.bank_account_authenticated
        cash_machine = CashMachineWithDraw.withdraw(bank_account, value_int)
        if cash_machine.value_remaining != 0:
            print('O caixa não tem cédulas disponíveis para este valor')
        else:
            print('Pegue as notas:')
            print(cash_machine.money_slips_user)
            print(vars(bank_account))


class InsertMoneyBillOperation:

    @staticmethod
    def do_operation():
        amount_typed = input('Digite a quantidade de cédulas: ')
        money_bill_typed = input('Digite a cédula a ser incluída: ')

        cash_machine = CashMachineInsertMoneyBill.insert_money_bill(money_bill_typed, int(amount_typed))
        print(cash_machine.money_slips)