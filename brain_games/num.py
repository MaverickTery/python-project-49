import random


def num_even(num):
    if num % 2 == 0:
        return 'yes'
    else:
        return 'no'


def num_even_dialog():
    from brain_games.greeting import name
    count = 0
    print('Answer "yes" if the number is even, otherwise answer "no".')
    while count < 3:
        random_num = random.randint(0, 9999)
        print(f"Question: {random_num}")
        user_answer = input('Your answer: ')
        right_answer = num_even(random_num)
        if right_answer != user_answer:
            print(f"'yes' is wrong answer ;(. Correct answer was 'no'. Let's try again, {name}!")
        else:
            print("Correct!")
        count += 1
    print(f"Congratilations, {name}!")




    

