#pip install feedparser

#import the feedparser

import feedparser
#main page rss https://archive.nytimes.com/www.nytimes.com/services/xml/rss/index.html?mcubz=0
"""news section """
# new york times =  https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml 
#new york time world = https://rss.nytimes.com/services/xml/rss/nyt/World.xml
""" tech section """
#Technology = https://rss.nytimes.com/services/xml/rss/nyt/Technology.xml
#Technology_parsonal="https://rss.nytimes.com/services/xml/rss/nyt/PersonalTech.xml"
"""Science section"""
# seience = "https://rss.nytimes.com/services/xml/rss/nyt/Science.xml"
# Space_&_Cosmos ="https://rss.nytimes.com/services/xml/rss/nyt/Space.xml"
# lifeHack= https://lifehacker.com/


Feed = feedparser.parse( "https://www.now14.co.il/category/c/%D7%97%D7%93%D7%A9%D7%95%D7%AA-%D7%95%D7%90%D7%A7%D7%98%D7%95%D7%90%D7%9C%D7%99%D7%94/%D7%90%D7%A7%D7%98%D7%95%D7%90%D7%9C%D7%99%D7%94-%D7%95%D7%97%D7%93%D7%A9%D7%95%D7%AA/feed/")
pointer = Feed.entries[0]
print (pointer.summary)
print (pointer.link)
