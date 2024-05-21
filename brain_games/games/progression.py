import random

DESCRIPTION = 'What number is missing in the progression?'


def generate_round():
    length = random.randint(5, 10)
    start = random.randint(1, 10)
    step = random.randint(1, 5)

    progression = [start + step * i for i in range(length)]

    hidden_index = random.randint(0, length - 1)
    correct_answer = progression[hidden_index]

    hidden_progression = progression[:]
    hidden_progression[hidden_index] = ".."

    return hidden_progression, str(correct_answer)


game = {
    'description': DESCRIPTION,
    'generate_round': generate_round,
}
