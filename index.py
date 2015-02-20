#!/usr/bin/env python

from cgi_header import print_cgi_header
import steam_api

print_cgi_header()

print '<h1>Steam API Testing Page</h1>'
print '<h2>Get Owned Games</h2>'

steam_api_connection = steam_api.steam_api_connector()
steam_api_connection.set_steam_api_key('AF4B3CC7FBF9CD34127CE10E6CCA9B62')
steam_api_connection.set_steam_api_id('76561197960434622')

user_games_json = steam_api_connection.get_owned_games()

print user_games_json
