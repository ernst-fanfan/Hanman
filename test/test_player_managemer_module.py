"""This test module tests the player_manager_module."""

from player_module.player_manager import PlayerManager
import pytest

class TestPlayerManagerModule:
    @pytest.mark.parametrize('name', ["Mark", "Paul", "Ark", "R2D2", "C3P0"])
    def test_player_creation(self, name):
        """Tests player creation."""
        player_manager = PlayerManager()
        player_manager.init_player(name)
        player = player_manager.players[name]
        assert player.get_info('name') == name
        assert len(player.data) == 1

    @pytest.mark.parametrize('name1, name2', [("Mark", "Paul"), ("Ark", "R2D2")])
    def test_multiple_players(self, name1, name2):
        """Tests player manager holds multiple players."""
        player_manager = PlayerManager()
        for name in [name1, name2]:
            player_manager.init_player(name)

        assert len(player_manager.players) == 2
        for name in [name1, name2]:
            assert player_manager.players[name].get_info('name') == name