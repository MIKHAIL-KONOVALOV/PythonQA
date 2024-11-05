import time
if __name__== '__main__':
    numberShutles = int(input('Введите количество шатлов:'))
    delay = 0
    for i in range(1,int(numberShutles +1)):
        for seconds in range(i,0,-1):
            print(f'Осталось {seconds - 1} секунд')
            time.sleep(1)
        print('Пуск - ', i)
        time.sleep(3) if i != (numberShutles) else time.sleep(0)