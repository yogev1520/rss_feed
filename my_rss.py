#pip install feedparser

#import the feedparser

import feedparser


Feed = feedparser.parse('http://photojournal.jpl.nasa.gov/rss/targetFamily/Earth')
pointer = Feed.entries[5]
print (pointer.summary)
print (pointer.link)