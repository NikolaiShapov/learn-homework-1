"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию hello_user() из задания while1, чтобы она
  перехватывала KeyboardInterrupt, писала пользователю "Пока!"
  и завершала работу при помощи оператора break

"""

def hello_user():
    try:
        while True:
            reply = input('Как дела?')
            if reply == 'Хорошо':
                break
    except KeyboardInterrupt:
        print('\nПока!')
        # завершала работу при помощи оператора break - не очень понял это условие и без break все заканчивается же ?


if __name__ == "__main__":
    hello_user()
