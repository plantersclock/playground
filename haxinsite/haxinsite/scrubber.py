from bs4 import BeautifulSoup

import sqlite3

import requests
import urllib.request
import re

forumurl = 'https://boardgamegeek.com/thread/browse/region/1?sort=recent'
top10url = "https://boardgamegeek.com/collection/user/mattman861?sort=rating&sortdir=desc&rankobjecttype=subtype&rankobjectid=1&columns=title%7Crating%7Cbggrating&minrating=8&geekranks=%0A%09%09%09%09%09%09%09%09%09Board+Game+Rank%0A%09%09%09%09%09%09%09%09&excludesubtype=boardgameexpansion&objecttype=thing&ff=1&subtype=boardgame"
####################################################################
# Go to top10url and save text into the file mattman861gamelist.txt

conn = sqlite3.connect('/HaxinAlone/haxinsite/db.sqlite3')
db = conn.cursor()
db.execute("INSERT INTO relatedgamesearch_bgguser(name) SELECT ('{0}') WHERE NOT EXISTS(SELECT 1 FROM relatedgamesearch_bgguser WHERE name = ('{0}'));".format('rahdo'))
conn.commit()

db.execute("SELECT id FROM relatedgamesearch_bgguser WHERE name = '{0}'".format('mattman861'))
bgguserid = db.fetchall()[0][0]
print(bgguserid)
db.execute("SELECT id FROM relatedgamesearch_bgggame WHERE name = '{0}'".format('Terra Mystica'))
bgggameid = db.fetchall()[0][0]
print(bgggameid)

db.execute("INSERT OR IGNORE INTO relatedgamesearch_usergameranking(user_name_id, game_name_id, rating) SELECT '%(bgguserid)s', '%(bgggameid)s', '%(rating)s'WHERE NOT EXISTS(SELECT 1 FROM relatedgamesearch_usergameranking WHERE user_name_id = ('%(bgguserid)s') AND game_name_id = ('%(bgggameid)s'));" % {'bgguserid' : bgguserid , 'bgggameid' : bgggameid , 'rating' : "10"})
test = db.fetchall()
print(test)

db.execute("UPDATE relatedgamesearch_usergameranking SET rating = '%(rating)s' WHERE user_name_id = ('%(bgguserid)s') AND game_name_id = ('%(bgggameid)s');" % {'bgguserid' : bgguserid , 'bgggameid' : bgggameid , 'rating' : "9"})
test = db.fetchall()
print(test)

#db.execute("UPDATE relatedgamesearch_usergameranking SET rating = '{2}' WHERE user_name = '(SELECT id FROM relatedgamesearch_bgggame WHERE name = {0})' AND game_name = '(SELECT id FROM relatedgamesearch_bgguser WHERE name = {1})';".format('mattman861', 'Terra Mystica', '9.99'))
conn.commit()

# page = urllib.request.urlopen(top10url)
# content = page.read()
# Go to top10url and save text into the file mattman861gamelist.txt
# mattstop10file = open("mattman861gamelist.txt", "wb")
# mattstop10file.write(content)
# mattstop10file.close()

top10urltext = open("mattman861gamelist.txt", "r")
#####################################################################
# Go to top10url and save text into the file mattman861gamelist.txt

# page = urllib.request.urlopen(forumurl)
# content = page.read()
# forumpage = open("forumpage.txt", "wb")
# forumpage.write(content)
# forumpage.close()

forumpagetext = open("forumpage.txt", "r")

def userscrubber(url):
    soup = BeautifulSoup(url, "html.parser")
    usersoup = soup.select("a[href*=/user/]")
    usersoup = list(set(usersoup))
    
    for x in usersoup:
        users = x.get_text()
        db.execute("INSERT INTO relatedgamesearch_bgguser(name) SELECT ('{0}') WHERE NOT EXISTS(SELECT 1 FROM relatedgamesearch_bgguser WHERE name = ('{0}'));".format(users))
        conn.commit()
        # print (users)
        

def top10scrubber(url):
    gamesoup = BeautifulSoup(url, "html.parser")
    count = 1
    
    while True:

        gamenameid = ('results_objectname%d' %(count))
        gamename = (gamesoup.find(id=gamenameid)).find('a').get_text()

        gamerankid = ('results_rating%d' %(count))
        gamerank = (gamesoup.find(id=gamerankid)).find(class_='ratingtext').get_text()
        gamerank = float(gamerank)

        if gamerank < 8:
            break
        if count == 10:
            game10rank = gamerank
        if count >= 10 and gamerank != game10rank:
            break

        count += 1

    #     print('------------------------------------------------')
    #     print(gamename)
    #     print(gamerank)
    # print('------------------------------------------------')

    

top10scrubber(top10urltext)
top10urltext.close()

userscrubber(forumpagetext)
conn.close()
forumpagetext.close()
