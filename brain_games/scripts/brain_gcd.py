from brain_games.engine import (
    end_game,
    get_good_day_name,
    get_random_num,
    start_game,
)
from brain_games.games.gcd import get_gcd, question


def main():
    user_name = get_good_day_name()
    start_game(question)
    for x in range(0, 3):
        num1 = get_random_num(1, 100)
        num2 = get_random_num(1, 100)
        print(f"Question: {num1} {num2}")
        right_answer = get_gcd(num1, num2)
        user_answer = input("Your answer: ")
        if right_answer == int(user_answer):
            print('Correct!')
        else:
            print(f"'{user_answer}' is wrong answer ;(."
                  f"Correct answer was '{right_answer}'.\n"
                  f"Let's try again, {user_name}!"
                  )
            break
    if x == 2 and right_answer == int(user_answer):
        end_game(user_name)
   

if __name__ == "__main__":
    main()
