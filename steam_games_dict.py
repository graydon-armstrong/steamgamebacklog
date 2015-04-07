#!/usr/bin/env python

import steam_api


class steam_games_dict():
    """A class for storing a dictionary of a users steam games"""

    games_dict = {}
    games_count = None

    def __init__(self, key, steam_id):
        steam_api_connection = steam_api.steam_api_connector()
        steam_api_connection.set_steam_api_key(key)
        steam_api_connection.set_steam_api_id(steam_id)

        steam_api_return = steam_api_connection.get_owned_games()
        self.games_dict = steam_api_return['games']
        self.games_count = steam_api_return['game_count']

    def get_game_name(self, appid):
        for game in self.games_dict:
            if game['appid'] == appid:
                return game['name']
        return None

    def get_number_of_games(self):
        return self.games_count

    def get_games_dict(self):
        return self.games_dict

    def print_top_played_games(self):
        pass

    def print_all_games(self):
        self.print_games_dict(self.games_dict)

    def print_games_dict(self, the_games_dictionary):
        print '<TABLE>'
        for game in the_games_dictionary:
            game['name'] = game['name'].encode('ascii', 'ignore')
            print '<TR>'
            print '<TD>Appid: %s</TD>' % game['appid']
            print '<TD>Game Name: %s</TD>' % game['name']
            print '<TD>Playtime: %s</TD>' % game['playtime_forever']
            print '</TR>'

        print '</TABLE>'
