# created by Miguel Flores

import scrapetube as st
from random import randint
from pytube import YouTube

SORT = 'upload_date'
# RESULTS_TYPE = 'video'


channel = str(input("Enter the channel URL:"))

# search_term = str(input("Enter a search term: "))
max_vid = int(input("Enter the maximum number of videos to scrape: "))

key_str = str(input("Enter keywords in the title to look for separated by spaces: "))

# videos = st.get_search(search_term, max_vid, randint(2,5), SORT)



"""
    in order to get the video's thumbnail:
    video['thumbnail']['thumbnails'][-1]['url']
    URL: https://www.youtube.com/watch?v=" + video['videoId']
"""

# vids = st.get_channel(None,'https://www.youtube.com/c/JazBazPhilippines', max_vid, randint(2,5))
vids = st.get_channel(None, channel, max_vid, randint(2,5))
print("done getting channel")

links = []

keywords = key_str.split()

for video in vids:
    title = video['title']['runs'][0]['text'].split(' ')
    for i in range(len(title)):
        title[i] = title[i].upper()
    print(title)
    for word in keywords:
        for title_word in title:
            if word.upper() in title_word:
                links.append("https://www.youtube.com/watch?v=" + video['videoId'])

for link in links:
    yt = YouTube(link)
    try:
        print("Trying to download: " + yt.title + " at " + link)
        yt.streams.filter(type='video').get_highest_resolution().download()
    except:
        print("Error downloading video, proceeding to the next one")

# yt = YouTube(links[0])
# print(yt.streams.filter(type='video', progressive="False").get_highest_resolution())