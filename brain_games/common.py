import prompt


def hello():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def play_game(game):
    name = hello()
    print(game['description'])
    count = 0

    while count < 3:
        question, correct_answer = game['generate_round']()
        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')

        if user_answer == str(correct_answer):
            print('Correct!')
            count += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            break

        if count == 3:
            print(f'Congratulations, {name}!')

#ref
