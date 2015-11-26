#!/usr/bin/env python

from python.steamgamesdict import *
from python.pagesetup import *


def main():
    print_cgi_header()
    print_html_start_tag()
    print_head("TESTING 123")

    print('<h1>Steam Game Backlog</h1>')
    print('<h2>Get Owned Games</h2>')

    steam_id = '76561197989244442'

    steam_games = SteamGamesDict(steam_id)

    # print get_owned_games_dict
    print('Games owned: %s' % steam_games.get_number_of_games())

    steam_games.print_all_games()

    print_html_end_tag()

if __name__ == '__main__':
    main()
