#!/usr/bin/env python

import unittest
from steam_games_dict import steam_games_dict


class test_steam_games_dict(unittest.TestCase):
    """Tests for steam_api class"""

    def setUp(self):
        self.steam_games_dict = steam_games_dict()

    def test_set_api_key(self):
        """Test that the api key can be set"""
        self.steam_api_connection.set_steam_api_key('123aas')
        self.assertEqual('123aas', self.steam_api_connection.steam_api_key)

if __name__ == '__main__':
    unittest.main()
