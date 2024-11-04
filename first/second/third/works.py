# from first.utils import multi
# Это не точка входа можно указать относительный путь

# Для отладки можно вручную прописать модуль
# __package__ = 'first.second.third'

from .utils import multi

def calc(a, b):
    multi('=', a)
    print(f'a + b = {a+b} ')

if __name__ == '__main__':
    calc(3, 9)