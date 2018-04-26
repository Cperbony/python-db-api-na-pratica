class BankAccount:
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


class Agency:
    id: int
    number: str
    address: str

    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            self.__setattr__(k, v)


class User:
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
print(vars(bank_account))
