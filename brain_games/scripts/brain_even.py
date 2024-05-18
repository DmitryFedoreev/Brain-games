import random
import prompt


def main():
    count = 0
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')
    print('Answer "yes" if the number is even, otherwise answer "no".')

    while count < 3:
        random_num = random.randint(1, 100)
        print(f'Question: {random_num}')
        answer = prompt.string('Your answer: ')

        if random_num % 2 == 0 and answer == 'yes':
            print('Correct!')
            count += 1

        elif random_num % 2 != 0 and answer == 'no':
            print('Correct!')
            count += 1

        else:
            print("'yes' is wrong answer ;(. Correct answer was 'no'.")
            print(f"Let's try again, {name}")
            break

    if count == 3:
        print(f'Congratulations, {name}')
