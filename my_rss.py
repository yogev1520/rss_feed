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


Feed = feedparser.parse( "https://www.tehila.co.il/feed/")# the rss link here 
pointer = Feed.entries[0] # intry point 
pointer2 = Feed.entries[1]#intry point
pointer3 = Feed.entries[2] # intry point 
pointer4 = Feed.entries[3]#intry point 

print (pointer.summary) #get summary the text content
print(pointer.published) # get date= day_mount__year, time=hour_minute_second
print(pointer.link)# the pointer. you can get from  print(pointer)
"""
print (pointer.link) # get link
print(pointer2.summary)
print(pointer2.link)
print (pointer3.summary)
print (pointer3.link)
print(pointer4.summary)
print(pointer4.link)
"""