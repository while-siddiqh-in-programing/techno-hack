import random

CHOICES = 'rpsq'

def get_player_choice():
    player_choice = input('''\nChoices: 
"R" for Rock
"P" for Paper 
"S" for Scissors
"Q" for Quit\n\nPick: ''').lower()
    return player_choice if player_choice in CHOICES else None

def get_computer_choice():
    return random.choice(CHOICES[:3])

def is_draw(player_choice, computer_choice):
    return player_choice == computer_choice

def print_winner(player_choice, computer_choice, player_point, computer_point):
    if player_choice == None:
        print("Enter a valid choice")
    elif player_choice == 'q':
        print("It was great playing with you!")
    elif (player_choice == 'r' and computer_choice == 's') or \
         (player_choice == 's' and computer_choice == 'p') or \
         (player_choice == 'p' and computer_choice == 'r'):
        print('Player wins!')
        return player_point + 1, computer_point
    else:
        print('Computer wins!')
        return player_point, computer_point + 1

def play_game():
    player_point, computer_point = 0, 0
    total_games = 0
    player_choice = None
    
    while player_choice != 'q':
        player_choice = get_player_choice()
        if player_choice == 'q':
            break
        
        computer_choice = get_computer_choice()
        if is_draw(player_choice, computer_choice):
            print(f"It's a draw! Both players picked {player_choice.upper()}")
        else:
            print(f"Computer picked: {computer_choice.upper()}")
            print(f"Player picked: {player_choice.upper()}")
            player_point, computer_point = print_winner(player_choice, computer_choice, player_point, computer_point)
        
        total_games += 1
    
    print(f"\nPlayer points: {player_point}\nComputer points: {computer_point}\nTotal games played: {total_games}")

if __name__ == "__main__":
    play_game()
