import random

DESCRIPTION = 'What is the result of the expression?'
MIN_NUM = 1
MAX_NUM = 100
OPERATOR = ('+', '-', '*')


def generate_round():
    operator = random.choice(OPERATOR)
    random_num1 = random.randint(MIN_NUM, MAX_NUM)
    random_num2 = random.randint(MIN_NUM, MAX_NUM)

    if operator == '+':
        correct_result = random_num1 + random_num2

    elif operator == '-':
        correct_result = random_num1 - random_num2

    elif operator == '*':
        correct_result = random_num1 * random_num2

    question = f'{random_num1} {operator} {random_num2}'
    return question, correct_result


game = {
    'description': DESCRIPTION,
    'generate_round': generate_round,
}
