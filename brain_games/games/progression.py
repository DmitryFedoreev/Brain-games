import random


DESCRIPTION = 'What number is missing in the progression?'
MIN_LENGTH = 5
MAX_LENGTH = 10
MIN_START = 1
MAX_START = 10
MIN_STEP = 1
MAX_STEP = 5


def generate_round():
    length = random.randint(MIN_LENGTH, MAX_LENGTH)
    start = random.randint(MIN_START, MAX_START)
    step = random.randint(MIN_STEP, MAX_STEP)

    progression = [start + step * i for i in range(length)]

    hidden_index = random.randint(0, length - 1)
    correct_answer = progression[hidden_index]

    progression[hidden_index] = '..'
    question = ' '.join(map(str, progression))

    return question, str(correct_answer)


game = {
    'description': DESCRIPTION,
    'generate_round': generate_round,
}
