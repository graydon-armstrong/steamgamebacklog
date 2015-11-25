#!/usr/bin/env python

import unittest
import steam_api


class TestSteamApi(unittest.TestCase):
    """Tests for steam_api class"""

    def setUp(self):
        self.steam_api_connection = steam_api.SteamApiConnector()

    def test_set_api_key(self):
        """Test that the api key can be set"""
        self.steam_api_connection.set_steam_api_key('123aas')
        self.assertEqual('123aas', self.steam_api_connection.steam_api_key)

    def test_set_api_id(self):
        """Test that the api id can be set"""
        self.steam_api_connection.set_steam_api_id('12333')
        self.assertEqual('12333', self.steam_api_connection.steam_api_id)

    def test_get_owned_games(self):
        pass

    def test_json_to_dictionary(self):
        pass

if __name__ == '__main__':
    unittest.main()
