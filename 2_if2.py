"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками.
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры
  и выводя на экран результаты

"""

def main(text_one, text_two):
    if type(text_one) != str or type(text_two) != str:
        return 0
    elif text_two == text_one:
        return 1
    elif text_one != text_two and len(text_one) > len(text_two):
        if text_one != text_two and text_two == 'learn':
            return 3
        else:
            return 2
    elif text_one != text_two and text_two == 'learn':
        return 3
    else:
        return 'По условиям задачи такого варианта не предусмотренно...'

if __name__ == "__main__":
    print(main(123,'Hi!')) # переменная не строка
    print(main('Python','Python')) # строки одинаковые
    print(main('I like Pyhon', 'Hello world!')) # len(строк) одинаковая,и вторая строка НЕ 'learn' ТАКОГО В УСЛОВИИ НЕТ!
    print(main('I like Pyhon', 'learnPython')) # строки разные и вторая строка 'learn'
    print(main('I like Pyhon', 'learn')) # строки разные и вторая строка 'learn'
    print(main("I'm", 'learn')) # строки разные и вторая строка 'learn' len(text1) < len(text2)
