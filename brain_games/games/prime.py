import random

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(n):
    if n <= 1 or (n % 2 == 0 and n != 2):
        return False
    if n == 2:
        return True

    for d in range(3, int(n**0.5) + 1, 2):
        if n % d == 0:
            return False
    return True


def generate_round():
    d = random.randint(2, 3571)
    question = f'{d}'
    correct_answer = 'yes' if is_prime(d) else 'no'
    return question, correct_answer


game = {
    'description': DESCRIPTION,
    'generate_round': generate_round,
}
