from typing import Dict, Iterator

from db.db import DB, Hydrator
from db.models import BankAccount, Agency, User, CashMachine
from exceptions import AppException


class BankAccountDB:

    @staticmethod
    def find_by_number_and_password_and_agency_number(bank_account: BankAccount) -> BankAccount:
        cursor = DB.cursor()
        query = """
            SELECT * FROM bank_accounts
            JOIN agencies ON agencies.id = bank_accounts.agency_id
            JOIN users ON users.id = bank_accounts.user_id
            WHERE bank_accounts.number = %s AND 
                  agencies.number = %s AND
                  password = %s
            LIMIT 1
            """
        row_affected = cursor.execute(query, [
            bank_account.number,
            bank_account.agency.number,
            bank_account.password
        ])
        if row_affected != 1:
            raise AppException('Bank Account not Found!')
            # print('Conta bancária inválida')
            # return bank_account

        row = cursor.fetchone()

        return BankAccountDB.__convert_to_object(row)

        # for k, v in BankAccount.get_fields().items():
        #     if k in row_cloned:
        #         setattr(bank_account, k, row_cloned[k])
        #         row_cloned.pop(k)
        #
        # bank_account.agency = Agency()
        # for k, v in Agency.get_fields().items():
        #     key_relation = "agencies.%s" % k
        #     if k in row_cloned or key_relation in row_cloned:
        #         key_in = k if k in row_cloned else key_relation
        #         setattr(bank_account.agency, k, row_cloned[key_in])
        #         row_cloned.pop(key_in)
        #
        # bank_account.user = User()
        # for k, v in User.get_fields().items():
        #     key_relation = "users.%s" % k
        #     if k in row_cloned or key_relation in row_cloned:
        #         key_in = k if k in row_cloned else key_relation
        #         setattr(bank_account.user, k, row_cloned[key_in])
        #         row_cloned.pop(key_in)

        # print('bank_account', vars(bank_account))
        # print('agency', vars(bank_account.agency))
        # print('user', vars(bank_account

    @staticmethod
    def __convert_to_object(row: Dict) -> BankAccount:
        row_cloned = row.copy()
        bank_account = BankAccount()
        Hydrator.hydrate(bank_account, row_cloned)

        bank_account.agency = Agency()
        Hydrator.hydrate(bank_account.agency, row_cloned, 'agencies')

        bank_account.user = User()
        Hydrator.hydrate(bank_account.user, row_cloned, 'users')

        return bank_account


class CashMachineDB:

    @staticmethod
    def get() -> CashMachine:
        cursor = DB.cursor()
        query = "SELECT * FROM cash_machines WHERE id = %s"
        row_affected = cursor.execute(query, [1])
        if row_affected != 1:
            raise AppException('Cash Machine not found')
        row = cursor.fetchone()
        cash_machine = CashMachineDB.__convert_to_object(row)
        CashMachineDB.__add_money_slips(cash_machine)
        return cash_machine

    @staticmethod
    def __convert_to_object(row: Dict) -> CashMachine:
        row_cloned = row.copy()
        cash_machine = CashMachine()
        Hydrator.hydrate(cash_machine, row_cloned)

        return cash_machine

    @staticmethod
    def __add_money_slips(cash_machine: CashMachine) -> None:
        money_slips = MoneySlipsDB.all(cash_machine.id)
        cash_machine.money_slips = {}
        for row in money_slips:
            money_bill = str(row['money_bill'])
            cash_machine.money_slips[money_bill] = row['value']


class MoneySlipsDB:

    @staticmethod
    def all(cash_machine_id: int) -> Iterator:
        cursor = DB.cursor()
        query = "SELECT * FROM money_slips WHERE cash_machine_id = %s"
        cursor.execute(query, [cash_machine_id])
        return cursor.fetchall()

    @staticmethod
    def update(cash_machine: CashMachine) -> None:
        cursor = DB.cursor()
        query = """
            UPDATE money_slips SET VALUES = %s
            WHERE cash_machine_id = %s
            AND money_bill = %s
        """
        money_slips = cash_machine.money_slips
        params = [[amount, cash_machine.id, money_bill]for money_bill, amount in money_slips.items()]
        #[ [40, 1, 20], [40, 1, 20], ]
        cursor.executemany(query, params)
