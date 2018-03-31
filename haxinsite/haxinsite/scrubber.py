from bs4 import BeautifulSoup

import sqlite3

import time

import requests
import urllib.request
import re

forumurl = 'https://boardgamegeek.com/thread/browse/region/1?sort=recent'
top10url = "https://boardgamegeek.com/collection/user/mattman861?sort=rating&sortdir=desc&rankobjecttype=subtype&rankobjectid=1&columns=title%7Crating%7Cbggrating&minrating=8&geekranks=%0A%09%09%09%09%09%09%09%09%09Board+Game+Rank%0A%09%09%09%09%09%09%09%09&excludesubtype=boardgameexpansion&objecttype=thing&ff=1&subtype=boardgame"
top10url2 = "https://boardgamegeek.com/collection/user/mattman861?sort=rating&sortdir=desc&rankobjecttype=subtype&rankobjectid=1&columns=title%7Crating&minrating=8.5&geekranks=Board+Game+Rank&excludesubtype=boardgameexpansion&objecttype=thing&ff=1&subtype=boardgame"

conn = sqlite3.connect('/HaxinAlone/haxinsite/db.sqlite3')
db = conn.cursor()

####################################################################
# Gets the FK references PK ID's to be used later in usergamerating record creation
####################################################################
# db.execute("SELECT id FROM relatedgamesearch_bgguser WHERE name = '{0}'".format('mattman861'))
# bgguserid = db.fetchall()[0][0]
# print(bgguserid)
# db.execute("SELECT id FROM relatedgamesearch_bgggame WHERE name = '{0}'".format('Terra Mystica'))
# bgggameid = db.fetchall()[0][0]
# print(bgggameid)

# name = 'myboardgamename'
# db.execute("INSERT OR IGNORE INTO relatedgamesearch_bgggame(name) SELECT '%(name)s' WHERE NOT EXISTS(SELECT 1 FROM relatedgamesearch_bgggame WHERE name = ('%(name)s'));" % {'name' : name})
# bgggamename = db.fetchall()
# print(bgggamename)

# db.execute("INSERT OR IGNORE INTO relatedgamesearch_usergameranking(user_name_id, game_name_id, rating) SELECT '%(bgguserid)s', '%(bgggameid)s', '%(rating)s'WHERE NOT EXISTS(SELECT 1 FROM relatedgamesearch_usergameranking WHERE user_name_id = ('%(bgguserid)s') AND game_name_id = ('%(bgggameid)s'));" % {'bgguserid' : bgguserid , 'bgggameid' : bgggameid , 'rating' : "10"})
# test = db.fetchall()
# print(test)

#####################################################################
# Updates Game Ratings for existing User/Game Combos
#####################################################################
# db.execute("UPDATE relatedgamesearch_usergameranking SET rating = '%(rating)s' WHERE user_name_id = ('%(bgguserid)s') AND game_name_id = ('%(bgggameid)s');" % {'bgguserid' : bgguserid , 'bgggameid' : bgggameid , 'rating' : "9"})
# test = db.fetchall()
# print(test)

#####################################################################
# Go to top10url and save text into the file mattman861gamelist.txt
#####################################################################
# page = urllib.request.urlopen(top10url)
# content = page.read()

# Go to top10url and save text into the file mattman861gamelist.txt
# mattstop10file = open("mattman861gamelist.txt", "wb")
# mattstop10file.write(content)
# mattstop10file.close()


#####################################################################
# Go to top10url and save text into the file mattman861gamelist.txt

# page = urllib.request.urlopen(forumurl)
# content = page.read()
# forumpage = open("forumpage.txt", "wb")
# forumpage.write(content)
# forumpage.close()



def userscrubber(url):
    soup = BeautifulSoup(url, "html.parser")
    usersoup = soup.select("a[href*=/user/]")
    usersoup = list(set(usersoup))
    
    for x in usersoup:
        users = x.get_text()
        db.execute("INSERT INTO relatedgamesearch_bgguser(name) SELECT ('{0}') WHERE NOT EXISTS(SELECT 1 FROM relatedgamesearch_bgguser WHERE name = ('{0}'));".format(users))
        conn.commit()
        # print (users)
        

