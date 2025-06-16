from brain_games.engine import if_prime

# вопрос/неправильный ответ
question = 'Answer "yes" if given number is prime. Otherwise answer "no".'


# '1' is wrong answer ;(. Correct answer was '25'.
# Let's try again, Sam!

# условие игры
def get_answer_prime(num):
    return if_prime(num)

