import random


def create_game_board():
    return list(range(1, 101))

board = create_game_board()
starting_space = board[0]
starting_turn = 1

def roll_die():
    _ = input("Press enter to roll the die")
    return random.randint(1, 6)

def player_turn(space: int, turn: int):
    roll = roll_die()
    turn += 1
    space += roll
    return space, turn, roll

def game():
    current_space, current_turn, last_roll = player_turn(starting_space, starting_turn)
    print(f"You rolled a {last_roll} and are now on space {current_space}. Your next turn will be #{current_turn}")
    while current_space < 100:
        current_space, current_turn, last_roll = player_turn(current_space, current_turn)
        print(f"You rolled a {last_roll} and are now on space {current_space}. Your next turn will be #{current_turn}")

game()
