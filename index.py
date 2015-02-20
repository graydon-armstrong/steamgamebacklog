#!/usr/bin/env python

import cgi_header
import urllib2

cgi_header.print_cgi_header()

print '<h1>TEST Title</h1>'
print '<p>Test LORUM IPSUM TEST</p>'

listtest = ['1', '2', '3', '4']

for item in listtest:
    print '<p>' + item + '</p>'


steam_api_key = 'AF4B3CC7FBF9CD34127CE10E6CCA9B62'
steam_id = '76561197960434622'
response = urllib2.urlopen("""
    http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key=%s&steamid=%s&format=json
    """ % (steam_api_key, steam_id))
html = response.read()
print html

# import steamapi

# steamapi.core.APIConnection(api_key="AF4B3CC7FBF9CD34127CE10E6CCA9B62")
# steamapi.user.SteamUser(userurl="smileybarry")

# print 'test2'
