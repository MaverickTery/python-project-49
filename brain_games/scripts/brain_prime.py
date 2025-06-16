from brain_games.engine import (
    end_game,
    get_good_day_name,
    get_random_num,
    start_game,
)
from brain_games.games.prime import (
    get_answer_prime,
    question,
)


def main():
    user_name = get_good_day_name()
    start_game(question)
    for x in range(0, 3):
        start_num = get_random_num(1, 100)
        right_answer = get_answer_prime(start_num)
        print(f"Question: {start_num}")
        user_answer = input("Your answer: ")
        if right_answer == user_answer:
            print('Correct!')
        else:
            print(f"'{user_answer}' is wrong answer ;(."
                  f"Correct answer was '{right_answer}'.\n"
                  f"Let's try again, {user_name}!"
                  )
            break
    if x == 2 and right_answer == user_answer:
        end_game(user_name)
   

if __name__ == "__main__":
    main()