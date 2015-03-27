#!/usr/bin/env python

import unittest
import steam_api


class test_steam_api(unittest.TestCase):
    """Tests for steam_api class"""

    def setUp(self):
        self.steam_api_connection = steam_api.steam_api_connector()

    def test_set_api_key(self):
        self.assertEqual('', self.steam_api_connection.steam_api_key)

if __name__ == '__main__':
    unittest.main()
