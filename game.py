import random


def create_game_board():
    return tuple(range(1, 101))

board = create_game_board()

def roll_die():
    _ = input("Press enter to roll the die")
    return random.randint(1, 6)

def player_turn(space: int, turn: int):
    roll = roll_die()
    turn += 1
    space += roll
    return space, turn, roll

def game():
    current_space, current_turn, last_roll = player_turn(board[0], 1)
    print(f"You rolled a {last_roll} and are now on space {current_space}. Your next turn will be #{current_turn}")
    while current_space < 100:
        if current_space >= 94:
            print("Roll precisely... Don't go past 100")
        current_space, current_turn, last_roll = player_turn(current_space, current_turn)
        if current_space > 100:
            print("Invalid roll. Try again...")
            current_space -= last_roll
        if current_space == 100:
            print(f"You rolled a {last_roll}, landed on space {current_space} and won!\nTerminating game...")
            break
        print(f"You rolled a {last_roll} and are now on space {current_space}. Your next turn will be #{current_turn}")

game()
