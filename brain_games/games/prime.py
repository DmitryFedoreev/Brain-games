import random

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
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
