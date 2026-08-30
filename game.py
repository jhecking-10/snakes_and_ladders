import random


def create_game_board():
    return list(range(1, 101))

board = create_game_board()
starting_position = board[0]

def roll_die():
    _ = input("Press enter to roll the die")
    return random.randint(1, 6)

def player_turn(current_space: int):
    roll = roll_die()
    print(f"You rolled a {roll} and are now on space {current_space + roll}")

def determine_current_space():
    pass
