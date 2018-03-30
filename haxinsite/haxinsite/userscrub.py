from bs4 import BeautifulSoup
import requests
import urllib.request
import re

forumurl = 'https://boardgamegeek.com/thread/browse/region/1?sort=recent'
top10url = "https://boardgamegeek.com/collection/user/mattman861?sort=rating&sortdir=desc&rankobjecttype=subtype&rankobjectid=1&columns=title%7Crating%7Cbggrating&minrating=8&geekranks=%0A%09%09%09%09%09%09%09%09%09Board+Game+Rank%0A%09%09%09%09%09%09%09%09&excludesubtype=boardgameexpansion&objecttype=thing&ff=1&subtype=boardgame"
####################################################################
# Go to top10url and save text into the file mattman861gamelist.txt

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
    print (soup)

    users = soup.find_all("a", href_=re.compile('/user/', re.IGNORECASE))
    print (users)

    users = soup.find_all(class_='sf')
    users = [(x.find('a')) for x in users]
   # print(users)

def top10scrubber(url):
    soup = BeautifulSoup(url, "html.parser")
    count = 1
    
    while True:

        gamenameid = ('results_objectname%d' %(count))
        gamerankid = ('results_rating%d' %(count))
        
        gamename = ((soup.find(id=gamenameid)).find('a')).get_text()
        
        gamerank = ((soup.find(id=gamerankid)).find(class_='ratingtext')).get_text()
        #othersoup = othersoup.find(class_='ratingtext')
        gamerank = float(gamerank)
        if gamerank < 8:
            break
        if count == 10:
            game10rank = gamerank
        if count >= 10 and gamerank != game10rank:
            break
        count += 1
        print('------------------------------------------------')
        print(gamename)
        print(gamerank)
    print('------------------------------------------------')

    
    # for x in soup.find_all('div'):
    #     print(x.get_text())

top10scrubber(top10urltext)
top10urltext.close()

userscrubber(forumpagetext)
forumpagetext.close()
