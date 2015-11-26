#!/usr/bin/env python

import unittest
from python.steamgamesdict import SteamGamesDict


class TestSteamGamesDict(unittest.TestCase):
    """Tests for steam_api class"""

    def setUp(self):
        key = 'AF4B3CC7FBF9CD34127CE10E6CCA9B62'
        steam_id = '76561197989244442'
        self.steam_games_dict = SteamGamesDict(key, steam_id)

    def test_get_number_of_games(self):
        """Test getting the amount of games owned by a user"""
        self.assertEqual(528, self.steam_games_dict.get_number_of_games())

    def test_get_game_name(self):
        """Test that you get back a game name"""
        self.assertEqual('Half-Life 2',
                         self.steam_games_dict.get_game_name(220))

    def test_get_game_name_invalid_appid(self):
        """Test that an invalid app_id doesnt work"""
        self.assertEqual(None, self.steam_games_dict.get_game_name(-1))

    def test_get_games(self):
        """Test getting the games dict"""
        # self.assertEqual()

if __name__ == '__main__':
    unittest.main()
