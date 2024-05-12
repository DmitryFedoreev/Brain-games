import prompt


#greetings = 'brain-games\nWelcome to the Brain Games!'
#print(greetings)


def welcome_user():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')
