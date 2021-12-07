import random
words = 'python', 'java', 'kotlin', 'javascript'
result = random.choice(words)
clue = result[0:3] + '-' * (len(result) - 3)
print('H A N G M A N')
answer = input(f'Guess the word {clue}: ')
if answer == result:
    print('You survived!')
else:
    print('You lost!')
