# lambda аналог def/ После : все равно что returne
# lambda НЕ ВЫПОЛНЯЕТСЯ до вызова

import functions


def square(x):
    return x * x


square2 = lambda x: x ** 2

even_odd = lambda x: 'Even' if x % 2 == 0 else 'Odd'

# Все нормально пока не произойдет вызов!
notWorkingLambda = lambda: noExistingFunction(noExistingFunction2())

if __name__ == '__main__':
    # print(square(4))
    # print(square2(5))
    # print(even_odd(17))
    #
    # x = 2
    # result_1 = lambda: x ** 2
    # x = 3
    # result_2 = lambda: x ** 2
    #
    # print(result_1())
    # print(result_2())
    # print(functions.defaultArgFunc())
    numbers = list(range(100))
    print(list(map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, numbers))))
    my_dict = {'a': 24, 'c': 46, 'b': 31, 'd': 11}
    print(sorted(my_dict.items(), key=lambda x: x[1]))

    print([x ** 100 **2 for x in numbers if x % 2 == 0])
