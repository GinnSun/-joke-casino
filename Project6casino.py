import sqlite3
import random
from time import sleep
# Создание базы данных
database_casino = sqlite3.connect('server_db_casino.db')
cursor = database_casino.cursor()

moretable = """
CREATE TABLE IF NOT EXISTS users(
    login TEXT,
    password TEXT,
    age INT(3),
    cash BIGINT NOT NULL DEFAULT 2000
);
CREATE TABLE IF NOT EXISTS casino(
    casino_name TEXT,
    balance BIGINT NOT NULL DEFAULT 10000000000
)"""
cursor.executescript(moretable)
database_casino.commit()
# создание логина и пароля
def user_login():
    global age
    global user
    user = input('Login😐: ')
    password = input('Password😐: ')
    age = int(input('Age😐: '))
    cursor.execute("SELECT login FROM users WHERE login = (?)", [user])
    if cursor.fetchone() is None:
        cursor.execute("INSERT INTO users(login, password, age) VALUES(?, ?, ?)", [user, password, age])
        database_casino.commit()
        check_login()
    else:
        print('Вы уже зарегистрированы!|You are already registered!')
        check_login()
# проверка логина и пароля на совместимость
def check_login():
    user_log = input('Repeat your login🤔: ')
    password_log = input('Repeat your password🤔: ')
    cursor.execute("SELECT password FROM users WHERE login = (?) AND password = (?)", [user_log, password_log])
    if cursor.fetchone() is None:
        print('Такого логина не существует!👺|👿This login does not exist!')
        user_login()
    else:
        print(f"Welcome {user_log}!")
        for i in cursor.execute("SELECT cash FROM users WHERE login = (?)", [user]):
            balance = i[0]
        print(f'YOUR CASH = {balance}')
        casino()
# создание казино)
def casino():
    print()
    for i in cursor.execute("SELECT casino_name FROM casino"):
        casino_nm = i[0]
    print(f'CASINO|{casino_nm}|🤩＼（〇_ｏ）／')
    cursor.execute("SELECT age FROM users WHERE login = (?) AND age >= (?)", [user,18])
    if cursor.fetchone() is None:
        print('Вам недостаточно лет!👺|🤬You are not old enough!')
        cursor.close()
        database_casino.close()
    else:
        number = random.randint(0,100)
        bet = int(input("Bet💯: "))
        color = int(input('1 or 2 or 0: '))
        num = int(input('Choose a number from 0 to 36♻: '))

        for i in cursor.execute("SELECT cash FROM users WHERE login = (?)", [user]):
            balance = i[0]

        for i in cursor.execute("SELECT balance FROM casino WHERE casino_name = (?)", [name_casino]):
            balance_casino = i[0]

        if balance <= bet:
            print('Недостаточно средств, гуляй работать! 👻')
            exit()
        elif balance <= 0:
            print('Недостаточно средств, гуляй работать! 👻')
            exit()

        cursor.execute("SELECT login FROM users WHERE login = (?)", [user])
        if cursor.fetchone() is None:
            print('Такого логина не существует!👺|😖This login does not exist!')
        else:
            if number <= 36 and number % 2 == 0 and num % 2 == 0 and num <= 36:
                cursor.execute(f"UPDATE users SET cash = {bet*1+balance} WHERE login = (?)", [user])
                cursor.execute(f'UPDATE casino SET balance = {balance_casino - (bet*1.5)}')
                database_casino.commit()
                for i in cursor.execute("SELECT login, cash FROM users WHERE login = (?)", [user]):
                    print('YOU WON😲😨!!!!')
                    sleep(4)
                    print('You got RED🤩!')
                    sleep(2)
                    print(i)
                    print('Хотите ли вы еще сыграть?')
                    n = input()
                    if n == 'YES':
                        casino()
                    else:
                        print('Sorry😔☹')
                        exit()
            elif number <= 36 and number % 2 != 0 and num % 2 != 0 and num <= 36:
                cursor.execute(f"UPDATE users SET cash = {bet*2+balance} WHERE login = (?)", [user])
                cursor.execute(f'UPDATE casino SET balance = {balance_casino - (bet *2)}')
                database_casino.commit()
                for i in cursor.execute("SELECT login, cash FROM users WHERE login = (?)", [user]):
                    print('YOU WON🧐🤓!!!!')
                    sleep(4)
                    print('You got BLACK🤩!')
                    sleep(2)
                    print(i)
                    print('Хотите ли вы еще сыграть?')
                    n = input()
                    if n == 'YES':
                        casino()
                    else:
                        exit()
            elif number == 0 and num == 0:
                cursor.execute(f"UPDATE users SET cash = {bet*10+balance} WHERE login = (?)", [user])
                cursor.execute(f'UPDATE casino SET balance = {balance_casino - (bet * 10)}')
                database_casino.commit()
                for i in cursor.execute("SELECT login, cash FROM users WHERE login = (?)", [user]):
                    print('YOU WON😲🤯!!!!')
                    sleep(4)
                    print('You got GREEN🤩!')
                    sleep(2)
                    print(i)
                    print('Хотите ли вы еще сыграть?')
                    n = input()
                    if n == 'YES':
                        casino()
                    else:
                        exit()
            else:
                if number > 36 and number % 2 == 0 and num % 2 == 0:
                    cursor.execute(f"UPDATE users SET cash = {balance - bet} WHERE login = (?)", [user])
                    cursor.execute(f'UPDATE casino SET balance = {balance_casino + (bet * 1.5)}')
                    database_casino.commit()
                    print('YOU LOSE!')
                    for i in cursor.execute("SELECT login, cash FROM users WHERE login = (?)", [user]):
                        print(i)
                    print('Хотите ли вы еще сыграть?')
                    n = input('if yes write YES')
                    if n == 'YES':
                        casino()
                    else:
                        exit()
                    casino()
                elif number > 36 and number % 2 != 0 and num % 2 != 0:
                    cursor.execute(f"UPDATE users SET cash = {balance - bet} WHERE login = (?)", [user])
                    cursor.execute(f"UPDATE casino SET balance = {balance_casino+(bet*2)}")
                    database_casino.commit()
                    print('YOU LOSE!')
                    for i in cursor.execute("SELECT login, cash FROM users WHERE login = (?)", [user]):
                        print(i)
                    print('Хотите ли вы еще сыграть?')
                    n = input('if yes write YES')
                    if n == 'YES':
                        casino()
                    else:
                        exit()
                elif number > 36 and num == 0:
                    cursor.execute(f"UPDATE users SET cash = {balance - bet} WHERE login = (?)", [user])
                    cursor.execute(f'UPDATE casino SET balance = {balance_casino + (bet * 10)}')
                    database_casino.commit()
                    print('YOU LOSE!')
                    for i in cursor.execute("SELECT login, cash FROM users WHERE login = (?)", [user]):
                        print(i)
                    print('Хотите ли вы еще сыграть?')
                    n = input('if yes write YES')
                    if n == 'YES':
                        casino()
                    else:
                        exit()
                    casino()
name_casino = 'DRAGON'
cursor.execute('INSERT INTO casino(casino_name) VALUES (?)', [name_casino])
database_casino.commit()
user_login()
