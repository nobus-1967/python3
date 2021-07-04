# Game 'Rock, Paper, Scissors'
import random

items = {1: 'ROCK', 2: 'PAPER', 3: 'SCISSORS'}
beats = {1: 3, 2: 1, 3: 2}


def main() -> None:
    '''Show rules and run a new game.'''
    show_rules()
    
    print('\nStaring a new game...')
    play_game()    
    
    print('\n.................')
    print('The game is over.\nThanks for playing with me!\n(c) Nobus, 2021')


def show_rules() -> None:
    '''Show game rules.'''
    print('The game is known as "ROCK-PAPER-SCISSORS".')
    print('...........................................')
    print('\nEach player chooses one of three items:')
    print('"rock" , "paper" or "scissors".')
    print('--"Rock crushes scissors" (a player who decides to play rock')
    print('will beat another player who has chosen scissors);')
    print('--"paper covers rock" (a player who decides to play paper')
    print('will beat another player who has chosen rock);')
    print('--"scissors cuts paper" (a player who decides to play scissors')
    print('will beat another player who has chosen paper);')
    print('If both players choose the same shape, the game is tied')
    print('and is replayed to break the tie.')


def play_game() -> None:
    '''Run the gameplay function.''' 
    print('\nI\'ve chosen the item; it\'s your turn now.')
    computer_choice = random.randint(1, 3)
    
    user_choice = input_choice()
    
    while user_choice == 0:
        user_choice = input_choice()
    
    print(f'\nMy choice is {items[computer_choice]}',
          f'and your choice is {items[user_choice]}.')
    
    if computer_choice == user_choice:
        print('Tie (draw); replaing the game...')
        play_game()
    else:
        if beats[computer_choice] == user_choice:
            print(f'{items[computer_choice]} beats {items[user_choice]}:',
                  'I win the game!')
        else:
            print(f'{items[user_choice]} beats {items[computer_choice]}:',
                  'you win the game!')


def input_choice() -> int:
    '''Input the user's choice (number) of item.'''
    try:
        user_input = input('Your choice (ROCK=1, PAPER=2, SCISSORS=3): ')

        if user_input not in '123':
            raise ValueError
        
        user_choice = int(user_input)
    except (TypeError, ValueError):
        print('Wrong input, try again!')
        user_choice = 0
    finally:
        return user_choice


if __name__ == '__main__':
    main()
    