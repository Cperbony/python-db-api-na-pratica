from db.repository import CashMachineDB, MoneySlipsDB


class CashMachineInsertMoneyBill:

    @staticmethod
    def insert_money_bill(money_bill, amount):
        cash_machine = CashMachineDB().get()
        cash_machine.money_slips[money_bill] += amount
        MoneySlipsDB.update(cash_machine)
        # from file import MoneySlipsFileWriter
        # MoneySlipsFileWriter().write_money_slips(cash_machine.money_slips)
        return cash_machine


class CashMachineWithDraw:

    @staticmethod
    def withdraw(bank_account, value):
        cash_machine = CashMachineDB().get()
        money_slips_user = cash_machine.withdraw(value)
        if money_slips_user:
            CashMachineWithDraw.__balance_debit(bank_account, value)
            # from file import MoneySlipsFileWriter
            # MoneySlipsFileWriter().write_money_slips(cash_machine.money_slips)
        return cash_machine

    @staticmethod
    def __balance_debit(bank_account, value):
        bank_account.balance_debit(value)
        # BankAccountFileWriter().write_bank_account(bank_account)

# accounts_list = [
#     BankAccount('0001-02', 'Fulano da Silva', '123456', 100, False),
#     BankAccount('0002-02', 'Cicrano da Silva', '123456', 50, False),
#     BankAccount('1111-11', 'Admin da Silva', '123456', 1000, True),
# ]
