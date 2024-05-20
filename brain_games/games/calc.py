import random

DESCRIPTION = 'What is the result of the expression?'


def generate_round():
    arithmetic = random.choice(['+', '-', '*'])
    random_num1 = random.randint(1, 100)
    random_num2 = random.randint(1, 100)

    if arithmetic == '+':
        correct_result = random_num1 + random_num2

    elif arithmetic == '-':
        correct_result = random_num1 - random_num2

    elif arithmetic == '*':
        correct_result = random_num1 * random_num2

    question = f'{random_num1} {arithmetic} {random_num2}'
    return question, correct_result


game = {
    'description': DESCRIPTION,
    'generate_round': generate_round,
}