def top10scrubber(username, url):
    gamesoup = BeautifulSoup(url, "html.parser")
    count = 1
    
    
    while True:
        try:
            gamenameid = ('results_objectname%d' %(count))
            gamename = (gamesoup.find(id=gamenameid)).find('a').get_text()
            gamename = re.sub("[\(\[].*?[\)\]]", "", gamename)
            

            gamerankid = ('results_rating%d' %(count))
            gamerating = (gamesoup.find(id=gamerankid)).find(class_='ratingtext').get_text()
            gamerating = float(gamerating)
            

            if count == 10:
                game10rank = gamerating
            if (count >= 10 and gamerating != game10rank) or gamerating < 8:
                break

            count += 1
            try:
                db.execute("SELECT id FROM relatedgamesearch_bgguser WHERE name = '{0}'".format(username))
                bgguserid = db.fetchall()[0][0]
                # print(bgguserid)

                db.execute("INSERT OR IGNORE INTO relatedgamesearch_bgggame(name) SELECT '%(name)s' WHERE NOT EXISTS(SELECT 1 FROM relatedgamesearch_bgggame WHERE name = ('%(name)s'));" % {'name' : gamename})
                db.execute("SELECT id FROM relatedgamesearch_bgggame WHERE name = '{0}'".format(gamename))
                bgggameid = db.fetchall()[0][0]
                # print(bgggameid)
                
                

                db.execute("INSERT OR IGNORE INTO relatedgamesearch_usergameranking(user_name_id, game_name_id, rating) SELECT '%(bgguserid)s', '%(bgggameid)s', '%(rating)s'WHERE NOT EXISTS(SELECT 1 FROM relatedgamesearch_usergameranking WHERE user_name_id = ('%(bgguserid)s') AND game_name_id = ('%(bgggameid)s'));" % {'bgguserid' : bgguserid , 'bgggameid' : bgggameid , 'rating' : gamerating})
            except:
                pass

        #     print('------------------------------------------------')
            print("{0}'s game #{1}: {2}".format(username, count-1, gamename))
            
        except:
            break

    print("------------------------------------------------")
#####################################################################################################################################
##################################################################
# Runs the Top 10 gamme scrubber on the user list
##################################################################
db.execute("SELECT name FROM relatedgamesearch_bgguser")
rgsuserlist = db.fetchall()
count = 0
for x in rgsuserlist:
    if count == 50:
        time.sleep(.1)
        count = 0
    rgsuser = x[0]
    db.execute("SELECT id FROM relatedgamesearch_bgguser WHERE name = '{0}'".format(rgsuser))
    userid = db.fetchall()[0][0]
    db.execute("SELECT rating FROM relatedgamesearch_usergameranking WHERE user_name_id = '{0}'".format(userid))
    completeduser = db.fetchall()
    print("------------------------------------------------")
    print ("{0}:  {1}".format(rgsuser, completeduser))
    if(len(completeduser) == 0):
        try:
            usertop10url = ("https://boardgamegeek.com/collection/user/{0}?sort=rating&sortdir=desc&rankobjecttype=subtype&rankobjectid=1&columns=title%7Crating%7Cbggrating&minrating=8&geekranks=%0A%09%09%09%09%09%09%09%09%09Board+Game+Rank%0A%09%09%09%09%09%09%09%09&excludesubtype=boardgameexpansion&objecttype=thing&ff=1&subtype=boardgame".format(rgsuser))
            page = urllib.request.urlopen(usertop10url)
            usertop10content = page.read()
            top10scrubber(rgsuser, usertop10content)
        except:
            continue

    db.execute("SELECT rating FROM relatedgamesearch_usergameranking WHERE user_name_id = '{0}'".format(userid))
    completeduser = db.fetchall()
    if (len(completeduser) == 0):
        db.execute("DELETE FROM relatedgamesearch_bgguser WHERE name = '{0}'".format(rgsuser))
    conn.commit()
    count += 1
    

##################################################################
# Adds Recently active users on BGG recent forum
##################################################################
# count = 0
# while count <= 5:
#     try:
#         page = urllib.request.urlopen('https://boardgamegeek.com/forum/19/boardgamegeek/general-gaming/page/{0}'.format(count))
#         forumcontent = page.read()
#         userscrubber(forumcontent)
#     except:
#         continue
#     count += 1

#######################################################################################################################################

##################################################################
# Scrubs the top 10 game mattman861 text file page .txt file
##################################################################
# top10urltext = open("mattman861gamelist.txt", "r")
# top10scrubber('mattman861', top10urltext)
# top10urltext.close()
##################################################################

##################################################################
# Scrubs the forum page .txt file
##################################################################
# forumpagetext = open("forumpage.txt", "r")
# userscrubber(forumpagetext)
# forumpagetext.close()
##################################################################

conn.commit()
conn.close()
