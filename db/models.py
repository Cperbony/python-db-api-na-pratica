from typing import Dict


class BankAccount(GetFieldsAnnotation):
    id: int
    number: str
    password: str
    value: float
    agency: 'Agency'
    user: 'User'

    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            self.__setattr__(k, v)

    # def check_account_number(self, number):
    #     return number == self.number
    #
    # def check_password(self, password):
    #     return password == self.password

    def balance_debit(self, value):
        self.value -= value


class Agency(GetFieldsAnnotation):
    id: int
    number: str
    address: str

    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            self.__setattr__(k, v)


class User(GetFieldsAnnotation):
    id: int
    name: str
    email: str
    address: str
    admin: bool

    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            self.__setattr__(k, v)


def check_account_number(self, number):
    return number == self.number


def check_password(self, password):
    return password == self.password


def balance_debit(self, value):
    self.value -= value


bank_account = BankAccount(number='0000', password='1234', value=100)


class CashMachine(GetFieldsAnnotation):
    id: int
    alias: str
    money_slips: Dict

    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            self.__setattr__(k, v)
        self.money_slips_user = {}
        self.value_remaining = 0

    def withdraw(self, value):
        self.value_remaining = value

        self.__calculate_money_slips_user('100')
        self.__calculate_money_slips_user('50')
        self.__calculate_money_slips_user('20')

        if self.value_remaining == 0:
            self.__decrease_money_slips()

        return False if self.value_remaining != 0 else self.money_slips

    def __calculate_money_slips_user(self, money_bill):
        money_bill_int = int(money_bill)
        if 0 < self.value_remaining // money_bill_int <= self.money_slips[money_bill]:
            self.money_slips_user[money_bill] = self.value_remaining // money_bill_int
            self.value_remaining = self.value_remaining - self.value_remaining // money_bill_int * money_bill_int

    def __decrease_money_slips(self):
        for money_bill in self.money_slips_user:
            self.money_slips[money_bill] -= self.money_slips_user[money_bill]