from brain_games.engine import get_divider

# вопрос/неправильный ответ
question = 'Find the greatest common divisor of given numbers.'
# '1' is wrong answer ;(. Correct answer was '25'.
#Let's try again, Sam!

# условие игры
def get_gcd(num1, num2):
    return get_divider(num1, num2)

  