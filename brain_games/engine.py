import random

from brain_games.greeting import greeting, welcome_user


def get_random_num():                   # рандомайзер
    random_num = random.randint(0, 100)
    return random_num


def if_even(num):                       # проверка на четность
    if num % 2 == 0:
        return num
    

def get_sum(num1, num2):                #сумма двух чисел
    return num1 + num2


def get_divider(num1, num2):            #наибольший общий делитель
    if num1 == 0 or num2 == 0:
        return num1 + num2
    if num1 > num2 and num1 % num2 == 0:
        return num2
    elif num2 > num1 and num2 % num1 == 0:
        return num1
    while num1 != 0 and num2 != 0:
        if num1 > num2:
            num1 = num1 % num2
        else:
            num2 = num2 % num1
    return num1 + num2 

    
# текстовый блок: приветствие, имя пользователя, 
# фразы начала и завершения игры   
def get_good_day_name():                
    user_name = greeting()
    welcome_user(user_name)
    return user_name


def start_game(question):
    print(question)


def end_game(user_name):
    farewall = f"Congratilations, {user_name}!"
    print(farewall)


