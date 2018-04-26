# design pattern - repository
from models import BankAccount, Agency, User
from db import DB
from typing import Dict


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
            print('Conta bancária inválida')
            return False

        row = cursor.fetchone()
        row_cloned = row.copy()

        bank_account = BankAccount()
        for k, v in BankAccount.__dict__['__annotations__'].items():
            if k in row_cloned:
                setattr(bank_account, k, row_cloned[k])
                row_cloned.pop(k)

        bank_account.agency = Agency()
        for k, v in Agency.__dict__['__annotations__'].items():
            key_relation = "agencies.%s" % k
            if k in row_cloned or key_relation in row_cloned:
                key_in = k if k in row_cloned else key_relation
                setattr(bank_account.agency, k, row_cloned[key_in])
                row_cloned.pop(key_in)

        bank_account.user = User()
        for k, v in User.__dict__['__annotations__'].items():
            key_relation = "users.%s" % k
            if k in row_cloned or key_relation in row_cloned:
                key_in = k if k in row_cloned else key_relation
                setattr(bank_account.user, k, row_cloned[key_in])
                row_cloned.pop(key_in)

        print('bank_account', vars(bank_account))
        print('agency', vars(bank_account.agency))
        print('user', vars(bank_account.user))
        # print(row)
        # bank_account = BankAccount(name=row['name'])


bank_account = BankAccount(
    number='0001-01',
    password='123456',
    agency=Agency(number='1111')
)

BankAccountDB.find_by_number_and_password_and_agency_number(bank_account)
