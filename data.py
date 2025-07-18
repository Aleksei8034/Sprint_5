from random import randint

class Person:
    user_name = 'Алексей'
    email = f'AlexeiDyaur27fs1991@yandex.ru'
    password = f'12345Pas'

class RandomData:
    user_name = 'User'
    email = f'user{randint(0, 999)}@yandex.ru'
    password = f'{randint(1000, 9999)}Pas'