import random

DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def generate_round():
    number = random.randint(1, 100)
    correct_answer = 'yes' if number % 2 == 0 else 'no'
    question = str(number)
    return question, correct_answer


game = {
    'description': DESCRIPTION,
    'generate_round': generate_round,
}
