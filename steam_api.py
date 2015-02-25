#!/usr/bin/env python

import urllib2
import json


class steam_api_connector():

    steam_api_key = ''
    steam_api_id = ''

    def set_steam_api_key(self, api_key):
        self.steam_api_key = api_key

    def set_steam_api_id(self, api_id):
        self.steam_api_id = api_id

    def get_owned_games(self):
        response = urllib2.urlopen("""
        http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key=%s&steamid=%s&format=json
        """ % (self.steam_api_key, self.steam_api_id))
        json_string = response.read()
        return self.json_to_dictionary(json_string)['response']

    def json_to_dictionary(self, json_string):
        # json_string = json_string.read()
        decoded_json = json.loads(json_string)
        return decoded_json
