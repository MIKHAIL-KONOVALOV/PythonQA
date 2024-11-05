if __name__ == "__main__":
    corectNumber = False
    while corectNumber == False:
        try:
            x = int(input('Enter number: '))
            corectNumber = True

        except ValueError:
            print("Enter a number, please...")
        except ZeroDivisionError:
            print('Division by Zero')
        else:
            print('Если ошибок нет')
        finally:
            print('Блок финали срабатывает всегда')
    x += 15
    print(x)
