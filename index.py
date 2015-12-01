#!/usr/bin/env python

from python.steamgamesdict import *
from python.pagesetup import *


def main():
    setup_page()

    steam_id = '76561197989244442'

    steam_games = SteamGamesDict(steam_id)

    # print get_owned_games_dict
    print('Games owned: %s' % steam_games.get_number_of_games())

    steam_games.print_all_games()

    print_html_end_tag()

if __name__ == '__main__':
    main()
