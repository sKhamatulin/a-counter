from functions import counter

lengs = ['en', 'rus']
while True:
    leng = input('Выберите язык, на котором будете вводит строку:'
                 '\n -> en \n -> rus \n '
                 'или выход для выхода: ')
    if leng in lengs:
        string = input('Введите строку для подсчитывать количество букв '
                       '«A» в строке, или введите выход, для выхода: ')
        if string == 'выход':
            break
        result = counter(string, leng)
        if result == '':
            string = input('Вы ничего не ввели, попробуйте ещё раз: ')
        print(f'\n -> Количество А в строке {string} = ', result, end='\n\n')
    elif leng == 'выход':
        break
    else:
        print('Такой язык я еще не знаю')
