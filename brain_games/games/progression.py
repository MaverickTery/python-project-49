from brain_games.engine import get_sequence

# вопрос/неправильный ответ
question = 'What number is missing in the progression?'


# '1' is wrong answer ;(. Correct answer was '25'.
# Let's try again, Sam!

# условие игры
def first_coll(start_num, step):
    return get_sequence(start_num, step)


def ask_sequence(coll, place):
    coll[place] = '..'
    ask_string = ' '.join(coll)
    return ask_string


def get_right_answer(coll, place):
    right_answer = coll[place]
    return right_answer