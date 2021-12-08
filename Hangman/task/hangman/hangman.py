import random
words = 'python', 'java', 'kotlin', 'javascript'
result = random.choice(words)
output = ['-' for x in range(len(result))]
letter_input = set()
letters = set('abcdefghijklmnopqrstuvwxyz')
choose = ''
# clue = result[0:3] + '-' * (len(result) - 3)


def game():
    live = 8
    while live > 0:
        input_invalid = True
        while input_invalid:
            print()
            print(*output, sep='')
            answer = input('Input a letter: ')
            if len(answer) == 1:
                if answer in letters:
                    if answer not in letter_input:
                        input_invalid = False
                        letter_input.add(answer)
                    else:
                        print("You've already guessed this letter")
                else:
                    print('Please enter a lowercase English letter')
            else:
                print('You should input a single letter')

        if answer in result:
            for c in range(result.rfind(answer) + 1):
                if answer == result[c]:
                    output[c] = answer
        else:
            print("That letter doesn't appear in the word")
            live -= 1
        if result == ''.join(output):
            print()
            print(result)
            print(f'''You guessed the word {result}!
You survived!''')
            break
    if live == 0 and result != ''.join(output):
        print('You lost!')


print('H A N G M A N')
game_continue = True
while game_continue:
    choose = input('Type "play" to play the game, "exit" to quit: ')
    if choose == 'play':
        game()
        print()
    elif choose == 'exit':
        break
    else:
        continue




