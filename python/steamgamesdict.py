#!/usr/bin/env python

import steam_api


class SteamGamesDict:
    """A class for storing a dictionary of a users steam games"""

    games_dict = {}
    games_count = None

    def __init__(self, steam_id, key='AF4B3CC7FBF9CD34127CE10E6CCA9B62'):
        steam_api_connection = steam_api.SteamApiConnector()
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

    @staticmethod
    def print_games_dict(the_games_dictionary):
        print('<TABLE>')
        print """<tr><th>App ID</th><th>Game Name</th><th>Minutes Played</th></tr>"""
        for game in the_games_dictionary:
            game['name'] = game['name'].encode('ascii', 'ignore')
            print('<TR>')
            print('<TD>%s</TD>' % game['appid'])
            print('<TD>%s</TD>' % game['name'])
            print('<TD>%s</TD>' % game['playtime_forever'])
            print('</TR>')

        print('</TABLE>')
