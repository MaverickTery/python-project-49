import random

from brain_games.greeting import greeting, welcome_user


def get_random_num():                   # рандомайзер
    random_num = random.randint(0, 100)
    return random_num


def if_even(num):                       # проверка на четность
    if num % 2 == 0:
        return num

    
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


