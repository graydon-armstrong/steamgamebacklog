#!/usr/bin/env python

from cgi_header import print_cgi_header
import steam_api


def main():
    print_cgi_header()

    print '<h1>Steam API Testing Page</h1>'
    print '<h2>Get Owned Games</h2>'

    key = 'AF4B3CC7FBF9CD34127CE10E6CCA9B62'
    steam_id = '76561197989244442'

    steam_api_connection = steam_api.steam_api_connector()
    steam_api_connection.set_steam_api_key(key)
    steam_api_connection.set_steam_api_id(steam_id)

    get_owned_games_dict = steam_api_connection.get_owned_games()
    number_of_games_owned = get_owned_games_dict['game_count']
    games_dict = get_owned_games_dict['games']

    print get_owned_games_dict
    print 'Games owned: %s' % number_of_games_owned

    print_all_games(games_dict)


def print_top_played_games(games_dict):
    pass


def print_all_games(games_dict):
    print '<TABLE>'
    for game in games_dict:
        print '<TR>'
        print '<TD>Appid: %s</TD>' % game['appid']
        print '<TD>Game Name: %s</TD>' % game['name']
        print '<TD>Playtime: %s</TD>' % game['playtime_forever']
        print '</TR>'

    print '</TABLE>'

if __name__ == '__main__':
    main()
