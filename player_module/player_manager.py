"""This module contains the classes for manages player game data."""

from player_module.player import Player

class PlayerManager:
    def __init__(self):
        self.players = {}

    def init_player(self, name:str)->None:
        self.players[name] = Player(name)

    def update_player_info(self, player:str, key:str, value)->None:
        self.players[player].update_info(key, value)

    def get_player_info(self, player:str, key:str):
        return self.players[player].get_info(key)
