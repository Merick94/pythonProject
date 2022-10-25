import time


def my_first_decorator(func):
    def wrap():
        start_time = time.time()
        func() # Вызов переданной функции
        print(time.time() - start_time)

    return wrap #Возврат обернутой функции
@my_first_decorator
def hello():
    print('Привет')
@my_first_decorator
def ask():
    return input('как дела?')

hello()

ask()
