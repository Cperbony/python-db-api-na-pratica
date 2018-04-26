# design pattern - repository
from models import BankAccount, Agency
from db import DB


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
        print(row)


bank_account = BankAccount(
    number='0001-01',
    password='123456',
    agency=Agency(number='1111')
)

BankAccountDB.find_by_number_and_password_and_agency_number(bank_account)
