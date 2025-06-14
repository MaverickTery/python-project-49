from brain_games.engine import (
    end_game,
    get_good_day_name,
    get_random_num,
    start_game,
)
from brain_games.games.progression import (
    ask_sequence,
    first_coll,
    get_right_answer,
    question,
)


def main():
    user_name = get_good_day_name()
    start_game(question)
    for x in range(0, 3):
        start_num = get_random_num(1, 100)
        step = get_random_num(1, 10)
        place = get_random_num(0, 9)
        first_sequence = first_coll(start_num, step)
        right_answer = int(get_right_answer(first_sequence, place))
        ask_string = ask_sequence(first_sequence, place)
        print(f"Question: {ask_string}")
        user_answer = input("Your answer: ")
        if right_answer == int(user_answer):
            print('Correct!')
        else:
            print(f"'{user_answer}' is wrong answer ;(."
                  f"Correct answer was '{right_answer}'.\n"
                  f"Let's try again, {user_name}!"
                  )
            break
    if x == 2:
        end_game(user_name)
   

if __name__ == "__main__":
    main()
