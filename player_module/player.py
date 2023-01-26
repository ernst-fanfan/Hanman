"""This module contains the classes for holds player data."""
class Player:
    def __init__(self, name: str = ''):
        self.data = {'name': name}

    def update_info(self, key: str, value):
        self.data[key] = value

    def get_info(self, key: str):
        return self.data[key]