import prompt


def hello():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def play_round(generate_round):
    question, correct_answer = generate_round()
    print(f'Question: {question}')
    user_answer = prompt.string('Your answer: ')
    return user_answer, correct_answer


def print_round_result(user_answer, correct_answer, name):
    if user_answer == str(correct_answer):
        print('Correct!')
        return True
    else:
        print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
        print(f"Let's try again, {name}!")
        return False


def play_game(game):
    name = hello()
    print(game['description'])
    count = 0

    while count < 3:
        user_answer, correct_answer = play_round(game['generate_round'])
        if print_round_result(user_answer, correct_answer, name):
            count += 1
        else:
            break

    if count == 3:
        print(f'Congratulations, {name}!')
