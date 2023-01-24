"""This module contains the classes for handling player game data."""

class PlayerManager:
    """Manages two players."""

    def __int__(self)->None:
        self.players = {}

    def set_player_info(self, name:str)->None:
        self.players[name] = Player(name)

    def update_player_info(self, player:str, key:str, value)->None:
        self.players[player].update_info(key, value)

    def get_player_info(self, player:str, key:str):
        return self.players[player].get_info(key)

class Player:
    """Contains data for one player."""

    def __int__(self, name:str):
        self.data = {'name': name}

    def update_info(self, key:str, value):
        self.data[key] = value

    def get_info(self, key:str):
        return self.data[key]