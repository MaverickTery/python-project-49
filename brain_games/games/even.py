from brain_games.engine import if_even

# вопрос/неправильный ответ
question = 'Answer "yes" if the number is even, otherwise answer "no".'
incorrect_answer = "'yes' is wrong answer ;(. Correct answer was 'no'. " \
"Let's try again,"


# условие игры
def get_even(num):
    if if_even(num):
        return 'yes'
    else:
        return 'no'
  
   



