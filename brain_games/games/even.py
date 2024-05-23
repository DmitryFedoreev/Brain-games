import random

DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'
MIN_NUM = 1
MAX_NUM = 100


def is_even(num) -> bool:
    return num % 2 == 0


def generate_round():
    number = random.randint(MIN_NUM, MAX_NUM)
    correct_answer = 'yes' if is_even(number) else 'no'
    question = str(number)
    return question, correct_answer


game = {
    'description': DESCRIPTION,
    'generate_round': generate_round,
}
