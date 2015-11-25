#!/usr/bin/env python

import urllib2
import json


def json_to_dictionary(json_string):
    decoded_json = json.loads(json_string)
    return decoded_json


class SteamApiConnector:
    """Class for connecting and getting information from the steam api"""

    def __init__(self):
        pass

    steam_api_key = ''
    steam_api_id = ''

    def set_steam_api_key(self, api_key):
        """Set the api key
        :param api_key: The Steam API Key"""
        self.steam_api_key = api_key

    def set_steam_api_id(self, api_id):
        """Set the api id
        :param api_id: The Steam API ID"""
        self.steam_api_id = api_id

    def get_owned_games(self):
        response = urllib2.urlopen("""
        http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key=%s&steamid=%s&include_appinfo=1&format=json
        """ % (self.steam_api_key, self.steam_api_id))
        json_string = response.read()
        return json_to_dictionary(json_string)['response']
