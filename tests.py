from functions import counter


def test_counter_en(string, result):
    """Тест англоязычной строки."""
    num = counter(string, leng)
    assert num == result, ('Проверьте что при передаче англоязычной строки, '
                           'правильно подсчитываются сиволы A \n'
                           f'{num} != {result}')
    print('*** Тест англоязычной строки пройден ***')


def test_counter_rus(string, result):
    """Тест рускоязычной строки."""
    num = counter(string, leng)
    assert num == result, ('Проверьте что при передаче рускоязычной строки, '
                           'правильно подсчитываются сиволы A \n'
                           f'{num} != {result}')
    print('*** Тест рускоязычной строки пройдет ***')


def test_counter_empty_string(string):
    """Тест пустой строки."""
    num = counter(string, leng)
    assert num == '', ('Проверьте что при передаче пустой строки, '
                       'возвращается пустая строка \n'
                       f'{num} != \'\' ')
    print('*** Тест пустой строки пройдет ***')


def test_counter_not_string(string):
    """Тест НЕ строки."""
    num = counter(string, leng)
    assert num == 0, ('Проверьте что при передаче не строкового значения, '
                      'возвращается 0 \n'
                      f'{num} == 0')
    print('*** Тест НЕ строки пройдет ***')


if __name__ == '__main__':

    leng = 'en'
    string = 'AAAaaabbbutltl'
    result = 6
    test_counter_en(string, result)

    leng = 'rus'
    string = 'ААааннрет'
    result = 4
    test_counter_rus(string, result)

    leng = 'en'
    string = ''
    test_counter_empty_string(string)

    leng = 'en'
    string = 12
    test_counter_not_string(string)
