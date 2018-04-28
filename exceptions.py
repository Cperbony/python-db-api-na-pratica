try:
    a = 1/0
except ZeroDivisionError:
    print('Divisão por zero')


class AppException(Exception):
    pass