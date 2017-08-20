import feedparser
 
feed = feedparser.parse('http://sg.entertainment.yahoo.com/rss/')
title = feed['entries'][1].title
description =  feed['entries'][1].summary,
url = feed['entries'][1].link,
posts = []
for i in range(0,len(feed['entries'])):
    posts.append({
        'title': feed['entries'][i].title,
        'description': feed['entries'][i].summary,
        'url': feed['entries'][i].link,
    })
