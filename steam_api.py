#!/usr/bin/env python

import urllib2


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
        return response.read()
