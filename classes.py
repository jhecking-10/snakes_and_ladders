from typing import override


class Player:
    def __init__(self, name: str):
        self.name: str = name

    # decorator and method to return name as a string
    @override
    def __str__(self) -> str:
        return self.name

player_name = input("Enter your name below:\n")
player_1 = Player(player_name)
