#!/usr/bin/env python

from cgi_header import print_cgi_header
from steam_games_dict import steam_games_dict


def main():
    print_cgi_header()

    print '<h1>Steam API Testing Page</h1>'
    print '<h2>Get Owned Games</h2>'

    key = 'AF4B3CC7FBF9CD34127CE10E6CCA9B62'
    steam_id = '76561197989244442'

    steam_games = steam_games_dict(key, steam_id)

    # print get_owned_games_dict
    print 'Games owned: %s' % steam_games.get_number_of_games()

    steam_games.print_all_games()

if __name__ == '__main__':
    main()
