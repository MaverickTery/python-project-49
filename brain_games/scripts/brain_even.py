from brain_games.engine import (
    end_game,
    get_good_day_name,
    get_random_num,
    start_game,
)
from brain_games.games.even import get_even, incorrect_answer, question


def main():
    user_name = get_good_day_name()
    start_game(question)
    for x in range(0, 3):
        ask_num = get_random_num()
        print(f"Question: {ask_num}")
        right_answer = get_even(ask_num)
        user_answer = input("Your answer: ")
        if right_answer == user_answer:
            print('Correct!')
        else:
            print(incorrect_answer, user_name)
        
    end_game(user_name)
   

if __name__ == "__main__":
    main()
 